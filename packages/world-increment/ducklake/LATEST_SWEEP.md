# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-18 02:13:22 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**Aptos chain height at sweep:** ~906,844,130 (epoch 16576)

---

## JOB 1: GitHub Social Graph Sweep

### Source Coverage

| Source | Repos Snapshotted | Latest Push |
|--------|-------------------|-------------|
| bmorphism | 100 | 2026-07-14 |
| plurigrid | 100 | 2026-07-18 |
| zubyul | 49 | 2026-04-24 |
| kubeflow | 49 | 2026-07-18 |
| AustinCStone | 41 | 2026-07-15 |
| migalkin | 19 | 2025-08-04 |
| M1shaaa | 8 | 2026-07-18 |
| DJedamski | 6 | 2018-03-07 |
| kristinezheng | 5 | 2026-07-01 |
| TeglonLabs | 5 | 2026-06-08 |
| wasita | 1 |  |

**Total:** 383 repos across 11 sources

### Top Repos by Stars

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | - | 15779 | 2026-07-10 |
| kubeflow/pipelines | Python | 4168 | 2026-07-17 |
| kubeflow/spark-operator | Python | 3138 | 2026-07-17 |
| kubeflow/trainer | Go | 2151 | 2026-07-18 |
| kubeflow/katib | Python | 1691 | 2026-07-16 |
| kubeflow/examples | Jsonnet | 1460 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1029 | 2026-07-17 |
| kubeflow/arena | Go | 815 | 2026-07-17 |
| kubeflow/kale | Python | 696 | 2026-07-16 |
| kubeflow/mpi-operator | Go | 530 | 2026-07-13 |
| kubeflow/fairing | Jsonnet | 337 | 2022-04-11 |
| kubeflow/pytorch-operator | Jsonnet | 310 | 2021-12-01 |
| kubeflow/community | Jupyter Notebook | 195 | 2026-07-16 |
| kubeflow/website | HTML | 184 | 2026-07-15 |
| kubeflow/mcp-apache-spark-history-server | Python | 183 | 2026-07-16 |

### Most Recently Active Repos

| Repo | Language | Last Push |
|------|----------|-----------|
| M1shaaa/M1shaaa | - | 2026-07-18 |
| plurigrid/gorj | Clojure | 2026-07-18 |
| kubeflow/trainer | Go | 2026-07-18 |
| kubeflow/spark-operator | Python | 2026-07-17 |
| kubeflow/hub | Go | 2026-07-17 |
| kubeflow/pipelines | Python | 2026-07-17 |
| kubeflow/sdk | Python | 2026-07-17 |
| kubeflow/community-distribution | YAML | 2026-07-17 |
| kubeflow/blog | Jupyter Notebook | 2026-07-17 |
| kubeflow/arena | Go | 2026-07-17 |

### GF(3) Color Chain Distribution

| Name | Color | Count |
|------|-------|-------|
| PLUS | `#b8bb26` | 128 |
| MINUS | `#cc241d` | 128 |
| ERGODIC | `#d3869b` | 127 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
All accounts returned `resource_not_found` → balance = 0 APT.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| A | `0x8699edc0...be9d7a` | 0.0 |
| B | `0x3f892ebe...77cb13` | 0.0 |
| C | `0x38b99e63...91535e` | 0.0 |
| D | `0xf7765624...fcfdd1` | 0.0 |
| E | `0xdc1d9d53...958d36` | 0.0 |
| F | `0x18a14b5b...c3cf71` | 0.0 |
| G | `0x69a394c0...cc7f32` | 0.0 |
| H | `0xce67c327...e5300f` | 0.0 |
| I | `0x070fe5d7...0c1fc9` | 0.0 |
| J | `0x4d964db8...e87f54` | 0.0 |
| K | `0xa732040a...425dc4` | 0.0 |
| L | `0x7c2eaeaf...37eba9` | 0.0 |
| M | `0x6fed37a7...b7f2e9` | 0.0 |
| N | `0xe7dde6da...551b2c` | 0.0 |
| O | `0x73252b60...25a89d` | 0.0 |
| P | `0x6218792d...1ec948` | 0.0 |
| Q | `0xac40fa50...5c89a9` | 0.0 |
| R | `0x7ce605cc...d76e10` | 0.0 |
| S | `0xb8753014...9d0386` | 0.0 |
| T | `0x35781dc0...3f4588` | 0.0 |
| U | `0x75860da4...ef9956` | 0.0 |
| V | `0xb59dd817...9af2c3` | 0.0 |
| W | `0x5f32aef7...ccc7b0` | 0.0 |
| X | `0xa95cbbd1...33047d` | 0.0 |
| Y | `0xd8e32848...2444c4` | 0.0 |
| Z | `0x7af0ef6e...4e197c` | 0.0 |
| alice | `0xc793acde...24cc7b` | 0.0 |
| bob | `0x0a3c00c5...512d5d` | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | ✓ |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✓ |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✓ |

**All 5 multisig contracts are 2-of-N, healthy.**

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — Vercel deployment protection requires visitor password authentication.  
No market data captured this run.

---

## Summary

- **383** GitHub repos snapshotted from 11 sources (plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)
- **28** Aptos wallets queried — all show 0 APT balance (accounts exist on-chain but no CoinStore resource registered)
- **5** multisig contracts probed — all require 2 signatures, all healthy
- **MNX testnet** inaccessible (auth wall)
- Aptos chain: ledger version **6,332,579,204**, epoch **16576**, block height **906,844,130**
