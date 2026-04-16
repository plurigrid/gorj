# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-16 22:09:42 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 99 |
| zubyul | user | 47 |
| migalkin | social-graph | 19 |
| DJedamski | social-graph | 6 |
| wasita | social-graph | 10 |
| kristinezheng | social-graph | 6 |
| M1shaaa | social-graph | 8 |
| AustinCStone | social-graph | 40 |

**Total this sweep:** 386 repos  
**Total in DB:** 409 world_increments, 1330 repo_snapshots (cumulative)

### GF(3) Trit Color Chain Distribution (this sweep)

```
┌──────────┬───────────┬───────┐
│ gf3_name │ gf3_color │ count │
│ varchar  │  varchar  │ int64 │
├──────────┼───────────┼───────┤
│ ERGODIC  │ #d3869b   │   128 │
│ MINUS    │ #cc241d   │   129 │
│ PLUS     │ #b8bb26   │   129 │
└──────────┴───────────┴───────┘
```

- **ERGODIC (trit=0, #d3869b):** id%3==0
- **PLUS (trit=1, #b8bb26):** id%3==1
- **MINUS (trit=-1, #cc241d):** id%3==2

### Top Repos by Stars

```
┌─────────────┬───────────────────────────┬───────┬──────────┬──────────────────────┐
│ org_or_user │         full_name         │ stars │ language │      pushed_at       │
│   varchar   │          varchar          │ int32 │ varchar  │       varchar        │
├─────────────┼───────────────────────────┼───────┼──────────┼──────────────────────┤
│ kubeflow    │ kubeflow/kubeflow         │ 15579 │          │ 2026-01-05T13:47:10Z │
│ kubeflow    │ kubeflow/pipelines        │  4121 │ Python   │ 2026-04-16T20:51:26Z │
│ kubeflow    │ kubeflow/spark-operator   │  3117 │ Python   │ 2026-04-16T20:50:24Z │
│ kubeflow    │ kubeflow/trainer          │  2085 │ Go       │ 2026-04-15T15:27:51Z │
│ kubeflow    │ kubeflow/katib            │  1679 │ Python   │ 2026-04-14T01:21:37Z │
│ kubeflow    │ kubeflow/examples         │  1460 │ Jsonnet  │ 2025-04-14T01:54:52Z │
│ kubeflow    │ kubeflow/manifests        │  1010 │ YAML     │ 2026-04-11T13:16:34Z │
│ kubeflow    │ kubeflow/arena            │   809 │ Go       │ 2026-04-16T20:51:18Z │
│ kubeflow    │ kubeflow/kale             │   682 │ Python   │ 2026-04-16T11:25:52Z │
│ kubeflow    │ kubeflow/mpi-operator     │   524 │ Go       │ 2026-04-14T03:16:20Z │
│ kubeflow    │ kubeflow/fairing          │   337 │ Jsonnet  │ 2022-04-11T05:28:47Z │
│ kubeflow    │ kubeflow/pytorch-operator │   309 │ Jsonnet  │ 2021-12-01T17:44:48Z │
│ kubeflow    │ kubeflow/community        │   195 │ Jsonnet  │ 2026-04-08T14:50:20Z │
│ kubeflow    │ kubeflow/website          │   184 │ HTML     │ 2026-04-08T05:10:14Z │
│ kubeflow    │ kubeflow/kfctl            │   182 │ Go       │ 2023-08-15T20:19:22Z │
└─────────────┴───────────────────────────┴───────┴──────────┴──────────────────────┘
  15 rows                                                                 5 columns
```

### Per-Source Breakdown

```
┌───────────────┬───────┬─────────────┬───────────────────────┐
│  org_or_user  │ repos │ total_stars │       top_lang        │
│    varchar    │ int64 │   int128    │        varchar        │
├───────────────┼───────┼─────────────┼───────────────────────┤
│ plurigrid     │   100 │          64 │ Zig                   │
│ bmorphism     │    99 │         248 │ Zig                   │
│ zubyul        │    47 │          14 │ Zig                   │
│ kubeflow      │    47 │       33892 │ YAML                  │
│ AustinCStone  │    40 │         108 │ TeX                   │
│ migalkin      │    19 │         278 │ Web Ontology Language │
│ wasita        │    10 │           2 │ Typst                 │
│ M1shaaa       │     8 │           0 │ TypeScript            │
│ kristinezheng │     6 │           0 │ Python                │
│ DJedamski     │     6 │           3 │ R                     │
│ TeglonLabs    │     4 │           2 │ Ruby                  │
└───────────────┴───────┴─────────────┴───────────────────────┘
  11 rows                                           4 columns
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A-Z)

**Endpoint:** `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{ADDR}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Status |
|-------|--------|
| alice | No CoinStore resource (account unfunded or not initialized) |
| bob | No CoinStore resource |
| A–Z (26 wallets) | No CoinStore resources on mainnet |

All 28 addresses queried. Accounts exist on-chain but have not been initialized with a CoinStore resource for AptosCoin (typical for fresh or testnet-only accounts probed on mainnet).

### Multisig Contract Probes

**Endpoint:** `POST https://fullnode.mainnet.aptoslabs.com/v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428...` | 2 | ✓ |
| A-G | `0xf56c4a1c...` | 2 | ✓ |
| Y-Z | `0xd3ffe181...` | 2 | ✓ |
| S-T | `0x3b1c3ae9...` | 2 | ✓ |
| V-W | `0x40fad7b4...` | 2 | ✓ |

**All 5 multisig contracts healthy** — each requires 2-of-N signatures.

### MNX Markets

**Endpoint probed:** `https://testnet.mnx.fi` + `/api/markets`, `/api/v1/markets`, `/markets`

**Status:** Unavailable — testnet.mnx.fi serves a SPA with no accessible JSON API endpoints. Market data recorded as N/A placeholder in `mnx_snapshots` table.

---

## DuckDB Ducklake Schema

```
world_increments  — 409 rows (GF3-tagged event log)
repo_snapshots    — 1330 rows (GitHub repo metadata snapshots)
aptos_snapshots   — 28 rows (Hamming swarm wallet balances)
multisig_probes   — 5 rows (multisig contract health)
mnx_snapshots     — 1 row (MNX market data, unavailable)
```

DB path: `packages/world-increment/ducklake/world-increments.duckdb`
