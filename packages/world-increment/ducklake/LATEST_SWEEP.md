# World-Increment Sweep + Hamming Snapshot
**Generated:** 2026-05-02 23:09 UTC
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources
| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 50 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | zubyul-social | 19 |
| DJedamski | zubyul-social | 6 |
| wasita | zubyul-social | 10 |
| kristinezheng | zubyul-social | 6 |
| M1shaaa | zubyul-social | 8 |
| AustinCStone | zubyul-social | 30 |

**Total repos snapshotted:** 279

### GF(3) Color Chain
| trit | name | color |
|------|------|-------|
| 0 | ERGODIC | #d3869b (rose) |
| +1 | PLUS | #b8bb26 (green) |
| -1 | MINUS | #cc241d (red) |

Current increment: `trit=1 PLUS #b8bb26`

### Notable Active Repos (by push date)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| plurigrid/gorj | Clojure | 0 | 2026-05-02 |
| bmorphism/Gay.jl | Julia | 1 | 2026-05-02 |
| M1shaaa/M1shaaa | - | 0 | 2026-05-02 |
| kubeflow/hub | Go | 174 | 2026-05-01 |
| kubeflow/pipelines | Python | 4130 | 2026-05-01 |
| kubeflow/notebooks | - | 71 | 2026-05-01 |
| kubeflow/trainer | Go | 2095 | 2026-05-01 |
| kubeflow/community | Jsonnet | 196 | 2026-05-01 |
| kubeflow/kale | Python | 684 | 2026-04-30 |
| kubeflow/dashboard | TypeScript | 17 | 2026-04-30 |
| kubeflow/manifests | YAML | 1013 | 2026-04-30 |
| plurigrid/zig-syrup | Zig | 2 | 2026-04-30 |
| bmorphism/boxxy | Move | 0 | 2026-04-30 |
| kubeflow/sdk | Python | 111 | 2026-04-29 |
| plurigrid/horse | TeX | 1 | 2026-04-29 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)
| World | Address | Balance APT |
|-------|---------|-------------|
| alice | `0xc793acde...24cc7b` | 0.00000000 |
| bob | `0x0a3c00c5...512d5d` | 0.00000000 |
| A | `0x8699edc0...be9d7a` | 0.00000000 |
| B | `0x3f892ebe...77cb13` | 0.00000000 |
| C | `0x38b99e63...91535e` | 0.00000000 |
| D | `0xf7765624...fcfdd1` | 0.00000000 |
| E | `0xdc1d9d53...958d36` | 0.00000000 |
| F | `0x18a14b5b...c3cf71` | 0.00000000 |
| G | `0x69a394c0...cc7f32` | 0.00000000 |
| H | `0xce67c327...e5300f` | 0.00000000 |
| I | `0x070fe5d7...0c1fc9` | 0.00000000 |
| J | `0x4d964db8...e87f54` | 0.00000000 |
| K | `0xa732040a...425dc4` | 0.00000000 |
| L | `0x7c2eaeaf...37eba9` | 0.00000000 |
| M | `0x6fed37a7...b7f2e9` | 0.00000000 |
| N | `0xe7dde6da...551b2c` | 0.00000000 |
| O | `0x73252b60...25a89d` | 0.00000000 |
| P | `0x6218792d...1ec948` | 0.00000000 |
| Q | `0xac40fa50...5c89a9` | 0.00000000 |
| R | `0x7ce605cc...d76e10` | 0.00000000 |
| S | `0xb8753014...9d0386` | 0.00000000 |
| T | `0x35781dc0...3f4588` | 0.00000000 |
| U | `0x75860da4...ef9956` | 0.00000000 |
| V | `0xb59dd817...9af2c3` | 0.00000000 |
| W | `0x5f32aef7...ccc7b0` | 0.00000000 |
| X | `0xa95cbbd1...33047d` | 0.00000000 |
| Y | `0xd8e32848...2444c4` | 0.00000000 |
| Z | `0x7af0ef6e...4e197c` | 0.00000000 |

> All 28 wallets returned 0.0 APT — accounts not initialized with CoinStore on Aptos mainnet.

### Multisig Contract Probes
| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...87003` | 2 | ✓ |
| A-G | `0xf56c4a1c...0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181...b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9...7883` | 2 | ✓ |
| V-W | `0x40fad7b4...eb6d` | 2 | ✓ |

All 5 multisig accounts healthy — require 2-of-N signatures.

### MNX Testnet Markets
- Site: `https://testnet.mnx.fi` (Next.js SPA, HTTP 200, served via Vercel)
- Backend: `https://api.testnet.mnx.fi` — WebSocket-first, no public REST endpoints
- Market data: **unavailable via HTTP** (SPA loads data via WebSocket after wallet connect)

---

## DuckDB Schema Summary
```sql
-- Tables
world_increments   -- GF(3) colored increment events
repo_snapshots     -- GitHub repo metadata (279 repos this run)
aptos_snapshots    -- Wallet APT balances (28 wallets)
multisig_probes    -- Multisig contract sigs_required (5 contracts)
mnx_snapshots      -- MNX market data (unavailable this run)
```
