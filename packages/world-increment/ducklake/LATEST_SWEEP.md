# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep date:** 2026-08-07  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos Catalogued |
|--------|------|-----------------|
| plurigrid | org | 103 (14 sampled) |
| kubeflow | org | 49 (9 sampled) |
| TeglonLabs | org | 5 (5 sampled) |
| bmorphism | user | 106 (9 sampled) |
| zubyul | user | 49 (6 sampled) |
| migalkin | social graph | 19 (5 sampled) |
| wasita | social graph | 14 (4 sampled) |
| AustinCStone | social graph | 41 (3 sampled) |
| kristinezheng | social graph | (prior sweep) |
| M1shaaa | social graph | (prior sweep) |
| DJedamski | social graph | (prior sweep) |

**Total repo_snapshots in DB: 999 (cumulative across sweeps)**  
**New world_increments this sweep: 78**

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| +1 | #b8bb26 | PLUS | 27 |
| -1 | #cc241d | MINUS | 26 |
| 0 | #d3869b | ERGODIC | 25 |

### Notable Repos

- **kubeflow/kubeflow** — 15,805 ⭐ ML Toolkit for Kubernetes
- **kubeflow/pipelines** — 4,181 ⭐ ML Pipelines
- **kubeflow/spark-operator** — 3,146 ⭐ Kubernetes Spark operator
- **kubeflow/trainer** — 2,173 ⭐ Distributed AI training
- **plurigrid/asi** — 59 ⭐ topological chemputer
- **bmorphism/ocaml-mcp-sdk** — 61 ⭐ OCaml MCP SDK
- **migalkin/NodePiece** — 144 ⭐ KG representations (ICLR'22)
- **AustinCStone/TextGAN** — 92 ⭐ Text GAN in TensorFlow
- **plurigrid/gorj** — 1,690 open issues, active (pushed 2026-08-07)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

**Addresses probed: 28**  
**Non-null balances: 0**  

All 28 addresses returned null from `fullnode.mainnet.aptoslabs.com`. These addresses are not currently holding APT in their CoinStore, or the accounts do not exist on mainnet. This is consistent with the swarm being dormant / not yet funded on mainnet.

### Multisig Probes

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428... | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a1c... | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | ✅ HEALTHY |
| V-W | 0x40fad7b4... | 2 | ✅ HEALTHY |

All 5 multisig accounts are configured as **2-of-N** and responding on-chain. No degraded contracts detected.

### MNX Markets (testnet.mnx.fi)

Status: **SPA — no public JSON API accessible**  
`https://testnet.mnx.fi` returns a Next.js client-rendered app. API routes (`/api/markets`, `/api/v1/markets`) returned no JSON data accessible via HTTP. MNX market data was not capturable in this sweep; the `mnx_snapshots` table remains empty for this run.

---

## DuckDB Table Summary

| Table | Row Count |
|-------|-----------|
| world_increments | 78 (this sweep) |
| repo_snapshots | 999 (cumulative) |
| aptos_snapshots | 28 (this sweep) |
| multisig_probes | 5 (this sweep) |
| mnx_snapshots | 0 (SPA unavailable) |
