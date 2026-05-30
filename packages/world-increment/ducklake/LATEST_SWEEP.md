# World-Increment Sweep + Hamming Snapshot

**Sweep timestamp:** 2026-05-30  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 20 |
| TeglonLabs | org | 4 |
| kubeflow | org | 13 |
| bmorphism | user | 10 |
| zubyul | user | 10 |
| migalkin | social | 5 |
| wasita | social | 4 |
| AustinCStone | social | 3 |
| DJedamski | social | 2 |
| kristinezheng | social | 2 |
| M1shaaa | social | 2 |
| **Total** | | **75 repos** |

### Top Repos by Stars

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,687 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,150 | Python | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,124 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,107 | Go | Distributed AI Model Training on Kubernetes |
| kubeflow/katib | 1,685 | Python | Automated Machine Learning on Kubernetes |
| migalkin/NodePiece | 144 | Python | Compositional KG representations (ICLR 2022) |
| AustinCStone/TextGAN | 92 | Python | Generative adversarial network for text |
| migalkin/StarE | 89 | Python | EMNLP 2020: Hyper-Relational KGs |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | OCaml SDK for Model Context Protocol |
| plurigrid/asi | 23 | HTML | everything is topological chemputer! |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | MCP server for analyzing claims |

### Most Active Repos (Recent pushes)

| Repo | Pushed At |
|------|-----------|
| bmorphism/Gay.jl | 2026-05-30T00:37:13Z |
| plurigrid/gorj | 2026-05-29T23:38:06Z |
| kubeflow/pipelines | 2026-05-29T21:32:20Z |
| kubeflow/katib | 2026-05-29T21:30:47Z |
| kubeflow/hub | 2026-05-29T21:13:12Z |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 25 |
| +1 | `#b8bb26` | PLUS | 26 |
| -1 | `#cc241d` | MINUS | 26 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

**Result:** All 28 addresses returned HTTP 404 — no `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource found. These wallets exist on-chain but have no APT coin store registered.

| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|---------------|--------|
| alice | 0xc793...cc7b | 0.0 | 404 no CoinStore |
| bob | 0x0a3c...2d5d | 0.0 | 404 no CoinStore |
| A–Z | (26 addresses) | 0.0 each | 404 no CoinStore |

### Multisig Contract Probes (5 contracts)

**All 5 contracts healthy — 2-of-N signatures required.**

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — All probed API paths returned HTTP 404:
- `/api/markets` → 404
- `/api/v1/markets` → 404
- `/api/tickers` → 404
- `/api/v1/tickers` → 404

---

## DuckDB Schema Summary

```
world_increments   77 rows   (GitHub repo sweep, GF3-colored)
repo_snapshots     77 rows   (repo metadata: lang, stars, forks, issues)
aptos_snapshots    28 rows   (28 wallets, all 404 no CoinStore)
multisig_probes     5 rows   (5 contracts, all healthy 2-of-N)
mnx_snapshots       1 rows   (placeholder: API unavailable)
```

## Notes

- Aptos mainnet fullnode responded correctly but all wallet addresses lack a registered `CoinStore<AptosCoin>` resource (uninitialized or non-APT wallets).
- All 5 multisig contracts are live on Aptos mainnet, returning `sigs_required = 2`.
- MNX testnet API is not publicly accessible via standard REST paths.
- GF(3) color chain balanced: ERGODIC (#d3869b) / PLUS (#b8bb26) / MINUS (#cc241d) across 77 world increments.
