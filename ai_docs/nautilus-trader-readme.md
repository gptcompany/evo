# NautilusTrader README

## Key Information for Production/Live Trading

### ⚠️ IMPORTANT PRODUCTION WARNING
**"We do not recommend using development wheels in production environments, such as live trading controlling real capital."**

### Latest Stable Version
- **Branch**: `master` (stable production release)
- **Release Schedule**: Bi-weekly releases
- **Installation**: Use official PyPI releases only for production

### System Requirements
#### Supported Platforms
- Linux (x86_64 and ARM64)
- macOS (ARM64)
- Windows (x86_64)

#### Software Requirements
- **Python**: 3.11-3.13
- **Rust**: 1.89.0 (for building from source)

### Production Installation Instructions
#### Recommended Method (PyPI)
```bash
pip install -U nautilus_trader
```

#### Alternative (Nautech Systems Package Index)
```bash
pip install -U nautilus_trader --pre --index-url=https://packages.nautechsystems.io/simple
```

#### Best Practices
- Use a virtual environment
- Recommended: Use `uv` package manager with vanilla CPython
- Install from stable `master` branch releases only

### Key Features & Architecture
#### Core Strengths
- **Performance**: Core written in Rust with asynchronous networking
- **Reliability**: Rust-powered type- and thread-safety
- **Event-driven architecture** with Python-native environment
- **High-frequency trading** capabilities
- **Identical strategy implementations** for backtesting and live trading

#### Supported Asset Classes
- FX (Foreign Exchange)
- Equities
- Futures
- Options
- Cryptocurrency
- DeFi

#### Advanced Trading Features
- Advanced order types and execution instructions
- Multiple venue support
- Real-time data processing
- Risk management systems

### Live Trading Capabilities & Setup
#### Supported Exchanges/Venues
- **Cryptocurrency**: Binance, Coinbase, dYdX
- **Traditional**: Interactive Brokers
- **Multiple other venues** (see full documentation)

#### Precision Modes
- **High-precision**: 128-bit integers, up to 16 decimal places
- **Standard-precision**: 64-bit integers, up to 9 decimal places

### Dependencies & Prerequisites
#### Core Dependencies
- Python 3.11-3.13
- Rust 1.89.0 (if building from source)
- Platform-specific build tools

#### Installation Dependencies
- Virtual environment management
- Package managers: pip (minimum) or uv (recommended)

### Production Deployment Considerations
#### Version Management
- **Production**: Use `master` branch releases only
- **Development**: `nightly` (daily snapshots) and `develop` branches available but NOT for production
- **Breaking Changes**: Potential breaking changes in active development

#### Performance Optimization
- Use recommended precision mode based on trading requirements
- Consider platform-specific optimizations (ARM64 vs x86_64)
- Utilize asynchronous networking capabilities

### Documentation & Support
- **Main Documentation**: https://nautilustrader.io/docs/
- **Website**: https://nautilustrader.io
- **Support**: support@nautilustrader.io

### Critical Production Notes
1. **Only use stable releases** from master branch for live trading
2. **Bi-weekly release cycle** - plan updates accordingly
3. **Rust-powered reliability** ensures type and thread safety
4. **High-performance core** suitable for HFT applications
5. **Multi-asset class support** with unified API
6. **Real capital warning** - development wheels explicitly not recommended for production

---

*This documentation extracted from NautilusTrader GitHub repository README.md for production deployment planning.*