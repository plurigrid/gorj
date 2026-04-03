# World-Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-04-03T12:26:41Z

---

## JOB 1: GitHub Social Graph Sweep

### Repos Fetched Per Source

| Source | Type | Repo Count |
|--------|------|-----------|
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 46 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 23 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |

> Note: `plurigrid` org API returned rate-limit error (unauthenticated); 0 repos fetched for that source.
> Total repos indexed: 369

### Top 10 Repos by Stars

| Source | Repo | Language | Stars | Forks |
|--------|------|----------|-------|-------|
| kubeflow | kubeflow | N/A | 15551 | 2628 |
| kubeflow | pipelines | Python | 4118 | 1983 |
| kubeflow | spark-operator | Python | 3110 | 1480 |
| kubeflow | trainer | Go | 2072 | 942 |
| kubeflow | katib | Python | 1674 | 519 |
| kubeflow | examples | Jsonnet | 1459 | 755 |
| kubeflow | manifests | YAML | 1007 | 1068 |
| kubeflow | arena | Go | 809 | 190 |
| kubeflow | kale | Python | 681 | 156 |
| kubeflow | mpi-operator | Go | 519 | 236 |

### GF(3) Color Chain Summary (world_increments)

| GF3 Name | Color | Count |
|----------|-------|-------|
| PLUS | #b8bb26 | 7 |
| MINUS | #cc241d | 7 |
| ERGODIC | #d3869b | 7 |

### Recent Events (bmorphism, zubyul)
Captured top 5 public events each: PushEvent, PullRequestEvent, CreateEvent, etc.
See `world_increments` table where `source_type='event'`.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793acde...24cc7b | 0.43643352 |
| bob | 0x0a3c00c5...512d5d | 12.65700700 |
| A | 0x8699edc0...be9d7a | 0.05176700 |
| B | 0x3f892ebe...77cb13 | 0.03625600 |
| C | 0x38b99e63...91535e | 0.01018500 |
| D | 0xf7765624...fcfdd1 | 0.01162900 |
| E | 0xdc1d9d53...958d36 | 0.01256100 |
| F | 0x18a14b5b...c3cf71 | 1.96051600 |
| G | 0x69a394c0...cc7f32 | 0.00068100 |
| H | 0xce67c327...e5300f | 0.00068100 |
| I | 0x070fe5d7...0c1fc9 | 0.00068100 |
| J | 0x4d964db8...e87f54 | 1.89509300 |
| K | 0xa732040a...425dc4 | 0.16196100 |
| L | 0x7c2eaeaf...37eba9 | 1.92726900 |
| M | 0x6fed37a7...b7f2e9 | 0.11228500 |
| N | 0xe7dde6da...551b2c | 0.10612100 |
| O | 0x73252b60...25a89d | 0.21013600 |
| P | 0x6218792d...1ec948 | 0.14013600 |
| Q | 0xac40fa50...5c89a9 | 0.10324000 |
| R | 0x7ce605cc...d76e10 | 0.09021700 |
| S | 0xb8753014...9d0386 | 0.09178800 |
| T | 0x35781dc0...3f4588 | 0.07371300 |
| U | 0x75860da4...ef9956 | 0.05577300 |
| V | 0xb59dd817...9af2c3 | 0.04783299 |
| W | 0x5f32aef7...ccc7b0 | 0.04070500 |
| X | 0xa95cbbd1...33047d | 0.04257700 |
| Y | 0xd8e32848...2444c4 | 0.04444900 |
| Z | 0x7af0ef6e...4e197c | 0.02326800 |

**Total APT across all wallets: 20.34496151 APT**

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428...987003 | 2 | YES |
| A-G | 0xf56c4a1c...bc0096 | 2 | YES |
| Y-Z | 0xd3ffe181...75b883 | 2 | YES |
| S-T | 0x3b1c3ae9...ed7883 | 2 | YES |
| V-W | 0x40fad7b4...80eb6d | 2 | YES |

All 5 multisig contracts probed. All report `num_signatures_required = 2` and are healthy.

### MNX Markets Status

- `https://testnet.mnx.fi/api/markets` → **HTTP 404** (page not found)
- `https://api.testnet.mnx.fi` → **deployment not found** (Vercel deployment unavailable)
- MNX testnet API is currently **UNAVAILABLE**. No market data captured.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 105 |
| repo_snapshots | 369 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

DB location: `packages/world-increment/ducklake/world-increments.duckdb`
