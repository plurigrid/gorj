# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-06-05  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Covered

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 25 |
| kubeflow | org | 18 |
| TeglonLabs | org | 4 |
| bmorphism | user | 23 |
| zubyul | user | 15 |
| migalkin | social graph | 5 |
| DJedamski | social graph | 3 |
| wasita | social graph | 4 |
| kristinezheng | social graph | 3 |
| M1shaaa | social graph | 3 |
| AustinCStone | social graph | 3 |
| **Total** | | **106** |

### Top Repositories by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,706 | — |
| kubeflow/pipelines | 4,152 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,111 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,020 | YAML |
| kubeflow/arena | 811 | Go |
| kubeflow/kale | 691 | Python |
| kubeflow/mpi-operator | 528 | Go |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/say-mcp-server | 20 | JavaScript |
| bmorphism/babashka-mcp-server | 19 | JavaScript |

### Notable Recent Activity (2026)

- **bmorphism/Gay.jl** — pushed 2026-06-05, 189 open issues, Julia wide-gamut color sampling
- **kubeflow/katib** — pushed 2026-06-05, AutoML on Kubernetes
- **kubeflow/pipelines** — pushed 2026-06-05, 490 open issues
- **kubeflow/community** — pushed 2026-06-05
- **zubyul/plurigrid-site** — pushed 2026-03-26, 11 open issues
- **plurigrid/nanoclj-zig** — pushed 2026-04-25, 20 open issues, NaN-boxed Clojure in Zig
- **plurigrid/zig-syrup** — pushed 2026-04-30, OCapN Syrup in Zig
- **plurigrid/asi-skills** — pushed 2026-04-26, 69 skills with Galois Hole Types

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b (rose) | 35 |
| 1 | PLUS | #b8bb26 (green) | 36 |
| -1 | MINUS | #cc241d (red) | 35 |

**Total world_increments:** 106 (balanced ±1)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**Network:** Mainnet (fullnode.mainnet.aptoslabs.com)  
**Snapshot:** 2026-06-05

All 28 Hamming swarm addresses (alice, bob, A-Z) returned 0 APT — accounts are uninitialized or hold zero CoinStore balance on Aptos mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...12d5 | 0.00000000 |
| A-Z (26 wallets) | 0x8699...–0x7af0... | 0.00000000 each |

### Multisig Contract Probes

Function: 0x1::multisig_account::num_signatures_required

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

All 5 multisig contracts are live 2-of-2 accounts on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

The MNX testnet frontend is a single-page application with no public REST API endpoints available. Probed /api/markets, /api/v1/markets, /api/tickers — all returned no data. Status: SPA-only, no machine-readable market data captured.

---

## DuckDB Schema Summary

- world_increments: 106 rows (GF3-tagged repo push events)
- repo_snapshots: 106 rows (org/user/repo metadata)
- aptos_snapshots: 28 rows (Hamming swarm balances)
- multisig_probes: 5 rows (2-of-2 contract health)
- mnx_snapshots: 0 rows (SPA unavailable)

---

Sweep agent: world-increment-sweep + hamming-swarm-snapshot
GF(3) color chain: ERGODIC=#d3869b PLUS=#b8bb26 MINUS=#cc241d
