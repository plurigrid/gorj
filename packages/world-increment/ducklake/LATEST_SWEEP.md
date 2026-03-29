# World Increment Sweep + Hamming Swarm Snapshot

**Date/Time:** 2026-03-29 UTC  
**Snapshot Hash:** b7cfc25aea7060191a6d95d12a927fb3  

---

## GitHub Social Graph Sweep

### Repo Snapshot Counts per Source

| Source | Type | Repo Count |
|--------|------|-----------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 46 |
| AustinCStone | user (zubyul graph) | 43 |
| migalkin | user (zubyul graph) | 30 |
| wasita | user (zubyul graph) | 28 |
| zubyul | user | 23 |
| kristinezheng | user (zubyul graph) | 18 |
| M1shaaa | user (zubyul graph) | 16 |
| DJedamski | user (zubyul graph) | 11 |
| **TOTAL** | | **468** |

Events queried: bmorphism (30 events), zubyul (30 events)

---

## Aptos Wallet Balances

All 26 addresses probed on Aptos Mainnet. APT CoinStore resource returned 0 for all addresses (accounts have no APT coin store or zero balance at time of sweep).

| World | Address (truncated) | APT Balance |
|-------|-------------------|-------------|
| A | 0xc793...c7b | 0.0 |
| B | 0x0a3c...12d | 0.0 |
| C | 0x8699...d7a | 0.0 |
| D | 0x3f89...b13 | 0.0 |
| E | 0x38b9...35e | 0.0 |
| F | 0xf776...dd1 | 0.0 |
| G | 0xdc1d...d36 | 0.0 |
| H | 0x18a1...f71 | 0.0 |
| I | 0x69a3...f32 | 0.0 |
| J | 0xce67...00f | 0.0 |
| K | 0x070f...c9 | 0.0 |
| L | 0x4d96...f54 | 0.0 |
| M | 0xa732...dc4 | 0.0 |
| N | 0x7c2e...ba9 | 0.0 |
| O | 0x6fed...2e9 | 0.0 |
| P | 0xe7dd...b2c | 0.0 |
| Q | 0x7325...89d | 0.0 |
| R | 0x6218...948 | 0.0 |
| S | 0xac40...a9 | 0.0 |
| T | 0x7ce6...e10 | 0.0 |
| U | 0xb875...386 | 0.0 |
| V | 0x3578...588 | 0.0 |
| W | 0x7586...956 | 0.0 |
| X | 0xb59d...2c3 | 0.0 |
| Y | 0x5f32...b0 | 0.0 |
| Z | 0xa95c...47d | 0.0 |

---

## Multisig Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|-------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

All multisig contracts are healthy (sigs_required=2 > 0).

---

## MNX Markets

**Status: UNAVAILABLE**  
Endpoints tried:
- `https://testnet.mnx.fi/api/markets` → HTML response (Next.js frontend, no JSON API)
- `https://testnet.mnx.fi/api/v1/markets` → HTML response
- `https://testnet.mnx.fi/api/tickers` → HTML response

MNX testnet API does not expose a JSON REST endpoint at the probed paths.

---

## GF(3) Color Chain Summary

| Trit | Color | Name | Count in world_increments |
|------|-------|------|--------------------------|
| 0 | #d3869b | ERGODIC | 3 |
| 1 | #b8bb26 | PLUS | 10 |
| -1 | #cc241d | MINUS | 8 |

GF(3) rule: `id%3==0 → trit=0 ERGODIC #d3869b`, `id%3==1 → trit=1 PLUS #b8bb26`, `id%3==2 → trit=-1 MINUS #cc241d`

---

## DuckDB Tables

| Table | Row Count |
|-------|-----------|
| world_increments | 21 |
| repo_snapshots | 468 |
| aptos_snapshots | 26 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

Database: `packages/world-increment/ducklake/sweep.db`
