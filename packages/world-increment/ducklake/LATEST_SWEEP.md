# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-05  
**Sweep ID:** 14  
**GF(3) Color:** MINUS `#cc241d` (trit=-1)

---

## Job 1: GitHub Social Graph Sweep

**Scope:** Session scoped to `plurigrid/gorj` — external org/user queries (kubeflow, TeglonLabs, bmorphism, zubyul social graph) require `gh` CLI or broader GitHub token scope.

### plurigrid/gorj snapshot

| Field | Value |
|-------|-------|
| Full name | plurigrid/gorj |
| Language | Clojure |
| Last pushed | 2026-05-08T14:04:34Z |
| Latest commit | `5b28fe016e0e` |
| Active sweep branches | 50 (world-increment/sweep-*) |
| Description | MCP server + hooks that give AI coding agents a Clojure REPL |

### Recent Activity (last 5 commits)
| SHA | Message | Date |
|-----|---------|------|
| `5b28fe01` | chore: ignore duckdb binary in repo root | 2026-05-08 |
| `ebf263f5` | world-increment ducklake: sync world.duckdb sweep state | 2026-04-14 |
| `b434a43c` | Merge sweep state into master | 2026-04-14 |
| `631518bc` | world-increment sweep 2026-04-12: insert id=12 ERGODIC | 2026-04-12 |
| `c4238bcf` | world-increments.duckdb: sync latest sweep state | 2026-04-10 |

### World Increments (last 5)
| ID | GF3 trit | Color | Name | Source | Event |
|----|----------|-------|------|--------|-------|
| 14 | -1 | `#cc241d` | MINUS | github_sweep/plurigrid/gorj | commit |
| 13 | 1 | `#b8bb26` | PLUS | aptos_sweep/hamming_swarm | snapshot |
| 12 | 0 | `#d3869b` | ERGODIC | org/bmorphism | sweep_complete |
| 11 | -1 | `#cc241d` | MINUS | user/AustinCStone | repo_snapshot |
| 11 | -1 | `#cc241d` | MINUS | user/AustinCStone | repo_sweep |

### GF(3) Chain Distribution
| Name | Count |
|------|-------|
| MINUS | 9 |
| PLUS | 9 |
| ERGODIC | 7 |

---

## Job 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Timestamp:** 2026-07-05T00:00:00Z  
**Chain:** Aptos Mainnet  
**Total wallets probed:** 28

### Wallet Balances
| World | Address (short) | Balance (APT) |
|-------|----------------|---------------|
| Z | `0x7af0ef6e...` | 0.00000000 |
| Y | `0xd8e32848...` | 0.00000000 |
| X | `0xa95cbbd1...` | 0.00000000 |
| W | `0x5f32aef7...` | 0.00000000 |
| V | `0xb59dd817...` | 0.00000000 |
| U | `0x75860da4...` | 0.00000000 |
| T | `0x35781dc0...` | 0.00000000 |
| S | `0xb8753014...` | 0.00000000 |
| R | `0x7ce605cc...` | 0.00000000 |
| Q | `0xac40fa50...` | 0.00000000 |
| P | `0x6218792d...` | 0.00000000 |
| O | `0x73252b60...` | 0.00000000 |
| N | `0xe7dde6da...` | 0.00000000 |
| M | `0x6fed37a7...` | 0.00000000 |
| L | `0x7c2eaeaf...` | 0.00000000 |
| K | `0xa732040a...` | 0.00000000 |
| J | `0x4d964db8...` | 0.00000000 |
| I | `0x070fe5d7...` | 0.00000000 |
| H | `0xce67c327...` | 0.00000000 |
| G | `0x69a394c0...` | 0.00000000 |
| F | `0x18a14b5b...` | 0.00000000 |
| E | `0xdc1d9d53...` | 0.00000000 |
| D | `0xf7765624...` | 0.00000000 |
| C | `0x38b99e63...` | 0.00000000 |
| B | `0x3f892ebe...` | 0.00000000 |
| A | `0x8699edc0...` | 0.00000000 |
| bob | `0x0a3c00c5...` | 0.00000000 |
| alice | `0xc793acde...` | 0.00000000 |

> All 28 wallets (alice, bob, A–Z) currently show 0.0 APT on mainnet.

### Multisig Probes
| Pair | Address (short) | Sigs Required | Healthy |
|------|----------------|---------------|---------|
| V-W | `0x40fad7b4...` | 2 | ✓ |
| S-T | `0x3b1c3ae9...` | 2 | ✓ |
| Y-Z | `0xd3ffe181...` | 2 | ✓ |
| A-G | `0xf56c4a1c...` | 2 | ✓ |
| A-B | `0x0da4f428...` | 2 | ✓ |

> All 5 multisig contracts healthy: A-B, A-G, Y-Z, S-T, V-W — each requiring 2-of-2 signatures.

### MNX Markets (testnet.mnx.fi)
Status: **SPA — no REST API endpoint found.** Paths tried: `/`, `/api/markets`, `/api/v1/markets`, `/markets`. All returned HTML (13,462 bytes). Market data unavailable via API probe.

---

## DuckDB Ducklake Summary
| Table | Row Count |
|-------|-----------|
| world_increments | 25 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
