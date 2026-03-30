# LATEST_SWEEP.md

**Sweep Timestamp:** 2026-03-30T19:30:00Z (UTC)

---

## GitHub Social Graph Sweep

### Repos Found by Org/User

| Org/User       | Repos Captured | Notes                        |
|----------------|---------------|------------------------------|
| plurigrid      | 16            | 93 total public (top 16 by stars) |
| kubeflow       | 14            | 46 total public (top 14 by stars) |
| TeglonLabs     | 3             | 3 total public               |
| bmorphism      | 14            | 97 total public (top 14 by stars) |
| zubyul         | 5             | 44 total (mix public/private)|
| migalkin       | 5             | 19 total public              |
| DJedamski      | 3             | 6 total public               |
| wasita         | 2             | 9 total public               |
| kristinezheng  | 2             | 6 total public               |
| M1shaaa        | 2             | 8 total public               |
| AustinCStone   | 3             | 40 total public              |
| **TOTAL**      | **68**        |                              |

### Top Repos by Stars

| Repo                         | Stars  | Language   |
|------------------------------|--------|------------|
| kubeflow/kubeflow             | 15,545 | -          |
| kubeflow/pipelines            | 4,114  | Python     |
| kubeflow/spark-operator       | 3,110  | Python     |
| kubeflow/trainer              | 2,069  | Go         |
| kubeflow/katib                | 1,673  | Python     |
| kubeflow/examples             | 1,459  | Jsonnet    |
| kubeflow/manifests            | 1,006  | YAML       |
| kubeflow/arena                | 810    | Go         |
| kubeflow/kale                 | 681    | Python     |
| AustinCStone/TextGAN          | 92     | Python     |
| bmorphism/ocaml-mcp-sdk       | 60     | OCaml      |
| migalkin/NodePiece            | 143    | Python     |
| migalkin/StarE                | 88     | Python     |
| plurigrid/asi                 | 13     | HTML       |

---

## GF(3) Color Chain Summary

IDs are assigned sequentially per repo snapshot. The color chain cycles:

| id % 3 | Trit | Color   | Name    | Count |
|--------|------|---------|---------|-------|
| 0      | 0    | #d3869b | ERGODIC | 23    |
| 1      | +1   | #b8bb26 | PLUS    | 23    |
| 2      | -1   | #cc241d | MINUS   | 22    |

Total world_increment events: **68**

---

## Aptos Wallet Balances (Hamming Swarm Snapshot)

All 28 addresses queried against Aptos mainnet fullnode. All returned 0.0 APT (accounts either unfunded or not initialized on mainnet).

| World | Address (truncated)       | Balance (APT) |
|-------|--------------------------|---------------|
| alice | 0xc793...cc7b             | 0.0           |
| bob   | 0x0a3c...512d             | 0.0           |
| A     | 0x8699...9d7a             | 0.0           |
| B     | 0x3f89...b13              | 0.0           |
| C     | 0x38b9...35e              | 0.0           |
| D     | 0xf776...fdd1             | 0.0           |
| E     | 0xdc1d...d36              | 0.0           |
| F     | 0x18a1...cf71             | 0.0           |
| G     | 0x69a3...f32              | 0.0           |
| H     | 0xce67...300f             | 0.0           |
| I     | 0x070f...1fc9             | 0.0           |
| J     | 0x4d96...f54              | 0.0           |
| K     | 0xa732...dc4              | 0.0           |
| L     | 0x7c2e...ba9              | 0.0           |
| M     | 0x6fed...2e9              | 0.0           |
| N     | 0xe7dd...b2c              | 0.0           |
| O     | 0x7325...89d              | 0.0           |
| P     | 0x6218...948              | 0.0           |
| Q     | 0xac40...89a9             | 0.0           |
| R     | 0x7ce6...e10              | 0.0           |
| S     | 0xb875...386              | 0.0           |
| T     | 0x3578...588              | 0.0           |
| U     | 0x7586...956              | 0.0           |
| V     | 0xb59d...2c3              | 0.0           |
| W     | 0x5f32...b0               | 0.0           |
| X     | 0xa95c...47d              | 0.0           |
| Y     | 0xd8e3...4c4              | 0.0           |
| Z     | 0x7af0...97c              | 0.0           |

---

## Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`. All healthy.

| Pair | Address (truncated)  | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4...003        | 2             | true    |
| A-G  | 0xf56c...096        | 2             | true    |
| Y-Z  | 0xd3ff...883        | 2             | true    |
| S-T  | 0x3b1c...883        | 2             | true    |
| V-W  | 0x40fa...eb6d       | 2             | true    |

---

## MNX Market Status

- `https://testnet.mnx.fi/api/markets` - Returns HTML (SPA, no REST API at this path)
- `https://testnet.mnx.fi/api/v1/markets` - Returns HTML (SPA, no REST API at this path)
- `https://testnet.mnx.fi` - Returns HTML (Next.js app, dark mode, no JSON market data accessible via curl)

**Status: MNX API unavailable via direct curl (client-side rendered SPA). No market data captured. mnx_snapshots table has 0 rows.**

---

## DuckDB Table Row Counts

| Table             | Rows |
|-------------------|------|
| world_increments  | 68   |
| repo_snapshots    | 68   |
| aptos_snapshots   | 28   |
| multisig_probes   | 5    |
| mnx_snapshots     | 0    |

Database location: `packages/world-increment/ducklake/world-increments.duckdb`
