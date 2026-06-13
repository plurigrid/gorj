# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-13  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 4 |
| AustinCStone | social graph | 3 |
| kristinezheng | social graph | 3 |
| M1shaaa | social graph | 3 |
| DJedamski | social graph | 3 |

**Total repo snapshots: 337**

### Top Repos by Stars
```
┌─────────────┬────────────────────────┬───────┬──────────────────┐
│ org_or_user │       repo_name        │ stars │     language     │
│   varchar   │        varchar         │ int32 │     varchar      │
├─────────────┼────────────────────────┼───────┼──────────────────┤
│ kubeflow    │ kubeflow               │ 15720 │                  │
│ kubeflow    │ pipelines              │  4152 │ Python           │
│ kubeflow    │ spark-operator         │  3127 │ Python           │
│ kubeflow    │ trainer                │  2112 │ Go               │
│ kubeflow    │ katib                  │  1683 │ Python           │
│ kubeflow    │ examples               │  1461 │ Jsonnet          │
│ kubeflow    │ community-distribution │  1023 │ YAML             │
│ kubeflow    │ arena                  │   812 │ Go               │
│ kubeflow    │ kale                   │   694 │ Python           │
│ kubeflow    │ mpi-operator           │   528 │ Go               │
│ kubeflow    │ fairing                │   337 │ Jsonnet          │
│ kubeflow    │ pytorch-operator       │   310 │ Jsonnet          │
│ kubeflow    │ community              │   194 │ Jupyter Notebook │
│ kubeflow    │ website                │   184 │ HTML             │
│ kubeflow    │ kfctl                  │   182 │ Go               │
└─────────────┴────────────────────────┴───────┴──────────────────┘
  15 rows                                               4 columns
```

### Source Breakdown
```
┌───────────────┬───────┬─────────────┐
│  org_or_user  │ repos │ total_stars │
│    varchar    │ int64 │   int128    │
├───────────────┼───────┼─────────────┤
│ plurigrid     │   100 │          77 │
│ bmorphism     │   100 │         247 │
│ zubyul        │    49 │          14 │
│ kubeflow      │    48 │       34201 │
│ migalkin      │    19 │         280 │
│ TeglonLabs    │     5 │           2 │
│ wasita        │     4 │           4 │
│ kristinezheng │     3 │           0 │
│ M1shaaa       │     3 │           0 │
│ AustinCStone  │     3 │         103 │
│ DJedamski     │     3 │           3 │
└───────────────┴───────┴─────────────┘
  11 rows                   3 columns
```

### GF(3) Color Chain Distribution
```
┌───────────┬──────────┬──────────────┐
│ gf3_color │ gf3_name │ count_star() │
│  varchar  │ varchar  │    int64     │
├───────────┼──────────┼──────────────┤
│ #d3869b   │ ERGODIC  │          113 │
│ #cc241d   │ MINUS    │          112 │
│ #b8bb26   │ PLUS     │          112 │
└───────────┴──────────┴──────────────┘
```
> trit=0 ERGODIC #d3869b | trit=1 PLUS #b8bb26 | trit=-1 MINUS #cc241d

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances
```
┌─────────┬─────────────┬────────────────────────────────────────────────────────────────────┐
│  world  │ balance_apt │                              address                               │
│ varchar │   double    │                              varchar                               │
├─────────┼─────────────┼────────────────────────────────────────────────────────────────────┤
│ bob     │   12.657007 │ 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d │
│ F       │    1.960516 │ 0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71 │
│ L       │    1.927269 │ 0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9 │
│ J       │    1.895093 │ 0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54 │
│ alice   │  0.43643352 │ 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b │
│ O       │    0.210136 │ 0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d │
│ K       │    0.161961 │ 0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4 │
│ P       │    0.140136 │ 0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948 │
│ M       │    0.112285 │ 0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9 │
│ N       │    0.106121 │ 0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c │
│ Q       │     0.10324 │ 0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9 │
│ S       │    0.091788 │ 0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386 │
│ R       │    0.090217 │ 0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10 │
│ T       │    0.073713 │ 0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588 │
│ U       │    0.055773 │ 0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956 │
│ A       │    0.051767 │ 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a │
│ V       │  0.04883299 │ 0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3 │
│ Y       │    0.044449 │ 0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4 │
│ X       │    0.042577 │ 0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d │
│ W       │    0.040705 │ 0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0 │
│ B       │    0.036256 │ 0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13 │
│ Z       │    0.024268 │ 0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c │
│ D       │    0.011629 │ 0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1 │
│ C       │    0.010185 │ 0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e │
│ E       │    0.009372 │ 0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36 │
│ H       │    0.001681 │ 0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f │
│ I       │    0.000681 │ 0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9 │
│ G       │    0.000681 │ 0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32 │
└─────────┴─────────────┴────────────────────────────────────────────────────────────────────┘
  28 rows                                                                          3 columns
```

**Total APT:**
```
┌─────────────┬─────────┐
│  total_apt  │ wallets │
│   double    │  int64  │
├─────────────┼─────────┤
│ 20.34477251 │      28 │
└─────────────┴─────────┘
```

### Multisig Contract Probes
All 5 multisig contracts healthy — **2-of-2 signatures required** each:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...4987003 | 2 | ✅ healthy |
| A-G | 0xf56c4a1c...bc0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✅ healthy |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✅ healthy |
| V-W | 0x40fad7b4...80eb6d | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)
Status: **Unavailable** — `https://testnet.mnx.fi` and `https://testnet.mnx.fi/api/markets` both returned HTTP 401 Unauthorized. No market data extractable.

---

## Notes
- Aptos accounts use **`0x1::coin::balance` view function** (not legacy CoinStore — accounts exist but run FA format)
- **bob** holds the largest balance: **12.657 APT**
- Worlds **F, L, J** all hold ~1.9 APT each
- All world_increment IDs assigned GF(3) color via `id % 3`
- DuckDB ducklake created at: `packages/world-increment/ducklake/world-increments.duckdb`
