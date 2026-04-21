# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-21
**Agent:** world-increment-sweep + hamming-swarm-snapshot
**DuckDB version:** v1.5.2 (Variegata)
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 47 |
| migalkin | social graph | 7 |
| DJedamski | social graph | 6 |
| wasita | social graph | 6 |
| kristinezheng | social graph | 4 |
| M1shaaa | social graph | 4 |
| AustinCStone | social graph | 6 |
| **TOTAL** | | **331** |

### Top Repos by Stars
| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15,587 | — |
| kubeflow | pipelines | 4,125 | Python |
| kubeflow | spark-operator | 3,117 | Python |
| kubeflow | trainer | 2,085 | Go |
| kubeflow | katib | 1,680 | Python |
| migalkin | NodePiece | 143 | Python |
| AustinCStone | TextGAN | 92 | Python |
| migalkin | StarE | 89 | Python |
| migalkin | kgcourse2021 | 25 | HTML |
| bmorphism | shitcoin | 5 | Python |
| plurigrid | gorj | — | Clojure |

### GF(3) Distribution (331 increments)
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 110 |
| 1 | PLUS | #b8bb26 | 111 |
| -1 | MINUS | #cc241d | 110 |

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0 · ERGODIC · #d3869b
- `id mod 3 == 1` → trit=1 · PLUS · #b8bb26
- `id mod 3 == 2` → trit=-1 · MINUS · #cc241d

### Recent plurigrid Activity
- `bci-blue-share` — pushed 2026-04-19
- `nanoclj-zig` — pushed 2026-04-18 (mirrored in bmorphism)
- `gorj` — pushed 2026-04-21 (this repo)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

Queried via `0x1::coin::balance` view function on `https://fullnode.mainnet.aptoslabs.com`.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| bob | 0x0a3c...512d | **12.657007** |
| F | 0x18a1...cf71 | 1.960516 |
| L | 0x7c2e...eba9 | 1.927269 |
| J | 0x4d96...7f54 | 1.895093 |
| alice | 0xc793...cc7b | 0.436434 |
| O | 0x7325...a89d | 0.210136 |
| K | 0xa732...dc4 | 0.161961 |
| P | 0x6218...c948 | 0.140136 |
| M | 0x6fed...f2e9 | 0.112285 |
| N | 0xe7dd...b2c | 0.106121 |
| Q | 0xac40...89a9 | 0.103240 |
| S | 0xb875...d386 | 0.091788 |
| R | 0x7ce6...6e10 | 0.090217 |
| T | 0x3578...4588 | 0.073713 |
| U | 0x7586...9956 | 0.055773 |
| A | 0x8699...9d7a | 0.051767 |
| V | 0xb59d...f2c3 | 0.048833 |
| Y | 0xd8e3...44c4 | 0.044449 |
| X | 0xa95c...047d | 0.042577 |
| W | 0x5f32...c7b0 | 0.040705 |
| B | 0x3f89...b13 | 0.036256 |
| Z | 0x7af0...97c | 0.024268 |
| D | 0xf776...fdd1 | 0.011629 |
| C | 0x38b9...35e | 0.010185 |
| E | 0xdc1d...d36 | 0.009372 |
| H | 0xce67...00f | 0.001681 |
| I | 0x070f...fc9 | 0.000681 |
| G | 0x69a3...f32 | 0.000681 |

**Total swarm APT:** ~20.77 APT
**Notable:** `bob` dominates with 12.66 APT (61% of swarm). F, L, J cluster around 1.9 APT.

### Multisig Contract Probes (5/5 healthy)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | healthy |
| A-G | 0xf56c...096 | 2 | healthy |
| Y-Z | 0xd3ff...883 | 2 | healthy |
| S-T | 0x3b1c...883 | 2 | healthy |
| V-W | 0x40fa...b6d | 2 | healthy |

All 5 multisig contracts respond as 2-of-2. Queried via `0x1::multisig_account::num_signatures_required`.

### MNX Markets (testnet.mnx.fi)

**Status: SPA — market data unavailable via static scraping.**
`testnet.mnx.fi` is a Next.js client-side app. No `__NEXT_DATA__` injection, no REST endpoints at `/api/markets`, `/api/v1/markets`, or `/api/tickers`. Data rendered entirely client-side. A headless browser would be required to extract live market data.

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

| Table | Rows |
|-------|------|
| world_increments | 331 |
| repo_snapshots | 331 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable marker) |
