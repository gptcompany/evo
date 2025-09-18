# TDD Guard Documentation

**Source:** https://github.com/nizos/tdd-guard

## Overview

TDD Guard is an automated Test-Driven Development (TDD) enforcement tool designed specifically for Claude Code. It ensures developers follow TDD principles by blocking implementation without failing tests and preventing over-implementation.

## Purpose

"TDD Guard ensures Claude Code follows Test-Driven Development principles. When your agent tries to skip tests or over-implement, TDD Guard blocks the action"

## Key Features

### Test-First Enforcement
- Blocks implementation without failing tests
- Ensures tests are written before code implementation
- Prevents skipping the testing phase in TDD workflow

### Minimal Implementation
- Prevents over-implementation of features
- Enforces writing only the minimum code needed to pass tests
- Maintains TDD's incremental development approach

### Multi-Language Support
- **TypeScript** - Full support with framework integration
- **JavaScript** - Complete TDD enforcement capabilities
- **Python** - Works with pytest and other testing frameworks
- **PHP** - Integration with PHPUnit
- **Go** - Support for Go 1.24+ testing
- **Rust** - Works with cargo and cargo-nextest

### Integration Features
- **Lint Integration** - Works with existing linting tools
- **Customizable Rules** - Flexible validation rules for different projects
- **Session Control** - Ability to toggle TDD enforcement on/off
- **Flexible Validation** - Adapts to different project structures and requirements

## Requirements

### System Requirements
- **Node.js 22+** - Required for TDD Guard runtime
- **Claude Code** or **Anthropic API key** - For AI integration
- **Test Framework** - Language-specific testing framework

### Language-Specific Requirements
- **JavaScript/TypeScript**: Jest, Vitest, or similar
- **Python**: pytest or other Python testing frameworks
- **PHP**: PHPUnit
- **Go**: Go 1.24+ built-in testing
- **Rust**: cargo or cargo-nextest

## Installation

### Global NPM Installation
```bash
npm install -g tdd-guard
```

### Homebrew Installation
```bash
brew install tdd-guard
```

## Core Functionality

### TDD Workflow Enforcement
TDD Guard integrates with Claude Code hooks to validate coding operations and ensure adherence to TDD principles:

1. **Red Phase**: Ensures failing tests exist before implementation
2. **Green Phase**: Allows minimal implementation to pass tests
3. **Refactor Phase**: Permits code improvements while maintaining test coverage

### Integration Mechanism
- Uses language-specific test reporters (e.g., tdd-guard-vitest, tdd-guard-jest)
- Captures test results in real-time
- Validates coding operations through Claude Code hooks
- Provides immediate feedback on TDD violations

### Validation Rules
- **Test-First Rule**: No implementation without failing tests
- **Minimal Implementation Rule**: Prevents over-engineering
- **Test Coverage Rule**: Ensures adequate test coverage
- **Incremental Development Rule**: Enforces small, iterative changes

## Setup Process

### Basic Setup
1. **Install TDD Guard** using npm or Homebrew
2. **Add Language-Specific Reporter** for your testing framework
3. **Configure Claude Code Hooks** to integrate with TDD Guard
4. **Configure Validation Rules** based on project requirements

### Security Considerations
⚠️ **Important Security Note**: Hooks execute with full user permissions. Users should carefully review security considerations and understand the implications of automated code validation.

## Project Information

### License
- **MIT License** - Open source and freely available

### Community
- **Open Source Project** - Welcomes contributions from developers
- **Active Maintenance** - Ongoing development and support
- **Framework Expansion** - Continuously adding support for new languages and frameworks

### Repository
- **GitHub**: https://github.com/nizos/tdd-guard
- **Issues**: Community-driven issue tracking and feature requests
- **Contributions**: Pull requests welcome for improvements and new features

## Use Cases

### Development Teams
- Enforce TDD practices across team members
- Maintain consistent development methodology
- Reduce technical debt through proper testing

### Educational Environments
- Teach proper TDD methodology
- Provide automated feedback on TDD compliance
- Ensure students follow best practices

### Enterprise Projects
- Maintain code quality standards
- Enforce development process compliance
- Integrate with existing CI/CD pipelines

## Technical Architecture

### Hook-Based System
TDD Guard operates through Claude Code's hook system, intercepting and validating development actions before they are executed.

### Reporter Integration
Language-specific reporters capture test execution results and communicate with TDD Guard to determine if development actions should be allowed.

### Rule Engine
Customizable validation rules allow teams to define their specific TDD requirements and enforcement policies.

## Benefits

### Code Quality
- Higher test coverage
- More reliable software
- Reduced bugs in production

### Development Process
- Consistent TDD methodology
- Faster feedback loops
- Better code design through test-first thinking

### Team Productivity
- Automated process enforcement
- Reduced code review overhead
- Standardized development practices