# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-22

## Sweep Metadata
- **Date:** 2026-07-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 (103 total) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 9 |
| DJedamski | social graph | 2 |
| wasita | social graph | 10 |
| kristinezheng | social graph | 3 |
| M1shaaa | social graph | 6 |
| AustinCStone | social graph | 30 |
| **TOTAL** | | **312** |

### Notable Repos (by stars)
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,789 | Go | 2026-07-22 |
| kubeflow/pipelines | 4,168 | Python | 2026-07-22 |
| kubeflow/spark-operator | 3,142 | Go | 2026-07-21 |
| kubeflow/trainer | 2,152 | Go | 2026-07-21 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| plurigrid/asi | 31 | HTML | 2026-07-10 |
| plurigrid/gorj | 1 | Clojure | 2026-07-22 |

### Recent Activity (plurigrid)
- **plurigrid/gorj** — pushed 2026-07-22 (today) — forj + Rama + GF(3) trit coloring, 1,314 open issues
- **plurigrid/eirobri** — pushed 2026-07-21 — EiRoBri replay world
- **plurigrid/place** — pushed 2026-07-14 — TeX/PDF
- **plurigrid/asi** — pushed 2026-07-10 — topological chemputer (31★)

### TeglonLabs Activity
- **TeglonLabs/jank-crane** — pushed 2026-06-08 — C++ crane-jank converged-IR hub with GF3 convergence maps

### GF(3) Color Chain Distribution
| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 111 |
| PLUS | +1 | `#b8bb26` | 112 |
| MINUS | -1 | `#cc241d` | 112 |

Assignment rule:
- `id mod 3 == 0` → trit=0, `#d3869b` ERGODIC
- `id mod 3 == 1` → trit=+1, `#b8bb26` PLUS
- `id mod 3 == 2` → trit=-1, `#cc241d` MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)
All 28 Hamming swarm wallets queried via Aptos fullnode mainnet API.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...4cc7b | 0.00000000 |
| bob | 0x0a3c...512d5d | 0.00000000 |
| A | 0x8699...ebe9d7a | 0.00000000 |
| B | 0x3f89...577cb13 | 0.00000000 |
| C | 0x38b9...691535e | 0.00000000 |
| D | 0xf776...fcfdd1 | 0.00000000 |
| E | 0xdc1d...958d36 | 0.00000000 |
| F | 0x18a1...3cf71 | 0.00000000 |
| G | 0x69a3...cc7f32 | 0.00000000 |
| H | 0xce67...e5300f | 0.00000000 |
| I | 0x070f...c1fc9 | 0.00000000 |
| J | 0x4d96...b7f54 | 0.00000000 |
| K | 0xa732...25dc4 | 0.00000000 |
| L | 0x7c2e...37eba9 | 0.00000000 |
| M | 0x6fed...7f2e9 | 0.00000000 |
| N | 0xe7dd...551b2c | 0.00000000 |
| O | 0x7325...5a89d | 0.00000000 |
| P | 0x6218...ec948 | 0.00000000 |
| Q | 0xac40...5c89a9 | 0.00000000 |
| R | 0x7ce6...76e10 | 0.00000000 |
| S | 0xb875...99d0386 | 0.00000000 |
| T | 0x3578...3f4588 | 0.00000000 |
| U | 0x7586...ef9956 | 0.00000000 |
| V | 0xb59d...89af2c3 | 0.00000000 |
| W | 0x5f32...6ccc7b0 | 0.00000000 |
| X | 0xa95c...e33047d | 0.00000000 |
| Y | 0xd8e3...2444c4 | 0.00000000 |
| Z | 0x7af0...4e197c | 0.00000000 |

**Total APT across all 28 swarm wallets: 0.00000000 APT**

All addresses have unfunded `CoinStore<AptosCoin>` on mainnet. The resource exists (API returns 200) but coin value is 0.

### Multisig Contract Probes (5 pairs)
All 5 probed via `0x1::multisig_account::num_signatures_required` view function.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

**All 5 multisig contracts respond correctly — 2-of-N threshold on all pairs.**

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE**  
`testnet.mnx.fi` serves only a mobile SPA splash screen ("optimized for portrait mode on mobile"). No API endpoint at `/api/markets` responded with data. No market data captured for this sweep.

---

## DuckDB Tables
| Table | Rows | Notes |
|-------|------|-------|
| world_increments | 312 | GF(3) colored events |
| repo_snapshots | 312 | One per world_increment |
| aptos_snapshots | 28 | All balances 0.0 APT |
| multisig_probes | 5 | All sigs_required=2 |
| mnx_snapshots | 0 | MNX unavailable |

---

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

*Generated by world-increment-sweep + hamming-swarm-snapshot scheduled agent — 2026-07-22.*
