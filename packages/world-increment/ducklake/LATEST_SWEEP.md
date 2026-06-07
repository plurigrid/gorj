# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-07

## Sweep Metadata
- **Date:** 2026-06-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (2026-06-07 sweep)

| Metric | Value |
|--------|-------|
| New World Increments | 62 |
| New Repo Snapshots | 62 |
| Cumulative World Increments | 85 |
| Cumulative Repo Snapshots | 1,006 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution (this sweep)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| +1 | `#b8bb26` | **PLUS** | 21 |
| -1 | `#cc241d` | **MINUS** | 21 |
| 0 | `#d3869b` | **ERGODIC** | 20 |

Rule: `id%3==0 → ERGODIC #d3869b` | `id%3==1 → PLUS #b8bb26` | `id%3==2 → MINUS #cc241d`

---

## Top Repos by Stars (this sweep)

| Org/User | Repo | Language | Stars | Pushed At |
|----------|------|----------|-------|-----------|
| kubeflow | kubeflow | — | 15,705 | 2026-06-07 |
| kubeflow | pipelines | Python | 4,152 | 2026-06-07 |
| kubeflow | spark-operator | Python | 3,126 | 2026-06-07 |
| kubeflow | trainer | Go | 2,112 | 2026-06-06 |
| kubeflow | katib | Python | 1,685 | 2026-06-05 |
| kubeflow | examples | Jsonnet | 1,462 | 2026-06-01 |
| kubeflow | arena | Go | 811 | 2026-05-27 |
| kubeflow | kale | Python | 691 | 2026-06-05 |
| migalkin | NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone | TextGAN | Python | 92 | 2025-03-03 |
| migalkin | StarE | Python | 89 | 2026-04-16 |
| bmorphism | ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| plurigrid | asi | HTML | 25 | 2026-06-04 |
| bmorphism | anti-bullshit-mcp-server | JavaScript | 23 | 2026-02-05 |
| bmorphism | say-mcp-server | JavaScript | 20 | 2026-03-19 |

---

## Repo Counts by Source (this sweep)

| Source | Type | Repos Sampled |
|--------|------|--------------|
| kubeflow | org | 10 |
| plurigrid | org | 13 |
| bmorphism | user | 10 |
| TeglonLabs | org | 4 |
| zubyul | user | 6 |
| migalkin | user | 4 |
| wasita | user | 4 |
| AustinCStone | user | 3 |
| DJedamski | user | 3 |
| kristinezheng | user | 3 |
| M1shaaa | user | 2 |
| **TOTAL** | | **62** |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances
**Snapshot:** 2026-06-07 UTC via `0x1::coin::balance` view function  
**Total APT (28 wallets):** 20.344773 APT  
**Average:** 0.726599 | **Max:** 12.657007 (bob) | **Min:** 0.000681 (G/I)

| World | Address | Balance (APT) |
|-------|---------|---------------|
| bob | 0x0a3c...2d5d | 12.657007 |
| F | 0x18a1...cf71 | 1.960516 |
| L | 0x7c2e...ba9 | 1.927269 |
| J | 0x4d96...7f54 | 1.895093 |
| alice | 0xc793...cc7b | 0.436434 |
| O | 0x7325...a89d | 0.210136 |
| K | 0xa732...5dc4 | 0.161961 |
| P | 0x6218...c948 | 0.140136 |
| M | 0x6fed...2e9 | 0.112285 |
| N | 0xe7dd...1b2c | 0.106121 |
| Q | 0xac40...89a9 | 0.103240 |
| S | 0xb875...0386 | 0.091788 |
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
| C | 0x38b9...535e | 0.010185 |
| E | 0xdc1d...8d36 | 0.009372 |
| H | 0xce67...300f | 0.001681 |
| G | 0x69a3...f32 | 0.000681 |
| I | 0x070f...1fc9 | 0.000681 |

### Multisig Contract Probes

All 5 probed via `POST /v1/view → 0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig accounts healthy, 2-of-N signing requirement confirmed.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — `https://testnet.mnx.fi` and API paths `/api/markets`, `/api/v1/markets` return Vercel authentication wall. No market data extractable without credentials. `mnx_snapshots` table has 0 rows.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,705 stars (+140 since 2026-04-12) — actively growing
- **kubeflow/pipelines**: 4,152 stars, pushed 2026-06-07 — latest activity
- **plurigrid/eirobri**: new repo (2026-05-19) — EiRoBri replay world in Clojure, 29 open issues
- **plurigrid/place**: 8 open issues, pushed 2026-06-04 — most recently active
- **bmorphism/world**: brand new (2026-06-02) — Local worlds launcher for SA3
- **bob wallet**: 12.657 APT — largest balance in the swarm
- **F, L, J wallets**: ~1.9 APT each — tier-2 holders
- **G, I wallets**: 0.000681 APT each — dust-level, possibly gas-reserve accounts
