# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-22

## Sweep Metadata
- **Date:** 2026-07-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos This Run |
|--------|------|---------------|
| plurigrid | org | 16 |
| kubeflow | org | 16 |
| TeglonLabs | org | 5 |
| bmorphism | user | 13 |
| zubyul | user | 10 |
| migalkin | social graph | 5 |
| wasita | social graph | 4 |
| AustinCStone | social graph | 5 |
| kristinezheng | social graph | 2 |
| M1shaaa | social graph | 2 |
| DJedamski | social graph | 2 |
| **Total this run** | | **80 repos** |

### Top Repos by Stars (this run)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/pipelines | 4,169 | Python | 2026-07-22 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-17 |
| kubeflow/trainer | 2,152 | Go | 2026-07-22 |
| kubeflow/katib | 1,692 | Python | 2026-07-22 |
| kubeflow/arena | 815 | Go | 2026-07-21 |
| kubeflow/kale | 695 | Python | 2026-07-21 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 31 | HTML | 2026-07-10 |

### Most Active Today (pushed 2026-07-22)

- **plurigrid/gorj** — 1,321 open issues; forj + Rama topology nREPL + GF(3) trit coloring
- **bmorphism/Gay.jl** — 187 open issues; wide-gamut color sampling with splittable determinism
- **kubeflow/trainer**, **kubeflow/pipelines**, **kubeflow/sdk**, **kubeflow/katib**, **kubeflow/notebooks**

### GF(3) Color Chain Distribution (this run, 80 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 27 |
| 1 | #b8bb26 | PLUS | 27 |
| -1 | #cc241d | MINUS | 26 |

### DB Totals (cumulative across all runs)

| Table | Rows |
|-------|------|
| world_increments | 103 |
| repo_snapshots | 1,024 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

All 28 Hamming swarm addresses returned **null** from Aptos mainnet fullnode. Accounts have no activated `0x1::coin::CoinStore<AptosCoin>` resource — wallets are uninitialized or hold non-APT assets only. Stored as -1.0 sentinel in `aptos_snapshots`.

| World | Address | APT Balance |
|-------|---------|------------|
| alice | 0xc793...cc7b | null |
| bob | 0x0a3c...512d | null |
| A | 0x8699...9d7a | null |
| B | 0x3f89...b13 | null |
| C | 0x38b9...35e | null |
| D | 0xf776...dd1 | null |
| E | 0xdc1d...d36 | null |
| F | 0x18a1...f71 | null |
| G | 0x69a3...f32 | null |
| H | 0xce67...00f | null |
| I | 0x070f...c9 | null |
| J | 0x4d96...f54 | null |
| K | 0xa732...dc4 | null |
| L | 0x7c2e...ba9 | null |
| M | 0x6fed...2e9 | null |
| N | 0xe7dd...b2c | null |
| O | 0x7325...89d | null |
| P | 0x6218...948 | null |
| Q | 0xac40...89a | null |
| R | 0x7ce6...e10 | null |
| S | 0xb875...386 | null |
| T | 0x3578...588 | null |
| U | 0x7586...956 | null |
| V | 0xb59d...2c3 | null |
| W | 0x5f32...7b0 | null |
| X | 0xa95c...47d | null |
| Y | 0xd8e3...4c4 | null |
| Z | 0x7af0...97c | null |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** — each requires exactly 2 signatures:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — `testnet.mnx.fi` is a Next.js SPA with no accessible REST/JSON endpoint. All API path probes (`/api/markets`, `/api/v1/markets`, `/api/v2/markets`) return the HTML shell. Recorded as `unavailable` in `mnx_snapshots`.

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
