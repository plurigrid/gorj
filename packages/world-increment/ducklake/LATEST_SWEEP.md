# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-02

## Sweep Metadata
- **Date:** 2026-06-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — 11 Increments

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 1  | TeglonLabs | org | 4 | +1 | `#b8bb26` | **PLUS** |
| 2  | plurigrid | org | 100 | -1 | `#cc241d` | **MINUS** |
| 3  | kubeflow | org | 48 | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | 100 | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 7 | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | 4 | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | 5 | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 4 | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | 4 | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | 6 | -1 | `#cc241d` | **MINUS** |

**Total repo snapshots: 331** (3 orgs + 8 users)

### Top Repos by Source

#### plurigrid (100 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| asi | HTML | 24 | 2026-04-26 |
| nash-portal | Rust | 2 | 2026-05-19 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| gorj | Clojure | 0 | **2026-06-02** |
| eirobri | Clojure | 0 | 2026-05-26 |

#### kubeflow (48 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| kubeflow | — | 15,702 | 2026-05-24 |
| pipelines | Python | 4,151 | **2026-06-02** |
| spark-operator | Python | 3,125 | 2026-06-01 |
| trainer | Go | 2,110 | **2026-06-02** |
| katib | Python | 1,685 | 2026-05-29 |

#### TeglonLabs (4 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

#### bmorphism (100 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| ocaml-mcp-sdk | OCaml | **61** | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| world | Python | 0 | **2026-06-02** |
| Gay.jl | Julia | 1 | **2026-06-02** |
| oxgame | OCaml | 0 | 2026-05-15 |

#### zubyul (49 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| WGCNA | HTML | 2 | 2023-07-05 |
| Nikolova_lab_data_analysis | R | 2 | 2023-06-16 |
| gay-world | Python | 1 | 2026-03-26 |
| voice-observatory | Python | 0 | 2026-04-24 |
| nash-tui | Rust | 0 | 2026-04-13 |

#### Social Graph (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)
| Repo | User | Language | Stars |
|------|------|----------|-------|
| NodePiece | migalkin | Python | 144 |
| StarE | migalkin | Python | 89 |
| TextGAN | AustinCStone | Python | 92 |
| StereoVisionMRF | AustinCStone | Python | 11 |
| kgcourse2021 | migalkin | HTML | 25 |
| wasita.github.io | wasita | Svelte | 1 |
| magic-garden | wasita | Python | 2 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, fullnode.mainnet.aptoslabs.com)

All 28 wallets queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
No wallet has a registered APT CoinStore — all return 0.0 APT. Addresses are live
on-chain (confirmed via multisig contract probes).

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793acd... | 0.0 |
| bob   | 0x0a3c00c... | 0.0 |
| A–Z   | (26 addresses) | 0.0 each |

### Multisig Contract Probes (0x1::multisig_account::num_signatures_required)

All 5 multisig contracts are healthy with threshold = 2.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

**Swarm governance intact: all 5 multisigs require 2-of-N threshold.**

### MNX Markets (testnet.mnx.fi)

`/api/markets` → 404 (SPA). Root page rendered live market data:

| Ticker | Name | Category | Price | Change |
|--------|------|----------|-------|--------|
| OAI26 | OpenAI Final 2026 Valuation | prediction | $529B | -1.12% |
| ANT26 | Anthropic Final 2026 Valuation | prediction | $419B | -0.24% |
| NVDA | NVIDIA | equity | $224.91 | +1.24% |
| TSLA | Tesla Inc | equity | $421.30 | +0.50% |
| MSFT | Microsoft | equity | $445.62 | -3.28% |
| AAPL | Apple | equity | $311.82 | +2.05% |
| AMZN | Amazon | equity | $259.04 | -1.42% |
| GOOGL | Alphabet (Google) | equity | $367.08 | -2.04% |
| META | Meta (Facebook) | equity | $607.82 | -0.73% |
| TSM | Taiwan Semiconductor | equity | $445.52 | +0.73% |
| ASML | ASML Holding | equity | $1,700 | +4.07% |
| VIX | CBOE Volatility Index | index | 16.02 | — |
| SPX | S&P 500 | index | 7,601 | — |
| GOLD | Gold | commodity | $4,500 | — |
| URA | Uranium ETF | etf | — | +5.69% |

---

## DuckDB Table Summary

```
world_increments    11 rows   GF3-colored sweep events
repo_snapshots     331 rows   GitHub repo snapshots
aptos_snapshots     28 rows   Hamming swarm wallet balances
multisig_probes      5 rows   Aptos multisig health checks
mnx_snapshots       15 rows   MNX market data
```

## GF(3) Assignment Rule

| id mod 3 | Trit | Color | Name |
|----------|------|-------|------|
| 0 | 0 | `#d3869b` (rose) | ERGODIC |
| 1 | +1 | `#b8bb26` (yellow-green) | PLUS |
| 2 | -1 | `#cc241d` (red) | MINUS |

## Schema
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

## Notable Highlights
- **kubeflow/kubeflow**: 15,702 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,151 stars — pushed 2026-06-02
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — GAN text generation in TensorFlow
- **migalkin/NodePiece**: 144 stars — ICLR'22 scalable KG embeddings
- **plurigrid/asi**: 24 stars — topological chemputer
- **plurigrid/gorj**: 305 open issues — this very repo, pushed 2026-06-02
- **Aptos swarm**: 28 wallets live, 5 multisigs all at 2-of-N threshold
- **MNX prediction**: OAI26 $529B (-1.12%), ANT26 $419B (-0.24%); ASML leads equities (+4.07%)
