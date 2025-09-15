#!/usr/bin/env python
"""
RAG CLI Tool for docs_scraper integration
Adapted from RAG-Anything examples with CLI support for both processing and querying
"""

import os
import argparse
import asyncio
import logging
from pathlib import Path
from dotenv import load_dotenv

# RAG-Anything imports
from lightrag.llm.openai import openai_complete_if_cache, openai_embed
from lightrag.utils import EmbeddingFunc, logger
from raganything import RAGAnything, RAGAnythingConfig

load_dotenv(override=False)

def setup_logging():
    """Setup basic logging"""
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

async def process_document(file_path: str, working_dir: str, api_key: str, base_url: str = None, parser: str = "mineru"):
    """Process document with RAG-Anything"""
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

        def vision_model_func(prompt, system_prompt=None, history_messages=[], 
                            image_data=None, messages=None, **kwargs):
            if messages:
                return openai_complete_if_cache(
                    "gpt-4o", "", system_prompt=None, history_messages=[],
                    messages=messages, api_key=api_key, base_url=base_url, **kwargs
                )
            elif image_data:
                return openai_complete_if_cache(
                    "gpt-4o", "", system_prompt=None, history_messages=[],
                    messages=[
                        {"role": "system", "content": system_prompt} if system_prompt else None,
                        {"role": "user", "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}
                        ]} if image_data else {"role": "user", "content": prompt}
                    ], api_key=api_key, base_url=base_url, **kwargs
                )
            else:
                return llm_model_func(prompt, system_prompt, history_messages, **kwargs)

        embedding_func = EmbeddingFunc(
            embedding_dim=3072, max_token_size=8192,
            func=lambda texts: openai_embed(texts, model="text-embedding-3-large", 
                                          api_key=api_key, base_url=base_url)
        )

        rag = RAGAnything(
            config=config, llm_model_func=llm_model_func,
            vision_model_func=vision_model_func, embedding_func=embedding_func
        )

        await rag.process_document_complete(file_path=file_path, output_dir="./output", parse_method="auto")
        print(f"✅ Successfully processed: {file_path}")
        
    except Exception as e:
        logger.error(f"Error processing document: {str(e)}")
        return False
    return True

async def query_documents(query: str, working_dir: str, api_key: str, base_url: str = None, mode: str = "hybrid"):
    """Query processed documents"""
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

        rag = RAGAnything(config=config, llm_model_func=llm_model_func, embedding_func=embedding_func)
        
        result = await rag.aquery(query, mode=mode)
        print(f"📋 Query: {query}")
        print(f"🔍 Result: {result}")
        return result
        
    except Exception as e:
        logger.error(f"Error querying documents: {str(e)}")
        return None

def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(description="RAG CLI Tool for docs_scraper")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Process command
    process_parser = subparsers.add_parser('process', help='Process a document')
    process_parser.add_argument('file_path', help='Path to document to process')
    process_parser.add_argument('--working-dir', '-w', default='./rag_storage', help='Working directory')
    process_parser.add_argument('--parser', default='mineru', choices=['mineru', 'docling'], help='Parser to use')
    
    # Query command
    query_parser = subparsers.add_parser('query', help='Query processed documents')
    query_parser.add_argument('query', help='Query text')
    query_parser.add_argument('--working-dir', '-w', default='./rag_storage', help='Working directory')
    query_parser.add_argument('--mode', default='hybrid', choices=['hybrid', 'local', 'global', 'naive'], help='Query mode')
    
    # Common arguments
    for p in [process_parser, query_parser]:
        p.add_argument('--api-key', default=os.getenv('OPENAI_API_KEY'), help='OpenAI API key')
        p.add_argument('--base-url', default=os.getenv('OPENAI_BASE_URL'), help='OpenAI base URL')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
        
    if not args.api_key:
        print("❌ Error: OpenAI API key required (set OPENAI_API_KEY env var or use --api-key)")
        return
    
    setup_logging()
    
    if args.command == 'process':
        success = asyncio.run(process_document(
            args.file_path, args.working_dir, args.api_key, args.base_url, args.parser
        ))
        if not success:
            exit(1)
            
    elif args.command == 'query':
        result = asyncio.run(query_documents(
            args.query, args.working_dir, args.api_key, args.base_url, args.mode
        ))
        if result is None:
            exit(1)

if __name__ == "__main__":
    main()