# LATEST_SWEEP.md

**Generated:** 2026-03-31 20:15:30 UTC  
**Total Repos Snapshotted:** 371  
**GF(3) Color Chain:** ERGODIC #d3869b / PLUS #b8bb26 / MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Repos Snapshotted per Org/User

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 93 |
| kubeflow | org | 46 |
| TeglonLabs | org | 3 |
| bmorphism | user | 97 |
| zubyul | user | 44 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 9 |
| kristinezheng | user | 6 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |

**Total:** 371 repos  

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

| Label | Address (first 16 chars) | Balance (APT) |
|-------|--------------------------|---------------|
| alice | `0xc793acdec12b4a63...` | 0.0000 |
| bob | `0x0a3c00c58fdf9020...` | 0.0000 |
| A | `0x8699edc0960dd5b9...` | 0.0000 |
| B | `0x3f892ebe6e45164e...` | 0.0000 |
| C | `0x38b99e63ada9b6fe...` | 0.0000 |
| D | `0xf77656248f64d5dd...` | 0.0000 |
| E | `0xdc1d9d533bac3507...` | 0.0000 |
| F | `0x18a14b5b4bec118c...` | 0.0000 |
| G | `0x69a394c0b0ac8421...` | 0.0000 |
| H | `0xce67c327a7844e54...` | 0.0000 |
| I | `0x070fe5d74e4eda30...` | 0.0000 |
| J | `0x4d964db8f5383740...` | 0.0000 |
| K | `0xa732040a6b0d5590...` | 0.0000 |
| L | `0x7c2eaeafad972549...` | 0.0000 |
| M | `0x6fed37a7553ef16b...` | 0.0000 |
| N | `0xe7dde6da0a65f510...` | 0.0000 |
| O | `0x73252b6011a75115...` | 0.0000 |
| P | `0x6218792de4a9bc38...` | 0.0000 |
| Q | `0xac40fa50b81b4ca6...` | 0.0000 |
| R | `0x7ce605cc8fda4f8e...` | 0.0000 |
| S | `0xb8753014e4888ea4...` | 0.0000 |
| T | `0x35781dc0e42fef3f...` | 0.0000 |
| U | `0x75860da47565f650...` | 0.0000 |
| V | `0xb59dd8170321dfab...` | 0.0000 |
| W | `0x5f32aef70f5ba530...` | 0.0000 |
| X | `0xa95cbbd116548ac9...` | 0.0000 |
| Y | `0xd8e32848f1dffa81...` | 0.0000 |
| Z | `0x7af0ef6e1bd706f4...` | 0.0000 |

**Note:** All balances returned 0.0 APT — accounts may be unfunded on mainnet or resource not found.

---

### Multisig Contract Probes

| Pair | Address (first 18 chars) | Sigs Required | Healthy |
|------|--------------------------|---------------|--------|
| A-B | `0x0da4f428a0c007da...` | 2 | YES |
| A-G | `0xf56c4a1c0906214f...` | 2 | YES |
| Y-Z | `0xd3ffe1812b2df406...` | 2 | YES |
| S-T | `0x3b1c3ae905d44c3a...` | 2 | YES |
| V-W | `0x40fad7b423a84365...` | 2 | YES |

**All 5 multisig contracts healthy, requiring 2 signatures each.**

---

### MNX Markets Status

**Status:** UNAVAILABLE  
`https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/tickers` both return HTML (Next.js web app), no JSON API endpoint exposed at these paths.

---

## Database Summary

- **File:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Tables:** `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`
- **world_increments rows:** 371
- **repo_snapshots rows:** 371
- **aptos_snapshots rows:** 28
- **multisig_probes rows:** 5
- **GF(3) trit distribution:** id%3==0 → trit=0 ERGODIC, id%3==1 → trit=1 PLUS, id%3==2 → trit=-1 MINUS
