# LATEST_SWEEP — 2026-06-14 14:11:33 UTC

## JOB 1: GitHub Social Graph Sweep

### Sources Crawled
| Source | Type |
|--------|------|
| plurigrid | org |
| kubeflow | org |
| TeglonLabs | org |
| bmorphism | user |
| zubyul | user |
| migalkin | social graph |
| DJedamski | social graph |
| wasita | social graph |
| kristinezheng | social graph |
| M1shaaa | social graph |
| AustinCStone | social graph |

### Top Repos by Stars
```
┌─────────────────────────┬──────────┬───────┬─────────────┐
│        full_name        │ language │ stars │ open_issues │
│         varchar         │ varchar  │ int32 │    int32    │
├─────────────────────────┼──────────┼───────┼─────────────┤
│ kubeflow/kubeflow       │          │ 15721 │           3 │
│ kubeflow/kubeflow       │ NULL     │ 15572 │           0 │
│ kubeflow/kubeflow       │          │ 15565 │           0 │
│ kubeflow/pipelines      │ Python   │  4153 │         479 │
│ kubeflow/pipelines      │ Python   │  4119 │         469 │
│ kubeflow/pipelines      │ Python   │  4119 │         471 │
│ kubeflow/spark-operator │ Python   │  3127 │         102 │
│ kubeflow/spark-operator │ Python   │  3114 │          86 │
│ kubeflow/spark-operator │ Python   │  3111 │          85 │
│ kubeflow/trainer        │ Go       │  2115 │         113 │
└─────────────────────────┴──────────┴───────┴─────────────┘
  10 rows                                        4 columns
```

### Hottest by Open Issues
```
┌────────────────────┬─────────────┐
│     full_name      │ open_issues │
│      varchar       │    int32    │
├────────────────────┼─────────────┤
│ plurigrid/gorj     │         572 │
│ kubeflow/pipelines │         479 │
│ kubeflow/pipelines │         471 │
│ kubeflow/pipelines │         469 │
│ bmorphism/Gay.jl   │         189 │
└────────────────────┴─────────────┘
```

### GF(3) Color Chain Distribution
```
┌──────────┬───────────┬──────────────┐
│ gf3_name │ gf3_color │ count_star() │
│ varchar  │  varchar  │    int64     │
├──────────┼───────────┼──────────────┤
│ PLUS     │ #b8bb26   │           12 │
│ MINUS    │ #cc241d   │           12 │
│ ERGODIC  │ #d3869b   │           10 │
└──────────┴───────────┴──────────────┘
```
- trit=0 ERGODIC #d3869b — id%3==0
- trit=1 PLUS #b8bb26 — id%3==1
- trit=-1 MINUS #cc241d — id%3==2

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, alice–Z)
All 28 Hamming-swarm wallets returned **0 APT** (CoinStore resource not initialized on mainnet for any address in the swarm).

Non-zero balances:
```
┌─────────┬─────────────┐
│  world  │ balance_apt │
│ varchar │   double    │
└─────────┴─────────────┘
         0 rows
```

### Multisig Contract Probes (5 pairs)
```
┌─────────┬───────────────┬─────────┐
│  pair   │ sigs_required │ healthy │
│ varchar │     int32     │ boolean │
├─────────┼───────────────┼─────────┤
│ A-B     │             2 │ true    │
│ A-G     │             2 │ true    │
│ Y-Z     │             2 │ true    │
│ S-T     │             2 │ true    │
│ V-W     │             2 │ true    │
└─────────┴───────────────┴─────────┘
```
All 5 multisig contracts are **healthy** — each requires **2-of-N signatures**.

### MNX Markets
`https://testnet.mnx.fi` is deployed behind **Vercel deployment protection** (authentication required). Market data is unavailable without a bypass token or trusted OIDC source. No mnx_snapshots inserted.

---

## DuckDB Schema Summary
- `world_increments` — GF(3) trit-colored sweep events
- `repo_snapshots` — GitHub repo metadata (stars, forks, language, open issues)
- `aptos_snapshots` — Hamming swarm wallet balances
- `multisig_probes` — Aptos multisig 2-of-N health checks
- `mnx_snapshots` — MNX market tickers (empty this sweep; auth required)

DB path: `packages/world-increment/ducklake/world-increments.duckdb`
