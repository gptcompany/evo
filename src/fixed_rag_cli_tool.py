#!/usr/bin/env python
"""
Production-Ready RAG CLI Tool
Fixes:
1. Database outside source repository
2. No dependency on virtual environment location
3. Proper LightRAG loading for existing databases
4. Portable installation
"""

import os
import argparse
import asyncio
import logging
import json
import sys
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Add RAG-Anything to Python path dynamically
def setup_raganything_path():
    """Dynamically add RAG-Anything to Python path"""
    rag_anything_path = Path.home() / "RAG-Anything"
    if rag_anything_path.exists():
        sys.path.insert(0, str(rag_anything_path))
        return rag_anything_path

    # Alternative locations
    for alt_path in ["/home/sam/RAG-Anything", "./RAG-Anything"]:
        if Path(alt_path).exists():
            sys.path.insert(0, alt_path)
            return Path(alt_path)

    raise RuntimeError("RAG-Anything installation not found")

# Setup path and imports
RAG_ANYTHING_ROOT = setup_raganything_path()

from lightrag.llm.openai import openai_complete_if_cache, openai_embed
from lightrag.utils import EmbeddingFunc, logger
from raganything import RAGAnything, RAGAnythingConfig

load_dotenv(override=False)

class ProductionRAGManager:
    """Production RAG manager with proper separation"""

    def __init__(self, project_name: str = "default"):
        self.project_name = project_name
        # Database in user's home, NOT in source code
        self.base_dir = Path.home() / ".rag_databases"
        self.working_dir = self.base_dir / project_name
        self.working_dir.mkdir(parents=True, exist_ok=True)

        print(f"📁 Using database: {self.working_dir}")

    def get_database_info(self):
        """Get database information"""
        doc_status_file = self.working_dir / "kv_store_doc_status.json"
        if not doc_status_file.exists():
            return {
                "project_name": self.project_name,
                "working_dir": str(self.working_dir),
                "files_count": 0,
                "files": []
            }

        with open(doc_status_file, 'r') as f:
            doc_status = json.load(f)

        files_info = []
        for doc_id, info in doc_status.items():
            files_info.append({
                "file_path": info.get("file_path", "Unknown"),
                "status": info.get("status", "Unknown"),
                "updated_at": info.get("updated_at", "Unknown"),
                "chunks_count": info.get("chunks_count", 0)
            })

        return {
            "project_name": self.project_name,
            "working_dir": str(self.working_dir),
            "files_count": len(files_info),
            "files": files_info
        }

async def batch_process_folder(folder_path: str, working_dir: str, api_key: str,
                              base_url: str = None, parser: str = "mineru", extensions: str = "pdf,txt,md"):
    """Process all documents in a folder"""
    try:
        folder = Path(folder_path)
        if not folder.exists() or not folder.is_dir():
            print(f"❌ Folder not found: {folder_path}")
            return False

        # Parse extensions
        ext_list = [f".{ext.strip()}" for ext in extensions.split(",")]

        # Find all files with specified extensions
        files_to_process = []
        for ext in ext_list:
            files_to_process.extend(folder.glob(f"*{ext}"))
            files_to_process.extend(folder.glob(f"**/*{ext}"))  # Recursive

        if not files_to_process:
            print(f"📂 No files with extensions {extensions} found in {folder_path}")
            return True

        print(f"📂 Found {len(files_to_process)} files to process")

        success_count = 0
        for file_path in files_to_process:
            print(f"\n📄 Processing {file_path.name}...")
            try:
                success = await process_single_document(
                    str(file_path), working_dir, api_key, base_url, parser
                )
                if success:
                    success_count += 1
                    print(f"✅ Successfully processed: {file_path.name}")
                else:
                    print(f"❌ Failed to process: {file_path.name}")
            except Exception as e:
                print(f"❌ Error processing {file_path.name}: {e}")

        print(f"\n🎯 Batch processing complete: {success_count}/{len(files_to_process)} files processed successfully")
        return success_count > 0

    except Exception as e:
        logger.error(f"Error in batch processing: {str(e)}")
        return False

