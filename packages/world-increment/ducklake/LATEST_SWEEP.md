# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-02  
**Aptos Ledger Version:** 6055149143 (epoch 16386, block 870884067)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| TeglonLabs | org | 5 |
| migalkin | social | 5 |
| wasita | social | 5 |
| AustinCStone | social | 4 |
| M1shaaa | social | 3 |
| DJedamski | social | 3 |
| kristinezheng | social | 2 |

**Total unique repos:** 324

### DuckDB Ducklake: `world-increments.duckdb`

Tables:
- `world_increments` — 324 rows, GF(3) color-coded
- `repo_snapshots` — 324 rows with full metadata
- `aptos_snapshots` — 28 rows
- `multisig_probes` — 5 rows
- `mnx_snapshots` — 0 rows (service unavailable)

### GF(3) Color Chain Distribution
| GF3 Name | Color | Count |
|----------|-------|-------|
| ERGODIC (trit=0) | #d3869b | 108 |
| PLUS (trit=1) | #b8bb26 | 108 |
| MINUS (trit=-1) | #cc241d | 108 |

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15756 | — |
| kubeflow/pipelines | 4166 | Python |
| kubeflow/spark-operator | 3130 | Python |
| kubeflow/trainer | 2128 | Go |
| kubeflow/katib | 1688 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| migalkin/NodePiece | 144 | Python |
| migalkin/kgcourse2021 | 25 | HTML |
| AustinCStone/StereoVisionMRF | 11 | Python |

### Notable Recent Activity
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"
- **wasita/wasita.github.io** (Svelte, pushed 2026-07-02): most recently pushed repo in sweep
- **kristinezheng/kristinezheng.github.io** (HTML, pushed 2026-07-01)
- **migalkin/RWL** (Python, pushed 2026-05-28): "Weisfeiler and Leman Go Relational (LOG 2022)"

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (2026-07-02)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version 6055149143.

This indicates **no APT CoinStore initialized** on these addresses. The Aptos mainnet node was fully reachable (HTTP 200, chain-id=1).

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts returned `num_signatures_required = 2` — all **healthy**.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — HTTP 401, Vercel authentication required. No market data extractable.

---

## Summary

- **GitHub sweep:** 324 unique repos across 11 sources snapshotted into DuckDB with GF(3) color chain (ERGODIC/PLUS/MINUS, 108 each)
- **Aptos swarm:** 28/28 wallet addresses have zero APT balance (CoinStore not initialized on mainnet)
- **Multisig health:** 5/5 contracts healthy, all 2-of-N
- **MNX markets:** Unavailable (Vercel auth-gated testnet)
