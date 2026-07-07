# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-07T00:00:00Z  
**GF(3) Color Chain:** ERGODIC (#d3869b) → PLUS (#b8bb26) → MINUS (#cc241d)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| wasita | social | 11 |
| AustinCStone | social | 40 |
| DJedamski | social | 6 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| **Total** | | **392** |

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,769 | — |
| kubeflow/pipelines | 4,169 | Python |
| kubeflow/spark-operator | 3,132 | Python |
| kubeflow/trainer | 2,129 | Go |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| TeglonLabs/mathpix-gem | 2 | Ruby |

### Notable TeglonLabs Repos
- **jank-crane** (C++, pushed 2026-06-08): crane-jank converged-IR hub — loopify pass spec, GF3 convergence maps
- **mathpix-gem** (Ruby, 2★): Mathematical image → LaTeX OCR gem
- **coin-flip-mcp** (JS, 2 forks): MCP server with random.org entropy

### DuckDB Storage
- `world_increments`: 343 rows (GF3 color-chained)
- `repo_snapshots`: 1,264 rows

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets queried at `fullnode.mainnet.aptoslabs.com`. CoinStore resource absent → 0.0 APT for all.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...9a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Note:** All wallets return no `CoinStore<AptosCoin>` resource — accounts exist on-chain but hold no liquid APT.

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

All multisig accounts require **2-of-N** signatures. All contracts are healthy and responsive.

### MNX Markets

`https://testnet.mnx.fi` is behind **Vercel authentication** — no API endpoints accessible without a bypass token or OIDC credential. Market data unavailable for this sweep.

### DuckDB Storage
- `aptos_snapshots`: 28 rows
- `multisig_probes`: 5 rows  
- `mnx_snapshots`: 1 row (unavailable placeholder)

---

## GF(3) Chain Summary

Total world-increments written: **343**  
- Trit=0 ERGODIC (#d3869b): 115 entries  
- Trit=+1 PLUS (#b8bb26): 114 entries  
- Trit=-1 MINUS (#cc241d): 114 entries  

Database: `packages/world-increment/ducklake/world-increments.duckdb`
