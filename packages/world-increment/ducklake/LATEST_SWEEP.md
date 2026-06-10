# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-10 00:18:29 UTC

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain

| id | trit | color | name | source_type | source |
|----|------|-------|------|-------------|--------|
| 1 | +1 | `#b8bb26` PLUS | PLUS | org | plurigrid |
| 2 | -1 | `#cc241d` MINUS | MINUS | org | kubeflow |
| 3 | 0 | `#d3869b` ERGODIC | ERGODIC | org | TeglonLabs |
| 4 | +1 | `#b8bb26` PLUS | PLUS | user | bmorphism |
| 5 | -1 | `#cc241d` MINUS | MINUS | user | zubyul |
| 6 | 0 | `#d3869b` ERGODIC | ERGODIC | user | migalkin |
| 7 | +1 | `#b8bb26` PLUS | PLUS | user | DJedamski |
| 8 | -1 | `#cc241d` MINUS | MINUS | user | wasita |
| 9 | 0 | `#d3869b` ERGODIC | ERGODIC | user | kristinezheng |
| 10 | +1 | `#b8bb26` PLUS | PLUS | user | M1shaaa |
| 11 | -1 | `#cc241d` MINUS | MINUS | user | AustinCStone |

### Repo Snapshots (DuckDB: `repo_snapshots`)

| source | repos snapshotted |
|--------|------------------|
| plurigrid | 50 |
| bmorphism | 50 |
| zubyul | 49 |
| kubeflow | 48 |
| TeglonLabs | 5 |
| migalkin | 4 |
| wasita | 3 |
| AustinCStone | 3 |
| M1shaaa | 2 |
| DJedamski | 2 |
| kristinezheng | 1 |
| **TOTAL** | **217** |

#### Top repos by stars (sampled)

- **kubeflow/kubeflow** — 15,713 ⭐ — Machine Learning Toolkit for Kubernetes
- **kubeflow/pipelines** — 4,153 ⭐ — Machine Learning Pipelines for Kubeflow
- **kubeflow/spark-operator** — 3,126 ⭐ — Kubernetes operator for Apache Spark
- **kubeflow/trainer** — 2,112 ⭐ — Distributed AI Training on Kubernetes
- **AustinCStone/TextGAN** — 92 ⭐ — GAN for text generation in TensorFlow
- **migalkin/NodePiece** — 144 ⭐ — Compositional KG Representations (ICLR'22)
- **migalkin/StarE** — 89 ⭐ — Hyper-Relational Knowledge Graphs (EMNLP'20)
- **bmorphism/ocaml-mcp-sdk** — 61 ⭐ — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **bmorphism/say-mcp-server** — 20 ⭐ — macOS text-to-speech MCP server
- **plurigrid/asi** — 25 ⭐ — everything is topological chemputer!
- **plurigrid/gorj** — 465 open issues — forj + Rama topology nREPL routing + GF(3)

#### Recently active (plurigrid, last 30d as of sweep)

- `plurigrid/place` — TeX — pushed 2026-06-04
- `plurigrid/eirobri` — Clojure — EiRoBri replay world — pushed 2026-06-03
- `plurigrid/gorj` — Clojure — pushed 2026-06-09 (most recent)

#### TeglonLabs snapshot

- `jank-crane` (C++) — crane-jank converged-IR hub, GF3 convergence maps — 2026-06-08
- `mathpix-gem` (Ruby) — LaTeX/SMILES OCR gem — 2⭐
- `coin-flip-mcp` (JavaScript) — MCP server for coin flipping — 2 forks
- `monad-mcp-server` — Monad MCP Server
- `topoi` (Python) — topological structures

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (DuckDB: `aptos_snapshots`)

All 28 wallets (alice, bob, A–Z) queried on Aptos mainnet.
Endpoint: `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result:** All 28 addresses returned 0.0 APT — CoinStore resource not found (unfunded or resource not initialized).

| world | address (truncated) | balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A–Z (26 addrs) | various | 0.0 each |

### Multisig Contract Probes (DuckDB: `multisig_probes`)

POST `/v1/view` → `0x1::multisig_account::num_signatures_required`

| pair | address (truncated) | sigs_required | healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

All 5 multisig contracts are **live, 2-of-2 signature threshold, healthy**.

### MNX Markets (DuckDB: `mnx_snapshots`)

**Status: UNAVAILABLE** — `https://testnet.mnx.fi` returns Vercel authentication wall (HTTP 200 with auth redirect). All API paths (`/api/markets`, `/api/v1/markets`) behind auth. No market data extractable.

---

## DuckDB Tables

```
packages/world-increment/ducklake/world-increments.duckdb
├── world_increments    (11 rows) — GF(3) color-chained increment log
├── repo_snapshots     (217 rows) — GitHub repos snapshot
├── aptos_snapshots     (28 rows) — Hamming swarm wallet balances
├── multisig_probes      (5 rows) — Multisig contract health probes
└── mnx_snapshots        (0 rows) — MNX markets (unavailable)
```
