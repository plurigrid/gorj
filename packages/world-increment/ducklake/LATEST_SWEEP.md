# World-Increment Sweep + Hamming Snapshot — 2026-04-07

## Sweep Metadata
- **Date:** 2026-04-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Surveyed
| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | Org | 95 |
| kubeflow | Org | 46 |
| TeglonLabs | Org | 3 |
| bmorphism | User | 98 |
| zubyul | User | 19 |
| migalkin | User | 44 |
| DJedamski | User | 6 |
| wasita | User | 9 |
| kristinezheng | User | 6 |
| M1shaaa | User | 8 |
| AustinCStone | User | 40 |
| **TOTAL** | | **374** |

### Top Repos by Stars
| Repo | Language | Stars | Forks | Open Issues |
|------|----------|-------|-------|-------------|
| kubeflow/kubeflow | — | 15,556 | 2,627 | 0 |
| kubeflow/pipelines | Python | 4,118 | 1,983 | 467 |
| kubeflow/spark-operator | Python | 3,111 | 1,481 | 83 |
| kubeflow/trainer | Go | 2,075 | 943 | 152 |
| kubeflow/katib | Python | 1,674 | 522 | 118 |
| kubeflow/examples | Jsonnet | 1,458 | 755 | 111 |
| kubeflow/manifests | YAML | 1,009 | 1,069 | 28 |
| kubeflow/arena | Go | 808 | 190 | 66 |
| kubeflow/kale | Python | 682 | 156 | 56 |
| kubeflow/mpi-operator | Go | 520 | 236 | 101 |
| migalkin/NodePiece | Python | 143 | 21 | 0 |
| migalkin/StarE | Python | 88 | 16 | 1 |
| AustinCStone/TextGAN | Python | 92 | 30 | 5 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | 2 | 0 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 | 1 |
| plurigrid/asi | HTML | 16 | 5 | 3 |

### Stars by Org/User
| Org/User | Repos | Total Stars |
|----------|-------|-------------|
| kubeflow | 46 | 67,642 |
| migalkin | 44 | 277 |
| bmorphism | 98 | 378 |
| AustinCStone | 40 | 116 |
| plurigrid | 95 | 100 |
| zubyul | 19 | ~10 |
| TeglonLabs | 3 | 2 |
| DJedamski | 6 | 3 |
| wasita | 9 | 2 |
| M1shaaa | 8 | 0 |
| kristinezheng | 6 | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-04-07)
All 28 queried addresses returned **0 APT** balance via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (abbreviated) | Balance (APT) |
|-------|----------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes
All 5 multisig contracts are **healthy**: 2-of-N threshold confirmed via `0x1::multisig_account::num_signatures_required`.

| Pair | Contract Address | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428...987003 | 2 | YES |
| A-G | 0xf56c4a1c...c0096 | 2 | YES |
| Y-Z | 0xd3ffe181...b883 | 2 | YES |
| S-T | 0x3b1c3ae9...d7883 | 2 | YES |
| V-W | 0x40fad7b4...b6d | 2 | YES |

### MNX Market Data
- `https://testnet.mnx.fi/api/markets` → HTTP 404
- `https://api.mnx.fi/markets` → HTTP 404
- `https://mnx.fi/api/markets` → HTTP 200 but returns HTML (SPA, no machine-readable API)
- `https://testnet.mnx.fi/api/v1/markets` → HTTP 404

**MNX JSON API is unavailable.** The `mnx_snapshots` table is empty. MNX appears to be a frontend-only SPA without a public REST API.

---

## GF(3) Color Chain Summary
World increments are colored using GF(3) arithmetic on `id % 3`:

| id % 3 | Trit | Color | Name | Count |
|--------|------|-------|------|-------|
| 1 | +1 | `#b8bb26` | PLUS | 125 |
| 2 | -1 | `#cc241d` | MINUS | 125 |
| 0 | 0 | `#d3869b` | ERGODIC | 124 |

**Assignment rule:**
- `id mod 3 == 0` → trit=0, color=#d3869b (pink), name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26 (yellow-green), name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d (red), name=MINUS

GF(3) chain repeats: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...` (374 increments total)

---

## DuckDB Schema
```sql
world_increments  — 374 rows  (GF3-colored event log)
repo_snapshots    — 374 rows  (GitHub repo metadata)
aptos_snapshots   — 28 rows   (Hamming swarm wallet balances)
multisig_probes   — 5 rows    (Aptos multisig contract health)
mnx_snapshots     — 0 rows    (MNX API unavailable)
```
