# World-Increment Sweep — 2026-07-10

## Sweep Metadata
- **Date:** 2026-07-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 282 |
| Total Repo Snapshots | 282 |
| Sources Covered | 3 orgs + 8 users (social graph) |

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 50 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| wasita | user (social) | 11 |
| M1shaaa | user (social) | 8 |
| DJedamski | user (social) | 6 |
| kristinezheng | user (social) | 5 |
| AustinCStone | user (social) | 30 |
| **TOTAL** | | **282** |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | ★15,771 | — |
| kubeflow/pipelines | ★4,169 | Python |
| kubeflow/spark-operator | ★3,136 | Python |
| kubeflow/trainer | ★2,134 | Go |
| kubeflow/katib | ★1,689 | Python |
| kubeflow/examples | ★1,460 | Jsonnet |
| kubeflow/community-distribution | ★1,029 | YAML |
| kubeflow/arena | ★815 | Go |

### GF(3) Color Chain

- `id % 3 == 0` → trit=0, **ERGODIC** `#d3869b`
- `id % 3 == 1` → trit=1, **PLUS** `#b8bb26`
- `id % 3 == 2` → trit=-1, **MINUS** `#cc241d`

282 repos colored across 94 complete GF(3) trit cycles.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-07-10)

All 28 addresses (alice, bob, A–Z) queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~6.2B.

**Result:** All 28 addresses: **0.00000000 APT** (`resource_not_found` — no CoinStore registered on mainnet for these addresses).

| Label | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...9a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes

Probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

All 5 multisig contracts operational, 2-of-N threshold confirmed.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — site behind Vercel deployment protection (visitor password required). No market data accessible without auth.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,771 stars — flagship ML platform for Kubernetes (up 206 stars since April sweep)
- **kubeflow/pipelines**: 4,169 stars — pushed 2026-07-09
- **plurigrid/gorj**: 1 star, 1,098 open issues — active development, pushed 2026-07-10
- **wasita/wasita.github.io**: active personal site (Svelte), pushed 2026-07-06
- **M1shaaa/M1shaaa**: profile repo pushed 2026-07-10 (active today)
- **All 5 multisig contracts**: healthy 2-of-N on Aptos mainnet
- **28 Hamming-swarm addresses**: all at 0 APT on mainnet (no CoinStore registered)
