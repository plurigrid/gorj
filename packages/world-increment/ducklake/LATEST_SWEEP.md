# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-03  
**Run:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 98 |
| kubeflow | org | 50 |
| TeglonLabs | org | 5 |
| bmorphism | user | 96 |
| zubyul | user | 54 |
| migalkin | social | 5 (top) |
| wasita | social | 3 (top) |
| AustinCStone | social | 2 (top) |
| DJedamski | social | 2 (top) |
| kristinezheng | social | 2 (top) |
| M1shaaa | social | 2 (top) |

**Total repo snapshots this run:** 314 new increments appended

### Notable Repos by Stars

| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15,803 | — |
| kubeflow | pipelines | 4,173 | Python |
| kubeflow | spark-operator | 3,142 | Python |
| kubeflow | trainer | 2,165 | Go |
| kubeflow | katib | 1,694 | Go |
| migalkin | NodePiece | 144 | Python |
| AustinCStone | TextGAN | 92 | Python |
| migalkin | StarE | 89 | Python |
| bmorphism | ocaml-mcp-sdk | 61 | OCaml |
| plurigrid | asi | 58 | HTML |

### TeglonLabs Repos

| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### GF(3) Color Chain Distribution

| GF3 Name | Color | Count |
|----------|-------|-------|
| ERGODIC (trit=0) | #d3869b | 111 |
| PLUS (trit=1) | #b8bb26 | 113 |
| MINUS (trit=-1) | #cc241d | 113 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) queried against Aptos mainnet fullnode.  
**Result: All addresses returned 0.0 APT** — accounts may be empty, unfunded, or the CoinStore resource is not initialized.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…12d5d | 0.0 |
| A–Z | 0x86…–0x7af0… | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** (2-of-2 signatures required):

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | yes |
| A-G | 0xf56c…0096 | 2 | yes |
| Y-Z | 0xd3ff…b883 | 2 | yes |
| S-T | 0x3b1c…7883 | 2 | yes |
| V-W | 0x40fa…eb6d | 2 | yes |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `https://testnet.mnx.fi/api/markets` returns a Next.js SPA shell with no extractable market data. The site loads client-side; no market JSON was accessible via direct API probe.

---

## DuckDB Table Summary

| Table | Row Count |
|-------|-----------|
| world_increments | 337 (cumulative) |
| repo_snapshots | 1,258 (cumulative) |
| aptos_snapshots | 28 (this run) |
| multisig_probes | 5 (this run) |
| mnx_snapshots | 0 (unavailable) |
