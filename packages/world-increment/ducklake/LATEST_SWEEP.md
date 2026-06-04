# LATEST_SWEEP — 2026-05-06

## JOB 1: GitHub Social Graph Sweep

| Source | Type | Repos |
|--------|------|-------|
| AustinCStone | user | 40 |
| DJedamski | user | 6 |
| M1shaaa | user | 8 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| kristinezheng | user | 6 |
| kubeflow | org | 100 |
| migalkin | user | 19 |
| plurigrid | org | 47 |
| wasita | user | 11 |
| zubyul | user | 49 |

**Total repo snapshots**: 390 across 11 sources

### GF(3) Color Chain
- trit=0 (ERGODIC) `#d3869b`: id%3==0
- trit=1 (PLUS)    `#b8bb26`: id%3==1
- trit=-1 (MINUS)  `#cc241d`: id%3==2

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | `0xc793acdec1...` | 0.43643352 |
| bob | `0x0a3c00c58f...` | 12.65700700 |
| A | `0x8699edc096...` | 0.05176700 |
| B | `0x3f892ebe6e...` | 0.03625600 |
| C | `0x38b99e63ad...` | 0.01018500 |
| D | `0xf77656248f...` | 0.01162900 |
| E | `0xdc1d9d533b...` | 0.00937200 |
| F | `0x18a14b5b4b...` | 1.96051600 |
| G | `0x69a394c0b0...` | 0.00068100 |
| H | `0xce67c327a7...` | 0.00168100 |
| I | `0x070fe5d74e...` | 0.00068100 |
| J | `0x4d964db8f5...` | 1.89509300 |
| K | `0xa732040a6b...` | 0.16196100 |
| L | `0x7c2eaeafad...` | 1.92726900 |
| M | `0x6fed37a755...` | 0.11228500 |
| N | `0xe7dde6da0a...` | 0.10612100 |
| O | `0x73252b6011...` | 0.21013600 |
| P | `0x6218792de4...` | 0.14013600 |
| Q | `0xac40fa50b8...` | 0.10324000 |
| R | `0x7ce605cc8f...` | 0.09021700 |
| S | `0xb8753014e4...` | 0.09178800 |
| T | `0x35781dc0e4...` | 0.07371300 |
| U | `0x75860da475...` | 0.05577300 |
| V | `0xb59dd81703...` | 0.04883299 |
| W | `0x5f32aef70f...` | 0.04070500 |
| X | `0xa95cbbd116...` | 0.04257700 |
| Y | `0xd8e32848f1...` | 0.04444900 |
| Z | `0x7af0ef6e1b...` | 0.02426800 |

**Total APT across 28 worlds**: 20.34477251 APT

### Multisig Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...` | 2 | ✓ |
| A-G | `0xf56c4a1c...` | 2 | ✓ |
| Y-Z | `0xd3ffe181...` | 2 | ✓ |
| S-T | `0x3b1c3ae9...` | 2 | ✓ |
| V-W | `0x40fad7b4...` | 2 | ✓ |

All 5 multisig contracts healthy, requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — `/api/markets` returns 404. SPA (Next.js) with no public REST API endpoints found.

---

## DuckDB Schema

Located at `packages/world-increment/ducklake/world-increments.duckdb`

Tables:
- `world_increments` — 390 rows (GF3 color chain applied)
- `repo_snapshots` — 390 rows
- `aptos_snapshots` — 28 rows
- `multisig_probes` — 5 rows
- `mnx_snapshots` — 0 rows (unavailable)
