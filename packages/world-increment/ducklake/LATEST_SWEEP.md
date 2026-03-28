# World-Increment Sweep + Hamming Snapshot — 2026-03-28

## Sweep Metadata
- **Date:** 2026-03-28
- **Agent:** world-increment-sweep v2 (full social graph + Aptos hamming swarm)
- **DuckDB:** packages/world-increment/ducklake/world-increments.duckdb

---

## Summary Counts

| Table             | Rows |
|-------------------|------|
| world_increments  | 376  |
| repo_snapshots    | 364  |
| aptos_snapshots   | 28   |
| multisig_probes   | 5    |
| mnx_snapshots     | 1    |

---

## GitHub Repos Found Per Org/User

| Org / User     | Repos | API Total |
|----------------|-------|-----------|
| plurigrid      | 87    | 87        |
| kubeflow       | 46    | 46        |
| bmorphism      | 96    | 96        |
| zubyul         | 44    | 44        |
| TeglonLabs     | 3     | 3         |
| migalkin       | 19    | 19        |
| DJedamski      | 6     | 6         |
| wasita         | 9     | 9         |
| kristinezheng  | 6     | 6         |
| M1shaaa        | 8     | 8         |
| AustinCStone   | 40    | 40        |
| **TOTAL**      | **364** |         |

### Notable Repos by Stars
- kubeflow/kubeflow: 15,538 stars — Machine Learning Toolkit for Kubernetes
- kubeflow/pipelines: 4,113 stars — ML Pipelines for Kubeflow
- kubeflow/spark-operator: 3,110 stars — Kubernetes Spark operator
- kubeflow/trainer: 2,068 stars — Distributed AI Model Training
- kubeflow/katib: 1,672 stars — Automated ML on Kubernetes
- migalkin/NodePiece: 143 stars — Compositional KG representations (ICLR'22)
- AustinCStone/TextGAN: 92 stars — TensorFlow text GAN
- migalkin/StarE: 88 stars — Hyper-relational KG message passing (EMNLP 2020)
- bmorphism/ocaml-mcp-sdk: 60 stars — OCaml SDK for MCP using oxcaml_effect
- plurigrid/asi: 13 stars — everything is topological chemputer!

---

## Aptos Wallet Balances (Hamming Swarm — alice/bob + A-Z)

All 28 addresses probed via Aptos mainnet fullnode API.
All CoinStore resources returned 0 APT (accounts exist on-chain, no APT held in standard CoinStore).

| World | Address (truncated)                    | Balance APT |
|-------|----------------------------------------|-------------|
| alice | 0xc793...c7b                           | 0.0         |
| bob   | 0x0a3c...d5d                           | 0.0         |
| A     | 0x8699...a7a                           | 0.0         |
| B     | 0x3f89...b13                           | 0.0         |
| C     | 0x38b9...35e                           | 0.0         |
| D     | 0xf776...dd1                           | 0.0         |
| E     | 0xdc1d...d36                           | 0.0         |
| F     | 0x18a1...f71                           | 0.0         |
| G     | 0x69a3...f32                           | 0.0         |
| H     | 0xce67...00f                           | 0.0         |
| I     | 0x070f...fc9                           | 0.0         |
| J     | 0x4d96...f54                           | 0.0         |
| K     | 0xa732...dc4                           | 0.0         |
| L     | 0x7c2e...ba9                           | 0.0         |
| M     | 0x6fed...2e9                           | 0.0         |
| N     | 0xe7dd...b2c                           | 0.0         |
| O     | 0x7325...89d                           | 0.0         |
| P     | 0x6218...948                           | 0.0         |
| Q     | 0xac40...a9                            | 0.0         |
| R     | 0x7ce6...e10                           | 0.0         |
| S     | 0xb875...386                           | 0.0         |
| T     | 0x3578...588                           | 0.0         |
| U     | 0x7586...956                           | 0.0         |
| V     | 0xb59d...2c3                           | 0.0         |
| W     | 0x5f32...7b0                           | 0.0         |
| X     | 0xa95c...47d                           | 0.0         |
| Y     | 0xd8e3...4c4                           | 0.0         |
| Z     | 0x7af0...97c                           | 0.0         |

---

## Multisig Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required` (POST /v1/view).
All returned **2 signatures required** and are healthy.

| Pair | Multisig Address                                                   | Sigs Required | Healthy |
|------|--------------------------------------------------------------------|---------------|---------|
| A-B  | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2             | true    |
| A-G  | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2             | true    |
| Y-Z  | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2             | true    |
| S-T  | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2             | true    |
| V-W  | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2             | true    |

---

## MNX Market Status

`https://testnet.mnx.fi/api/markets` — **No JSON API available**

The endpoint returns a Next.js HTML frontend application (HTTP 200 with HTML document).
No structured market data accessible via REST/JSON. Stored as null marker in mnx_snapshots.

---

## GF(3) Color Chain Summary

Each world_increment is assigned a GF(3) trit based on `id % 3`:

| Trit | Color   | Name    | Hex     | Count |
|------|---------|---------|---------|-------|
| 0    | ERGODIC | pink    | #d3869b | 125   |
| 1    | PLUS    | green   | #b8bb26 | 126   |
| -1   | MINUS   | red     | #cc241d | 125   |

**Total:** 376 increments across 364 repos from 11 orgs/users.

GF(3) assignment: `id%3==0 → ERGODIC (#d3869b), id%3==1 → PLUS (#b8bb26), id%3==2 → MINUS (#cc241d)`

The balanced ternary distribution (125/126/125) across the social graph snapshot demonstrates
near-perfect ergodic balance — the GF(3) color chain tiles uniformly across the repo universe.

---

## Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)

multisig_probes(timestamp, pair, address, sigs_required, healthy)

mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```
