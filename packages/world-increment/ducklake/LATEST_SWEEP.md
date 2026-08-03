# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-03T00:00Z  
**Run type:** Scheduled autonomous sweep  
**GF(3) color chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| # | Type | Source | Repos | GF3 |
|---|------|--------|-------|-----|
| 1 | org | plurigrid | 100 | PLUS #b8bb26 |
| 2 | org | kubeflow | 49 | MINUS #cc241d |
| 3 | org | TeglonLabs | 5 | ERGODIC #d3869b |
| 4 | user | bmorphism | 49 | PLUS #b8bb26 |
| 5 | user | zubyul | 100 | MINUS #cc241d |
| 6 | user | migalkin | 19 | ERGODIC #d3869b |
| 7 | user | DJedamski | 6 | PLUS #b8bb26 |
| 8 | user | wasita | 12 | MINUS #cc241d |
| 9 | user | kristinezheng | 5 | ERGODIC #d3869b |
| 10 | user | M1shaaa | 8 | PLUS #b8bb26 |
| 11 | user | AustinCStone | 20 | MINUS #cc241d |

**Total repos this sweep:** 373  
**Total repo_snapshots in DB (cumulative):** 1317

### Top Repos by Stars (this sweep)
- `kubeflow/kubeflow`: 15,803 ⭐ (ML platform for Kubernetes)
- `kubeflow/pipelines`: 4,173 ⭐ (Python)
- `kubeflow/spark-operator`: 3,142 ⭐ (Python)
- `kubeflow/trainer`: 2,165 ⭐ (Go)

### Language Breakdown (this sweep)
Python: 226 · Rust: 57 · HTML: 54 · JavaScript: 51 · Go: 51 · TypeScript: 46 · Jupyter Notebook: 40 · Clojure: 30 · Jsonnet: 23 · R: 22

### Notable Recent Activity
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): crane-jank converged-IR hub with GF3 convergence maps and simonw workflow
- **M1shaaa/M1shaaa** (pushed 2026-08-03): Active TODAY — profile config update
- **kristinezheng/kristinezheng.github.io** (HTML, pushed 2026-07-01): Personal site recently updated
- **wasita/wasita.github.io** (Svelte, pushed 2026-07-21): Active personal site

### GF(3) Increment Chain (this run)
```
#1 plurigrid    PLUS     (+1) #b8bb26
#2 kubeflow     MINUS    (-1) #cc241d
#3 TeglonLabs   ERGODIC  ( 0) #d3869b
#4 bmorphism    PLUS     (+1) #b8bb26
#5 zubyul       MINUS    (-1) #cc241d
#6 migalkin     ERGODIC  ( 0) #d3869b
#7 DJedamski    PLUS     (+1) #b8bb26
#8 wasita       MINUS    (-1) #cc241d
#9 kristinezheng ERGODIC ( 0) #d3869b
#10 M1shaaa     PLUS     (+1) #b8bb26
#11 AustinCStone MINUS   (-1) #cc241d
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets (alice, bob, A–Z) queried via `fullnode.mainnet.aptoslabs.com`.  
**Result: All balances = 0.0 APT** — CoinStore resource (`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`) not found for any address. Accounts are likely testnet-only or the CoinStore has not been initialized.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9... | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf78... | 0.0 |
| A–Z | (see aptos_snapshots table) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee208... | 2 | ✅ healthy |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6... | 2 | ✅ healthy |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae... | 2 | ✅ healthy |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0c... | 2 | ✅ healthy |

**All 5 multisig contracts require 2-of-N signatures and are responding correctly on Aptos mainnet.**

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` returns HTTP 200 with a Next.js SPA (client-side rendered). Neither `/api/markets` nor `/api/v1/markets` return JSON data — market data is fetched client-side by the browser. **Status: unavailable via headless probe.** No entries in `mnx_snapshots` table.

---

## DuckDB State (`world-increments.duckdb`)

| Table | Row Count |
|-------|-----------|
| world_increments | 34 |
| repo_snapshots | 1317 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`  
**DuckDB version:** v1.5.5 (Variegata)

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
