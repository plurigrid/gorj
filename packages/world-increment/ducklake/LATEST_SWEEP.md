# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-10  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| kubeflow | org | 12 | 29,795 | 2026-06-09 |
| migalkin | user (social) | 6 | 279 | 2026-05-28 |
| bmorphism | user | 22 | 132 | 2026-06-10 |
| AustinCStone | user (social) | 8 | 107 | 2026-04-01 |
| plurigrid | org | 22 | 54 | 2026-06-10 |
| zubyul | user | 12 | 6 | 2026-04-24 |
| wasita | user (social) | 6 | 5 | 2026-06-01 |
| DJedamski | user (social) | 5 | 3 | 2023-04-21 |
| TeglonLabs | org | 5 | 2 | 2026-06-08 |
| kristinezheng | user (social) | 5 | 0 | 2026-06-07 |
| M1shaaa | user (social) | 5 | 0 | 2026-02-04 |

**Total:** 108 repos across 11 sources (3 orgs + 8 users)

### Notable Repos

- **kubeflow/kubeflow** — 15,713 stars — Machine Learning Toolkit for Kubernetes
- **kubeflow/pipelines** — 4,153 stars — ML Pipelines for Kubeflow
- **kubeflow/spark-operator** — 3,126 stars — Kubernetes Spark lifecycle operator
- **kubeflow/trainer** — 2,112 stars — Distributed AI training + LLM fine-tuning
- **migalkin/NodePiece** — 144 stars — Compositional KG representations (ICLR 2022)
- **AustinCStone/TextGAN** — 92 stars — TensorFlow GAN for text generation
- **bmorphism/ocaml-mcp-sdk** — 61 stars — OCaml SDK for Model Context Protocol
- **plurigrid/gorj** — 466 open issues — Clojure GF(3) REPL orchestration (this repo)
- **bmorphism/Gay.jl** — 189 open issues — Wide-gamut color sampling (active dev)

### GF(3) Color Chain (108 world-increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 36 |
| 1 | `#b8bb26` | PLUS | 36 |
| -1 | `#cc241d` | MINUS | 36 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses, alice + bob + A-Z)

Queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**All 28 wallets: 0.00000000 APT** (accounts exist on-chain but hold zero balance)

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 |
| A–Z | (see DB) | 0.0 each |

### Multisig Contract Probes (5 pairs)

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | healthy |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | healthy |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | healthy |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | healthy |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | healthy |

**All 5 multisig contracts: 2-of-2 signatures required, all healthy.**

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — site protected by Vercel deployment authentication (HTTP 401). No market data extractable without bypass token.

---

## DuckDB Tables

| Table | Rows | Notes |
|-------|------|-------|
| `world_increments` | 108 | GF(3) color chain, id 1-108 |
| `repo_snapshots` | 108 | stars, forks, open_issues, pushed_at |
| `aptos_snapshots` | 28 | alice, bob, A-Z; all 0 APT |
| `multisig_probes` | 5 | all 2-of-2, all healthy |
| `mnx_snapshots` | 0 | Vercel auth protected |
