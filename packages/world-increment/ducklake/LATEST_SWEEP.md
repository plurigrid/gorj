# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-06  
**Sweep ID:** world-increment/sweep-2026-08-06  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos | Total Stars | GF(3) Trit | Color |
|--------|------|-------|-------------|------------|-------|
| plurigrid | org | 100 | 112 | PLUS (1) | #b8bb26 |
| kubeflow | org | 49 | 34,474 | MINUS (-1) | #cc241d |
| TeglonLabs | org | 5 | 2 | ERGODIC (0) | #d3869b |
| bmorphism | user | 100 | 247 | PLUS (1) | #b8bb26 |
| zubyul | user | 49 | 14 | MINUS (-1) | #cc241d |
| migalkin | social | 5 | 275 | ERGODIC (0) | #d3869b |
| DJedamski | social | 2 | 1 | PLUS (1) | #b8bb26 |
| wasita | social | 4 | 3 | MINUS (-1) | #cc241d |
| kristinezheng | social | 2 | 0 | ERGODIC (0) | #d3869b |
| M1shaaa | social | 2 | 0 | PLUS (1) | #b8bb26 |
| AustinCStone | social | 3 | 92 | MINUS (-1) | #cc241d |

**Total repos snapshotted:** 321  
**Total stars across all sources:** 35,220

### Most Recently Pushed (Top 10)

| Repo | Stars | Language | Pushed At |
|------|-------|----------|-----------|
| wasita/xoxowasita-analysis | 0 | Python | 2026-08-06T19:06Z |
| plurigrid/gorj | 1 | Clojure | 2026-08-06T18:18Z |
| kubeflow/dashboard | 16 | TypeScript | 2026-08-06T17:48Z |
| kubeflow/notebooks | 73 | — | 2026-08-06T17:34Z |
| kubeflow/sdk | 133 | Python | 2026-08-06T17:08Z |
| kubeflow/trainer | 2,171 | Go | 2026-08-06T15:33Z |
| bmorphism/Gay.jl | 2 | Julia | 2026-08-06T02:26Z |
| kubeflow/pipelines | 4,178 | Python | 2026-08-05T18:54Z |
| kubeflow/kale | 699 | Python | 2026-08-05T14:52Z |
| kubeflow/mcp-apache-spark-history-server | 186 | Python | 2026-08-04T23:23Z |

### Notable Repos

- **kubeflow/pipelines** — 4,178★ 2,080 forks, ML Pipelines for Kubeflow
- **kubeflow/trainer** — 2,171★ Distributed AI/LLM fine-tuning on Kubernetes
- **kubeflow/kubeflow** — 15,805★ (meta repo, no recent push)
- **migalkin/NodePiece** — 144★ ICLR'22 KG compositional representations
- **migalkin/StarE** — 89★ EMNLP 2020 hyper-relational KG message passing
- **AustinCStone/TextGAN** — 92★ GAN for text generation (TensorFlow)
- **bmorphism/Gay.jl** — Julia wide-gamut color sampling, updated today
- **plurigrid/gorj** — This repo! Clojure, pushed today
- **TeglonLabs/jank-crane** — C++, GF3 convergence maps, jank IR hub
- **wasita/xoxowasita-analysis** — Python, pushed today (brand new)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses: alice, bob, A–Z)

**Result:** All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

This indicates no APT coin store initialized on any of these addresses — **effective balance: 0.00 APT** for all wallets. Addresses exist on-chain but have not received or held APT via the legacy CoinStore module (accounts may use Fungible Asset framework instead).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 (resource_not_found) |
| bob | 0x0a3c...12d5 | 0.0 (resource_not_found) |
| A–Z | (26 addresses) | 0.0 each (resource_not_found) |

### Multisig Contract Probes

All 5 multisig contracts responded healthy with 2-of-N threshold:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All multisig contracts are responsive and require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA — no public REST API exposed. Market data is loaded client-side via internal calls. Status: **unavailable via curl**. Recorded as `N/A` in `mnx_snapshots`.

---

## DuckDB Schema Summary

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 11 | GF(3) color-coded sweep events per source |
| `repo_snapshots` | 321 | Full repo metadata for all snapshotted sources |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances |
| `multisig_probes` | 5 | Multisig contract health probes |
| `mnx_snapshots` | 1 | MNX market data (unavailable this run) |

---

## GF(3) Color Chain Legend

| id % 3 | Trit | Name | Color |
|--------|------|------|-------|
| 0 | 0 | ERGODIC | #d3869b |
| 1 | +1 | PLUS | #b8bb26 |
| 2 | -1 | MINUS | #cc241d |
