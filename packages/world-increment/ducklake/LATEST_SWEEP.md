# World-Increment Sweep + Hamming Snapshot

**Sweep Date/Time:** 2026-04-07T00:00:00Z (automated sweep)

---

## Job 1: GitHub Social Graph Sweep

### Orgs and Users Queried

| Source | Type | Repos Collected |
|--------|------|-----------------|
| plurigrid | org | 100 |
| kubeflow | org | 46 |
| TeglonLabs | org | 53 |
| bmorphism | user | 100 |
| zubyul | user | 23 |
| migalkin | user (social graph) | 30 |
| DJedamski | user (social graph) | 11 |
| wasita | user (social graph) | 29 |
| kristinezheng | user (social graph) | 18 |
| M1shaaa | user (social graph) | 16 |
| AustinCStone | user (social graph) | 43 |

**Total repos collected: 469**

### Top 10 Repos by Stars

| Org/User | Full Name | Language | Stars | Forks |
|----------|-----------|----------|-------|-------|
| kubeflow | kubeflow/kubeflow | - | 15554 | 2627 |
| kubeflow | kubeflow/pipelines | Python | 4118 | 1983 |
| kubeflow | kubeflow/spark-operator | Python | 3111 | 1481 |
| kubeflow | kubeflow/trainer | Go | 2074 | 943 |
| kubeflow | kubeflow/katib | Python | 1674 | 522 |
| kubeflow | kubeflow/examples | Jsonnet | 1459 | 755 |
| kubeflow | kubeflow/manifests | YAML | 1009 | 1069 |
| kubeflow | kubeflow/arena | Go | 808 | 190 |
| kubeflow | kubeflow/kale | Python | 682 | 156 |
| kubeflow | kubeflow/mpi-operator | Go | 519 | 236 |

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
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
| Z | 0x7af0...97c | 0.0 |

Note: All 28 addresses returned 0.0 APT balance (accounts may not have CoinStore resources initialized on mainnet).

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

All 5 multisig contracts are **healthy** (2-of-N signatures required).

### MNX Markets

**Status: unavailable**

`testnet.mnx.fi` returns a Next.js SPA (HTML) at all probed endpoints (`/api/markets`, `/api/v1/markets`, `/`). No structured JSON market data was accessible via direct API calls.

---

## GF3 Color Chain Note

Each repo snapshot row is assigned a GF(3) field element based on `id % 3`:
- `id % 3 == 0` -> trit=0, color=**ERGODIC** (#d3869b)
- `id % 3 == 1` -> trit=1, color=**PLUS** (#b8bb26)
- `id % 3 == 2` -> trit=-1, color=**MINUS** (#cc241d)

469 total rows distributed across the GF(3) chain:
- ERGODIC (trit=0): 156 rows
- PLUS (trit=1): 157 rows
- MINUS (trit=-1): 156 rows

---

## Database

- Path: `packages/world-increment/ducklake/world-increments.duckdb`
- Tables: `world_increments` (469), `repo_snapshots` (469), `aptos_snapshots` (28), `multisig_probes` (5), `mnx_snapshots` (0 - unavailable)
