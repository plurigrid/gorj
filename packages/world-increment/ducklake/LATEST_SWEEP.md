# World Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-05-03 (sweep completed)

---

## GitHub Social Graph Sweep

### Orgs/Users Scanned
- **Orgs:** plurigrid, kubeflow (0 public repos returned), TeglonLabs
- **Users:** bmorphism, zubyul
- **Zubyul social graph:** migalkin, DJedamski (0 public repos), wasita (0 public repos), kristinezheng (0 public repos), M1shaaa, AustinCStone (0 public repos)

### Total Repos Collected: 57

### Breakdown by Org/User

| Org/User | Type | Repos Captured |
|---|---|---|
| plurigrid | org | 20 |
| TeglonLabs | org | 9 |
| bmorphism | user | 10 |
| zubyul | user | 8 |
| migalkin | user | 6 |
| M1shaaa | user | 4 |

### Top Repos by Stars

| Rank | Repo | Stars |
|---|---|---|
| 1 | migalkin/NodePiece | 143 |
| 2 | migalkin/StarE | 89 |
| 3 | bmorphism/ocaml-mcp-sdk | 60 |
| 4 | migalkin/kgcourse2021 | 25 |
| 5 | plurigrid/asi | 17 |
| 6 | migalkin/NBFNet_mlx | 10 |
| 7 | plurigrid/ontology | 7 |
| 8 | migalkin/RWL | 7 |
| 9 | bmorphism/shitcoin | 5 |
| 10 | plurigrid/asi-skills | 3 |

---

## Aptos Hamming Snapshot

All 28 addresses queried against `fullnode.mainnet.aptoslabs.com`. All accounts returned resource-not-found — accounts appear to be unfunded or non-existent on Aptos mainnet.

| Label | Address (truncated) | Balance APT |
|---|---|---|
| alice | 0xc793...cc7b | NULL |
| bob | 0x0a3c...2d5d | NULL |
| A | 0x8699...9d7a | NULL |
| B | 0x3f89...b13 | NULL |
| C | 0x38b9...535e | NULL |
| D | 0xf776...fdd1 | NULL |
| E | 0xdc1d...8d36 | NULL |
| F | 0x18a1...f71 | NULL |
| G | 0x69a3...f32 | NULL |
| H | 0xce67...300f | NULL |
| I | 0x070f...1fc9 | NULL |
| J | 0x4d96...7f54 | NULL |
| K | 0xa732...5dc4 | NULL |
| L | 0x7c2e...ba9 | NULL |
| M | 0x6fed...f2e9 | NULL |
| N | 0xe7dd...1b2c | NULL |
| O | 0x7325...a89d | NULL |
| P | 0x6218...c948 | NULL |
| Q | 0xac40...89a9 | NULL |
| R | 0x7ce6...6e10 | NULL |
| S | 0xb875...0386 | NULL |
| T | 0x3578...4588 | NULL |
| U | 0x7586...9956 | NULL |
| V | 0xb59d...f2c3 | NULL |
| W | 0x5f32...c7b0 | NULL |
| X | 0xa95c...047d | NULL |
| Y | 0xd8e3...44c4 | NULL |
| Z | 0x7af0...197c | NULL |

**Total APT across all addresses: 0 (all accounts not found on mainnet)**

---

## Multisig Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

**All 5 multisig contracts healthy (sigs_required=2 > 0)**

---

## MNX Markets

Status: **Unavailable via API**

Probed endpoints:
- `https://testnet.mnx.fi/api/markets` — returned HTML (Next.js SPA)
- `https://testnet.mnx.fi/api/v1/markets` — returned HTML (Next.js SPA)
- `https://testnet.mnx.fi` — rendered JavaScript frontend, no public JSON API

No machine-readable market data available.

---

## GF(3) Color Chain Statistics

Applied to 57 world increment records (id % 3):

| GF3 Name | Trit | Color | Count |
|---|---|---|---|
| ERGODIC | 0 | #d3869b | 19 |
| PLUS | +1 | #b8bb26 | 19 |
| MINUS | -1 | #cc241d | 19 |

**Perfect balance: 19 ERGODIC + 19 PLUS + 19 MINUS = 57 total**

---

## Database Location

`packages/world-increment/ducklake/world-increments.duckdb`

Tables:
- `world_increments` — 57 rows (GF3 color chain over repo events)
- `repo_snapshots` — 57 rows (full repo metadata)
- `aptos_snapshots` — 28 rows (all NULL balances)
- `multisig_probes` — 5 rows (all healthy, sigs=2)
- `mnx_snapshots` — 1 row (unavailable marker)

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
