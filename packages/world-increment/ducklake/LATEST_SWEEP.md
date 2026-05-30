# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-30

## Sweep Metadata
- **Date:** 2026-05-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted (127 repos across 11 orgs/users)

| Source | Type | Repos (sampled) | Total Stars |
|--------|------|-----------------|-------------|
| plurigrid | org | 45 | 68 |
| kubeflow | org | 19 | 32,244 |
| TeglonLabs | org | 4 | 2 |
| bmorphism | user | 20 | 210 |
| zubyul | user | 15 | 8 |
| migalkin | user | 6 | 276 |
| wasita | user | 6 | 4 |
| AustinCStone | user | 5 | 103 |
| DJedamski | user | 3 | 2 |
| M1shaaa | user | 2 | 0 |
| kristinezheng | user | 2 | 0 |
| **Total** | | **127** | **32,917** |

### GF(3) Color Chain Distribution (127 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 1 | `#b8bb26` | PLUS | 43 |
| -1 | `#cc241d` | MINUS | 42 |
| 0 | `#d3869b` | ERGODIC | 42 |

### Notable Repos

**plurigrid (org):**
- `gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring (257 open issues)
- `asi` — everything is topological chemputer! (23 ⭐)
- `eirobri` — EiRoBri replay world (28 open issues)
- `nanoclj-zig` — NaN-boxed Clojure interpreter in Zig 0.15
- `nash-portal` — NASH token TUI in the browser (Rust)

**kubeflow (org):**
- `kubeflow/kubeflow` — Machine Learning Toolkit for Kubernetes (15,686 ⭐)
- `kubeflow/spark-operator` — Kubernetes operator for Apache Spark (3,124 ⭐)
- `kubeflow/pipelines` — Machine Learning Pipelines (4,150 ⭐)
- `kubeflow/trainer` — Distributed AI Model Training and LLM Fine-Tuning (2,107 ⭐)

**bmorphism (user):**
- `ocaml-mcp-sdk` — OCaml SDK for Model Context Protocol (61 ⭐)
- `anti-bullshit-mcp-server` — MCP server for detecting manipulation (23 ⭐)
- `risc0-cosmwasm-example` — CosmWasm + zkVM RISC-V EFI template (23 ⭐)
- `say-mcp-server` — macOS text-to-speech MCP server (20 ⭐)
- `Gay.jl` — Wide-gamut color sampling with splittable determinism (189 open issues)

**TeglonLabs (org):**
- `mathpix-gem` — Transform mathematical images to LaTeX (Ruby)
- `coin-flip-mcp` — MCP server for coins with varying randomness from random.org

**migalkin (user) — KG researcher:**
- `NodePiece` — Compositional Representations for Large Knowledge Graphs (144 ⭐)
- `StarE` — Message Passing for Hyper-Relational Knowledge Graphs (89 ⭐)
- `RWL` — Weisfeiler and Leman Go Relational (active 2026-05-28)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 28 wallets)

All wallets queried via `fullnode.mainnet.aptoslabs.com`. All returned **0.0 APT** — addresses appear empty/uninitialized on mainnet.

| Range | Wallets | Total APT |
|-------|---------|----------:|
| alice, bob | 2 | 0.0 |
| A–N | 14 | 0.0 |
| O–Z | 12 | 0.0 |
| **All 28** | | **0.0 APT** |

### Multisig Contract Probes (5 pairs, all healthy)

| Pair | Address (truncated) | Sigs Required | Status |
|------|--------------------|--------------:|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

**All 5 multisig contracts responding — 2-of-N threshold confirmed on Aptos mainnet.**

### MNX Markets (testnet.mnx.fi — SPA, no REST API)

#### Stocks (top movers)
| Ticker | Name | Price | Change |
|--------|------|------:|-------:|
| MU | Micron Technology | $961.36 | +2.91% |
| MSFT | Microsoft | $448.55 | **+5.16%** |
| META | Meta | $632.30 | -0.20% |
| TSLA | Tesla | $435.09 | -1.42% |
| NVDA | NVIDIA | $213.01 | -0.69% |
| INTC | Intel | $115.79 | **-4.43%** |
| GOOGL | Alphabet | $380.32 | -2.31% |
| AAPL | Apple | $310.82 | -0.19% |
| AMZN | Amazon | $270.25 | -0.88% |
| TSM | Taiwan Semi | $419.30 | -1.46% |

#### Indices & Commodities
| Ticker | Name | Price | Change |
|--------|------|------:|-------:|
| SPX | S&P 500 | 7,575 | +0.28% |
| GOLD | Gold Spot | $4,500 | +1.02% |
| SILVER | Silver | $75.38 | -0.49% |
| VIX | Volatility | 15.32 | -2.85% |
| USO | Oil Fund | $129.00 | -0.79% |

#### Event Contracts
| Ticker | Description | Price | Change |
|--------|-------------|------:|-------:|
| OAI26 | OpenAI Final 2026 Valuation | $531B | -0.38% |
| ANT26 | Anthropic Final 2026 Valuation | $417B | -0.71% |
| DPREZ | Democrat 2028 President | 50% | +0.80% |
| INVADE27 | Taiwan invasion before 2027 | 17% | **+6.29%** |

---

## Database Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## Row Counts

```
world_increments:   127  (GF3 color chain, PLUS=43 / MINUS=42 / ERGODIC=42)
repo_snapshots:     127  (11 orgs/users, 32,917 total stars)
aptos_snapshots:     28  (alice, bob, A–Z — all 0.0 APT)
multisig_probes:      5  (all healthy, 2-of-N)
mnx_snapshots:       19  (stocks, indices, events)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

---

*Sweep generated autonomously — 2026-05-30*