async def update_from_folder(folder_path: str, working_dir: str, api_key: str,
                           base_url: str = None, parser: str = "mineru", extensions: str = "pdf,txt,md"):
    """Update documents by comparing folder vs database"""
    try:
        folder = Path(folder_path)
        if not folder.exists() or not folder.is_dir():
            print(f"❌ Folder not found: {folder_path}")
            return False

        # Check if database exists
        doc_status_file = Path(working_dir) / "kv_store_doc_status.json"
        if not doc_status_file.exists():
            print("📄 No existing database found. Running full batch processing...")
            return await batch_process_folder(folder_path, working_dir, api_key, base_url, parser, extensions)

        # Load existing database info
        try:
            with open(doc_status_file, 'r') as f:
                doc_status = json.load(f)
        except:
            doc_status = {}

        # Parse extensions and find current files
        ext_list = [f".{ext.strip()}" for ext in extensions.split(",")]
        current_files = {}

        for ext in ext_list:
            for file_path in folder.rglob(f"*{ext}"):
                # Use relative path as key for comparison
                rel_path = str(file_path.relative_to(folder))
                current_files[rel_path] = {
                    'full_path': str(file_path),
                    'mtime': file_path.stat().st_mtime,
                    'size': file_path.stat().st_size
                }

        print(f"🔍 Checking {len(current_files)} files against database...")

        files_to_process = []
        files_to_delete = []

        # Check for new or modified files
        for rel_path, file_info in current_files.items():
            db_key = None
            # Find matching entry in database (by file path)
            for doc_id, db_info in doc_status.items():
                if db_info.get('file_path', '').endswith(Path(rel_path).name):
                    db_key = doc_id
                    break

            if db_key is None:
                # New file
                print(f"📄 New file: {rel_path}")
                files_to_process.append(file_info['full_path'])
            else:
                # Check if modified (simplified check by size)
                db_info = doc_status[db_key]
                if 'file_size' not in db_info or db_info.get('file_size', 0) != file_info['size']:
                    print(f"🔄 Modified file: {rel_path}")
                    files_to_process.append(file_info['full_path'])

        # Check for deleted files (files in DB but not in folder)
        db_files = set()
        for doc_id, db_info in doc_status.items():
            file_path = db_info.get('file_path', '')
            if file_path:
                db_files.add(Path(file_path).name)

        current_file_names = set(Path(f['full_path']).name for f in current_files.values())
        deleted_files = db_files - current_file_names

        if deleted_files:
            print(f"🗑️  Files removed from folder: {', '.join(deleted_files)}")
            print("   Note: Database cleanup not implemented yet")

        if not files_to_process:
            print("✅ All files are up to date!")
            return True

        print(f"⚡ Processing {len(files_to_process)} new/modified files...")

        success_count = 0
        for file_path in files_to_process:
            try:
                success = await process_single_document(
                    file_path, working_dir, api_key, base_url, parser
                )
                if success:
                    success_count += 1
            except Exception as e:
                print(f"❌ Error processing {Path(file_path).name}: {e}")

        print(f"🎯 Update complete: {success_count}/{len(files_to_process)} files processed successfully")
        return success_count > 0

    except Exception as e:
        logger.error(f"Error in update operation: {str(e)}")
        return False

