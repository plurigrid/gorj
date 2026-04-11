# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-11  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC `#d3869b` | id%3==1 → trit=1 PLUS `#b8bb26` | id%3==2 → trit=-1 MINUS `#cc241d`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources queried

| Source | Type | Repos captured |
|--------|------|---------------|
| plurigrid | org | 20 |
| TeglonLabs | org | 20 |
| kubeflow | org | 0 (rate-limited / private) |
| bmorphism | user | 7 |
| migalkin | user | 5 |
| wasita | user | 4 |
| DJedamski | user | 2 |
| M1shaaa | user | 4 |
| AustinCStone | user | 5 |
| zubyul | user | 0 (no public repos) |
| kristinezheng | user | 0 (no public repos) |

**Total world_increments:** 66 (GF3-colored repo push events)

### GF(3) Color Distribution

| Color | Trit | Name | Count |
|-------|------|------|-------|
| `#d3869b` | 0 | ERGODIC | 22 (ids: 3,6,9,...,66) |
| `#b8bb26` | +1 | PLUS | 22 (ids: 1,4,7,...,64) |
| `#cc241d` | -1 | MINUS | 22 (ids: 2,5,8,...,65) |

### Notable repos (most-starred)

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| migalkin/StarE | 88 | Python | EMNLP 2020 hyper-relational KG message passing |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | OCaml SDK for MCP (Jane Street oxc) |
| migalkin/kgcourse2021 | 25 | HTML | Knowledge Graphs course 2021 |
| plurigrid/asi | 16 | HTML | Topological chemputer ASI |
| bmorphism/shitcoin | 5 | Python | CW20 denom for permissionless degeneracy |

### Most recently active repos

| Repo | Pushed | Language |
|------|--------|----------|
| plurigrid/gorj | 2026-04-11T19:24:49Z | Clojure |
| M1shaaa/M1shaaa | 2026-04-11T12:51:31Z | — |
| plurigrid/nanoclj-zig | 2026-04-09T19:53:30Z | Zig |
| bmorphism/boxxy | 2026-04-09T12:27:25Z | Move |
| wasita/wm-cv | 2026-04-08T22:54:06Z | Svelte |

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-04-11)

Queried via `0x1::coin::balance` view function. All 28 addresses live on mainnet.  
Note: accounts use FungibleAsset standard (legacy CoinStore not registered).

| World | APT Balance | Address (prefix) |
|-------|------------|-----------------|
| bob | **12.657007** | `0x0a3c00c5...` |
| F | **1.960516** | `0x18a14b5b...` |
| L | **1.927269** | `0x7c2eaeaf...` |
| J | **1.895093** | `0x4d964db8...` |
| alice | 0.436434 | `0xc793acde...` |
| O | 0.210136 | `0x73252b60...` |
| K | 0.161961 | `0xa732040a...` |
| P | 0.140136 | `0x62187926...` |
| M | 0.112285 | `0x6fed37a7...` |
| N | 0.106121 | `0xe7dde6da...` |
| Q | 0.103240 | `0xac40fa50...` |
| S | 0.091788 | `0xb8753014...` |
| R | 0.090217 | `0x7ce605cc...` |
| T | 0.073713 | `0x35781dc0...` |
| U | 0.055773 | `0x75860da4...` |
| A | 0.051767 | `0x8699edc0...` |
| V | 0.047833 | `0xb59dd817...` |
| Y | 0.044449 | `0xd8e32848...` |
| X | 0.042577 | `0xa95cbbd1...` |
| W | 0.040705 | `0x5f32aef7...` |
| B | 0.036256 | `0x3f892ebe...` |
| Z | 0.023268 | `0x7af0ef6e...` |
| E | 0.012561 | `0xdc1d9d53...` |
| D | 0.011629 | `0xf7765624...` |
| C | 0.010185 | `0x38b99e63...` |
| G | 0.000681 | `0x69a394c0...` |
| H | 0.000681 | `0xce67c327...` |
| I | 0.000681 | `0x070fe5d7...` |

**Total swarm balance:** ~22.16 APT

### Multisig Contract Probes (5/5 healthy)

| Pair | sigs_required | Address (prefix) | Status |
|------|--------------|-----------------|--------|
| A-B | 2 | `0x0da4f428...` | HEALTHY |
| A-G | 2 | `0xf56c4a1c...` | HEALTHY |
| Y-Z | 2 | `0xd3ffe181...` | HEALTHY |
| S-T | 2 | `0x3b1c3ae9...` | HEALTHY |
| V-W | 2 | `0x40fad7b4...` | HEALTHY |

All contracts require 2-of-N signatures. Probed via `0x1::multisig_account::num_signatures_required`.

### MNX Markets (testnet.mnx.fi, 30 instruments)

Data from SPA at `testnet.mnx.fi`. 6 categories: AI/Tech, Stocks, Commodities, Indices, Political, Bonds.

#### AI/Tech Valuations
| Ticker | Name | Price | D24h |
|--------|------|-------|------|
| OAI26 | OpenAI 2026 Valuation | $530B | +0.95% |
| ANT26 | Anthropic 2026 Valuation | $421B | -1.86% |
| ARC26 | Arc AGI 2 Score | 60% | +7.14% |
| ECI26 | Epoch Index 2026 | 166 | -1.19% |
| FMATH26 | FrontierMath Score | 47% | 0.00% |

#### Equities (selected)
| Ticker | Price | D24h |
|--------|-------|------|
| NVDA | $188.63 | -0.20% |
| MSFT | $371.92 | +0.15% |
| TSLA | $351.74 | +1.40% |
| META | $630.21 | +0.42% |
| MU | $420.07 | -0.63% |
| ASML | $1,483 | -0.07% |
| CRWV | $102.92 | +1.21% |

#### Commodities, Indices & Compute
| Ticker | Name | Price | D24h |
|--------|------|-------|------|
| GOLD | Gold | $4,744 | -0.21% |
| SPX | S&P 500 | 6,813 | +0.10% |
| VIX | Volatility Index | 19.23 | -2.04% |
| H100 | H100 GPU Hour | $2.82 | +0.36% |

#### Political/Economic Futures
| Ticker | Name | Price |
|--------|------|-------|
| DPREZ | Democrat 2028 Presidency | 51% (+2.02%) |
| INVADE27 | Taiwan Invasion 2027 | 16% (-5.85%) |
| CPI26 | US CPI 2026 | 2.57% |

---

## DuckDB Table Counts

```
world_increments  — 66 rows  (GF3-colored repo push events)
repo_snapshots    — 66 repos (org/user -> repo metadata)
aptos_snapshots   — 28 rows  (Hamming swarm alice+bob+A..Z)
multisig_probes   —  5 rows  (A-B, A-G, Y-Z, S-T, V-W)
mnx_snapshots     — 30 rows  (MNX testnet market instruments)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` -> trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` -> trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` -> trit=-1, color=#cc241d, name=MINUS

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

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent.*
