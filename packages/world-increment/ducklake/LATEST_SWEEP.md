# LATEST_SWEEP — 2026-05-14 11:12 UTC

## Job 1: GitHub Social Graph Sweep

**Total world-increments:** 391  
**Sweep date:** 2026-05-14 11:12 UTC

### Sources

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| kristinezheng | user | 6 |
| DJedamski | user | 6 |

### Top Languages

| Language | Repos |
|----------|-------|
| Python | 81 |
| Rust | 26 |
| JavaScript | 25 |
| TypeScript | 23 |
| HTML | 15 |
| Go | 15 |
| Jupyter Notebook | 14 |
| Clojure | 13 |
| Julia | 9 |
| Jsonnet | 8 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| -1 | #cc241d | MINUS | 130 |
| 0 | #d3869b | ERGODIC | 130 |
| 1 | #b8bb26 | PLUS | 131 |

### Top Repos by Stars

| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow/kubeflow |  | 15629 | 2026-05-07 |
| kubeflow/pipelines | Python | 4140 | 2026-05-12 |
| kubeflow/spark-operator | Python | 3125 | 2026-05-12 |
| kubeflow/trainer | Go | 2098 | 2026-05-13 |
| kubeflow/katib | Python | 1682 | 2026-05-09 |
| kubeflow/examples | Jsonnet | 1462 | 2025-04-14 |
| kubeflow/manifests | YAML | 1017 | 2026-05-13 |
| kubeflow/arena | Go | 810 | 2026-05-07 |
| kubeflow/kale | Python | 686 | 2026-05-13 |
| kubeflow/mpi-operator | Go | 526 | 2026-05-12 |

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 Hamming swarm addresses queried against Aptos mainnet.
Result: all addresses returned `null` for `CoinStore<AptosCoin>` resource.
Interpretation: accounts have no APT balance or CoinStore resource not initialized.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| A | `0x8699edc0...aebe9d7a` | null (no resource) |
| B | `0x3f892ebe...4577cb13` | null (no resource) |
| C | `0x38b99e63...2691535e` | null (no resource) |
| D | `0xf7765624...d9fcfdd1` | null (no resource) |
| E | `0xdc1d9d53...d0958d36` | null (no resource) |
| F | `0x18a14b5b...74c3cf71` | null (no resource) |
| G | `0x69a394c0...dbcc7f32` | null (no resource) |
| H | `0xce67c327...94e5300f` | null (no resource) |
| I | `0x070fe5d7...c00c1fc9` | null (no resource) |
| J | `0x4d964db8...93e87f54` | null (no resource) |
| K | `0xa732040a...7a425dc4` | null (no resource) |
| L | `0x7c2eaeaf...6337eba9` | null (no resource) |
| M | `0x6fed37a7...49b7f2e9` | null (no resource) |
| N | `0xe7dde6da...11551b2c` | null (no resource) |
| O | `0x73252b60...a525a89d` | null (no resource) |
| P | `0x6218792d...621ec948` | null (no resource) |
| Q | `0xac40fa50...5e5c89a9` | null (no resource) |
| R | `0x7ce605cc...36d76e10` | null (no resource) |
| S | `0xb8753014...f99d0386` | null (no resource) |
| T | `0x35781dc0...2d3f4588` | null (no resource) |
| U | `0x75860da4...95ef9956` | null (no resource) |
| V | `0xb59dd817...a89af2c3` | null (no resource) |
| W | `0x5f32aef7...a6ccc7b0` | null (no resource) |
| X | `0xa95cbbd1...be33047d` | null (no resource) |
| Y | `0xd8e32848...fa2444c4` | null (no resource) |
| Z | `0x7af0ef6e...6e4e197c` | null (no resource) |
| alice | `0xc793acde...d624cc7b` | null (no resource) |
| bob | `0x0a3c00c5...05512d5d` | null (no resource) |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428...f4987003` | 2 | YES |
| A-G | `0xf56c4a1c...3fbc0096` | 2 | YES |
| S-T | `0x3b1c3ae9...3ded7883` | 2 | YES |
| V-W | `0x40fad7b4...2c80eb6d` | 2 | YES |
| Y-Z | `0xd3ffe181...8e75b883` | 2 | YES |

### MNX Markets (testnet.mnx.fi)

Site is a Next.js SPA — no embedded market data available via HTTP fetch.
Status: **unavailable** (SPA requires JS execution to hydrate market data).

## DuckDB Schema

Location: `packages/world-increment/ducklake/world-increments.duckdb`

Tables:
- `world_increments` — GF(3) colored event log (391 rows)
- `repo_snapshots` — full repo metadata (391 rows)
- `aptos_snapshots` — Hamming swarm wallet balances (28 rows)
- `multisig_probes` — Aptos multisig contract health (5 rows)
- `mnx_snapshots` — MNX market data (0 rows — SPA unavailable)