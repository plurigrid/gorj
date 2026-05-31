# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep date:** 2026-05-31  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 21 |
| kubeflow | org | 14 |
| TeglonLabs | org | 4 |
| bmorphism | user | 16 |
| zubyul | user | 8 |
| migalkin | user (zubyul social) | 5 |
| DJedamski | user (zubyul social) | 2 |
| wasita | user (zubyul social) | 4 |
| kristinezheng | user (zubyul social) | 2 |
| M1shaaa | user (zubyul social) | 2 |
| AustinCStone | user (zubyul social) | 3 |
| **Total** | | **81** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 27 |
| 1 | `#b8bb26` | PLUS | 27 |
| -1 | `#cc241d` | MINUS | 27 |

**Perfect GF(3) balance: 27/27/27**

### Notable Repos

| Org/User | Repo | Stars | Language | Description |
|----------|------|-------|----------|-------------|
| kubeflow | kubeflow | 15,692 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow | pipelines | 4,149 | Python | ML Pipelines for Kubeflow |
| kubeflow | spark-operator | 3,124 | Python | Kubernetes operator for Apache Spark |
| kubeflow | trainer | 2,106 | Go | Distributed AI Model Training on Kubernetes |
| kubeflow | katib | 1,685 | Python | Automated ML on Kubernetes |
| migalkin | NodePiece | 144 | Python | Parameter-Efficient KG Representations (ICLR22) |
| migalkin | StarE | 89 | Python | Message Passing for Hyper-Relational KGs |
| AustinCStone | TextGAN | 92 | Python | GAN for text generation in TensorFlow |
| bmorphism | ocaml-mcp-sdk | 61 | OCaml | OCaml SDK for Model Context Protocol |
| bmorphism | risc0-cosmwasm-example | 23 | Rust | CosmWasm + zkVM RISC-V EFI template |
| plurigrid | asi | 23 | HTML | everything is topological chemputer! |
| plurigrid | gorj | 0 | Clojure | forj + Rama topology + GF(3) trit coloring (269 open issues) |

### Hot Activity (recently pushed)

- **plurigrid/gorj** — pushed 2026-05-31 (269 open issues — most active)
- **bmorphism/Gay.jl** — pushed 2026-05-31 (189 open issues — core color lib)
- **wasita/wasita.github.io** — pushed 2026-05-20
- **M1shaaa/M1shaaa** — pushed 2026-05-30

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 addresses (alice, bob, A–Z) via Aptos fullnode mainnet API.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26) | various | 0.0 each |

**Total APT across 28 worlds: 0.0 APT**  
All accounts returned 0.0 — no APT CoinStore resource initialized on mainnet.

### Multisig Contract Probes

Probed `0x1::multisig_account::num_signatures_required` on 5 contracts:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy. All require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

The site is a Next.js SPA. The `/api/markets` and `/api/v1/markets` endpoints return HTML (SPA shell), not JSON. No market data extractable via HTTP without browser JS execution. **Status: unavailable.**

---

## DuckDB Schema

| Table | Rows | Notes |
|-------|------|-------|
| world_increments | 81 | GF(3)-colored event log |
| repo_snapshots | 81 | GitHub repo state at sweep time |
| aptos_snapshots | 28 | Aptos wallet balances |
| multisig_probes | 5 | Multisig health checks |
| mnx_snapshots | 0 | MNX market data (SPA — unavailable) |
