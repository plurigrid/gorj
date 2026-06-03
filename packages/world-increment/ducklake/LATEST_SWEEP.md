# World Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-06-03T22:30:00Z  
**Branch:** world-increment/sweep  
**GF(3) Color Chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| kubeflow | org | 10 (top by stars) | 30,002 |
| migalkin | user | 3 (top) | 258 |
| bmorphism | user | 11 (top) | 191 |
| AustinCStone | user (social) | 1 | 92 |
| plurigrid | org | 15 (top) | 59 |
| wasita | user (social) | 2 | 3 |
| zubyul | user | 5 | 2 |
| TeglonLabs | org | 4 | 2 |
| DJedamski | user (social) | 1 | 0 |
| M1shaaa | user (social) | 1 | 0 |
| kristinezheng | user (social) | 1 | 0 |

**Total: 54 repo snapshots stored in DuckDB**

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,705 | — | 2026-05-24 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-03 |
| kubeflow/spark-operator | 3,125 | Python | 2026-06-03 |
| kubeflow/trainer | 2,110 | Go | 2026-06-03 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 24 | HTML | 2026-04-26 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 |

### Most Active (Pushed 2026-06-03)

- **kubeflow/pipelines** – ML Pipelines, Python
- **kubeflow/spark-operator** – Kubernetes Spark operator
- **kubeflow/trainer** – Distributed AI training
- **plurigrid/gorj** – forj + Rama + GF(3) gay trit coloring (334 open issues!)
- **plurigrid/eirobri** – EiRoBri replay world (29 open issues)
- **bmorphism/Gay.jl** – Wide-gamut color sampling, Julia (189 open issues)

### GF(3) Distribution

| Name | Color | Trit | Count |
|------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 18 |
| PLUS | #b8bb26 | +1 | 18 |
| MINUS | #cc241d | -1 | 18 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried 28 addresses (alice, bob, A-Z) on fullnode.mainnet.aptoslabs.com.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | (all 26 addresses) | 0.0 each |

All 28 addresses returned 0.0 APT — unfunded addresses on Aptos mainnet (CoinStore resource absent or zero balance).

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Contract Address (truncated) | Sigs Required | Healthy |
|------|------------------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

All 5 multisig accounts require 2-of-N signatures and are healthy.

### MNX Markets (testnet.mnx.fi)

The site is a Next.js SPA titled "The AI Exchange". Direct REST calls to /api/markets return 404. CSP headers reveal backend at api.testnet.mnx.fi. Market data unavailable via curl (client-side rendering required).

---

## DuckDB Schema

```
packages/world-increment/ducklake/world-increments.duckdb
world_increments    (54 rows) — GF(3) colored increment log
repo_snapshots      (54 rows) — GitHub repo metadata
aptos_snapshots     (28 rows) — Hamming swarm wallet balances
multisig_probes      (5 rows) — Multisig health checks
mnx_snapshots        (0 rows) — MNX market data (SPA, unavailable)
```