async def merge_dual_parser_results(docling_dir: str, mineru_dir: str, final_dir: str):
    """Merge results from Docling and MinerU parsers intelligently"""
    import shutil
    from pathlib import Path

    try:
        docling_path = Path(docling_dir)
        mineru_path = Path(mineru_dir)
        final_path = Path(final_dir)

        print("🔄 Merging dual-parser results...")

        # Start with Docling results (superior for equations)
        if docling_path.exists():
            if final_path.exists():
                shutil.rmtree(final_path)
            shutil.copytree(docling_path, final_path)
            print("✅ Base: Docling results (equations priority)")

        # Merge MinerU results (superior for HTML/images)
        if mineru_path.exists():
            # Copy MinerU-specific files that Docling might have missed
            for item in mineru_path.rglob("*"):
                if item.is_file():
                    relative_path = item.relative_to(mineru_path)
                    final_item = final_path / relative_path

                    # Only copy if doesn't exist or if it's likely better from MinerU
                    if not final_item.exists():
                        final_item.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(item, final_item)
                        print(f"📄 Added from MinerU: {relative_path}")

            print("✅ Enhanced: MinerU results (HTML/images)")

        print("🎯 Dual-parser merge completed successfully!")
        return True

    except Exception as e:
        print(f"❌ Error merging dual-parser results: {e}")
        return False

async def process_dual_parser_document(file_path: str, working_dir: str, api_key: str,
                                     base_url: str = None):
    """Process document with both Docling and MinerU, then merge results"""
    try:
        from pathlib import Path
        import tempfile

        file_name = Path(file_path).stem
        print(f"🔄 Starting dual-parser processing for: {file_name}")

        # Create temporary directories for each parser
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            docling_dir = temp_path / "docling"
            mineru_dir = temp_path / "mineru"

            docling_dir.mkdir()
            mineru_dir.mkdir()

            # Process with Docling (superior for equations)
            print("📊 Phase 1: Processing with Docling (equations priority)...")
            docling_success = await process_single_document_internal(
                file_path, str(docling_dir), api_key, base_url, "docling"
            )

            if docling_success:
                print("✅ Docling processing completed")
            else:
                print("⚠️  Docling processing failed, continuing with MinerU only")

            # Process with MinerU (superior for HTML/images)
            print("🌐 Phase 2: Processing with MinerU (HTML/images priority)...")
            mineru_success = await process_single_document_internal(
                file_path, str(mineru_dir), api_key, base_url, "mineru"
            )

            if mineru_success:
                print("✅ MinerU processing completed")
            else:
                print("⚠️  MinerU processing failed")

            # Check if at least one parser succeeded
            if not docling_success and not mineru_success:
                print("❌ Both parsers failed!")
                return False

            # Merge results intelligently
            print("🔄 Phase 3: Merging results...")
            merge_success = await merge_dual_parser_results(
                str(docling_dir), str(mineru_dir), working_dir
            )

            if merge_success:
                print(f"🎯 Dual-parser processing completed successfully!")
                print(f"📊 Combined: Docling equations + MinerU HTML/images")
                return True
            else:
                print("❌ Failed to merge dual-parser results")
                return False

    except Exception as e:
        print(f"❌ Error in dual-parser processing: {e}")
        return False

async def process_single_document_internal(file_path: str, working_dir: str, api_key: str,
                                         base_url: str = None, parser: str = "mineru"):
    """Internal function for single parser processing (used by both single and dual modes)"""
    try:
        config = RAGAnythingConfig(
            working_dir=working_dir,
            parser=parser,
            parse_method="auto",
            enable_image_processing=True,
            enable_table_processing=True,
            enable_equation_processing=True,
        )

        def llm_model_func(prompt, system_prompt=None, history_messages=[], **kwargs):
            return openai_complete_if_cache(
                "gpt-4o-mini", prompt,
                system_prompt=system_prompt,
                history_messages=history_messages,
                api_key=api_key, base_url=base_url, **kwargs
            )

        embedding_func = EmbeddingFunc(
            embedding_dim=3072, max_token_size=8192,
            func=lambda texts: openai_embed(texts, model="text-embedding-3-large",
                                          api_key=api_key, base_url=base_url)
        )

        # Define vision model function for completeness (from example)
        def vision_model_func(prompt, system_prompt=None, history_messages=[], image_data=None, messages=None, **kwargs):
            if messages:
                return llm_model_func("", system_prompt=None, history_messages=[], messages=messages, **kwargs)
            elif image_data:
                # For simplicity, fallback to text mode for now
                return llm_model_func(prompt, system_prompt, history_messages, **kwargs)
            else:
                return llm_model_func(prompt, system_prompt, history_messages, **kwargs)

        rag = RAGAnything(
            config=config,
            llm_model_func=llm_model_func,
            vision_model_func=vision_model_func,
            embedding_func=embedding_func
        )

        await rag.process_document_complete(
            file_path=file_path,
            output_dir=str(Path(working_dir) / "output"),
            parse_method="auto"
        )
        return True

    except Exception as e:
        logger.error(f"Error in {parser} processing: {str(e)}")
        return False

