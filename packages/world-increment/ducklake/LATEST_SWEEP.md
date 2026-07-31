# World-Increment Sweep + Hamming Snapshot — 2026-07-31

## Sweep Metadata
- **Date:** 2026-07-31
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source (this run)
| Source | Type | Repos This Run |
|--------|------|---------------|
| plurigrid | org | 30 |
| kubeflow | org | 20 |
| bmorphism | user | 13 |
| zubyul | user | 13 |
| migalkin | user (social) | 7 |
| wasita | user (social) | 5 |
| AustinCStone | user (social) | 5 |
| TeglonLabs | org | 5 |
| DJedamski | user (social) | 3 |
| kristinezheng | user (social) | 3 |
| M1shaaa | user (social) | 2 |
| **TOTAL** | | **106** |

### GF(3) Color Chain Distribution (this run)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 35 |
| 1 | `#b8bb26` | PLUS | 36 |
| -1 | `#cc241d` | MINUS | 35 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

### Notable Repos (by stars)
| Repo | Stars | Pushed At |
|------|-------|-----------|
| kubeflow/kubeflow | 15,798 | 2026-07-10 |
| kubeflow/pipelines | 4,171 | 2026-07-29 |
| kubeflow/spark-operator | 3,142 | **2026-07-31** ← active today |
| kubeflow/trainer | 2,164 | **2026-07-31** ← active today |
| kubeflow/katib | 1,694 | 2026-07-26 |
| migalkin/NodePiece | 144 | 2026-05-07 |
| AustinCStone/TextGAN | 92 | 2025-03-03 |
| migalkin/StarE | 89 | 2026-04-16 |
| bmorphism/anti-bullshit-mcp-server | 22 | 2026-07-12 |
| plurigrid/zig-syrup | 2 | 2026-07-28 ← recent |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet — 28 addresses)
**Status:** All 28 wallets (alice, bob, A–Z) returned `resource_not_found`
for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

These are uninitialized Aptos accounts with no on-chain APT balance.
Recorded as `0.0 APT` in `aptos_snapshots`.

### Multisig Contract Probes (5 pairs)
All probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428...7003` | 2 | ✅ |
| A-G | `0xf56c4a1c...0096` | 2 | ✅ |
| Y-Z | `0xd3ffe181...b883` | 2 | ✅ |
| S-T | `0x3b1c3ae9...7883` | 2 | ✅ |
| V-W | `0x40fad7b4...eb6d` | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-N threshold on Aptos mainnet.**

### MNX Markets (testnet.mnx.fi)
**Status:** API unavailable. `https://testnet.mnx.fi/api/markets` returns a
Next.js SPA (no public JSON REST endpoint). No market data extractable.
`mnx_snapshots` table remains empty.

---

## Database Summary (cumulative)
| Table | Rows Total | Notes |
|-------|-----------|-------|
| `world_increments` | 129 | +106 this run |
| `repo_snapshots` | 1050 | +106 this run |
| `aptos_snapshots` | 28 | +28 this run |
| `multisig_probes` | 5 | +5 this run |
| `mnx_snapshots` | 0 | SPA, no API |

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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
