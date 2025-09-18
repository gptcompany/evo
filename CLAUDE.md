# Project: EVO

Evolutionary multi-agent orchestration system that learns and optimizes autonomously through evolutionary algorithms.

## Architecture Overview
- **Core Language**: Python ≥3.11 with async/await patterns
- **AI Framework**: Pydantic AI for data validation and models
- **Orchestration**: Claude Code MCP framework
- **Document Processing**: RAG-Anything with dual-parser (Docling + MinerU)
- **Data Storage**: SQLite/PostgreSQL for evolution data
- **Testing**: Python (pytest) + JavaScript (Vitest) with TDD Guard
- **Package Management**: uv (Python) + bun (JavaScript)

## Development Guidelines
- Use performance-first tools: `uv` not `pip`, `bun` not `npm`, `ruff` not `black`
- Write type hints for all Python functions (≥3.11 syntax)
- Implement TDD workflow with automatic enforcement via hooks
- Use async/await patterns for concurrent operations
- Follow Pydantic models for data validation
- Use dual-parser for scientific documents with mathematical content
- Apply semantic commit messages

## Key Files
- `/src/` - Main source code (Python CLI tools and core logic)
- `/tests/` - Test files for both Python (pytest) and JavaScript (Vitest)
- `/.claude/` - Claude Code configurations, agents, and hooks
- `/rag_storage/` - RAG system data and processed documents
- `pyproject.toml` - Python dependencies and tool configuration
- `package.json` - JavaScript dependencies and scripts

## Essential Commands

### Setup
```bash
uv sync --group dev     # Python environment
bun install             # JavaScript environment
```

### Testing & Quality
```bash
bun test               # JS tests (fastest)
uv run pytest         # Python tests
bun run lint           # ESLint check
uv run ruff check .    # Python linting
```

### RAG Operations
```bash
./rag_cli process /path/to/doc --parser dual    # Dual-parser (recommended)
./rag_cli query "your question"                 # Query RAG system
```

## Environment Setup
Required variables in `.env`:
```bash
OPENAI_API_KEY=your_key
LINTER_TYPE=eslint
PARSER=dual
```