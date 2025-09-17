# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

EVO is an evolutionary multi-agent orchestration system that learns and optimizes autonomously through evolutionary algorithms to find the optimal combination of agents, tools, and workflows for specific tasks.

### Architecture
- **Claude Code**: Master orchestrator with high-level coordination and decision making
- **Claude Subagents**: Domain experts for requirements, planning, and architecture
- **MCP Server Pydantic**: Deep specialists for code generation and domain expertise

### Tech Stack
- Python ≥3.11 with async/await patterns
- Pydantic AI for data validation and models
- Claude Code MCP framework
- RAG-Anything for document processing
- SQLite/PostgreSQL for evolution data storage

## Commands

### RAG CLI Operations
```bash
# Process a document with RAG (default: MinerU parser)
./rag_cli process /path/to/document

# Process with specific parser
./rag_cli process /path/to/document --parser mineru
./rag_cli process /path/to/document --parser docling

# 🎯 DUAL-PARSER: Combine Docling + MinerU for maximum equation extraction
./rag_cli process /path/to/document --parser dual

# Query the RAG system
./rag_cli query "your question here"

# Batch process folder with dual-parser
./rag_cli batch /path/to/folder --parser dual

# Get help
./rag_cli --help
```

### Parser Selection Guide
- **MinerU**: General-purpose, good for HTML and images
- **Docling**: Superior for mathematical equations (5x better extraction)
- **Dual**: 🚀 **RECOMMENDED for scientific documents** - combines Docling equations + MinerU HTML/images

### Development Environment
```bash
# Setup environment (requires RAG-Anything installation)
source /home/sam/RAG-Anything/.venv/bin/activate

# Run CLI tool directly
python src/fixed_rag_cli_tool.py --help

# Check environment variables
cat .env.sample  # See required environment variables
```

### Git Operations
```bash
git status              # Check working tree status
git add .              # Stage all changes
git commit -m "msg"    # Commit changes
```

## Directory Structure

```
.claude/                # Claude Code configurations
├── agents/            # Subagent definitions
├── hooks/             # Hook scripts (context_bundle_builder.py)
├── context_bundles/   # Stored context bundles with operations tracking
└── logs/              # Tool usage logs

src/                   # Source code
├── rag_cli_tool.py           # Original RAG CLI implementation
├── enhanced_rag_cli_tool.py  # Enhanced version
└── fixed_rag_cli_tool.py     # Current stable version

rag_storage/           # RAG data storage
logs/                  # Application logs
output/                # Output files
```

## Code Style

### Python Conventions
- Type hints required (Python ≥3.11)
- Async/await patterns for concurrent operations
- Pydantic models for data validation
- JSON for configuration and data serialization

### File Organization
Scripts should include UV header for dependencies:
```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["asyncio", "pydantic"]
# ///
```

### Naming Conventions
- Files: snake_case
- Functions: snake_case
- Classes: PascalCase
- Constants: UPPER_CASE

## Environment Configuration

Required environment variables (see `.env.sample`):
```bash
OPENAI_API_KEY=your_openai_api_key
OPENAI_BASE_URL=https://api.openai.com/v1
PARSER=mineru
PARSE_METHOD=auto
RAG_WORKING_DIR=./rag_storage
RAG_OUTPUT_DIR=./output
```

## MCP Integration

The project uses several MCP servers:
- Context7 for documentation access
- Git-MCP for repository operations
- Serena for codebase analysis
- Custom agents defined in `.claude/agents/`

## RAG System

The RAG implementation uses RAG-Anything with:
- Multiple parser options (MinerU, Docling, Dual)
- OpenAI GPT-4o models for LLM operations
- Vector embeddings for semantic search
- Support for images, tables, and equations

### Key Features
- Document processing with multiple parser options
- Vision model support for image analysis
- Configurable embedding dimensions
- Async processing capabilities

## 🎯 Dual-Parser Innovation

### Revolutionary Combination
The dual-parser mode combines the strengths of both parsers:
- **Docling**: 5x superior equation extraction (mathematical documents)
- **MinerU**: Superior HTML and image processing
- **Intelligent Merge**: Combines results without duplication

### Performance Metrics
Tested on scientific documents (jump_prova.pdf):
- **Equations extracted**: 5 (Docling) vs 1 (MinerU)
- **Graph complexity**: 67 nodes, 117 edges (vs 24 nodes, 26 edges MinerU-only)
- **Query quality**: Accurate mathematical equation retrieval
- **Processing time**: <10 minutes for dual-parser mode

### Use Cases
Dual-parser is **highly recommended** for:
- Scientific papers with mathematical content
- Technical documents with equations and images
- Academic research papers
- Financial modeling documents
- Engineering specifications

### Example Usage
```bash
# Process scientific document with dual-parser
./rag_cli --project research-papers process paper.pdf --parser dual

# Query mathematical content
./rag_cli --project research-papers query "What equations are mentioned?"

# Batch process research folder
./rag_cli --project research-papers batch ./papers/ --parser dual
```