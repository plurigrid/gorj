# LATEST_SWEEP — 2026-08-08

## GitHub Social Graph Sweep

### Table Counts
```
┌──────────────────┬───────┐
│       tbl        │  cnt  │
│     varchar      │ int64 │
├──────────────────┼───────┤
│ world_increments │   101 │
│ repo_snapshots   │  1022 │
│ aptos_snapshots  │    28 │
│ multisig_probes  │     5 │
└──────────────────┴───────┘

```

### Orgs/Users Snapshotted
```
┌───────────────┬───────┬──────────────────────┐
│  org_or_user  │ repos │     latest_push      │
│    varchar    │ int64 │       varchar        │
├───────────────┼───────┼──────────────────────┤
│ plurigrid     │   216 │ 2026-08-08T20:14:20Z │
│ bmorphism     │   215 │ 2026-08-07T02:35:47Z │
│ TeglonLabs    │   111 │ 2026-06-08T19:03:03Z │
│ kubeflow      │   107 │ 2026-08-08T17:09:05Z │
│ AustinCStone  │    90 │ 2026-07-15T05:19:33Z │
│ migalkin      │    66 │ 2026-07-10T15:40:00Z │
│ wasita        │    65 │ 2026-08-07T20:46:15Z │
│ zubyul        │    55 │ 2026-07-18T12:02:57Z │
│ kristinezheng │    38 │ 2026-07-01T20:57:48Z │
│ M1shaaa       │    34 │ 2026-04-13T13:19:39Z │
│ DJedamski     │    25 │ 2023-04-21T01:42:35Z │
└───────────────┴───────┴──────────────────────┘
  11 rows                            3 columns

```

### Top Repos by Stars
```
┌─────────────┬────────────────────────┬──────────┬───────┬───────┬──────────────────────┐
│ org_or_user │       repo_name        │ language │ stars │ forks │      pushed_at       │
│   varchar   │        varchar         │ varchar  │ int32 │ int32 │       varchar        │
├─────────────┼────────────────────────┼──────────┼───────┼───────┼──────────────────────┤
│ kubeflow    │ kubeflow               │          │ 15806 │  2691 │ 2026-07-10T11:31:26Z │
│ kubeflow    │ kubeflow               │ NULL     │ 15572 │  2633 │ 2026-01-05T13:47:10Z │
│ kubeflow    │ kubeflow               │          │ 15565 │  2626 │ 2026-01-05T13:47:10Z │
│ kubeflow    │ pipelines              │ Python   │  4182 │  2084 │ 2026-08-07T18:28:08Z │
│ kubeflow    │ pipelines              │ Python   │  4119 │  1984 │ 2026-04-10T23:07:19Z │
│ kubeflow    │ pipelines              │ Python   │  4119 │  1985 │ 2026-04-14T01:20:50Z │
│ kubeflow    │ spark-operator         │ Python   │  3145 │  1512 │ 2026-08-08T13:53:59Z │
│ kubeflow    │ spark-operator         │ Python   │  3114 │  1483 │ 2026-04-13T18:28:43Z │
│ kubeflow    │ spark-operator         │ Python   │  3111 │  1483 │ 2026-04-10T18:21:12Z │
│ kubeflow    │ trainer                │ Go       │  2176 │  1018 │ 2026-08-08T00:56:11Z │
│ kubeflow    │ trainer                │ Go       │  2082 │   945 │ 2026-04-13T23:41:09Z │
│ kubeflow    │ trainer                │ Go       │  2080 │   944 │ 2026-04-10T13:35:59Z │
│ kubeflow    │ katib                  │ Python   │  1694 │   535 │ 2026-08-06T23:09:31Z │
│ kubeflow    │ katib                  │ Python   │  1678 │   521 │ 2026-04-14T01:21:37Z │
│ kubeflow    │ katib                  │ Python   │  1676 │   521 │ 2026-04-02T07:08:12Z │
│ kubeflow    │ examples               │ Jsonnet  │  1461 │   755 │ 2025-04-14T01:54:52Z │
│ kubeflow    │ examples               │ Jsonnet  │  1459 │   756 │ 2025-04-14T01:54:52Z │
│ kubeflow    │ examples               │ Jsonnet  │  1458 │   755 │ 2025-04-14T01:54:52Z │
│ kubeflow    │ community-distribution │ YAML     │  1030 │  1070 │ 2026-08-04T17:39:30Z │
│ kubeflow    │ manifests              │ YAML     │  1010 │  1069 │ 2026-04-11T13:16:34Z │
└─────────────┴────────────────────────┴──────────┴───────┴───────┴──────────────────────┘
  20 rows                                                                      6 columns

```

## Hamming Swarm Snapshot — Aptos Mainnet

### Wallet Balances (alice–Z, 28 addresses)
All 28 Hamming swarm addresses returned **CoinStore not found** on Aptos mainnet
(ledger version ~6.67B). These addresses have not been initialized with APT coin
storage — balances read as 0.0 APT across all worlds (alice, bob, A–Z).

```
┌─────────┬────────────────────────────────────────────────────────────────────┬─────────────┐
│  world  │                              address                               │ balance_apt │
│ varchar │                              varchar                               │   double    │
├─────────┼────────────────────────────────────────────────────────────────────┼─────────────┤
│ A       │ 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a │         0.0 │
│ B       │ 0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13 │         0.0 │
│ C       │ 0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e │         0.0 │
│ D       │ 0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1 │         0.0 │
│ E       │ 0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36 │         0.0 │
│ F       │ 0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71 │         0.0 │
│ G       │ 0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32 │         0.0 │
│ H       │ 0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f │         0.0 │
│ I       │ 0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9 │         0.0 │
│ J       │ 0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54 │         0.0 │
└─────────┴────────────────────────────────────────────────────────────────────┴─────────────┘
  10 rows                                                                          3 columns

```
*(first 10 shown; all 28 stored in aptos_snapshots table)*

### Multisig Contract Probes (5 pairs)
```
┌─────────┬────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
│  pair   │                              address                               │ sigs_required │ healthy │
│ varchar │                              varchar                               │     int32     │ boolean │
├─────────┼────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
│ A-B     │ 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 │             2 │ true    │
│ A-G     │ 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 │             2 │ true    │
│ S-T     │ 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 │             2 │ true    │
│ V-W     │ 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d │             2 │ true    │
│ Y-Z     │ 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 │             2 │ true    │
└─────────┴────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

```
All 5 multisig pairs are **healthy** — each requires exactly **2 signatures**.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4... | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)
**Unavailable** — testnet.mnx.fi serves a Next.js SPA with client-side rendering;
no REST/JSON API endpoint responded with market data at `/api/markets` or `/api/v1/markets`.
No rows inserted into mnx_snapshots.

## GF(3) Color Chain

Increment IDs cycle through the GF(3) trit color chain:
- `id % 3 == 0` → trit=0, **ERGODIC** `#d3869b`
- `id % 3 == 1` → trit=1, **PLUS** `#b8bb26`
- `id % 3 == 2` → trit=-1, **MINUS** `#cc241d`

## Sources Covered

| Source | Type | Notes |
|--------|------|-------|
| plurigrid | org | 100 repos (incl. gorj, place, asi, zig-syrup) |
| kubeflow | org | 49 repos (kubeflow 15.8k★, pipelines 4.2k★) |
| TeglonLabs | org | 5 repos (jank-crane, mathpix-gem, coin-flip-mcp) |
| bmorphism | user | 100 repos (ocaml-mcp-sdk 61★, Gay.jl, MCP servers) |
| zubyul | user | 49 repos (gay-world, nash-tui, tilelang-kernels) |
| migalkin | social | 19 repos (NodePiece 144★, StarE 89★) |
| DJedamski | social | 6 repos |
| wasita | social | 14 repos (active: wm-cv pushed 2026-08-07) |
| kristinezheng | social | 5 repos |
| M1shaaa | social | 8 repos |
| AustinCStone | social | 41 repos (TextGAN 92★) |

DuckDB: `packages/world-increment/ducklake/world-increments.duckdb`
