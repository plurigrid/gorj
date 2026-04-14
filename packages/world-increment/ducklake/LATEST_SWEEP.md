# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-14

## Sweep Metadata
- **Date:** 2026-04-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 385 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Healthy | 5/5 |
| MNX Market Data | SPA-unavailable |

---

## GF(3) Color Chain — All 12 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (org) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Repo Counts by Source (this sweep)

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| plurigrid | org | 99 | 63 |
| kubeflow | org | 47 | 33,874 |
| TeglonLabs | org | 4 | 2 |
| bmorphism | user | 99 | 247 |
| zubyul | user | 47 | 14 |
| AustinCStone | user (zubyul graph) | 40 | 108 |
| migalkin | user (zubyul graph) | 19 | 277 |
| wasita | user (zubyul graph) | 10 | 2 |
| M1shaaa | user (zubyul graph) | 8 | 0 |
| kristinezheng | user (zubyul graph) | 6 | 0 |
| DJedamski | user (zubyul graph) | 6 | 3 |
| **TOTAL** | | **385** | **34,590** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 hamming-swarm addresses queried via `fullnode.mainnet.aptoslabs.com`.  
All returned `resource_not_found` — no `CoinStore<AptosCoin>` registered, balance recorded as **0.0 APT**.

| World | Address (truncated) | Balance |
|-------|---------------------|---------|
| alice | 0xc793...c7b | 0.0 APT |
| bob | 0x0a3c...d5d | 0.0 APT |
| A–Z | (26 addresses) | 0.0 APT each |

### Multisig Contract Probes — All HEALTHY ✓

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ healthy |
| A-G | 0xf56c...096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✓ healthy |
| S-T | 0x3b1c...883 | 2 | ✓ healthy |
| V-W | 0x40fa...b6d | 2 | ✓ healthy |

All 5 multisig pairs are 2-of-N threshold contracts and responded successfully.

### MNX Markets

`https://testnet.mnx.fi` — **SPA unavailable**: Next.js single-page app returns HTML at all paths; no REST JSON API endpoints found at `/api/markets` or `/api/v1/markets`. Recorded as `SPA-unavailable` in `mnx_snapshots` table.

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

### GitHub
- **kubeflow/kubeflow**: 15,565★ — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119★ — most popular ML pipeline for K8s
- **migalkin/NodePiece**: 143★ — scalable knowledge graph embeddings
- **bmorphism**: 247 total stars across 99 repos — active MCP/Clojure/Zig ecosystem
- **AustinCStone/TextGAN**: 92★ — text generation with GANs
- **wasita**: recently active (ch3-lib pushed 2026-04-12, wasita.github.io pushed 2026-04-13)
- **M1shaaa/M1shaaa**: profile repo pushed 2026-04-14 (today!)

### Aptos Hamming Swarm
- All 28 addresses have 0 APT (no CoinStore initialized on mainnet)
- All 5 multisig contracts respond healthy with threshold=2 sigs

### DuckDB Tables
| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 385 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |
