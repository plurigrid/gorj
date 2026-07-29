# LATEST_SWEEP.md

**Sweep timestamp:** 2026-07-29 03:13 UTC
**World increments this run:** 239
**Unique repos snapshotted:** 547

---

## JOB 1: GitHub Social Graph Sweep

### Sources Covered

| Source | Repos |
|--------|-------|
| bmorphism | 250 |
| plurigrid | 250 |
| kubeflow | 143 |
| TeglonLabs | 111 |
| zubyul | 97 |
| AustinCStone | 89 |
| migalkin | 65 |
| wasita | 62 |
| kristinezheng | 37 |
| M1shaaa | 33 |
| DJedamski | 23 |

### Top Repos by Stars

| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow |  | 15794 | 2689 | 2026-07-10 |
| kubeflow/kubeflow |  | 15572 | 2633 | 2026-01-05 |
| kubeflow/kubeflow |  | 15565 | 2626 | 2026-01-05 |
| kubeflow/pipelines | Python | 4171 | 2069 | 2026-07-29 |
| kubeflow/pipelines | Python | 4119 | 1984 | 2026-04-10 |
| kubeflow/pipelines | Python | 4119 | 1985 | 2026-04-14 |
| kubeflow/spark-operator | Python | 3142 | 1509 | 2026-07-25 |
| kubeflow/spark-operator | Python | 3114 | 1483 | 2026-04-13 |
| kubeflow/spark-operator | Python | 3111 | 1483 | 2026-04-10 |
| kubeflow/trainer | Go | 2159 | 1000 | 2026-07-27 |
| kubeflow/trainer | Go | 2082 | 945 | 2026-04-13 |
| kubeflow/trainer | Go | 2080 | 944 | 2026-04-10 |
| kubeflow/katib | Python | 1693 | 532 | 2026-07-26 |
| kubeflow/katib | Python | 1678 | 521 | 2026-04-14 |
| kubeflow/katib | Python | 1676 | 521 | 2026-04-02 |

### Recent Activity (plurigrid / TeglonLabs / bmorphism / zubyul)

| Org/User | Repo | Language | Stars | Last Push |
|----------|------|----------|-------|-----------|
| bmorphism | Gay.jl | Julia | 2 | 2026-07-29 |
| plurigrid | gorj | Clojure | 1 | 2026-07-29 |
| plurigrid | zig-syrup | Zig | 2 | 2026-07-28 |
| plurigrid | eirobri | Clojure | 0 | 2026-07-21 |
| zubyul | from-possible-worlds | TeX | 0 | 2026-07-18 |
| bmorphism | gay-chat | Scheme | 0 | 2026-07-14 |
| plurigrid | place | TeX | 1 | 2026-07-14 |
| plurigrid | asi | HTML | 52 | 2026-07-10 |
| plurigrid | shrimp |  | 0 | 2026-07-03 |
| bmorphism | satreadout | HTML | 0 | 2026-06-20 |

### Social Graph (zubyul contacts)
- **migalkin**: Knowledge Graph researcher — NodePiece (144★), StarE (89★), kgcourse2021 (24★)
- **DJedamski**: Data science / Kaggle competitor
- **wasita**: Svelte/Typst developer — personal site, pnas-typst-template, magic-garden bot
- **kristinezheng**: Cognitive science / MIT — auditory illusion, lookit-jenga
- **M1shaaa**: Yale — lab-bookshelf TypeScript, MNIST-Classifier
- **AustinCStone**: ML/CV — TextGAN (92★), StereoVisionMRF (11★), byteruckus

### GF(3) Color Chain Distribution

| GF3 Name | Color | Count |
|----------|-------|-------|
| ERGODIC | #d3869b | 79 |
| MINUS | #cc241d | 80 |
| PLUS | #b8bb26 | 80 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Probe time:** 2026-07-29 03:13 UTC
**Wallets queried:** 28 (alice, bob, A–Z)
**Wallets with non-zero APT:** 0

> All 28 Hamming-swarm addresses returned 0 APT balance.
> This indicates the CoinStore<AptosCoin> resource is not initialized on these
> mainnet addresses (wallets exist on-chain but hold no liquid APT).

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...4987003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c...fbc0096 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4...c80eb6d | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181...e75b883 | 2 | ✓ HEALTHY |

> All 5 multisig contracts are healthy with 2-of-N signature threshold.

### MNX Testnet Markets

> **testnet.mnx.fi** is a Next.js SPA (server-side rendered).
> No REST API endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) returned JSON data.
> SPA content is loaded client-side via JavaScript bundles — unavailable to curl.
> Status: **UNAVAILABLE** (SPA-only, no accessible API)

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 239 |
| repo_snapshots | 547 (distinct repos) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (SPA placeholder) |

Database: `packages/world-increment/ducklake/world-increments.duckdb`
