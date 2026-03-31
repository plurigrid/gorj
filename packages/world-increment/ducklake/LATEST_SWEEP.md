# World Increment Sweep + Hamming Snapshot

**Sweep timestamp:** 2026-03-31T07:28Z
**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repos Swept Per Source

| Source | Type | Repos Collected |
|--------|------|-----------------|
| plurigrid | org | 100 |
| kubeflow | org | 46 |
| TeglonLabs | org | 53 |
| bmorphism | user | 100 |
| zubyul | user | 0 (no public repos / rate-limited) |
| migalkin | user | 30 |
| DJedamski | user | 0 (no public repos / rate-limited) |
| wasita | user | 28 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| AustinCStone | user | 43 |
| **Total** | | **434** |

### GF(3) Color Chain Assignments

| ID | Source | Trit | Color | Name |
|----|--------|------|-------|------|
| 1 | plurigrid | +1 | #b8bb26 | PLUS |
| 2 | kubeflow | -1 | #cc241d | MINUS |
| 3 | TeglonLabs | 0 | #d3869b | ERGODIC |
| 4 | bmorphism | +1 | #b8bb26 | PLUS |
| 5 | zubyul | -1 | #cc241d | MINUS |
| 6 | migalkin | 0 | #d3869b | ERGODIC |
| 7 | DJedamski | +1 | #b8bb26 | PLUS |
| 8 | wasita | -1 | #cc241d | MINUS |
| 9 | kristinezheng | 0 | #d3869b | ERGODIC |
| 10 | M1shaaa | +1 | #b8bb26 | PLUS |
| 11 | AustinCStone | -1 | #cc241d | MINUS |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

Balances fetched via `0x1::primary_fungible_store::balance` (FA method, APT metadata `0xa`).

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.43643352 |
| bob | 0x0a3c...2d5d | 12.65700700 |
| A | 0x8699...e9d7a | 0.05176700 |
| B | 0x3f89...b13 | 0.03625600 |
| C | 0x38b9...535e | 0.01018500 |
| D | 0xf776...fdd1 | 0.01162900 |
| E | 0xdc1d...8d36 | 0.01256100 |
| F | 0x18a1...cf71 | 1.96051600 |
| G | 0x69a3...7f32 | 0.00068100 |
| H | 0xce67...300f | 0.00068100 |
| I | 0x070f...1fc9 | 0.00068100 |
| J | 0x4d96...f54 | 1.89509300 |
| K | 0xa732...5dc4 | 0.16196100 |
| L | 0x7c2e...eba9 | 1.92726900 |
| M | 0x6fed...f2e9 | 0.11228500 |
| N | 0xe7dd...b2c | 0.10612100 |
| O | 0x7325...a89d | 0.21013600 |
| P | 0x6218...c948 | 0.14013600 |
| Q | 0xac40...89a9 | 0.10324000 |
| R | 0x7ce6...6e10 | 0.09021700 |
| S | 0xb875...0386 | 0.09178800 |
| T | 0x3578...4588 | 0.07371300 |
| U | 0x7586...9956 | 0.05577300 |
| V | 0xb59d...f2c3 | 0.04783299 |
| W | 0x5f32...c7b0 | 0.04070500 |
| X | 0xa95c...047d | 0.04257700 |
| Y | 0xd8e3...44c4 | 0.04444900 |
| Z | 0x7af0...97c | 0.02326800 |

**Total APT across swarm:** ~18.31 APT

Note: CoinStore resource not present on these accounts; balances retrieved via FA (fungible asset) store.

### Multisig Contract Probes

All 5 multisig contracts responded successfully. All require 2-of-N signatures (healthy).

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

### MNX Markets

`https://testnet.mnx.fi/api/markets` and `/api/v1/markets` return HTML (Next.js frontend), not a JSON API. No machine-readable market data available via direct API call. Status: **unavailable / frontend-only**.

---

## Database Tables

| Table | Rows |
|-------|------|
| world_increments | 24 |
| repo_snapshots | 434 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (availability note) |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/pipelines**: most-starred kubeflow repo in sweep
- **TeglonLabs**: 53 repos swept including Stahl (Rust), vibespace (HTML)
- **bmorphism**: 100 public repos swept; sequence_number=72 on alice's Aptos account
- **bob** holds the highest APT balance in the swarm: 12.657 APT
- **F, J, L** each hold ~1.9 APT, next highest tier
- All 5 multisig contracts healthy, all 2-of-N
