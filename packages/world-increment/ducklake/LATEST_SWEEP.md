# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-20

## Sweep Metadata
- **Date:** 2026-04-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 408 |
| Total Repo Snapshots | 1329 |
| Unique Repos Ingested | 385 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain Distribution

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | #d3869b (rose) | 0 | 135 |
| PLUS | #b8bb26 (lime) | +1 | 137 |
| MINUS | #cc241d (red) | -1 | 136 |

GF(3) rule: `id%3==0 → ERGODIC`, `id%3==1 → PLUS`, `id%3==2 → MINUS`

---

### Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 47 |
| zubyul | user | 47 |
| AustinCStone | user | 40 |
| migalkin | user (zubyul graph) | 19 |
| M1shaaa | user (zubyul graph) | 8 |
| wasita | user (zubyul graph) | 8 |
| kristinezheng | user (zubyul graph) | 6 |
| DJedamski | user (zubyul graph) | 6 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **385** |

### Top Repos by Stars

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,586 | 2026-01-05 |
| kubeflow/pipelines | Python | 4,124 | 2026-04-18 |
| kubeflow/spark-operator | Python | 3,116 | 2026-04-16 |
| kubeflow/trainer | Go | 2,086 | 2026-04-17 |
| plurigrid/asi | HTML | 17 | 2026-04-20 |

### Notable Activity (2026-04-20)
- **plurigrid/asi** pushed today — topological chemputer
- **M1shaaa/M1shaaa** pushed today — profile config
- **wasita/wasita.github.io** pushed 2026-04-13 (Svelte personal site)
- **kristinezheng/kristinezheng.github.io** pushed 2026-04-09
- **wasita/ch3-lib** pushed 2026-04-12 (Typst library)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-04-20)

All 28 addresses probed (alice, bob, A–Z). **All balances: 0.0 APT** — addresses appear unfunded on mainnet at time of sweep.

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...cc7b | 0.0 APT |
| bob | 0x0a3c...2d5d | 0.0 APT |
| A–Z (26 wallets) | various | 0.0 APT each |

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig contracts are **healthy** — confirmed 2-of-N threshold.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

### MNX Markets (`testnet.mnx.fi`)
Status: **SPA only** — Next.js frontend with no accessible public REST API.  
Recorded as `N/A` in `mnx_snapshots`.

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
