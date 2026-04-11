# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-11 03:35 UTC
**Branch:** world-increment/sweep-2026-04-11-0335

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 98 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 99 |
| zubyul | user | 45 |
| migalkin | user (social graph) | 19 |
| AustinCStone | user (social graph) | 40 |
| wasita | user (social graph) | 9 |
| DJedamski | user (social graph) | 6 |
| kristinezheng | user (social graph) | 6 |
| M1shaaa | user (social graph) | 8 |
| **TOTAL** | | **366 unique repos** |

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,565 | - |
| kubeflow/pipelines | 4,119 | Python |
| kubeflow/spark-operator | 3,111 | Python |
| kubeflow/trainer | 2,080 | Go |
| kubeflow/katib | 1,676 | Python |
| kubeflow/examples | 1,458 | Jsonnet |
| kubeflow/manifests | 1,010 | YAML |
| kubeflow/arena | 808 | Go |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml |
| plurigrid/asi | 16 | HTML |

### Recently Active Repos (pushed < 48h ago)
- **plurigrid/gorj** – forj + Rama topology nREPL routing + GF(3) gay trit coloring (Clojure)
- **plurigrid/horse** – (TeX)
- **plurigrid/asi** – everything is topological chemputer! (HTML)
- **kubeflow/pipelines** – Machine Learning Pipelines for Kubeflow (Python)
- **kubeflow/model-registry** – Model Registry for ML models (Go)
- **bmorphism/boxxy** – (Move)
- **bmorphism/postweb** – postweb — evolved from prepostweb (Go)
- **zubyul/big-bad-plurigrid-quiz** – flashcards from plurigrid community (Emacs Lisp)
- **wasita/wm-cv** – Academic CV written as a single page web app (Svelte)
- **kristinezheng/kristinezheng.github.io** – personal site (HTML)

### GF(3) Color Chain
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 122 |
| +1 | PLUS | #b8bb26 | 122 |
| -1 | MINUS | #cc241d | 122 |

**Total world increments logged:** 366

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice + A–Z)
All 28 wallets probed via Aptos mainnet fullnode API.
```
Endpoint: https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>
Status: All wallets returned 0 APT
Note: Addresses exist on-chain but hold no native APT CoinStore balance
      (funds may be held as object-based fungible assets or wallets are empty)
```

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ace... | 0.00 |
| bob   | 0x0a3c00c... | 0.00 |
| A | 0x8699edc... | 0.00 |
| B | 0x3f892eb... | 0.00 |
| C | 0x38b99e6... | 0.00 |
| D | 0xf776562... | 0.00 |
| E | 0xdc1d9d5... | 0.00 |
| F | 0x18a14b5... | 0.00 |
| G | 0x69a394c... | 0.00 |
| H | 0xce67c32... | 0.00 |
| I | 0x070fe5d... | 0.00 |
| J | 0x4d964db... | 0.00 |
| K | 0xa732040... | 0.00 |
| L | 0x7c2eaea... | 0.00 |
| M | 0x6fed37a... | 0.00 |
| N | 0xe7dde6d... | 0.00 |
| O | 0x73252b6... | 0.00 |
| P | 0x6218792... | 0.00 |
| Q | 0xac40fa5... | 0.00 |
| R | 0x7ce605c... | 0.00 |
| S | 0xb875301... | 0.00 |
| T | 0x35781dc... | 0.00 |
| U | 0x75860da... | 0.00 |
| V | 0xb59dd81... | 0.00 |
| W | 0x5f32aef... | 0.00 |
| X | 0xa95cbbd... | 0.00 |
| Y | 0xd8e3284... | 0.00 |
| Z | 0x7af0ef6... | 0.00 |

### Multisig Contract Probes
| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f42... | 2 | ✅ healthy |
| A-G | 0xf56c4a1... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe18... | 2 | ✅ healthy |
| S-T | 0x3b1c3ae... | 2 | ✅ healthy |
| V-W | 0x40fad7b... | 2 | ✅ healthy |

All 5 multisig contracts healthy — 2-of-2 threshold confirmed via `0x1::multisig_account::num_signatures_required`.

### MNX Markets (testnet.mnx.fi)
MNX is "The AI Exchange" — a prediction market platform with 30+ tradable assets.

| Ticker | Name | Category | Price | Change |
|--------|------|----------|-------|--------|
| OAI26 | OpenAI Final 2026 Valuation | Valuations | 20B | -1.70% |
| ANT26 | Anthropic Final 2026 Valuation | Valuations | 24B | +1.68% |
| AAPL | Apple | Stocks | 60.65 | +0.39% |
| ASML | ASML Holding | Stocks | ,500 | +2.34% |
| NVDA | NVIDIA | Stocks | 88.49 | +2.83% |
| MSFT | Microsoft | Stocks | - | - |
| TSLA | Tesla | Stocks | - | - |
| SPY | S&P 500 | Financial | - | - |
| GLD | Gold | Commodities | - | - |
| ARCAGI2 | Arc AGI 2 | AI | - | - |
| FRONTIERMATH | FrontierMath | AI | - | - |
| H100 | H100 GPU pricing | Compute | - | - |
| POLS | 2028 Election | Politics | - | - |
| CPI | CPI Index | Financial | - | - |

---

## DuckDB Schema

```
packages/world-increment/ducklake/world-increments.duckdb
  → world_increments   (366 rows) — GF(3) trit-colored event log
  → repo_snapshots     (366 rows) — GitHub repo metadata snapshots
  → aptos_snapshots    (28 rows)  — Hamming swarm wallet balances
  → multisig_probes    (5 rows)   — On-chain multisig threshold checks
  → mnx_snapshots      (15 rows)  — MNX prediction market prices
```

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent*
*GF(3) color chain: ERGODIC(#d3869b) → PLUS(#b8bb26) → MINUS(#cc241d)*
