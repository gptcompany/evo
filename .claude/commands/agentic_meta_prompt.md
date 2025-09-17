---
description: Build dynamic agentic prompts using structured sections
argument-hint: [prompt topic] [target sections]
allowed-tools: Write, Edit, Read
---

# Agentic Meta Prompt

Build structured prompts dynamically using ordered agentic prompt sections.

## Variables

PROMPT_TOPIC: $1
TARGET_SECTIONS: $2 (defaults to core sections if not specified)

## Instructions

- Select relevant sections from the agentic prompt library based on PROMPT_TOPIC
- Use core sections: Variables, Instructions, Workflow, Report
- Add specialized sections as needed: Metadata, Purpose, Relevant Files, Codebase Structure, Expertise, Template, Examples
- Structure sections in logical order for the specific use case
- Keep content focused and actionable

## Workflow

1. Analyze PROMPT_TOPIC to determine required sections
2. Select from available agentic sections:
   - `Metadata` - Context and parameters
   - `# Title` - Main heading
   - `## Purpose` - Clear objective statement  
   - `## Variables` - Input parameters and defaults
   - `## Instructions` - Core behavioral guidelines
   - `## Relevant Files` - Required file references
   - `## Codebase Structure` - Technical architecture context
   - `## Workflow` - Step-by-step execution plan
   - `## Expertise` - Domain-specific knowledge requirements
   - `## Template` - Output format specifications
   - `## Examples` - Usage demonstrations
   - `## Report` - Final output structure
3. Generate structured prompt with selected sections
4. Save to appropriate command file

## Report

Output the complete prompt structure with:
- Selected sections and rationale
- File path where prompt was saved
- Usage instructions for the new prompt
