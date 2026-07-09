# LATEST_SWEEP — 2026-07-09

Generated: 2026-07-09T09:13:50Z
Agent: world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned

| Source Type | Source | Repos Captured |
|---|---|---|
| org | plurigrid | 50 |
| org | kubeflow | 30 |
| org | TeglonLabs | 5 |
| user | bmorphism | 50 |
| user | zubyul | 30 |
| user | migalkin | 19 |
| user | AustinCStone | 20 |
| user | wasita | 11 |
| user | kristinezheng | 5 |
| user | M1shaaa | 8 |
| user | DJedamski | 6 |

**Total repo entries this sweep:** ~234 sources across 11 orgs/users

### Top Repos by Stars (this sweep)

| Full Name | Stars | Language | Open Issues |
|---|---|---|---|
| kubeflow/kubeflow | 15,768 | — | 0 |
| kubeflow/pipelines | 4,169 | Python | 421 |
| kubeflow/spark-operator | 3,136 | Python | 106 |
| kubeflow/trainer | 2,134 | Go | 148 |
| kubeflow/katib | 1,689 | Python | 111 |
| kubeflow/community-distribution | 1,029 | YAML | 27 |
| kubeflow/arena | 815 | Go | 47 |
| kubeflow/examples | 1,460 | Jsonnet | 111 |
| migalkin/NodePiece | 144 | Python | 0 |
| migalkin/StarE | 89 | Python | 1 |
| AustinCStone/TextGAN | 92 | Python | 5 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 0 |
| plurigrid/asi | 30 | HTML | 4 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 1 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 1 |

### GF(3) World Increment Chain (this sweep)

| Increment | Source | GF3 Trit | Color | Name |
|---|---|---|---|---|
| +1 | plurigrid | 0 | #d3869b | ERGODIC |
| +2 | kubeflow | 1 | #b8bb26 | PLUS |
| +3 | TeglonLabs | -1 | #cc241d | MINUS |
| +4 | bmorphism | 0 | #d3869b | ERGODIC |
| +5 | zubyul | 1 | #b8bb26 | PLUS |
| +6 | migalkin | -1 | #cc241d | MINUS |
| +7 | AustinCStone | 0 | #d3869b | ERGODIC |
| +8 | wasita | 1 | #b8bb26 | PLUS |
| +9 | kristinezheng | -1 | #cc241d | MINUS |
| +10 | M1shaaa | 0 | #d3869b | ERGODIC |
| +11 | DJedamski | 1 | #b8bb26 | PLUS |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 hamming-swarm addresses (alice, bob, A–Z) were probed against
`fullnode.mainnet.aptoslabs.com`. Accounts **exist** (verified via sequence_number)
but the `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource is not
initialized, indicating 0 APT balance / accounts not yet funded on mainnet.

| World | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

**Status:** All 28 accounts on Aptos mainnet. CoinStore not initialized → 0 APT.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...003 | 2 | ✅ |
| A-G | 0xf56c...096 | 2 | ✅ |
| Y-Z | 0xd3ff...883 | 2 | ✅ |
| S-T | 0x3b1c...883 | 2 | ✅ |
| V-W | 0x40fa...b6d | 2 | ✅ |

**Status:** All 5 multisig accounts healthy — 2-of-2 required signatures each.

### MNX Markets (`testnet.mnx.fi`)

All probed API paths (`/api/markets`, `/api/v1/markets`, `/markets`, `/api/tokens`,
`/api/tickers`) returned **HTTP 401 Unauthorized**. The SPA loads over TLS but
market data APIs require authentication. No market data captured.

**Status:** UNAVAILABLE — auth required.

---

## DuckDB Tables (cumulative)

| Table | Rows |
|---|---|
| world_increments | 33+ |
| repo_snapshots | 1001+ |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

DB: `packages/world-increment/ducklake/world-increments.duckdb`
