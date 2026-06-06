# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-06  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social (zubyul graph) | 19 |
| DJedamski | social (zubyul graph) | 6 |
| wasita | social (zubyul graph) | 11 |
| kristinezheng | social (zubyul graph) | 5 |
| M1shaaa | social (zubyul graph) | 8 |
| AustinCStone | social (zubyul graph) | 40 |
| **Total** | | **390 repos** |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,706 | — |
| kubeflow/pipelines | 4,152 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,111 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,020 | YAML |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |

### Language Distribution (top 10)

| Language | Repos |
|----------|-------|
| Python | 216 |
| Rust | 56 |
| Go | 51 |
| JavaScript | 49 |
| HTML | 49 |
| TypeScript | 47 |
| Jupyter Notebook | 39 |
| Clojure | 30 |
| Jsonnet | 23 |
| Julia | 19 |

### GF(3) Color Chain

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

11 world_increment rows, one per source entity.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 addresses queried against `mainnet.aptoslabs.com`. All returned `null` — no `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource found (wallets unactivated or hold no native APT on mainnet).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0xc793ac…624cc7b | null |
| bob | 0x0a3c00…512d5d | null |
| A–Z (26) | 0x8699ed…–0x7af0ef… | null (all) |

### Multisig Contract Probes

All 5 resolved via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4f4…987003 | 2 | healthy |
| A-G | 0xf56c4a…c0096 | 2 | healthy |
| Y-Z | 0xd3ffe1…5b883 | 2 | healthy |
| S-T | 0x3b1c3a…d7883 | 2 | healthy |
| V-W | 0x40fad7…0eb6d | 2 | healthy |

All 5 multisig contracts require 2-of-N signers and are live on Aptos mainnet.

### MNX Markets

`testnet.mnx.fi` is Vercel-auth-gated — no market data accessible without a bypass token. `mnx_snapshots` table is empty this sweep.

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 390 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth-gated) |
