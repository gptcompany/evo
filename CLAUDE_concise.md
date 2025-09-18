# Global Development Preferences

## Coding Standards
- Write type hints for all functions (Python ≥3.11, TypeScript preferred over JavaScript)
- Use functional programming patterns and immutable data structures
- Implement async/await patterns for concurrent operations
- Write comprehensive error handling with proper exception types
- Follow semantic commit messages and meaningful variable names
- Use composition over inheritance
- Keep functions pure and side-effect free when possible

## Performance-First Philosophy
- **ALWAYS choose 10x faster tools**: uv > pip, bun > npm, ruff > black/pylint
- **Search optimized**: fd > find, rg > grep, exa > ls
- **Runtime performance**: Rust/Go > Python > JavaScript for compute-heavy tasks
- **Avoid premature optimization but measure everything**
- **Choose native tools over interpreted when possible**

## Security Practices
- Always validate input parameters at boundaries
- Use environment variables for secrets, never hardcode
- Implement proper authentication and authorization checks
- Follow OWASP security guidelines and threat modeling
- Use parameterized queries, never string concatenation for SQL
- Apply principle of least privilege for all system access
- Regular dependency auditing and updates

## Testing & Quality Assurance
- **TDD workflow**: Red-Green-Refactor with automatic enforcement
- Write unit tests for all pure functions
- Integration tests for API endpoints and external dependencies
- Use property-based testing for complex logic
- Maintain >90% code coverage but focus on meaningful tests
- Performance benchmarks for critical paths
- Static analysis with strict linting rules

## Documentation Standards
- Include comprehensive docstrings/JSDoc for all public functions
- Maintain clear README files with setup and usage examples
- Document API endpoints with request/response examples
- Architecture Decision Records (ADRs) for significant design choices
- Keep documentation co-located with code when possible
- Use diagrams for complex system interactions

## Architecture Principles
- **Favor composition over inheritance**
- **Dependency injection for testability**
- **Event-driven architecture for loose coupling**
- **Immutable data structures where feasible**
- **Clear separation of concerns and single responsibility**
- **Fail fast with meaningful error messages**
- **Design for observability from the start**

## Tool Preferences by Category
- **Package Management**: uv (Python), bun (JavaScript), cargo (Rust)
- **Linting/Formatting**: ruff (Python), ESLint (JavaScript), clippy (Rust)
- **Testing**: pytest (Python), Vitest (JavaScript), built-in (Rust/Go)
- **Database**: PostgreSQL > SQLite > MySQL, avoid NoSQL unless specific need
- **Containers**: Docker with multi-stage builds, prefer Alpine base images
- **Version Control**: Git with conventional commits, trunk-based development