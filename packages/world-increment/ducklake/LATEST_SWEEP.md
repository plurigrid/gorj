# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-13T00:00Z  
**Branch:** world-increment/sweep  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Captured

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul social) | 19 |
| DJedamski | user (zubyul social) | 6 |
| wasita | user (zubyul social) | 11 |
| kristinezheng | user (zubyul social) | 6 |
| M1shaaa | user (zubyul social) | 8 |
| AustinCStone | user (zubyul social) | 40 |
| **TOTAL** | | **391** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,630 | -- | 2026-05-07 |
| kubeflow/pipelines | 4,140 | Python | 2026-05-12 |
| kubeflow/spark-operator | 3,125 | Python | 2026-05-12 |
| kubeflow/trainer | 2,098 | Go | 2026-05-13 |
| kubeflow/katib | 1,682 | Python | 2026-05-09 |
| kubeflow/manifests | 1,017 | YAML | 2026-05-13 |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Increments |
|------|-------|------|-----------|
| 0 | #d3869b | ERGODIC | 137 |
| +1 | #b8bb26 | PLUS | 139 |
| -1 | #cc241d | MINUS | 138 |

Total world_increments: **414** (391 repo events + GF3 chain links)

### Notable Findings

- **plurigrid**: 100 repos - Clojure, TypeScript, Python; active ML/AI infra org
- **bmorphism**: 100 repos; extensive personal research spanning math, ML, distributed systems
- **kubeflow**: 48 repos; flagship ML platform (kubeflow/kubeflow: 15.6k stars)
- **TeglonLabs**: 4 repos - mathpix-gem (Ruby, math OCR), coin-flip-mcp (JS, MCP), topoi (Python), monad-mcp-server
- **AustinCStone**: 40 repos, heavy ML/CV focus
- **M1shaaa**: Profile README pushed today 2026-05-13 (live activity)
- **zubyul social graph**: 6 connected users captured (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses (alice, bob, A-Z) queried against Aptos mainnet fullnode.

**Result:** All addresses return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version 5,257,900,402. These are unfunded accounts with no APT CoinStore initialized. Balance recorded as **0.0 APT** for all 28 wallets.

| Wallet | Address | APT Balance |
|--------|---------|-------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 |
| A | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a | 0.0 |
| B | 0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13 | 0.0 |
| C | 0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e | 0.0 |
| D | 0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1 | 0.0 |
| E | 0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36 | 0.0 |
| F | 0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71 | 0.0 |
| G | 0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32 | 0.0 |
| H | 0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f | 0.0 |
| I | 0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9 | 0.0 |
| J | 0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54 | 0.0 |
| K | 0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4 | 0.0 |
| L | 0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9 | 0.0 |
| M | 0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9 | 0.0 |
| N | 0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c | 0.0 |
| O | 0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d | 0.0 |
| P | 0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948 | 0.0 |
| Q | 0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9 | 0.0 |
| R | 0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10 | 0.0 |
| S | 0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386 | 0.0 |
| T | 0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588 | 0.0 |
| U | 0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956 | 0.0 |
| V | 0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3 | 0.0 |
| W | 0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0 | 0.0 |
| X | 0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d | 0.0 |
| Y | 0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4 | 0.0 |
| Z | 0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | HEALTHY |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | HEALTHY |

**All 5 multisig contracts are live on Aptos mainnet with threshold 2-of-N.**

### MNX Markets

`https://testnet.mnx.fi` is a Next.js SPA. No REST API found at `/api/markets` or `/api/v1/markets` - both endpoints return the rendered HTML shell. Market data **unavailable** via direct API probe (client-side rendered).

---

## DuckDB Schema Summary

```
world-increments.duckdb
  world_increments  414 rows  -- GF(3) event ledger
  repo_snapshots    643 distinct repos  -- GitHub snapshots
  aptos_snapshots    28 rows  -- Hamming swarm wallet balances (all 0.0 APT)
  multisig_probes     5 rows  -- all 2-of-N healthy
  mnx_snapshots       0 rows  -- SPA, API unavailable
```

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent*  
*Aptos mainnet ledger version: 5,257,900,402*  
*Sweep date: 2026-05-13*
