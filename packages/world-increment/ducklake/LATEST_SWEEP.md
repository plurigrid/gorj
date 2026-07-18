# World Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-07-18T04:10 UTC
**Branch:** world-increment/sweep-2026-07-18

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapshotted | Notable |
|--------|------|-------------------|---------|
| plurigrid | org | 19 | gorj (1231 open issues), asi (31*), active Zig/Clojure/Rust |
| kubeflow | org | 22 | kubeflow/kubeflow (15779*), pipelines (4168*), trainer (2151*) |
| TeglonLabs | org | 5 | jank-crane (C++, 2026-06), mathpix-gem (Ruby) |
| bmorphism | user | 15 | ocaml-mcp-sdk (61*), Gay.jl (187 open issues), MCP ecosystem |
| zubyul | user | 12 | gay-world, tilelang-kernels, GF(3)/SPI focused |
| migalkin | user | 5 | NodePiece (144*), StarE (89*) -- Knowledge Graph research |
| DJedamski | user | 3 | Academic/data science |
| wasita | user | 4 | magic-garden, wasita.github.io (recently active) |
| kristinezheng | user | 3 | Neuroscience/MIT |
| M1shaaa | user | 3 | Yale/Lookit research |
| AustinCStone | user | 5 | TextGAN (92*), ML/vision research |
| **TOTAL** | | **96** | |

### GF(3) Color Chain Distribution
- trit=0 ERGODIC #d3869b: 32 increments
- trit=1 PLUS #b8bb26: 32 increments
- trit=-1 MINUS #cc241d: 32 increments

### Most Active Repos (by push recency, 2026-07-18)
1. plurigrid/gorj -- pushed 2026-07-18T03:14
2. kubeflow/sdk -- pushed 2026-07-18T03:01
3. kubeflow/trainer -- pushed 2026-07-18T02:23
4. kubeflow/website -- pushed 2026-07-18T02:07
5. kubeflow/spark-operator -- pushed 2026-07-17T23:31

### Top Starred Repos in Sweep
1. kubeflow/kubeflow -- 15,779*
2. kubeflow/pipelines -- 4,168*
3. kubeflow/spark-operator -- 3,139*
4. kubeflow/trainer -- 2,151*
5. kubeflow/katib -- 1,691*
6. migalkin/NodePiece -- 144*
7. AustinCStone/TextGAN -- 92*
8. migalkin/StarE -- 89*
9. bmorphism/ocaml-mcp-sdk -- 61*

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-18)

All 28 wallets queried via fullnode.mainnet.aptoslabs.com.

| World | Balance (APT) | Status |
|-------|--------------|--------|
| alice | 0.0 | no CoinStore initialized |
| bob | 0.0 | no CoinStore initialized |
| A-Z (26 wallets) | 0.0 each | no CoinStore initialized |

All 28 wallets returned raw=0 for the APT CoinStore resource.
These addresses have not been funded or have not initialized the APT coin store on mainnet.

### Multisig Contract Probes (5/5 Healthy)

All 5 multisig contracts probed via 0x1::multisig_account::num_signatures_required:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4f428...987003 | 2 | YES |
| A-G | 0xf56c4a1c...c0096 | 2 | YES |
| Y-Z | 0xd3ffe181...b883 | 2 | YES |
| S-T | 0x3b1c3ae9...7883 | 2 | YES |
| V-W | 0x40fad7b4...eb6d | 2 | YES |

All multisig contracts are 2-of-2. All responsive and healthy.

### MNX Markets (testnet.mnx.fi)

Status: UNAVAILABLE -- testnet.mnx.fi returns HTTP 401 with password_enabled=true
(Vercel password-protected deployment). No market data accessible.

---

## DuckDB Ducklake Stats

Database: packages/world-increment/ducklake/world-increments.duckdb

| Table | Rows |
|-------|------|
| world_increments | 96 |
| repo_snapshots | 96 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

---

## Notes
- GF(3) trit color chain applied to all 96 world_increment rows (32 each trit, balanced)
- DuckDB 1.5.4 via pip (DuckDB CLI binary blocked by proxy at 403)
- GitHub search results capped at 100/page; plurigrid total_count=103 (3 missed via API cap)
- Aptos API accessible; all wallets show 0 APT (accounts unfunded on mainnet)
