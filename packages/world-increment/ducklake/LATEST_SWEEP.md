# World-Increment Sweep + Hamming Snapshot

**Sweep timestamp:** 2026-06-23T18:09 UTC  
**GF(3) Color Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos in DB | Notes |
|--------|------|-------------|-------|
| bmorphism | user | 219 | Active: Gay.jl (187 open issues), anti-bullshit-mcp-server (23★), satreadout pushed 2026-06-20 |
| plurigrid | org | 218 | Active: nanoclj-zig, zig-syrup, graded-optic, asi-skills |
| zubyul | user | 57 | Active: gay-world, ghostel-emacs-worlds, nash-tui |
| kubeflow | org | 105 | Active: kubeflow/kubeflow (15,741★), pipelines (4,157★), trainer (2,119★) |
| TeglonLabs | org | 111 | Active: jank-crane (GF3 convergence maps, 2026-06-08) |
| migalkin | social | 60 | (cumulative) |
| DJedamski | social | 22 | (cumulative) |
| wasita | social | 60 | (cumulative) |
| kristinezheng | social | 36 | (cumulative) |
| M1shaaa | social | 32 | (cumulative) |
| AustinCStone | social | 86 | (cumulative) |

### Top Repos by Stars (this sweep)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,741 | — |
| kubeflow/pipelines | 4,157 | Python |
| kubeflow/spark-operator | 3,128 | Python |
| kubeflow/trainer | 2,119 | Go |
| kubeflow/mpi-operator | 528 | Go |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/say-mcp-server | 20 | JavaScript |
| bmorphism/babashka-mcp-server | 19 | JavaScript |
| bmorphism/Gay.jl | 2 | Julia (187 open issues!) |

### Notable Activity

- **bmorphism/Gay.jl** — 187 open issues, pushed 2026-06-23 (today). Wide-gamut color sampling, Pigeons.jl SPI.
- **bmorphism/satreadout** — pushed 2026-06-20. Machine-checked saturating non-Riemannian perceptual readout.
- **TeglonLabs/jank-crane** — pushed 2026-06-08. crane-jank converged-IR hub with GF3 convergence maps.
- **kubeflow/mpi-operator** — pushed 2026-06-23. MPI Kubernetes operator active.

### GF(3) Distribution (cumulative)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 27 |
| 1 | PLUS | #b8bb26 | 29 |
| -1 | MINUS | #cc241d | 29 |
| **Total** | | | **85** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A-Z) returned resource_not_found for CoinStore<AptosCoin>. These accounts have not been funded with APT on mainnet.

**Total APT across swarm: 0.0 APT**

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A-Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | null | NO (not found) |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

**4/5 multisigs healthy.** A-G (0xf56c...0096) not found on mainnet.

### MNX Markets (testnet.mnx.fi)

**Unavailable.** The testnet endpoint is protected by Vercel deployment authentication. No market data extractable without bypass credentials.

---

## DuckDB Schema Summary

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 85 |
| repo_snapshots | 1,006 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
