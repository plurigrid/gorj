# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-06-06 11:14:16 UTC
**Ledger:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Metric | Value |
|--------|-------|
| Total repositories snapshotted | 325 |
| World increments logged | 325 |
| Sources covered | 11 |

### GF(3) Color Chain Distribution

| GF(3) Name | Trit | Color | Count |
|-----------|------|-------|-------|
| MINUS | -1 | `#cc241d` | 108 |
| ERGODIC | 0 | `#d3869b` | 108 |
| PLUS | 1 | `#b8bb26` | 109 |

### Repos by Source

| Source | Repos |
|--------|-------|
| plurigrid | 100 |
| bmorphism | 100 |
| zubyul | 49 |
| kubeflow | 48 |
| migalkin | 5 |
| wasita | 5 |
| AustinCStone | 5 |
| TeglonLabs | 4 |
| kristinezheng | 3 |
| M1shaaa | 3 |
| DJedamski | 3 |

### Top 15 Repositories by Stars

| Repo | Language | Stars | Forks | Open Issues |
|------|----------|-------|-------|-------------|
| kubeflow/kubeflow | - | 15706 | 2670 | 3 |
| kubeflow/pipelines | Python | 4152 | 2005 | 492 |
| kubeflow/spark-operator | Python | 3125 | 1488 | 99 |
| kubeflow/trainer | Go | 2111 | 964 | 123 |
| kubeflow/katib | Python | 1685 | 525 | 120 |
| kubeflow/examples | Jsonnet | 1462 | 756 | 111 |
| kubeflow/manifests | YAML | 1020 | 1065 | 22 |
| kubeflow/arena | Go | 811 | 191 | 49 |
| kubeflow/kale | Python | 691 | 155 | 48 |
| kubeflow/mpi-operator | Go | 528 | 235 | 103 |
| kubeflow/fairing | Jsonnet | 337 | 143 | 134 |
| kubeflow/pytorch-operator | Jsonnet | 310 | 143 | 63 |
| kubeflow/community | Jupyter Notebook | 194 | 257 | 15 |
| kubeflow/website | HTML | 184 | 921 | 44 |
| kubeflow/kfctl | Go | 182 | 134 | 94 |

### Language Distribution (Top 10)

| Language | Repo Count |
|----------|------------|
| Python | 62 |
| Rust | 25 |
| TypeScript | 23 |
| JavaScript | 21 |
| Go | 15 |
| Clojure | 14 |
| Jupyter Notebook | 13 |
| HTML | 13 |
| Julia | 9 |
| Zig | 7 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) probed via Aptos mainnet fullnode at ledger ~v5.6B.

**Status:** All addresses returned `resource_not_found` — no initialized APT `CoinStore` on mainnet. Balance recorded as 0.0 APT.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| A | `0x8699edc0...be9d7a` | 0.00000000 |
| B | `0x3f892ebe...77cb13` | 0.00000000 |
| C | `0x38b99e63...91535e` | 0.00000000 |
| D | `0xf7765624...fcfdd1` | 0.00000000 |
| E | `0xdc1d9d53...958d36` | 0.00000000 |
| F | `0x18a14b5b...c3cf71` | 0.00000000 |
| G | `0x69a394c0...cc7f32` | 0.00000000 |
| H | `0xce67c327...e5300f` | 0.00000000 |
| I | `0x070fe5d7...0c1fc9` | 0.00000000 |
| J | `0x4d964db8...e87f54` | 0.00000000 |
| K | `0xa732040a...425dc4` | 0.00000000 |
| L | `0x7c2eaeaf...37eba9` | 0.00000000 |
| M | `0x6fed37a7...b7f2e9` | 0.00000000 |
| N | `0xe7dde6da...551b2c` | 0.00000000 |
| O | `0x73252b60...25a89d` | 0.00000000 |
| P | `0x6218792d...1ec948` | 0.00000000 |
| Q | `0xac40fa50...5c89a9` | 0.00000000 |
| R | `0x7ce605cc...d76e10` | 0.00000000 |
| S | `0xb8753014...9d0386` | 0.00000000 |
| T | `0x35781dc0...3f4588` | 0.00000000 |
| U | `0x75860da4...ef9956` | 0.00000000 |
| V | `0xb59dd817...9af2c3` | 0.00000000 |
| W | `0x5f32aef7...ccc7b0` | 0.00000000 |
| X | `0xa95cbbd1...33047d` | 0.00000000 |
| Y | `0xd8e32848...2444c4` | 0.00000000 |
| Z | `0x7af0ef6e...4e197c` | 0.00000000 |
| alice | `0xc793acde...24cc7b` | 0.00000000 |
| bob | `0x0a3c00c5...512d5d` | 0.00000000 |

### Multisig Contract Probes

All 5 pairs probed via `0x1::multisig_account::num_signatures_required` on Aptos mainnet.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | Y |
| A-G | `0xf56c4a1c...bc0096` | 2 | Y |
| S-T | `0x3b1c3ae9...ed7883` | 2 | Y |
| V-W | `0x40fad7b4...80eb6d` | 2 | Y |
| Y-Z | `0xd3ffe181...75b883` | 2 | Y |

**Result:** All 5 multisigs require 2-of-2 signatures. All probes healthy.

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable. `testnet.mnx.fi` is protected by Vercel deployment authentication (HTTP 401). No market data extractable without a bypass token. No rows inserted into `mnx_snapshots`.

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| `world_increments` | 325 |
| `repo_snapshots` | 325 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 |

---

## Notes

- **GF(3) chain:** id%3==0 → ERGODIC (`#d3869b`), id%3==1 → PLUS (`#b8bb26`), id%3==2 → MINUS (`#cc241d`)
- **Aptos mainnet:** Ledger version ~5,599,978,000, epoch 16074, block height ~812M. All swarm addresses uninitialized (no CoinStore resource found).
- **Multisigs:** All 5 contracts live on-chain with 2-of-2 threshold — A-B, A-G, Y-Z, S-T, V-W.
- **GitHub scope:** plurigrid (100), kubeflow (48), TeglonLabs (4), bmorphism (100), zubyul (49), social graph — migalkin (5), DJedamski (3), wasita (5), kristinezheng (3), M1shaaa (3), AustinCStone (5) = 325 total repos.
- **Top repo:** kubeflow/kubeflow with 15,706 stars.
