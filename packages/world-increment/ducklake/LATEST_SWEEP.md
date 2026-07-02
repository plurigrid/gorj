# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-02

## Sweep Metadata
- **Date:** 2026-07-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|------:|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user | 40 |
| migalkin | user (zubyul social) | 19 |
| wasita | user (zubyul social) | 11 |
| M1shaaa | user (zubyul social) | 8 |
| DJedamski | user (zubyul social) | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user (zubyul social) | 5 |
| **TOTAL** | | **391** |

### Most Starred Repos

| Repo | Stars | Language | Pushed |
|------|------:|----------|--------|
| kubeflow/kubeflow | 15,757 | — | 2026-06-30 |
| kubeflow/pipelines | 4,167 | Python | 2026-07-02 |
| kubeflow/spark-operator | 3,130 | Python | 2026-06-30 |
| kubeflow/trainer | 2,129 | Go | 2026-07-02 |
| kubeflow/katib | 1,688 | Python | 2026-07-02 |
| kubeflow/examples | 1,460 | Jsonnet | 2026-04-30 |
| kubeflow/community-distribution | 1,028 | YAML | 2026-07-01 |
| kubeflow/arena | 814 | Go | 2026-06-19 |
| kubeflow/kale | 694 | Python | 2024-09-10 |
| kubeflow/mpi-operator | 529 | Go | 2026-06-30 |

### Recently Active (pushed 2026-07-01 or 2026-07-02)

- `wasita/wasita.github.io` — Svelte personal site, pushed 2026-07-02
- `M1shaaa/M1shaaa` — GitHub profile config, pushed 2026-07-02
- `kristinezheng/kristinezheng.github.io` — HTML personal site, pushed 2026-07-01
- `kubeflow/pipelines` — Python ML pipelines, pushed 2026-07-02
- `kubeflow/trainer` — Go ML trainer, pushed 2026-07-02
- `kubeflow/katib` — Python hyperparameter tuning, pushed 2026-07-02

### GF(3) World-Increment Distribution

| Trit | Name | Color | Count |
|-----:|------|-------|------:|
| 0 | ERGODIC | #d3869b | 130 |
| +1 | PLUS | #b8bb26 | 131 |
| −1 | MINUS | #cc241d | 130 |

GF(3) chain pattern: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...` (repeating, 391 increments = 130 full cycles + 1 PLUS)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses probed via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. All returned **null** — CoinStore resource not found. These accounts are either not initialized on Aptos mainnet or hold zero APT.

| World | Address | Balance APT |
|-------|---------|:-----------:|
| alice | 0xc793ac…624cc7b | null |
| bob | 0x0a3c00…512d5d | null |
| A | 0x8699ed…9d7a | null |
| B | 0x3f892e…cb13 | null |
| C | 0x38b99e…535e | null |
| D | 0xf77656…cfdd1 | null |
| E | 0xdc1d9d…8d36 | null |
| F | 0x18a14b…cf71 | null |
| G | 0x69a394…7f32 | null |
| H | 0xce67c3…300f | null |
| I | 0x070fe5…1fc9 | null |
| J | 0x4d964d…7f54 | null |
| K | 0xa73204…dc4 | null |
| L | 0x7c2eae…ba9 | null |
| M | 0x6fed37…2e9 | null |
| N | 0xe7dde6…1b2c | null |
| O | 0x73252b…a89d | null |
| P | 0x621879…c948 | null |
| Q | 0xac40fa…89a9 | null |
| R | 0x7ce605…6e10 | null |
| S | 0xb87530…0386 | null |
| T | 0x35781d…4588 | null |
| U | 0x75860d…f9956 | null |
| V | 0xb59dd8…f2c3 | null |
| W | 0x5f32ae…c7b0 | null |
| X | 0xa95cbb…047d | null |
| Y | 0xd8e328…444c4 | null |
| Z | 0x7af0ef…197c | null |

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`. All **healthy** — each requires exactly 2 signatures.

| Pair | Address | Sigs Required | Status |
|------|---------|:-------------:|:------:|
| A-B | 0x0da4f4…7003 | 2 | healthy |
| A-G | 0xf56c4a…0096 | 2 | healthy |
| Y-Z | 0xd3ffe1…b883 | 2 | healthy |
| S-T | 0x3b1c3a…7883 | 2 | healthy |
| V-W | 0x40fad7…eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — testnet.mnx.fi returns HTTP 401 "Authentication Required" (Vercel deployment protection). All probed paths (`/api/markets`, `/api/tickers`, `/api/v1/markets`) are behind a visitor password gate. No market data captured; `mnx_snapshots` table has 0 rows.

---

## DuckDB Schema

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=−1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,757 stars — flagship ML platform; actively maintained as of July 2026
- **kubeflow/pipelines**: 4,167 stars — pushed 2026-07-02 (today)
- **kubeflow/trainer**: 2,129 stars — pushed 2026-07-02 (today)
- **TeglonLabs/jank-crane**: C++ GF3 convergence maps + simonw workflow — most recently pushed of TeglonLabs repos (2026-06-08)
- **bmorphism**: 100 repos collected; likely includes ocaml-mcp-sdk, anti-bullshit-mcp-server
- **Hamming swarm**: All 28 wallet addresses return null balance on Aptos mainnet — addresses likely not funded/initialized
- **All 5 multisig contracts**: 2-of-N threshold confirmed healthy
