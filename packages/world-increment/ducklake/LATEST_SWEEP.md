# World-Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-04-07T00:00:00Z (sweep run date)

---

## Job 1: GitHub Social Graph Sweep

### Sources Queried

| Type | Name | Repos Found |
|------|------|-------------|
| org | plurigrid | 2 |
| org | kubeflow | 46 |
| org | TeglonLabs | 53 |
| user | bmorphism | 100 |
| user | zubyul | 2 |
| user | migalkin | 30 |
| user | DJedamski | 11 |
| user | wasita | 29 |
| user | kristinezheng | 18 |
| user | M1shaaa | 16 |
| user | AustinCStone | 2 |

**Total repos found:** 309 (distinct: 469 across all sources)
**Events queried:** bmorphism (30), zubyul (30)

### Top Repos by Stars

| Repo | Org/User | Stars | Language |
|------|----------|-------|----------|
| kubeflow/kubeflow | kubeflow | 15554 | — |
| kubeflow/pipelines | kubeflow | 4118 | Python |
| kubeflow/spark-operator | kubeflow | 3111 | Python |
| kubeflow/trainer | kubeflow | 2075 | Go |
| kubeflow/katib | kubeflow | 1674 | Python |
| kubeflow/examples | kubeflow | 1459 | Jsonnet |
| kubeflow/manifests | kubeflow | 1009 | YAML |
| kubeflow/arena | kubeflow | 808 | Go |
| kubeflow/kale | kubeflow | 682 | Python |
| kubeflow/mpi-operator | kubeflow | 519 | Go |

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

| World Label | Address (truncated) | Balance (APT) |
|-------------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A | 0x8699...b97a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

> All 28 addresses returned 0.0 APT (CoinStore resources returned zero balance on Aptos mainnet).

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

All 5 multisig contracts are healthy and require 2-of-N signatures.

### MNX Markets Status

**Status: Unavailable (SPA/HTML)**

`https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/tickers` both return a Next.js single-page application HTML rather than JSON API responses. No market data could be parsed.

---

## GF(3) Color Chain Stats

| GF3 Name | Color | Trit | Increment Count |
|----------|-------|------|-----------------|
| ERGODIC | #d3869b | 0 | 101 |
| PLUS | #b8bb26 | +1 | 101 |
| MINUS | #cc241d | -1 | 101 |

- **Total world_increments:** 303
- **Total repo_snapshots rows:** 772 (includes duplicate inserts across execution passes)
- **Distribution:** uniform across GF(3) — 101 per trit value

---

## Database Location

`packages/world-increment/ducklake/world-increments.duckdb`

Tables: `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`
