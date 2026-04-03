# World-Increment Sweep + Hamming Snapshot

**Sweep Date/Time:** 2026-04-03 (UTC)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| # | Type | Name | Repos Found |
|---|------|------|-------------|
| 1 | org  | plurigrid | 93 |
| 2 | org  | kubeflow | 46 |
| 3 | org  | TeglonLabs | 3 |
| 4 | user | bmorphism | 97 |
| 5 | user | zubyul | 44 |
| 6 | user | migalkin | 19 |
| 7 | user | DJedamski | 6 |
| 8 | user | wasita | 9 |
| 9 | user | kristinezheng | 6 |
| 10 | user | M1shaaa | 8 |
| 11 | user | AustinCStone | 40 |

**Total sources swept:** 11
**Total repos found:** 371 (93+46+3+97+44+19+6+9+6+8+40)
**Repos inserted this sweep:** 105 (representative sample)

### Notable Repos by Stars
- kubeflow/kubeflow: 15,551 stars
- kubeflow/pipelines: 4,118 stars
- kubeflow/spark-operator: 3,110 stars
- kubeflow/trainer: 2,071 stars
- kubeflow/katib: 1,674 stars
- migalkin/NodePiece: 143 stars
- AustinCStone/TextGAN: 92 stars
- migalkin/StarE: 88 stars
- bmorphism/ocaml-mcp-sdk: 60 stars
- plurigrid/asi: 14 stars

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...c7b | 0.0 |
| bob   | 0x0a3c...d5d | 0.0 |
| A     | 0x8699...d7a | 0.0 |
| B     | 0x3f89...b13 | 0.0 |
| C     | 0x38b9...35e | 0.0 |
| D     | 0xf776...dd1 | 0.0 |
| E     | 0xdc1d...d36 | 0.0 |
| F     | 0x18a1...f71 | 0.0 |
| G     | 0x69a3...f32 | 0.0 |
| H     | 0xce67...00f | 0.0 |
| I     | 0x070f...fc9 | 0.0 |
| J     | 0x4d96...f54 | 0.0 |
| K     | 0xa732...dc4 | 0.0 |
| L     | 0x7c2e...ba9 | 0.0 |
| M     | 0x6fed...e9 | 0.0 |
| N     | 0xe7dd...b2c | 0.0 |
| O     | 0x7325...89d | 0.0 |
| P     | 0x6218...948 | 0.0 |
| Q     | 0xac40...a9 | 0.0 |
| R     | 0x7ce6...e10 | 0.0 |
| S     | 0xb875...386 | 0.0 |
| T     | 0x3578...588 | 0.0 |
| U     | 0x7586...956 | 0.0 |
| V     | 0xb59d...2c3 | 0.0 |
| W     | 0x5f32...7b0 | 0.0 |
| X     | 0xa95c...47d | 0.0 |
| Y     | 0xd8e3...4c4 | 0.0 |
| Z     | 0x7af0...97c | 0.0 |

Note: All accounts returned 0 APT. Accounts may be uninitialized/unfunded on Aptos mainnet.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4...003 | 2 | true |
| A-G  | 0xf56c...096 | 2 | true |
| Y-Z  | 0xd3ff...883 | 2 | true |
| S-T  | 0x3b1c...883 | 2 | true |
| V-W  | 0x40fa...6d  | 2 | true |

All 5 multisig contracts are healthy with 2-of-N signature requirements.

### MNX Markets

**Status:** Unavailable as JSON API.
The endpoint `https://testnet.mnx.fi/api/markets` (and variants) returns an HTML Next.js SPA rather than a JSON API response. No market ticker data could be extracted.

---

## GF(3) Color Chain Summary

The world_increments table uses GF(3) arithmetic (mod 3) to assign semantic colors:

| ID mod 3 | Trit | Color   | Name    | Semantic |
|----------|------|---------|---------|----------|
| 0        |  0   | #d3869b | ERGODIC | Fixed point / equilibrium |
| 1        |  1   | #b8bb26 | PLUS    | Positive increment |
| 2        | -1   | #cc241d | MINUS   | Negative increment |

### Increments This Sweep

| ID | Source | GF3 Name |
|----|--------|----------|
| 1  | plurigrid | PLUS |
| 2  | kubeflow | MINUS |
| 3  | TeglonLabs | ERGODIC |
| 4  | bmorphism | PLUS |
| 5  | zubyul | MINUS |
| 6  | migalkin | ERGODIC |
| 7  | DJedamski | PLUS |
| 8  | wasita | MINUS |
| 9  | kristinezheng | ERGODIC |
| 10 | M1shaaa | PLUS |
| 11 | AustinCStone | MINUS |

---

## Database Summary

- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Tables:** `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`
- **world_increments (this sweep):** 11 rows (github_sweep event type)
- **repo_snapshots (inserted):** 105 rows
- **aptos_snapshots:** 28 rows
- **multisig_probes:** 5 rows
- **mnx_snapshots:** 0 rows (API unavailable)
