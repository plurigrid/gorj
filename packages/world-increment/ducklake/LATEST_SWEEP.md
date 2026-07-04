# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-04  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources

| Source | Type | Repos |
|--------|------|------:|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| AustinCStone | social | 40 |
| wasita | social | 11 |
| DJedamski | social | 6 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| **TOTAL** | | **391** |

### Top Languages (repo_snapshots)

| Language | Count |
|----------|------:|
| Python | 81 |
| JavaScript | 26 |
| Rust | 26 |
| TypeScript | 22 |
| HTML | 17 |
| Go | 15 |
| Jupyter Notebook | 15 |
| Clojure | 12 |
| Julia | 9 |
| Jsonnet | 7 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|------:|
| 0 | `#d3869b` | ERGODIC | 130 |
| 1 | `#b8bb26` | PLUS | 131 |
| -1 | `#cc241d` | MINUS | 130 |

### Notable Recent Activity

- **TeglonLabs/jank-crane** (C++) — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence" — pushed 2026-06-08
- **TeglonLabs/mathpix-gem** (Ruby) — "Transform mathematical images to LaTeX" — 2 stars, 11 open issues
- **M1shaaa/M1shaaa** — profile config updated 2026-07-03 (yesterday)
- **kristinezheng/kristinezheng.github.io** (HTML) — pushed 2026-07-01
- **wasita/wasita.github.io** (Svelte) — pushed 2026-07-02

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (26 worlds + alice + bob)

All 28 addresses returned **Resource not found** from the Aptos mainnet CoinStore resource. These wallets have not been initialized with an APT CoinStore on mainnet.

| Status | Count |
|--------|------:|
| Uninitialized (no CoinStore) | 28 |
| Active balance | 0 |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** and returned `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | `0x0da4f428...987003` | 2 | ✓ |
| A-G | `0xf56c4a1c...c0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181...b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9...7883` | 2 | ✓ |
| V-W | `0x40fad7b4...eb6d` | 2 | ✓ |

**5/5 multisig contracts healthy. All are 2-of-2 threshold.**

### MNX Markets (testnet.mnx.fi)

All probed API paths (`/api/markets`, `/api/tickers`, `/api/v1/markets`, `/api/v2/markets`) returned **Authentication Required**. Market data unavailable without credentials.

---

## DuckDB Schema Summary

```
world_increments  391 rows  GF3-colored repo snapshot increments
repo_snapshots    391 rows  Full repo metadata (language/stars/forks/issues)
aptos_snapshots    28 rows  Hamming swarm wallet states (mainnet)
multisig_probes     5 rows  On-chain 2-of-2 multisig health
mnx_snapshots       1 row   MNX testnet stub (auth_required)
```

---

## Conclusions

- **391 GitHub repos** snapshotted across 11 sources (3 orgs + 2 direct users + 6 social-graph nodes)
- **GF(3) chain** balanced: 130 ERGODIC / 131 PLUS / 130 MINUS
- **Aptos swarm**: 28 addresses probed, all uninitialized on mainnet (no APT CoinStore resource found)
- **Multisig health**: 5/5 contracts live with 2-of-2 threshold — swarm coordination layer intact
- **MNX testnet**: auth-gated, no public market data accessible
