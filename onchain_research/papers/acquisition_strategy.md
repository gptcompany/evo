# PDF Acquisition Strategy for CheckOnChain Research Papers

## Current Status: ❌ Direct Downloads Failed

All direct PDF download attempts failed due to:
- Publisher access restrictions
- Paywall protections  
- CORS/security blocks
- Redirect loops

## Target Papers

### 1. TFT SOPR Framework 2025 ⚠️ BLOCKED
- **Paper**: "Temporal Fusion Transformer-Based Trading Strategy for Multi-Crypto Assets Using On-Chain and Technical Indicators"
- **Author**: Ming Che Lee
- **Journal**: Systems (MDPI)
- **DOI**: 10.3390/systems13060474
- **Direct URL**: https://www.mdpi.com/2079-8954/13/6/474/pdf?version=1750055296
- **Status**: Access blocked by publisher

### 2. NUPL Market Efficiency 2022 ⚠️ BLOCKED  
- **DOI**: 10.2478/ijme-2022-0030
- **Direct URL**: https://sciendo.com/2/v2/download/article/10.2478/ijme-2022-0030.pdf
- **Status**: Redirects to AWS S3 with signed URLs (expires quickly)

### 3. Post-ETF MVRV Model 2025 ⚠️ BLOCKED
- **Direct URL**: https://enigma.or.id/index.php/economy/article/download/91/100/
- **Status**: Returns encoded PDF content, not downloadable

### 4. Bitcoin Mining Energy Efficiency 2023 ⚠️ BLOCKED
- **Paper**: "Energy and cost efficiency of Bitcoin mining endeavor"  
- **Authors**: Jabłczyńska, M. et al.
- **Journal**: PLOS ONE
- **DOI**: 10.1371/journal.pone.0283687
- **Direct URL**: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0283687&type=printable
- **Status**: Returns PDF metadata only

## Alternative Acquisition Methods

### Method A: Academic Database Access
- [ ] University library access
- [ ] Institutional subscriptions
- [ ] IEEE Xplore, ACM Digital Library
- [ ] ScienceDirect, SpringerLink

### Method B: Author Contact
- [ ] Email authors directly for preprints
- [ ] Check author personal/institutional pages
- [ ] Request via ResearchGate/Academia.edu

### Method C: Open Access Repositories  
- [ ] arXiv.org (preprints)
- [ ] SSRN (economics/finance papers)
- [ ] RePEc (economics papers)
- [ ] Institutional repositories

### Method D: Interlibrary Loan
- [ ] Request through academic libraries
- [ ] Document delivery services

## Next Steps

1. **Setup institutional access** if available
2. **Contact paper authors** via email/ResearchGate  
3. **Check preprint repositories**
4. **Use document delivery services**
5. **Monitor for open access versions**

## Metadata Extracted

### TFT SOPR Paper Details:
- **Abstract**: Integrates on-chain indicators (SOPR, TVL, Active Addresses, Exchange Net Flow, Realized Cap HODL Waves, Crypto Fear & Greed Index) with technical indicators (RSI, MACD)
- **Methodology**: Temporal Fusion Transformer vs LSTM, GRU, SVR, XGBoost
- **Assets**: BTC, ETH, USDT, XRP, BNB
- **Focus**: Multi-asset cryptocurrency forecasting and trading strategy optimization

### Mining Economics Paper Details:
- **Title**: "Energy and cost efficiency of Bitcoin mining endeavor"
- **Authors**: Małgorzata Jabłczyńska, Krzysztof Kosc, Przemysław Ryś, Paweł Sakowski, Robert Ślepaczuk, Grzegorz Zakrzewski  
- **Publication**: PLOS ONE, March 30, 2023
- **DOI**: 10.1371/journal.pone.0283687

## Alternative Research Sources

Based on arXiv searches, related papers found:
- "Adaptive Temporal Fusion Transformers for Cryptocurrency Price Prediction"
- "Comprehensive Modeling Approaches for Forecasting Bitcoin Transaction Fees"
- "Quantum Blockchain Miners Provide Massive Energy Savings" (2023)
- "Leveraging Surplus Electricity" for Bitcoin mining (2025)

## Recommendation

Focus on acquiring the **TFT SOPR paper** first as it directly addresses multiple CheckOnChain metrics (SOPR, TVL, Active Addresses, Exchange Net Flow) using advanced ML techniques.