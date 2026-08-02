# World Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-08-02 21:12:53 UTC
**Branch:** world-increment/sweep-2026-08-02-2112

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|---|---|---|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 12 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 41 |
| **TOTAL** | | **394** |

### Top Starred Repos (GF(3) sweep)
| Repo | Stars | Forks | Last Push |
|---|---|---|---|
| kubeflow/kubeflow | 15,803 | 2,690 | 2026-07-10 |
| kubeflow/pipelines | 4,173 | 2,074 | 2026-08-02 |
| kubeflow/spark-operator | 3,142 | 1,509 | 2026-07-31 |
| kubeflow/trainer | 2,165 | 1,008 | 2026-07-31 |
| kubeflow/katib | 1,694 | 534 | 2026-08-02 |
| migalkin/NodePiece | 144 | 21 | 2026-05-07 |
| plurigrid/asi | 58 | 13 | 2026-07-10 |
| migalkin/StarE | 89 | 16 | 2026-04-16 |
| bmorphism/Gay.jl | 2 | 1 | 2026-08-02 |
| plurigrid/gorj | 1 | 0 | 2026-08-02 |

### Notable Recent Activity
- **plurigrid/gorj** (Clojure) — pushed 2026-08-02: "forj + Rama topology nREPL routing + GF(3) gay trit coloring"
- **plurigrid/zig-syrup** (Zig) — pushed 2026-07-28: "High-performance OCapN Syrup with CapTP optimizations"
- **plurigrid/place** (TeX) — pushed 2026-08-02: active BCI place forest
- **bmorphism/Gay.jl** (Julia) — pushed 2026-08-02: "Wide-gamut color sampling with splittable determinism (SPI pattern)"
- **TeglonLabs/jank-crane** (C++) — pushed 2026-06-08: "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"
- **kubeflow/mcp-server** (Python) — 31 stars: "MCP Server for AI-Assisted Development with Kubeflow Tools"
- **wasita/wasita.github.io** (Svelte) — pushed 2026-07-21

### GF(3) Color Chain Distribution
- **ERGODIC** (trit=0, #d3869b): id%3==0 — 106 repos
- **PLUS** (trit=1, #b8bb26): id%3==1 — 106 repos
- **MINUS** (trit=-1, #cc241d): id%3==2 — 105 repos

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)
All 28 Hamming-swarm addresses (alice, bob, A–Z) queried on Aptos Mainnet.

| World | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | 0xc793...7b | 0.00 |
| bob | 0x0a3c...5d | 0.00 |
| A–Z | 0x8699...7a – 0x7af0...7c | 0.00 each |

**Result:** All 28 addresses hold 0 APT. No CoinStore resources found — accounts are either unfunded or the coin resource has not been initialized. This is consistent with clean/placeholder addresses on Aptos mainnet.

### Multisig Contract Probes (5 pairs)
| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...03 | 2 | ✓ |
| A-G | 0xf56c...96 | 2 | ✓ |
| Y-Z | 0xd3ff...83 | 2 | ✓ |
| S-T | 0x3b1c...83 | 2 | ✓ |
| V-W | 0x40fa...6d | 2 | ✓ |

**Result:** All 5 multisig contracts respond and require 2 signatures. All healthy.

### MNX Markets (testnet.mnx.fi)
- `/api/markets` endpoint: **404 / not found**
- Root `https://testnet.mnx.fi`: Returns Next.js SPA HTML (no embedded market data)
- **Status:** MNX testnet API is SPA-rendered; no REST market data accessible without browser JS execution. Market data recorded as unavailable.

---

## DuckDB Ducklake State

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (cumulative) |
|---|---|
| world_increments | 340+ |
| repo_snapshots | 1,261+ |
| aptos_snapshots | 28 (this sweep) |
| multisig_probes | 5 (this sweep) |
| mnx_snapshots | 0 (unavailable) |

