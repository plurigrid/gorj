# World-Increment Sweep — 2026-08-06

## Sweep Metadata
- **Date:** 2026-08-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Run time:** ~08:16 UTC

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all time) | 35 |
| New Increments This Sweep | 12 |
| Total Repo Snapshots (all time) | 1007 |
| New Repo Snapshots This Sweep | 63 |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | SPA (REST unavailable) |

---

## GF(3) Color Chain — This Sweep (IDs 12–23)

| ID | Source | Type | Event | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 12 | plurigrid (org) | org | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 13 | kubeflow (org) | org | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 14 | TeglonLabs (org) | org | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 15 | bmorphism (user) | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 16 | zubyul (user) | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 17 | migalkin (user) | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 18 | DJedamski (user) | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 19 | wasita (user) | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 20 | kristinezheng (user) | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 21 | M1shaaa (user) | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 22 | AustinCStone (user) | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 23 | plurigrid (org) | org | sweep_complete (gorj) | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → PLUS → ERGODIC → PLUS → MINUS`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Covered
- **Orgs (3):** plurigrid, kubeflow, TeglonLabs
- **Users (8):** bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

### Repo Counts by Source

| Source | Repos Snapshotted | Max Stars |
|--------|------------------|-----------|
| kubeflow | 20 | 15,805 |
| bmorphism | 15 | 61 |
| plurigrid | 10 | 59 |
| AustinCStone | 5 | 92 |
| migalkin | 5 | 144 |
| zubyul | 6 | 2 |
| TeglonLabs | 5 | 2 |
| wasita | 5 | 2 |
| DJedamski | 3 | 1 |
| kristinezheng | 2 | 0 |
| M1shaaa | 3 | 0 |

### Top Repos by Stars

| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow/kubeflow | — | 15,805 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,178 | 2026-08-05 |
| kubeflow/spark-operator | Python | 3,144 | 2026-08-05 |
| kubeflow/katib | Python | 1,694 | 2026-08-05 |
| kubeflow/arena | Go | 816 | 2026-07-29 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| plurigrid/asi | HTML | 59 | 2026-07-10 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |

### Notable Activity
- **plurigrid/gorj** (1,661 open issues): Actively developed, pushed 2026-08-06T01:16Z
- **plurigrid/eirobri**: 31 open issues, EiRoBri replay world
- **wasita/xoxowasita-analysis**: Created 2026-08-04, already pushed 2026-08-05
- **wasita/joint-planning-lit**: Created 2026-08-04 (brand new)
- **kubeflow/trainer**: Pushed 2026-08-05 (active LLM training infra)
- **kubeflow/mcp-apache-spark-history-server**: 186 stars, active MCP integration

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses probed. **Result: All are contract/module accounts** — they deploy custom Move modules (`store_v2::ACSetMeta2`, `address_book::Mapping`, `lending_pool::UserPosition`, `multiverse::MultiverseState`) and have no standard `0x1::coin::CoinStore<AptosCoin>` resource. They use the Aptos Fungible Asset (FA) model or are purely contract accounts.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | contract account |
| bob | 0x0a3c...2d5d | contract account |
| A | 0x8699...9d7a | contract account |
| B | 0x3f89...b13 | contract account |
| C | 0x38b9...535e | contract account |
| D | 0xf776...fdd1 | contract account |
| E | 0xdc1d...8d36 | contract account |
| F | 0x18a1...cf71 | contract account |
| G–Z | ... | contract account |

**Note:** `alice` (0xc793...) deploys `multiverse::MultiverseState` and `lending_pool::UserPosition` — active on-chain contract.

### Multisig Contract Probes

All 5 multisig contracts probed via `/v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4...003 | **2** | ✅ HEALTHY |
| A-G | 0xf56c...096 | **2** | ✅ HEALTHY |
| Y-Z | 0xd3ff...883 | **2** | ✅ HEALTHY |
| S-T | 0x3b1c...883 | **2** | ✅ HEALTHY |
| V-W | 0x40fa...b6d | **2** | ✅ HEALTHY |

All 5 multisig contracts require **2-of-N signatures** and are responding correctly.

### MNX Markets

- `https://testnet.mnx.fi` returns a Next.js SPA (HTML only, JS bundle loads data client-side)
- No REST API endpoint found at `/api/markets` — the app uses client-side data fetching
- **Status: SPA — market data unavailable via REST probe**

---

## Database State

```sql
SELECT table_name, COUNT(*) FROM (
  SELECT 'world_increments' AS table_name FROM world_increments
  UNION ALL SELECT 'repo_snapshots' FROM repo_snapshots
  UNION ALL SELECT 'aptos_snapshots' FROM aptos_snapshots
  UNION ALL SELECT 'multisig_probes' FROM multisig_probes
  UNION ALL SELECT 'mnx_snapshots' FROM mnx_snapshots
) GROUP BY 1;
```

| Table | Rows |
|-------|------|
| world_increments | 35 |
| repo_snapshots | 1,007 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |
