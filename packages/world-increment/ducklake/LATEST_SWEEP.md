# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-06-15 13:17:26 UTC
**Branch:** world-increment/sweep-2026-06-15-1317

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Users:** bmorphism, zubyul
- **Zubyul social graph:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

### This-Sweep GF(3) Color Chain Distribution
```
┌──────────┬───────────┬───────┐
│ gf3_name │ gf3_color │   n   │
│ varchar  │  varchar  │ int64 │
├──────────┼───────────┼───────┤
│ PLUS     │ #b8bb26   │   119 │
│ MINUS    │ #cc241d   │   119 │
│ ERGODIC  │ #d3869b   │   119 │
└──────────┴───────────┴───────┘
```

### Repo Count by Source (this sweep)
```
┌──────────────┬───────┬─────────┬────────┬────────┐
│ source_name  │ repos │ ergodic │  plus  │ minus  │
│   varchar    │ int64 │ int128  │ int128 │ int128 │
├──────────────┼───────┼─────────┼────────┼────────┤
│ bmorphism    │   100 │      33 │     34 │     33 │
│ plurigrid    │   100 │      33 │     34 │     33 │
│ social_graph │    55 │      19 │     18 │     18 │
│ zubyul       │    49 │      16 │     16 │     17 │
│ kubeflow     │    48 │      16 │     16 │     16 │
│ TeglonLabs   │     5 │       2 │      1 │      2 │
└──────────────┴───────┴─────────┴────────┴────────┘
```

### Top Repos by Stars (this sweep)
```
┌─────────────────────────────────┬──────────────────┬───────┬───────┬─────────────┐
│            full_name            │     language     │ stars │ forks │ open_issues │
│             varchar             │     varchar      │ int32 │ int32 │    int32    │
├─────────────────────────────────┼──────────────────┼───────┼───────┼─────────────┤
│ kubeflow/kubeflow               │                  │ 15725 │  2673 │           3 │
│ kubeflow/pipelines              │ Python           │  4154 │  2007 │         473 │
│ kubeflow/spark-operator         │ Python           │  3127 │  1490 │         101 │
│ kubeflow/trainer                │ Go               │  2115 │   969 │         115 │
│ kubeflow/katib                  │ Python           │  1683 │   527 │         116 │
│ kubeflow/examples               │ Jsonnet          │  1461 │   756 │         111 │
│ kubeflow/community-distribution │ YAML             │  1023 │  1065 │          22 │
│ kubeflow/arena                  │ Go               │   812 │   190 │          44 │
│ kubeflow/kale                   │ Python           │   694 │   154 │          48 │
│ kubeflow/mpi-operator           │ Go               │   528 │   236 │         106 │
│ kubeflow/fairing                │ Jsonnet          │   337 │   143 │         134 │
│ kubeflow/pytorch-operator       │ Jsonnet          │   310 │   143 │          63 │
│ kubeflow/community              │ Jupyter Notebook │   194 │   260 │          24 │
│ kubeflow/website                │ HTML             │   184 │   923 │          51 │
│ kubeflow/kfctl                  │ Go               │   182 │   134 │          94 │
└─────────────────────────────────┴──────────────────┴───────┴───────┴─────────────┘
  15 rows                                                                5 columns
```

### Most Recently Pushed (since 2026-06-14)
```
┌─────────────────────────────────┬──────────────────────┬───────┐
│            full_name            │      pushed_at       │ stars │
│             varchar             │       varchar        │ int32 │
├─────────────────────────────────┼──────────────────────┼───────┤
│ kubeflow/mpi-operator           │ 2026-06-15T13:03:34Z │   528 │
│ kubeflow/hub                    │ 2026-06-15T12:57:58Z │   173 │
│ plurigrid/gorj                  │ 2026-06-15T12:17:01Z │     0 │
│ kubeflow/website                │ 2026-06-15T11:38:22Z │   184 │
│ kubeflow/community-distribution │ 2026-06-15T09:56:57Z │  1023 │
│ kubeflow/pipelines              │ 2026-06-15T07:37:49Z │  4154 │
│ bmorphism/Gay.jl                │ 2026-06-15T00:44:40Z │     1 │
│ kubeflow/community              │ 2026-06-14T21:03:42Z │   194 │
│ kubeflow/spark-operator         │ 2026-06-14T16:43:38Z │  3127 │
└─────────────────────────────────┴──────────────────────┴───────┘
```

### Key Observations
- **plurigrid/gorj** (this repo): 594 open issues, last pushed 2026-06-15 — active
- **kubeflow/kubeflow**: 15,725 stars — flagship ML toolkit
- **kubeflow/pipelines**: 4,154 stars, 473 open issues — very active
- **bmorphism/Gay.jl**: 189 open issues, pushed today — most active bmorphism repo
- **bmorphism/ocaml-mcp-sdk**: 61 stars — highest starred bmorphism repo
- **plurigrid/asi**: 26 stars, pushed 2026-06-10 — most starred plurigrid repo
- **migalkin/NodePiece**: 144 stars — top social-graph repo
- **TeglonLabs/jank-crane** (C++): pushed 2026-06-08 — most recent TeglonLabs activity

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice–Z)

All 28 Hamming swarm addresses queried. **All returned 0.0 APT** — CoinStore resources not found on mainnet (addresses may not hold APT or may be empty).

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
│ K       │ 0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4 │         0.0 │
│ L       │ 0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9 │         0.0 │
│ M       │ 0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9 │         0.0 │
│ N       │ 0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c │         0.0 │
│ O       │ 0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d │         0.0 │
│ P       │ 0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948 │         0.0 │
│ Q       │ 0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9 │         0.0 │
│ R       │ 0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10 │         0.0 │
│ S       │ 0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386 │         0.0 │
│ T       │ 0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588 │         0.0 │
│ U       │ 0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956 │         0.0 │
│ V       │ 0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3 │         0.0 │
│ W       │ 0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0 │         0.0 │
│ X       │ 0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d │         0.0 │
│ Y       │ 0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4 │         0.0 │
│ Z       │ 0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c │         0.0 │
│ alice   │ 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b │         0.0 │
│ bob     │ 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d │         0.0 │
└─────────┴────────────────────────────────────────────────────────────────────┴─────────────┘
  28 rows                                                                          3 columns
```

### Multisig Contract Probes

**All 5 multisig contracts healthy** — each requires 2 signatures.

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

| Pair | Contract | Sigs Required | Status |
|------|----------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ healthy |
| A-G | 0xf56c4a1c... | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181... | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9... | 2 | ✓ healthy |
| V-W | 0x40fad7b4... | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — All probed endpoints (/, /api/markets, /api/v1/markets, /markets) returned no data. The testnet SPA does not expose a public REST API at these paths.

---

## DuckDB Ducklake Stats

| Table | Cumulative Rows |
|-------|-----------------|
| world_increments | 380 |
| repo_snapshots | 1301 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

Database: `packages/world-increment/ducklake/world-increments.duckdb`