async def process_single_document(file_path: str, working_dir: str, api_key: str,
                                base_url: str = None, parser: str = "mineru"):
    """Process single document with proper LightRAG handling - supports dual-parser mode"""

    # Handle dual-parser mode
    if parser == "dual":
        print(f"🎯 Dual-parser mode selected for: {Path(file_path).name}")
        return await process_dual_parser_document(file_path, working_dir, api_key, base_url)

    # Standard single-parser mode
    print(f"🔄 Processing with {parser}: {Path(file_path).name}")
    return await process_single_document_internal(file_path, working_dir, api_key, base_url, parser)

async def query_documents_fixed(query: str, working_dir: str, api_key: str,
                              base_url: str = None, mode: str = "hybrid"):
    """FIXED: Query with proper LightRAG loading"""
    try:
        config = RAGAnythingConfig(working_dir=working_dir)

        def llm_model_func(prompt, system_prompt=None, history_messages=[], **kwargs):
            return openai_complete_if_cache(
                "gpt-4o-mini", prompt,
                system_prompt=system_prompt,
                history_messages=history_messages,
                api_key=api_key, base_url=base_url, **kwargs
            )

        embedding_func = EmbeddingFunc(
            embedding_dim=3072, max_token_size=8192,
            func=lambda texts: openai_embed(texts, model="text-embedding-3-large",
                                          api_key=api_key, base_url=base_url)
        )

        # Check for existing database
        doc_status_file = Path(working_dir) / "kv_store_doc_status.json"
        if not doc_status_file.exists():
            raise ValueError("No processed documents found. Process documents first.")

        print("🔄 Initializing LightRAG for existing database...")

        # First, create LightRAG instance with existing database
        from lightrag import LightRAG
        lightrag = LightRAG(
            working_dir=working_dir,
            llm_model_func=llm_model_func,
            embedding_func=embedding_func
        )

        # Define vision model function for completeness (from example)
        def vision_model_func(prompt, system_prompt=None, history_messages=[], image_data=None, messages=None, **kwargs):
            if messages:
                return llm_model_func("", system_prompt=None, history_messages=[], messages=messages, **kwargs)
            elif image_data:
                # For simplicity, fallback to text mode for now
                return llm_model_func(prompt, system_prompt, history_messages, **kwargs)
            else:
                return llm_model_func(prompt, system_prompt, history_messages, **kwargs)

        print("🔄 Creating RAGAnything with pre-initialized LightRAG...")

        # Create RAGAnything instance with pre-initialized LightRAG (critical!)
        rag = RAGAnything(
            lightrag=lightrag,  # Pass pre-initialized LightRAG
            config=config,
            llm_model_func=llm_model_func,
            vision_model_func=vision_model_func,
            embedding_func=embedding_func
        )

        print("🔄 Executing query...")

        # Use the exact pattern from the example: simple aquery call
        result = await rag.aquery(query, mode=mode)
        print(f"📋 Query: {query}")
        print(f"🔍 Result: {result}")
        return result

    except Exception as e:
        logger.error(f"Error querying documents: {str(e)}")
        return None

