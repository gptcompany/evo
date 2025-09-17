---
allowed-tools: Bash, Read
description: Load context for a new agent session by analyzing codebase structure and README
---
# Prime
> Execute the following sections to understand the codebase then summarize your understanding.

## Run
git ls-files

## Read
@README.md

## Read and Execute
@ai_docs/README.md

## Context
- Codebase structure git accessible: !`git ls-files`
- Codebase structure all: !`eza . --tree`
- Project README: @README.md
- Documentation: 
  - @ai_docs/*.md
