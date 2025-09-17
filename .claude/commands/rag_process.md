---
description: Advanced multimodal RAG processing with database management and batch operations
argument-hint: [command] [args...] | query [question]
allowed-tools: Bash, Task
---

# RAG Process - Advanced Multimodal Document Processing

Process documents with RAG-Anything for advanced multimodal content analysis, including mathematical formulas, tables, and images. Features complete database management, batch processing, and automatic updates.

## Variables

COMMAND: $1 (process|query|batch|update|info|list-projects)
ARGS: $2... (command-specific arguments)

## Instructions

- **Script Used**: `/home/sam/EVO/src/fixed_rag_cli_tool.py`
- **Wrapper**: `/home/sam/EVO/rag_cli`
- **Database Location**: `~/.rag_databases/[project-name]/`
- **API**: OpenAI for semantic understanding

## Complete Command Reference

### 1. Database Management

#### List All Projects/Databases
```bash
/home/sam/EVO/rag_cli list-projects
```

#### Show Project Info
```bash
/home/sam/EVO/rag_cli --project [project-name] info
```

### 2. Document Processing

#### Single Document Processing
```bash
# Dual-parser: combines Docling + MinerU
/home/sam/EVO/rag_cli --project [project-name] process [document-path] --parser dual --timeout 900

# Scientific/mathematical documents
/home/sam/EVO/rag_cli --project [project-name] process [document-path] --parser docling --timeout 600

# HTML or image-heavy documents
/home/sam/EVO/rag_cli --project [project-name] process [document-path] --parser mineru --timeout 600
```

#### Batch Processing
```bash
# Dual-parser batch
/home/sam/EVO/rag_cli --project [project-name] batch [folder-path] --parser dual --extensions pdf,docx,pptx --timeout 1800

# Scientific papers
/home/sam/EVO/rag_cli --project [project-name] batch [folder-path] --parser docling --extensions pdf,docx,pptx --timeout 1200

# Mixed content
/home/sam/EVO/rag_cli --project [project-name] batch [folder-path] --parser mineru --extensions pdf,html,txt,md --timeout 1200
```

#### Incremental Update
```bash
# Dual-parser update
/home/sam/EVO/rag_cli --project [project-name] update [folder-path] --parser dual --extensions pdf,docx,pptx --timeout 1200

# Standard update
/home/sam/EVO/rag_cli --project [project-name] update [folder-path] --parser docling --extensions pdf,docx,pptx --timeout 900
```

### 3. Timeout Configuration

| Operation | Default | Dual-Parser | Max |
|-----------|---------|-------------|-----|
| Single Document | 600s | 900s | 1800s |
| Batch Processing | 600s | 1800s | 3600s |
| Updates | 600s | 1200s | 2400s |
| Queries | 300s | 600s | 900s |

### 4. Querying

#### Query Modes
```bash
# Hybrid mode (default)
/home/sam/EVO/rag_cli --project [project-name] query "[question]" --mode hybrid

# Other modes
/home/sam/EVO/rag_cli --project [project-name] query "[question]" --mode naive
/home/sam/EVO/rag_cli --project [project-name] query "[question]" --mode local
/home/sam/EVO/rag_cli --project [project-name] query "[question]" --mode global
```

#### Mathematical Queries
```bash
# Extract mathematical formulas
/home/sam/EVO/rag_cli --project [project-name] query "what mathematical formulas are in the document?" --mode hybrid

# Find specific equations
/home/sam/EVO/rag_cli --project [project-name] query "quadratic equations and derivatives" --mode hybrid

# Mathematical relationships
/home/sam/EVO/rag_cli --project [project-name] query "how are these mathematical concepts related?" --mode global
```

## Parser Selection Guide

| Document Type | Parser | Reason |
|---------------|--------|--------|
| Scientific Papers | dual | Best equation extraction + multimodal |
| Mathematical Content | dual | 5x more equations than single parser |
| Technical Reports | dual | Comprehensive analysis |
| HTML with Math | mineru | Reliable HTML processing |
| General PDFs | docling | Better content structure |
| Images/OCR | mineru | Optimized for visual content |

## Workflow Examples

### Research Paper Analysis
```bash
# Process paper with dual-parser
/home/sam/EVO/rag_cli --project research process paper.pdf --parser dual --timeout 1200

# Query mathematical content
/home/sam/EVO/rag_cli --project research query "what mathematical formulas are in the document?"

# Check results
/home/sam/EVO/rag_cli --project research info
```

### Batch Scientific Collection
```bash
# Process collection
/home/sam/EVO/rag_cli --project science batch ~/papers/ --parser dual --extensions pdf,docx --timeout 2400

# Query relationships
/home/sam/EVO/rag_cli --project science query "How are the mathematical models related?" --mode global

# Incremental updates
/home/sam/EVO/rag_cli --project science update ~/papers/ --parser dual --extensions pdf,docx --timeout 1800
```

## Technical Features

### Multimodal Content Support
- Mathematical formulas: LaTeX equations, complex mathematical notation
- Tables: Data extraction and semantic understanding
- Images: Visual content analysis with vision models
- Text: Advanced semantic chunking and entity extraction
- HTML: Full HTML support with mathematical formula extraction
- PDFs: Complete PDF processing with multimodal content

### Database Features
- Separate database per project in `~/.rag_databases/`
- Smart update detection (file modification time and size)
- Processes only new/modified files
- Automatic fallback to batch processing for new databases
- Safe for concurrent operations

### Dual-Parser Features
- Combines Docling (superior equation extraction) + MinerU (HTML/images)
- 5x more equation extraction vs single parser
- Intelligent merge without duplication
- Fallback if one parser fails
- Production-ready with error handling

## Environment Requirements

- API Key: Set `OPENAI_API_KEY` environment variable
- Models: Uses `gpt-4o-mini` for text, `text-embedding-3-large` for embeddings
- Base URL: Optional `OPENAI_BASE_URL` for custom endpoints

## Integration Notes

Perfect integration with Claude Code workflow:
- `/rag_process list-projects` - See all available databases
- `/rag_process --project research query "question"` - Query specific database
- `/rag_process --project docs batch ~/folder/` - Process documentation folders
- `/rag_process --project docs update ~/folder/` - Keep databases synchronized

All data stored in `~/.rag_databases/[project-name]/` for easy backup and management.