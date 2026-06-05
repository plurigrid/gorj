# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-05  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Increment Chain

| ID | Trit | Color   | Name    | Source Type | Source        |
|----|------|---------|---------|-------------|---------------|
| 1  | +1   | #b8bb26 | PLUS    | org         | plurigrid     |
| 2  | -1   | #cc241d | MINUS   | org         | kubeflow      |
| 3  | 0    | #d3869b | ERGODIC | org         | TeglonLabs    |
| 4  | +1   | #b8bb26 | PLUS    | user        | bmorphism     |
| 5  | -1   | #cc241d | MINUS   | user        | zubyul        |
| 6  | 0    | #d3869b | ERGODIC | user        | migalkin      |
| 7  | +1   | #b8bb26 | PLUS    | user        | wasita        |
| 8  | -1   | #cc241d | MINUS   | user        | AustinCStone  |
| 9  | 0    | #d3869b | ERGODIC | user        | DJedamski     |
| 10 | +1   | #b8bb26 | PLUS    | user        | kristinezheng |
| 11 | -1   | #cc241d | MINUS   | user        | M1shaaa       |

### Repo Counts by Source

| Source         | Type | Repos | Top Stars                                              |
|----------------|------|-------|--------------------------------------------------------|
| plurigrid      | org  | 100   | asi (25), ontology (8), vcg-auction (7)               |
| kubeflow       | org  | 48    | kubeflow (15706), pipelines (4152), spark-operator (3125) |
| TeglonLabs     | org  | 4     | mathpix-gem (2)                                        |
| bmorphism      | user | 100   | ocaml-mcp-sdk (61), anti-bullshit-mcp-server (23), risc0-cosmwasm-example (23) |
| zubyul         | user | 49    | WGCNA (2), jonikas_lab (2), gay-world (1)             |
| migalkin       | user | 19    | NodePiece (144), StarE (89), kgcourse2021 (25)        |
| wasita         | user | 11    | magic-garden (2), wasita.github.io (1)                |
| AustinCStone   | user | 30    | TextGAN (92), StereoVisionMRF (11), SpectralClustering (3) |
| DJedamski      | user | 6     | Kaggle (1), Getting-and-Cleaning-Data (1), School (1) |
| kristinezheng  | user | 5     | (all 0 stars)                                          |
| M1shaaa        | user | 8     | (all 0 stars)                                          |

**Total repos snapshotted: 380**

### Top 10 Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15706 | — | 2026-05-24 |
| kubeflow/pipelines | 4152 | Python | 2026-06-05 |
| kubeflow/spark-operator | 3125 | Python | 2026-06-04 |
| kubeflow/trainer | 2111 | Go | 2026-06-05 |
| kubeflow/katib | 1684 | Python | 2026-06-04 |
| kubeflow/examples | 1462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1020 | YAML | 2026-06-05 |
| kubeflow/arena | 811 | Go | 2026-05-07 |
| kubeflow/kale | 690 | Python | 2026-06-04 |
| kubeflow/mpi-operator | 528 | Go | 2026-06-02 |

### Notable Recent Activity

- **plurigrid/gorj** (this repo): 365 open issues, pushed 2026-06-05 — Clojure
- **bmorphism/Gay.jl**: 189 open issues, pushed 2026-06-05 — Julia, wide-gamut GF(3) color sampling
- **plurigrid/eirobri**: 29 open issues, pushed 2026-06-03 — EiRoBri replay world
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for Model Context Protocol
- **migalkin/NodePiece**: 144 stars — Compositional KG Representations (ICLR 2022)
- **AustinCStone/TextGAN**: 92 stars — GAN for text generation in TensorFlow

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-05)

All 28 swarm addresses (alice, bob, A–Z) returned **0.0 APT** balance.
The `CoinStore<AptosCoin>` resource was not found on any address — these
are placeholder/test addresses not yet funded on Aptos mainnet.

| World | Address (truncated)  | APT Balance |
|-------|----------------------|-------------|
| alice | 0xc793...cc7b        | 0.0         |
| bob   | 0x0a3c...2d5d        | 0.0         |
| A–Z   | (26 addresses)       | 0.0 each    |

### Multisig Contract Probes

All 5 multisig contracts responded successfully. All require **2 signatures** (healthy 2-of-N multisig).

| Pair | Address (truncated)  | Sigs Required | Healthy |
|------|----------------------|---------------|---------|
| A-B  | 0x0da4...7003        | 2             | ✓       |
| A-G  | 0xf56c...0096        | 2             | ✓       |
| Y-Z  | 0xd3ff...b883        | 2             | ✓       |
| S-T  | 0x3b1c...7883        | 2             | ✓       |
| V-W  | 0x40fa...eb6d        | 2             | ✓       |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is behind Vercel deployment protection (authentication required).
No market data extractable without bypass token. Status: **UNAVAILABLE**.

---

## DuckDB Schema Summary

```
world_increments  — 11 rows  (GF(3) color-coded source increments)
repo_snapshots    — 380 rows (GitHub repo metadata snapshots)
aptos_snapshots   —  28 rows (Aptos mainnet wallet balance probes)
multisig_probes   —   5 rows (Aptos multisig contract status)
mnx_snapshots     —   0 rows (MNX markets unavailable)
```

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent — 2026-06-05*
