# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-12 05:37:53 UTC
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Users:** bmorphism, zubyul
- **Social graph (zubyul connections):** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone
- **Events:** bmorphism and zubyul recent public events

### Repository Counts by Source

```
┌───────────────┬───────┐
│  org_or_user  │ repos │
│    varchar    │ int64 │
├───────────────┼───────┤
│ plurigrid     │   104 │
│ bmorphism     │   100 │
│ TeglonLabs    │    53 │
│ kubeflow      │    47 │
│ AustinCStone  │    43 │
│ migalkin      │    30 │
│ wasita        │    29 │
│ zubyul        │    24 │
│ kristinezheng │    18 │
│ M1shaaa       │    16 │
│ DJedamski     │    11 │
└───────────────┴───────┘
  11 rows     2 columns
```

**Total distinct repos snapshotted:** │                       475 │

### Top Repos by Stars

```
┌───────────────────────────┬───────┬──────────┐
│         full_name         │ stars │ language │
│          varchar          │ int32 │ varchar  │
├───────────────────────────┼───────┼──────────┤
│ kubeflow/kubeflow         │ 15566 │ NULL     │
│ kubeflow/kubeflow         │ 15565 │          │
│ kubeflow/pipelines        │  4119 │ Python   │
│ kubeflow/spark-operator   │  3111 │ Python   │
│ kubeflow/trainer          │  2080 │ Go       │
│ kubeflow/katib            │  1676 │ Python   │
│ kubeflow/examples         │  1458 │ Jsonnet  │
│ kubeflow/manifests        │  1010 │ YAML     │
│ kubeflow/arena            │   808 │ Go       │
│ kubeflow/kale             │   682 │ Python   │
│ kubeflow/mpi-operator     │   522 │ Go       │
│ kubeflow/fairing          │   337 │ Jsonnet  │
│ kubeflow/pytorch-operator │   309 │ Jsonnet  │
│ kubeflow/community        │   194 │ Jsonnet  │
│ kubeflow/website          │   184 │ HTML     │
└───────────────────────────┴───────┴──────────┘
  15 rows                            3 columns
```

### Recent Events (bmorphism + zubyul)

```
┌───────────┬──────────────────┬─────────────┐
│   actor   │    event_type    │  repo_name  │
│  varchar  │     varchar      │   varchar   │
├───────────┼──────────────────┼─────────────┤
│ bmorphism │ PushEvent        │ asi         │
│ bmorphism │ PushEvent        │ horse       │
│ bmorphism │ CreateEvent      │ horse       │
│ bmorphism │ PullRequestEvent │ horse       │
│ bmorphism │ PushEvent        │ web-browser │
│ bmorphism │ PushEvent        │ graywall    │
│ zubyul    │ PullRequestEvent │ horse       │
│ zubyul    │ PullRequestEvent │ gorj        │
│ zubyul    │ CreateEvent      │ gorj        │
│ zubyul    │ PushEvent        │ gorj        │
└───────────┴──────────────────┴─────────────┘
  10 rows                          3 columns
```

### GF(3) Color Chain Distribution

| Name | Color | Count | Trit |
|------|-------|-------|------|
| ERGODIC | #d3869b (pink) | ~26 | 0 |
| PLUS | #b8bb26 (green) | ~28 | 1 |
| MINUS | #cc241d (red) | ~27 | -1 |

```
┌──────────┬───────────┬───────┐
│ gf3_name │ gf3_color │ count │
│ varchar  │  varchar  │ int64 │
├──────────┼───────────┼───────┤
│ ERGODIC  │ #d3869b   │    26 │
│ MINUS    │ #cc241d   │    27 │
│ PLUS     │ #b8bb26   │    28 │
└──────────┴───────────┴───────┘
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses queried against Aptos mainnet `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
All returned **HTTP 404** — wallets are unfunded/inactive on mainnet (no CoinStore resource).

```
┌─────────┬─────────────┐
│  world  │ balance_apt │
│ varchar │   double    │
├─────────┼─────────────┤
│ alice   │         0.0 │
│ bob     │         0.0 │
│ A       │         0.0 │
│ B       │         0.0 │
│ C       │         0.0 │
│ D       │         0.0 │
│ E       │         0.0 │
│ F       │         0.0 │
│ G       │         0.0 │
│ H       │         0.0 │
└─────────┴─────────────┘
  10 rows     2 columns
```

### Multisig Contract Probes

```
┌─────────┬────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
│  pair   │                              address                               │ sigs_required │ healthy │
│ varchar │                              varchar                               │     int32     │ boolean │
├─────────┼────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
│ A-B     │ 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 │             2 │ true    │
│ A-G     │ 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 │             2 │ true    │
│ Y-Z     │ 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 │             2 │ true    │
│ S-T     │ 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 │             2 │ true    │
│ V-W     │ 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d │             2 │ true    │
└─────────┴────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘
```

**Result:** All 5 multisig contracts are **healthy** — each requires 2-of-N signatures.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

### MNX Testnet Markets

**Status: UNAVAILABLE** — `testnet.mnx.fi` is a Next.js SPA connecting to `api.testnet.mnx.fi` via WebSocket only. No REST endpoints are publicly accessible. Recorded as unavailable in `mnx_snapshots`.

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 81 |
| repo_snapshots | 531 (475 distinct repos) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## Notes

- GitHub API rate limit hit for unauthenticated requests (plurigrid org fetched via MCP search tool; others via public API)
- kristinezheng repos rate-limited during social graph sweep
- Aptos addresses: 404 = account exists but has never received APT (no `CoinStore` resource initialized)
- All multisig accounts on Aptos mainnet: 2 sigs required, healthy
- MNX testnet is WebSocket-only SPA; no REST market data API available
