# World-Increment Sweep + Hamming Snapshot

**Sweep Date/Time:** 2026-03-30 09:30 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Repos Discovered Per Org/User

| Org/User | Repos | Max Stars | Top Repo by Stars |
|---|---|---|---|
| bmorphism | 97 | 60 | ocaml-mcp-sdk |
| plurigrid | 93 | 13 | asi |
| kubeflow | 46 | 15,541 | kubeflow |
| zubyul | 44 | 2 | jonikas_lab_data_analysis_misc |
| AustinCStone | 40 | 92 | TextGAN |
| migalkin | 19 | 143 | NodePiece |
| wasita | 9 | 1 | magic-garden |
| M1shaaa | 8 | 0 | M1shaaa |
| kristinezheng | 6 | 0 | kristinezheng.github.io |
| DJedamski | 6 | 1 | Kaggle |
| TeglonLabs | 3 | 2 | mathpix-gem |

**Total unique repos ingested:** 371

Notable: kubeflow/kubeflow has 15,541 stars. migalkin's NodePiece (graph ML) has 143 stars. AustinCStone's TextGAN has 92 stars. bmorphism's ocaml-mcp-sdk has 60 stars.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 wallets queried against Aptos mainnet. All returned 0.0 APT (no CoinStore<AptosCoin> resource active).

| World | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...d7a | 0.0 |
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
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts responded with `num_signatures_required = 2` — all healthy.

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...003 | 2 | true |
| A-G | 0xf56c...096 | 2 | true |
| Y-Z | 0xd3ff...883 | 2 | true |
| S-T | 0x3b1c...883 | 2 | true |
| V-W | 0x40fa...b6d | 2 | true |

### MNX Markets Status

**UNAVAILABLE** - `https://testnet.mnx.fi/api/markets` returns HTML (Next.js SPA) rather than a JSON API. The testnet frontend is live but no machine-readable market data endpoint is accessible. No records inserted into mnx_snapshots.

---

## GF(3) Color Chain Summary

GF(3) field assigns each world-increment a trit value cycling ERGODIC(0) -> PLUS(1) -> MINUS(-1):

| GF3 Name | Trit | Color | Hex | Count |
|---|---|---|---|---|
| ERGODIC | 0 | Pink/Rose | #d3869b | 124 |
| PLUS | 1 | Yellow-Green | #b8bb26 | 124 |
| MINUS | -1 | Red | #cc241d | 123 |

**Total world-increments stored: 371**

## GF(3) Assignment Rule
- `id mod 3 == 0` -> trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` -> trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` -> trit=-1, color=#cc241d, name=MINUS

---

## Database

- Location: `packages/world-increment/ducklake/world-increments.duckdb`
- Tables: `world_increments` (371), `repo_snapshots` (371), `aptos_snapshots` (28), `multisig_probes` (5), `mnx_snapshots` (0)
- Engine: DuckDB v1.5.1 (Variegata)

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)

multisig_probes(timestamp, pair, address, sigs_required, healthy)

mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```
