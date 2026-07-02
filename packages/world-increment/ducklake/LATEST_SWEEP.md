# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-02  
**GF(3) color chain:** ERGODIC #d3869b (id%3=0) · PLUS #b8bb26 (id%3=1) · MINUS #cc241d (id%3=2)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social graph) | 7 |
| DJedamski | user (social graph) | 6 |
| wasita | user (social graph) | 7 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| AustinCStone | user (social graph) | 6 |
| **Total** | | **341** |

### DuckDB Tables

- `world_increments`: 341 rows — each repo snapshot as a world-increment event with GF(3) trit assignment
- `repo_snapshots`: 341 rows — full repo metadata (language, stars, forks, pushed_at, description)

### GF(3) Distribution

| Name | Color | Count |
|------|-------|-------|
| ERGODIC | #d3869b | 113 |
| PLUS | #b8bb26 | 114 |
| MINUS | #cc241d | 114 |

### Notable Repos

**kubeflow** — kubeflow/kubeflow: 15,757 stars · kubeflow/pipelines: 4,167 stars · kubeflow/spark-operator: 3,130 stars · kubeflow/trainer: 2,128 stars  
**bmorphism** — manifold-mcp-server: 14 stars · world (pushed 2026-06-02) · signal-mcp (Rust, 2025-12)  
**zubyul** — gay-world: 1 star · cascade-world: 1 star · Gay.jl (Julia, 2026-03)  
**plurigrid** — ontology: 8 stars · nanoclj-zig: 1 star · zig-syrup: 2 stars  
**migalkin** — NodePiece: 144 stars (ICLR'22) · StarE: 89 stars (EMNLP'20)  
**AustinCStone** — TextGAN: 92 stars · StereoVisionMRF: 11 stars  
**TeglonLabs** — jank-crane (C++, pushed 2026-06-08) · mathpix-gem (Ruby)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A-Z)

**Status:** All 28 addresses queried against Aptos mainnet fullnode.  
**Result:** `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource **not found** for all addresses.  
Addresses have not registered an APT CoinStore — likely unfunded or not yet initialized on-chain.  
All balances recorded as NULL in `aptos_snapshots`.

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...c0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...5b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | HEALTHY |

All 5 multisig contracts are 2-of-2 and responding on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — all API paths return the SPA shell HTML. No structured market data exposed via REST API. `mnx_snapshots` table is empty.

---

## DuckDB Schema Summary

```
packages/world-increment/ducklake/world-increments.duckdb
├── world_increments (341 rows) — GF3-tagged repo events
├── repo_snapshots  (341 rows) — full repo metadata
├── aptos_snapshots  (28 rows) — Hamming swarm wallet snapshot (all NULL)
├── multisig_probes   (5 rows) — all 2-of-2, healthy
└── mnx_snapshots     (0 rows) — SPA, no data
```
