# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-29 21:13:21 UTC
**Branch:** world-increment/sweep

---

## JOB 1: GitHub Social Graph Sweep

### Sources Covered

| Source | Type |
|--------|------|
| plurigrid | Org |
| kubeflow | Org |
| TeglonLabs | Org |
| bmorphism | User |
| zubyul | User |
| migalkin | Social (zubyul graph) |
| DJedamski | Social (zubyul graph) |
| wasita | Social (zubyul graph) |
| kristinezheng | Social (zubyul graph) |
| M1shaaa | Social (zubyul graph) |
| AustinCStone | Social (zubyul graph) |

### Repo Distribution by Source

```
┌───────────────┬───────┐
│  org_or_user  │ repos │
│    varchar    │ int64 │
├───────────────┼───────┤
│ plurigrid     │   100 │
│ bmorphism     │   100 │
│ zubyul        │    49 │
│ kubeflow      │    48 │
│ migalkin      │     6 │
│ wasita        │     5 │
│ AustinCStone  │     5 │
│ TeglonLabs    │     4 │
│ DJedamski     │     4 │
│ kristinezheng │     3 │
│ M1shaaa       │     3 │
└───────────────┴───────┘
  11 rows     2 columns
```

**Total repos captured: 327**

### GF(3) Color Chain Distribution

```
┌──────────┬───────────┬───────┐
│ gf3_name │ gf3_color │   n   │
│ varchar  │  varchar  │ int64 │
├──────────┼───────────┼───────┤
│ #b8bb26  │ PLUS      │   109 │
│ #cc241d  │ MINUS     │   109 │
│ #d3869b  │ ERGODIC   │   109 │
└──────────┴───────────┴───────┘
```

- **ERGODIC** (#d3869b): trit=0, id%3==0
- **PLUS** (#b8bb26): trit=1, id%3==1
- **MINUS** (#cc241d): trit=-1, id%3==2

### Top plurigrid Repos (by stars)

```
┌─────────────┬───────┬──────────────────┬──────────────────────┐
│  repo_name  │ stars │     language     │      pushed_at       │
│   varchar   │ int32 │     varchar      │       varchar        │
├─────────────┼───────┼──────────────────┼──────────────────────┤
│ asi         │    23 │ HTML             │ 2026-04-26T08:51:41Z │
│ ontology    │     8 │ JavaScript       │ 2025-05-27T18:18:34Z │
│ vcg-auction │     7 │ Rust             │ 2023-03-16T21:53:08Z │
│ agent       │     5 │ Python           │ 2023-03-31T18:45:23Z │
│ StochFlow   │     4 │ Python           │ 2024-03-20T23:34:57Z │
│ asi-skills  │     3 │ Julia            │ 2026-04-26T08:09:26Z │
│ Plurigraph  │     3 │ JavaScript       │ 2025-01-05T08:39:09Z │
│ act         │     3 │ Python           │ 2024-07-26T08:27:08Z │
│ microworlds │     3 │ Rust             │ 2023-05-13T03:54:56Z │
│ org         │     2 │ Jupyter Notebook │ 2023-11-07T01:08:05Z │
└─────────────┴───────┴──────────────────┴──────────────────────┘
  10 rows                                             4 columns
```

### Top kubeflow Repos (by stars)

```
┌────────────────┬───────┬──────────┐
│   repo_name    │ stars │ language │
│    varchar     │ int32 │ varchar  │
├────────────────┼───────┼──────────┤
│ kubeflow       │ 15686 │ NULL     │
│ pipelines      │  4150 │ Python   │
│ spark-operator │  3124 │ Python   │
│ trainer        │  2107 │ Go       │
│ katib          │  1685 │ Python   │
└────────────────┴───────┴──────────┘
```

### Top bmorphism Repos (by stars)

```
┌──────────────────────────┬───────┬────────────┐
│        repo_name         │ stars │  language  │
│         varchar          │ int32 │  varchar   │
├──────────────────────────┼───────┼────────────┤
│ ocaml-mcp-sdk            │    61 │ OCaml      │
│ anti-bullshit-mcp-server │    23 │ JavaScript │
│ risc0-cosmwasm-example   │    23 │ Rust       │
│ say-mcp-server           │    20 │ JavaScript │
│ babashka-mcp-server      │    18 │ JavaScript │
└──────────────────────────┴───────┴────────────┘
```

### Top migalkin Repos (Knowledge Graph research)

```
┌──────────────┬───────┐
│  repo_name   │ stars │
│   varchar    │ int32 │
├──────────────┼───────┤
│ NodePiece    │   144 │
│ StarE        │    89 │
│ kgcourse2021 │    25 │
│ NBFNet_mlx   │    10 │
│ RWL          │     8 │
└──────────────┴───────┘
```

### TeglonLabs Repos

```
┌──────────────────┬───────┬────────────┬─────────────────────────────────────────────────────────────────────────────────────────────────┐
│    repo_name     │ stars │  language  │                                           description                                           │
│     varchar      │ int32 │  varchar   │                                             varchar                                             │
├──────────────────┼───────┼────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ mathpix-gem      │     2 │ Ruby       │ Transform mathematical images to LaTeX chemistry structures to SMILES and documents to markdown │
│ coin-flip-mcp    │     0 │ JavaScript │ MCP server for flipping coins with varying degrees of randomness from random.org                │
│ monad-mcp-server │     0 │ NULL       │ Monad MCP Server                                                                                │
│ topoi            │     0 │ Python     │ NULL                                                                                            │
└──────────────────┴───────┴────────────┴─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### zubyul Top Repos

```
┌────────────────────────────────┬───────┬──────────────────┐
│           repo_name            │ stars │     language     │
│            varchar             │ int32 │     varchar      │
├────────────────────────────────┼───────┼──────────────────┤
│ jonikas_lab_data_analysis_misc │     2 │ Jupyter Notebook │
│ WGCNA                          │     2 │ HTML             │
│ Nikolova_lab_data_analysis     │     2 │ R                │
│ zubyul.github.io               │     1 │ CSS              │
│ cascade-world                  │     1 │ Python           │
└────────────────────────────────┴───────┴──────────────────┘
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

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

**Note:** All 28 addresses returned `resource_not_found` — accounts have not initialized `CoinStore<AptosCoin>` on-chain (no APT received yet or accounts inactive).

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

**All 5 multisig accounts healthy — 2-of-N signature threshold confirmed on each.**

### MNX Markets

```
┌─────────┬────────────────────┬──────────┬────────┐
│ ticker  │        name        │ category │ price  │
│ varchar │      varchar       │ varchar  │ double │
├─────────┼────────────────────┼──────────┼────────┤
│ UNAVAIL │ MNX-testnet.mnx.fi │ unknown  │    0.0 │
└─────────┴────────────────────┴──────────┴────────┘
```

**Status:** `testnet.mnx.fi` returns a Next.js SPA shell — no JSON market API endpoints accessible. Data marked UNAVAILABLE.

---

## DuckDB Ducklake Schema

| Table | Rows |
|-------|------|
| world_increments | 327 |
| repo_snapshots | 327 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

**Location:** `packages/world-increment/ducklake/world-increments.duckdb`
