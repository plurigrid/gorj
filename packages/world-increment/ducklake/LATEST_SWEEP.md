# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-07

## Sweep Metadata
- **Date:** 2026-05-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all sweeps) | 70 |
| Total Repo Snapshots (all sweeps) | 991 |
| Distinct Repos in DB | 475 |
| New kubeflow repos this sweep | 47 |
| Aptos wallets snapshotted | 28 |
| Multisig contracts probed | 5 |
| MNX instruments captured | 27 |

---

## JOB 1: GitHub Social Graph Sweep

### Source Coverage
| Source | Type | Status | Repos This Sweep |
|--------|------|--------|-----------------|
| kubeflow | org | ✓ fetched | 47 |
| plurigrid | org | rate-limited (prior data in DB) | — |
| TeglonLabs | org | rate-limited (prior data in DB) | — |
| bmorphism | user | rate-limited (prior data in DB) | — |
| zubyul | user | rate-limited (prior data in DB) | — |
| migalkin | user | rate-limited (prior data in DB) | — |
| DJedamski | user | rate-limited (prior data in DB) | — |
| wasita | user | rate-limited (prior data in DB) | — |
| kristinezheng | user | rate-limited (prior data in DB) | — |
| M1shaaa | user | rate-limited (prior data in DB) | — |
| AustinCStone | user | rate-limited (prior data in DB) | — |

> GitHub unauthenticated REST API (60 req/hr) exhausted after kubeflow fetch. All other sources have prior-sweep data in the database. Historical data preserved.

### GF(3) Color Chain — This Sweep (IDs 1–47)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 16 |
| 1 | `#b8bb26` | PLUS | 16 |
| -1 | `#cc241d` | MINUS | 15 |

GF(3) chain: `PLUS → MINUS → ERGODIC → ...` cycling every 3 increments.

### Top Kubeflow Repos (by Stars)

| Repo | Language | Stars | Forks | Description |
|------|----------|-------|-------|-------------|
| kubeflow/kubeflow | — | 15,625 | 2,647 | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | Python | 4,136 | 1,988 | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | Python | 3,124 | 1,483 | Kubernetes operator for Apache Spark on K8s |
| kubeflow/trainer | Go | 2,095 | 948 | Distributed AI Model Training + LLM Fine-Tuning on K8s |
| kubeflow/katib | Go | 1,683 | 522 | Kubernetes-native AutoML |
| kubeflow/examples | Jupyter | 1,461 | 756 | End-to-end examples |
| kubeflow/manifests | Shell | 1,015 | 1,069 | Kustomize configurations |
| kubeflow/arena | Go | 810 | 190 | CLI for deep learning on Kubernetes |

### Recently Active (pushed 2026-05)
- `kubeflow/kubeflow` — 2026-05-07T13:46:41Z
- `kubeflow/trainer` — 2026-05-07T07:26:14Z
- `kubeflow/pipelines` — 2026-05-07T01:34:49Z
- `kubeflow/spark-operator` — 2026-05-05T16:00:20Z

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Ledger Version:** 5,172,535,886 (epoch 15,715)  
**Block Height:** 753,108,878  
**Snapshot Time:** 2026-05-07  
**Total wallets:** 28 | **Total APT:** ~20.345 APT

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| bob | 0x0a3c...512d5d | **12.657007** |
| F | 0x18a1...c3cf71 | 1.960516 |
| L | 0x7c2e...7eba9 | 1.927269 |
| J | 0x4d96...87f54 | 1.895093 |
| alice | 0xc793...4cc7b | 0.436434 |
| O | 0x7325...5a89d | 0.210136 |
| K | 0xa732...25dc4 | 0.161961 |
| P | 0x6218...ec948 | 0.140136 |
| M | 0x6fed...7f2e9 | 0.112285 |
| N | 0xe7dd...551b2c | 0.106121 |
| Q | 0xac40...c89a9 | 0.103240 |
| S | 0xb875...d0386 | 0.091788 |
| R | 0x7ce6...76e10 | 0.090217 |
| T | 0x3578...f4588 | 0.073713 |
| U | 0x7586...f9956 | 0.055773 |
| A | 0x8699...e9d7a | 0.051767 |
| Y | 0xd8e3...444c4 | 0.044449 |
| X | 0xa95c...3047d | 0.042577 |
| V | 0xb59d...af2c3 | 0.048833 |
| W | 0x5f32...cc7b0 | 0.040705 |
| B | 0x3f89...cb13 | 0.036256 |
| Z | 0x7af0...197c | 0.024268 |
| C | 0x38b9...535e | 0.010185 |
| D | 0xf776...cfdd1 | 0.011629 |
| E | 0xdc1d...8d36 | 0.009372 |
| H | 0xce67...5300f | 0.001681 |
| G | 0x69a3...cf32 | 0.000681 |
| I | 0x070f...1fc9 | 0.000681 |

**Top holder:** `bob` with 12.657 APT (62.2% of total swarm balance)

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts respond healthy — **2-of-N signatures required**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...87003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi) — 27 Instruments

| Ticker | Name | Category | Price |
|--------|------|----------|-------|
| NVDA | NVIDIA | tech | $213.17 (+3.85%) |
| META | Meta | tech | $622.41 |
| MSFT | Microsoft | tech | $425.12 |
| TSLA | Tesla | tech | $412.28 |
| GOOGL | Alphabet | tech | $396.38 |
| AAPL | Apple | tech | $290.28 |
| AMZN | Amazon | tech | $273.05 |
| INTC | Intel | tech | $112.82 |
| MU | Micron | semiconductor | $668.41 |
| ASML | ASML | semiconductor | ~$1,500 |
| TSM | TSMC | semiconductor | $416.94 |
| OAI26 | OpenAI 2026 | ai_valuation | $519B |
| ANT26 | Anthropic 2026 | ai_valuation | $428B |
| ARC26 | ARC 2026 | ai_benchmark | 56% |
| ECI26 | ECI 2026 | ai_benchmark | 168 |
| GOLD | Gold | commodity | $4,800 |
| SILVER | Silver | commodity | $81.85 |
| USO | US Oil Fund | commodity | $128.78 |
| URA | Uranium | commodity | $58.27 |
| CPER | Copper | commodity | $37.82 |
| SPX | S&P 500 | index | 7,374 |
| VIX | Volatility | index | 17.11 |
| IEF | 7-10yr Treasury | bond | $95.16 |
| TLT | 20+yr Treasury | bond | $86.06 |
| DPREZ | DPREZ Political | political | 49% |
| INVADE27 | INVADE27 | political | 16% |
| CPI26 | CPI 2026 | political | 3% |

---

## Database Summary

| Table | Rows |
|-------|------|
| world_increments | 70 |
| repo_snapshots | 991 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 27 |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**

## Notable Highlights
- **kubeflow/kubeflow**: 15,625 stars — flagship ML platform (pushed today)
- **kubeflow/pipelines**: 4,136 stars — ML pipeline for K8s (pushed today)
- **kubeflow/trainer**: 2,095 stars — Distributed AI training + LLM fine-tuning (pushed today)
- **Aptos swarm**: `bob` holds 62.2% of total swarm APT (12.66 APT)
- **Multisig**: All 5 pairs (A-B, A-G, Y-Z, S-T, V-W) respond with 2-of-N — healthy
- **MNX testnet**: 27 instruments live including AI valuations (OAI26=$519B, ANT26=$428B)
- **Anthropic on MNX**: ANT26 valued at $428B on testnet prediction market