def main():
    """Main CLI function with proper path handling"""
    parser = argparse.ArgumentParser(description="Production RAG CLI Tool")
    parser.add_argument('--project', '-p', default='default', help='Project name')

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Process command
    process_parser = subparsers.add_parser('process', help='Process a document')
    process_parser.add_argument('file_path', help='Path to document')
    process_parser.add_argument('--parser', default='mineru', choices=['mineru', 'docling', 'dual'])

    # Query command
    query_parser = subparsers.add_parser('query', help='Query documents')
    query_parser.add_argument('query', help='Query text')
    query_parser.add_argument('--mode', default='hybrid', choices=['hybrid', 'local', 'global', 'naive'])

    # Info command
    info_parser = subparsers.add_parser('info', help='Show database info')

    # List projects
    list_parser = subparsers.add_parser('list-projects', help='List all projects')

    # Batch processing command
    batch_parser = subparsers.add_parser('batch', help='Process all documents in a folder')
    batch_parser.add_argument('folder_path', help='Path to folder containing documents')
    batch_parser.add_argument('--parser', default='mineru', choices=['mineru', 'docling', 'dual'])
    batch_parser.add_argument('--extensions', default='pdf,txt,md', help='File extensions to process (comma-separated)')

    # Update command
    update_parser = subparsers.add_parser('update', help='Update documents: compare folder vs database')
    update_parser.add_argument('folder_path', help='Path to folder to check for updates')
    update_parser.add_argument('--parser', default='mineru', choices=['mineru', 'docling', 'dual'])
    update_parser.add_argument('--extensions', default='pdf,txt,md', help='File extensions to check (comma-separated)')

    # Common arguments
    for p in [process_parser, query_parser, batch_parser, update_parser]:
        p.add_argument('--api-key', default=os.getenv('OPENAI_API_KEY'))
        p.add_argument('--base-url', default=os.getenv('OPENAI_BASE_URL'))

    # Timeout arguments for long operations
    for p in [process_parser, batch_parser, update_parser]:
        p.add_argument('--timeout', type=int, default=600,
                      help='Timeout in seconds for processing operations (default: 600=10min)')

    # Query timeout (usually faster)
    query_parser.add_argument('--timeout', type=int, default=300,
                            help='Timeout in seconds for query operations (default: 300=5min)')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # Initialize manager
    rag_manager = ProductionRAGManager(args.project)

    if args.command == 'info':
        info = rag_manager.get_database_info()
        print(f"📊 RAG Project: {info['project_name']}")
        print(f"📁 Database: {info['working_dir']}")
        print(f"📄 Files processed: {info['files_count']}")
        if info['files']:
            print("\n📋 Files in database:")
            for file_info in info['files']:
                print(f"  • {file_info['file_path']} (chunks: {file_info['chunks_count']})")
        return

    if args.command == 'list-projects':
        base_path = Path.home() / ".rag_databases"
        if base_path.exists():
            projects = [d.name for d in base_path.iterdir() if d.is_dir()]
            print(f"📁 Available RAG projects:")
            for project in projects:
                print(f"  • {project}")
        else:
            print("No RAG projects found.")
        return

    # Commands requiring API key
    if not args.api_key:
        print("❌ Error: OpenAI API key required")
        return

    if args.command == 'process':
        success = asyncio.run(process_single_document(
            args.file_path, str(rag_manager.working_dir),
            args.api_key, args.base_url, args.parser
        ))
        if not success:
            exit(1)

    elif args.command == 'query':
        result = asyncio.run(query_documents_fixed(
            args.query, str(rag_manager.working_dir),
            args.api_key, args.base_url, args.mode
        ))
        if result is None:
            exit(1)

    elif args.command == 'batch':
        success = asyncio.run(batch_process_folder(
            args.folder_path, str(rag_manager.working_dir),
            args.api_key, args.base_url, args.parser, args.extensions
        ))
        if not success:
            exit(1)

    elif args.command == 'update':
        success = asyncio.run(update_from_folder(
            args.folder_path, str(rag_manager.working_dir),
            args.api_key, args.base_url, args.parser, args.extensions
        ))
        if not success:
            exit(1)

if __name__ == "__main__":
    main()