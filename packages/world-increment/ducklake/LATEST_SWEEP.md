# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-05

## Sweep Metadata

| Field | Value |
|-------|-------|
| **Date** | 2026-05-05 |
| **Agent** | world-increment-sweep + hamming-swarm-snapshot |
| **DuckDB** | v1.2.x |
| **Database** | `packages/world-increment/ducklake/world-increments.duckdb` |

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 336 |
| Total Repo Snapshots | 336 |
| Orgs Covered | plurigrid (100), kubeflow (47), TeglonLabs (4) |
| Primary Users | bmorphism (100), zubyul (49) |
| Social Graph Users | migalkin (6), DJedamski (6), wasita (6), kristinezheng (6), M1shaaa (6), AustinCStone (6) |

### Source Breakdown

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 47 |
| migalkin | user_social | 6 |
| DJedamski | user_social | 6 |
| wasita | user_social | 6 |
| kristinezheng | user_social | 6 |
| M1shaaa | user_social | 6 |
| AustinCStone | user_social | 6 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **336** |

### GF(3) Color Chain — First 15 Increments

| ID | Source | Repo | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1 | plurigrid | zig-syrup | +1 | `#b8bb26` | **PLUS** |
| 2 | plurigrid | asi | -1 | `#cc241d` | **MINUS** |
| 3 | plurigrid | nash-portal | 0 | `#d3869b` | **ERGODIC** |
| 4 | plurigrid | horse | +1 | `#b8bb26` | **PLUS** |
| 5 | plurigrid | asi-skills | -1 | `#cc241d` | **MINUS** |
| 6 | plurigrid | bci-blue-share | 0 | `#d3869b` | **ERGODIC** |
| 7 | plurigrid | nanoclj-zig | +1 | `#b8bb26` | **PLUS** |
| 8 | plurigrid | spi-race | -1 | `#cc241d` | **MINUS** |
| 9 | plurigrid | reafference | 0 | `#d3869b` | **ERGODIC** |
| 10 | plurigrid | gorj | +1 | `#b8bb26` | **PLUS** |
| 11 | plurigrid | web-browser | -1 | `#cc241d` | **MINUS** |
| 12 | plurigrid | vivarium | 0 | `#d3869b` | **ERGODIC** |
| 13 | plurigrid | flowglad-rs | +1 | `#b8bb26` | **PLUS** |
| 14 | plurigrid | tree-sitter-nanoclj-zig | -1 | `#cc241d` | **MINUS** |
| 15 | plurigrid | forester | 0 | `#d3869b` | **ERGODIC** |

GF(3) distribution: **112 PLUS** / **112 MINUS** / **112 ERGODIC** — perfectly balanced across 336 increments.

### Top Repos by Stars

| Repo | Language | Stars |
|------|----------|-------|
| kubeflow/kubeflow | — | 15,622 |
| kubeflow/pipelines | Python | 4,132 |
| kubeflow/spark-operator | Python | 3,123 |
| kubeflow/trainer | Go | 2,096 |
| kubeflow/katib | Python | 1,683 |
| kubeflow/examples | Jsonnet | 1,460 |
| kubeflow/manifests | YAML | 1,015 |
| migalkin/NodePiece | Python | 143 |
| AustinCStone/TextGAN | Python | 92 |
| migalkin/StarE | Python | 89 |

### Notable Social Graph Activity

- **migalkin**: Knowledge graph researcher — NodePiece (ICLR'22, 143★), StarE (EMNLP'20, 89★), NBFNet_mlx (Apple Silicon)
- **wasita**: Active Svelte developer; magic-garden bot pushed 2026-04-22, personal site pushed 2026-04-28
- **AustinCStone**: ML/CV; `bmfork` (May 2025) and `bitmind-fork` (Jan 2025) indicate plurigrid adjacency
- **DJedamski**: Data science / Kaggle focus (R, Jupyter)
- **kristinezheng**: Cognitive science / MIT (lookit studies, HackMIT 2021)
- **M1shaaa**: Yale CS / cognitive science (lookit studies, TypeScript lab bookshelf)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Probed 28 wallets via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~5,146,502,279.

**Result:** All 28 addresses returned `resource_not_found`. No APT CoinStore is registered on any wallet — these wallets have not been initialized with APT on mainnet.

| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|---------------|--------|
| alice | 0xc793...cc7b | 0.00000000 | resource_not_found |
| bob | 0x0a3c...2d5d | 0.00000000 | resource_not_found |
| A | 0x8699...9d7a | 0.00000000 | resource_not_found |
| B | 0x3f89...b13 | 0.00000000 | resource_not_found |
| C | 0x38b9...35e | 0.00000000 | resource_not_found |
| D | 0xf776...dd1 | 0.00000000 | resource_not_found |
| E | 0xdc1d...d36 | 0.00000000 | resource_not_found |
| F | 0x18a1...f71 | 0.00000000 | resource_not_found |
| G | 0x69a3...f32 | 0.00000000 | resource_not_found |
| H | 0xce67...00f | 0.00000000 | resource_not_found |
| I | 0x070f...c9 | 0.00000000 | resource_not_found |
| J | 0x4d96...f54 | 0.00000000 | resource_not_found |
| K | 0xa732...dc4 | 0.00000000 | resource_not_found |
| L | 0x7c2e...ba9 | 0.00000000 | resource_not_found |
| M | 0x6fed...e9 | 0.00000000 | resource_not_found |
| N | 0xe7dd...2c | 0.00000000 | resource_not_found |
| O | 0x7325...89d | 0.00000000 | resource_not_found |
| P | 0x6218...948 | 0.00000000 | resource_not_found |
| Q | 0xac40...a9 | 0.00000000 | resource_not_found |
| R | 0x7ce6...e10 | 0.00000000 | resource_not_found |
| S | 0xb875...386 | 0.00000000 | resource_not_found |
| T | 0x3578...588 | 0.00000000 | resource_not_found |
| U | 0x7586...956 | 0.00000000 | resource_not_found |
| V | 0xb59d...2c3 | 0.00000000 | resource_not_found |
| W | 0x5f32...7b0 | 0.00000000 | resource_not_found |
| X | 0xa95c...47d | 0.00000000 | resource_not_found |
| Y | 0xd8e3...4c4 | 0.00000000 | resource_not_found |
| Z | 0x7af0...97c | 0.00000000 | resource_not_found |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...987003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a1c...c0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe181...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | ✅ HEALTHY |

All 5 multisig accounts are live on Aptos mainnet, each requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

| Field | Value |
|-------|-------|
| **Status** | UNAVAILABLE via REST |
| **Root URL** | `testnet.mnx.fi` — Next.js SPA, last deployed 2026-04-28 |
| **REST API** | All paths return 404 (Express "Cannot GET") |
| **WebSocket** | `wss://api.testnet.mnx.fi` — live but requires WS client |
| **Data** | 0 rows in `mnx_snapshots` |

The MNX frontend CSP reveals it connects to `api.testnet.mnx.fi` via WebSocket. REST probing of all common market endpoints was exhausted without data return.

---

## DuckDB Schema & Row Counts

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 336 | GF(3)-tagged world-state events |
| `repo_snapshots` | 336 | GitHub repo metadata snapshots |
| `aptos_snapshots` | 28 | Hamming swarm wallet readings |
| `multisig_probes` | 5 | Multisig sigs_required probes |
| `mnx_snapshots` | 0 | MNX market data (unavailable) |

## GF(3) Assignment Rule
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
