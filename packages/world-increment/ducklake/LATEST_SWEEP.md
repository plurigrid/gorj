# World Increment Sweep — 2026-06-21

**Run:** 2026-06-21T00:11:17Z
**GF(3) Color Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user (zubyul graph) | 40 |
| migalkin | user (zubyul graph) | 19 |
| wasita | user (zubyul graph) | 11 |
| M1shaaa | user (zubyul graph) | 8 |
| DJedamski | user (zubyul graph) | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user (zubyul graph) | 5 |
| **Total** | | **391** |

### Top Repos by Stars

```
full_name,stars,language,pushed_at
full_name,stars,language,pushed_at
kubeflow/kubeflow,15737,,2026-06-18T11:45:16Z
kubeflow/pipelines,4155,Python,2026-06-20T19:12:02Z
kubeflow/spark-operator,3127,Python,2026-06-18T15:39:22Z
kubeflow/trainer,2118,Go,2026-06-19T15:46:05Z
kubeflow/katib,1683,Python,2026-06-20T23:29:45Z
kubeflow/examples,1460,Jsonnet,2025-04-14T01:54:52Z
kubeflow/community-distribution,1025,YAML,2026-06-18T19:10:25Z
kubeflow/arena,813,Go,2026-05-07T06:46:17Z
kubeflow/kale,694,Python,2026-06-20T11:20:36Z
kubeflow/mpi-operator,528,Go,2026-06-15T13:03:34Z
```

### Language Distribution (Top 10)

```
language,count
language,cnt
Python,81
JavaScript,26
Rust,26
TypeScript,23
HTML,17
Jupyter Notebook,15
Go,15
Clojure,12
Julia,9
Jsonnet,7
```

### Most Recently Pushed (Top 10)

```
org_or_user,repo_name,pushed_at
org_or_user,repo_name,pushed_at
kubeflow,katib,2026-06-20T23:29:45Z
plurigrid,gorj,2026-06-20T23:09:59Z
kubeflow,pipelines,2026-06-20T19:12:02Z
kubeflow,notebooks,2026-06-20T17:12:47Z
kubeflow,hub,2026-06-20T15:40:26Z
kubeflow,dashboard,2026-06-20T15:13:23Z
M1shaaa,M1shaaa,2026-06-20T13:54:08Z
bmorphism,satreadout,2026-06-20T13:05:41Z
kubeflow,kale,2026-06-20T11:20:36Z
kubeflow,pipelines-components,2026-06-20T03:06:51Z
```

### GF(3) Trit Distribution

```
gf3_name,gf3_color,count
gf3_name,gf3_color,count_star()
PLUS,#b8bb26,131
MINUS,#cc241d,130
ERGODIC,#d3869b,130
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All 28 wallets (alice, bob, A–Z) queried against Aptos Mainnet.

**Result:** All wallets returned 0 APT — the `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource is absent on all addresses, indicating these wallets exist on-chain but hold no native APT (possibly Move objects / fungible asset model accounts).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0 |
| bob | 0x0a3c...512d | 0 |
| A–Z | (26 addresses) | 0 each |

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig contracts are live and require 2-of-N signatures.

### MNX Markets

**Status:** Unavailable — `testnet.mnx.fi` is behind Vercel deployment protection (visitor password required). No market data could be extracted.

---

## DuckDB Ducklake Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 391 |
| repo_snapshots | 391 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
