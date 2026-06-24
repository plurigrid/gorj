# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-24  
**DuckDB:** `world-increments.duckdb`  
**GF(3) Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Source Type | Source | Repos |
|-------------|--------|-------|
| org | plurigrid | 100 |
| org | kubeflow | 48 |
| org | TeglonLabs | 5 |
| user | bmorphism | 100 |
| user | zubyul | 49 |
| social | migalkin | 19 |
| social | AustinCStone | 30 |
| social | wasita | 11 |
| social | DJedamski | 6 |
| social | M1shaaa | 8 |
| social | kristinezheng | 5 |
| **TOTAL** | | **381** |

### GF(3) World Increment Distribution

| Name | Trit | Color | Count |
|------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 127 |
| PLUS | +1 | `#b8bb26` | 127 |
| MINUS | -1 | `#cc241d` | 127 |

*381 = 127 × 3 — perfectly balanced trit chain*

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,741 | — |
| kubeflow/pipelines | 4,157 | Python |
| kubeflow/spark-operator | 3,128 | Python |
| kubeflow/trainer | 2,119 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| kubeflow/community-distribution | 1,028 | YAML |
| kubeflow/arena | 813 | Go |
| kubeflow/kale | 694 | Python |
| kubeflow/mpi-operator | 528 | Go |

### Most Recently Pushed

| Repo | Pushed At |
|------|-----------|
| kubeflow/mcp-apache-spark-history-server | 2026-06-23T23:14:00Z |
| plurigrid/gorj | 2026-06-23T23:11:38Z |
| kubeflow/pipelines-components | 2026-06-23T19:17:11Z |
| kubeflow/spark-operator | 2026-06-23T18:27:52Z |
| kubeflow/notebooks | 2026-06-23T18:13:30Z |

### Most Open Issues

| Repo | Open Issues |
|------|-------------|
| plurigrid/gorj | 776 |
| kubeflow/pipelines | 453 |
| bmorphism/Gay.jl | 187 |
| kubeflow/notebooks | 179 |
| kubeflow/docs-agent | 153 |

### Notable Observations

- **plurigrid/gorj** (this repo) has 776 open issues — highest in the plurigrid org
- **bmorphism** is prolific in MCP servers: say-mcp-server (20★), babashka-mcp-server (19★), manifold-mcp-server (14★), anti-bullshit-mcp-server (23★), ocaml-mcp-sdk (61★)
- **Gay.jl** ecosystem spans plurigrid, bmorphism, zubyul — GF(3) trit coloring is a shared theme
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08) is the most recently active TeglonLabs repo

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets (alice, bob, A–Z) queried via Aptos fullnode mainnet API.

**Result: All wallets returned 0 APT** — CoinStore<AptosCoin> resource not found on any address. These are either uninitialized accounts or the coin store has migrated to the fungible_asset module.

| Wallets Probed | Total APT |
|----------------|-----------|
| 28 | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | YES |
| A-G | 0xf56c4a1c... | 2 | YES |
| Y-Z | 0xd3ffe181... | 2 | YES |
| S-T | 0x3b1c3ae9... | 2 | YES |
| V-W | 0x40fad7b4... | 2 | YES |

**All 5 multisig contracts healthy — 2-of-N threshold across all pairs.**

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — Vercel deployment protection active (HTTP 401). All API paths (/api/markets, /api/v1/markets, /api/tickers) return authentication challenge. Access requires Vercel bypass token or trusted source OIDC configuration.

---

## Database Schema

```
world_increments  : 381 rows  (GF3-colored world event log)
repo_snapshots    : 381 rows  (GitHub repo metadata)
aptos_snapshots   :  28 rows  (Hamming swarm wallet balances)
multisig_probes   :   5 rows  (multisig contract health)
mnx_snapshots     :   1 rows  (market data — unavailable)
```
