# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-26
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 8 (recent) |
| kubeflow | org | 5 (recent) |
| TeglonLabs | org | 4 |
| bmorphism | user | 6 (recent) |
| zubyul | user | 3 (recent) |
| migalkin | social graph | 2 (notable) |
| DJedamski | social graph | 1 |
| kristinezheng | social graph | 1 |
| M1shaaa | social graph | 1 |
| AustinCStone | social graph | 1 |
| **Total** | | **32 repo snapshots** |

### Notable Repos (by stars)
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,600 | - | 2026-01-05 |
| kubeflow/pipelines | 4,125 | Python | 2026-04-26 |
| kubeflow/spark-operator | 3,120 | Python | 2026-04-24 |
| kubeflow/trainer | 2,092 | Go | 2026-04-25 |
| migalkin/NodePiece | 143 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| plurigrid/asi | 17 | HTML | 2026-04-26 |

### GF(3) Color Chain Summary
- **ERGODIC** (`#d3869b`, trit=0): ids 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
- **PLUS** (`#b8bb26`, trit=1): ids 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31
- **MINUS** (`#cc241d`, trit=-1): ids 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)
All 28 addresses (alice, bob, A-Z) queried against Aptos mainnet
`/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.00 |
| bob | 0x0a3c...512d | 0.00 |
| A | 0x8699...d7a | 0.00 |
| B | 0x3f89...b13 | 0.00 |
| C | 0x38b9...35e | 0.00 |
| D | 0xf776...dd1 | 0.00 |
| E | 0xdc1d...d36 | 0.00 |
| F | 0x18a1...f71 | 0.00 |
| G | 0x69a3...f32 | 0.00 |
| H | 0xce67...00f | 0.00 |
| I | 0x070f...fc9 | 0.00 |
| J | 0x4d96...f54 | 0.00 |
| K | 0xa732...dc4 | 0.00 |
| L | 0x7c2e...ba9 | 0.00 |
| M | 0x6fed...2e9 | 0.00 |
| N | 0xe7dd...b2c | 0.00 |
| O | 0x7325...89d | 0.00 |
| P | 0x6218...948 | 0.00 |
| Q | 0xac40...89a9 | 0.00 |
| R | 0x7ce6...6e10 | 0.00 |
| S | 0xb875...386 | 0.00 |
| T | 0x3578...588 | 0.00 |
| U | 0x7586...956 | 0.00 |
| V | 0xb59d...2b3 | 0.00 |
| W | 0x5f32...b0 | 0.00 |
| X | 0xa95c...47d | 0.00 |
| Y | 0xd8e3...4c4 | 0.00 |
| Z | 0x7af0...97c | 0.00 |

All CoinStore resources returned 0 APT. Addresses exist on-chain but hold no native APT in their registered CoinStore.

### Multisig Contract Probes (5 pairs)
| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

All 5 multisig accounts are 2-of-2 and responding. Swarm is healthy.

### MNX Markets
`https://testnet.mnx.fi` - UNAVAILABLE. SPA with no accessible REST API endpoints.
`/api/markets` and `/api/v1/markets` both returned no data. No market data captured this sweep.

---

## DuckDB Schema Summary
```
world_increments  - 32 rows  (GF3 color chain over repo snapshots)
repo_snapshots    - 32 rows  (GitHub repo metadata)
aptos_snapshots   - 28 rows  (Hamming swarm wallet balances)
multisig_probes   -  5 rows  (on-chain multisig health)
mnx_snapshots     -  0 rows  (MNX unavailable this sweep)
```
