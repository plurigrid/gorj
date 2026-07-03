# LATEST_SWEEP — 2026-07-03 03:12:48 UTC

## JOB 1: GitHub Social Graph Sweep

**Snapshot date:** 2026-07-03 03:12:48 UTC  
**Total repo snapshots this run:** 322

### Source Breakdown

| Source | Repos |
|--------|-------|
| bmorphism | 100 |
| kubeflow | 100 |
| zubyul | 49 |
| plurigrid | 48 |
| social | 20 |
| TeglonLabs | 5 |

### GF(3) Color Chain Distribution (this run)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| ? | #d3869b | `ERGODIC` | 107 |
| ? | #b8bb26 | `PLUS` | 108 |
| ? | #cc241d | `MINUS` | 107 |

### Top Repos by Stars

| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow | — | 15758 | 2682 | 2026-06-18 |
| kubeflow/pipelines | Python | 4167 | 2020 | 2026-07-02 |
| kubeflow/spark-operator | Python | 3131 | 1496 | 2026-07-02 |
| kubeflow/trainer | Go | 2129 | 974 | 2026-07-02 |
| kubeflow/katib | Python | 1688 | 529 | 2026-07-01 |
| kubeflow/examples | Jsonnet | 1460 | 756 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1028 | 1067 | 2026-06-30 |
| kubeflow/arena | Go | 814 | 194 | 2026-07-03 |
| kubeflow/kale | Python | 694 | 156 | 2026-07-01 |
| kubeflow/mpi-operator | Go | 529 | 237 | 2026-07-02 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Ledger queried:** mainnet.aptoslabs.com  
**Total wallets probed:** 28  
**Total APT across swarm:** 20.344773 APT

### Wallet Balances

| World | Address (short) | Balance (APT) |
|-------|----------------|---------------|
| bob | `0x0a3c00c5...512d5d` | 12.65700700 |
| F | `0x18a14b5b...c3cf71` | 1.96051600 |
| L | `0x7c2eaeaf...37eba9` | 1.92726900 |
| J | `0x4d964db8...e87f54` | 1.89509300 |
| alice | `0xc793acde...24cc7b` | 0.43643352 |
| O | `0x73252b60...25a89d` | 0.21013600 |
| K | `0xa732040a...425dc4` | 0.16196100 |
| P | `0x6218792d...1ec948` | 0.14013600 |
| M | `0x6fed37a7...b7f2e9` | 0.11228500 |
| N | `0xe7dde6da...551b2c` | 0.10612100 |
| Q | `0xac40fa50...5c89a9` | 0.10324000 |
| S | `0xb8753014...9d0386` | 0.09178800 |
| R | `0x7ce605cc...d76e10` | 0.09021700 |
| T | `0x35781dc0...3f4588` | 0.07371300 |
| U | `0x75860da4...ef9956` | 0.05577300 |
| A | `0x8699edc0...be9d7a` | 0.05176700 |
| V | `0xb59dd817...9af2c3` | 0.04883299 |
| Y | `0xd8e32848...2444c4` | 0.04444900 |
| X | `0xa95cbbd1...33047d` | 0.04257700 |
| W | `0x5f32aef7...ccc7b0` | 0.04070500 |
| B | `0x3f892ebe...77cb13` | 0.03625600 |
| Z | `0x7af0ef6e...4e197c` | 0.02426800 |
| D | `0xf7765624...fcfdd1` | 0.01162900 |
| C | `0x38b99e63...91535e` | 0.01018500 |
| E | `0xdc1d9d53...958d36` | 0.00937200 |
| H | `0xce67c327...e5300f` | 0.00168100 |
| I | `0x070fe5d7...0c1fc9` | 0.00068100 |
| G | `0x69a394c0...cc7f32` | 0.00068100 |

### Multisig Probes

| Pair | Address (short) | Sigs Required | Healthy |
|------|----------------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | ✓ |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✓ |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — Vercel deployment protection (authentication required, no bypass token available).

---

## DuckDB Schema

- `world_increments` — GF(3) tagged event log (total rows: combined from all runs)
- `repo_snapshots` — GitHub repo metadata
- `aptos_snapshots` — Aptos wallet balances
- `multisig_probes` — Multisig sig-threshold probes
- `mnx_snapshots` — MNX market data (currently unavailable)

**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
