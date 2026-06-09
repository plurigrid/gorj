# LATEST_SWEEP — 2026-06-09 10:14:23 UTC

## Job 1: GitHub Social Graph Sweep

### Sources
| Source | Type | Repos Snapshotted |
|--------|------|------------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| wasita | user (social) | 11 |
| M1shaaa | user (social) | 8 |
| DJedamski | user (social) | 6 |
| kristinezheng | user (social) | 5 |
| AustinCStone | user (social) | 30 |
| **TOTAL** | | **381** |

### DuckDB Schema
- `world_increments` — 11 rows (one per source, GF(3) color-chained)
- `repo_snapshots` — 381 rows
- `aptos_snapshots` — 28 rows
- `multisig_probes` — 5 rows
- `mnx_snapshots` — 1 row (unavailable)

### GF(3) Color Chain
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 3 |
| 1 | #b8bb26 | PLUS | 4 |
| -1 | #cc241d | MINUS | 4 |

### Notable Repos (recently pushed)
- `TeglonLabs/jank-crane` (C++) — crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps — pushed 2026-06-08
- `plurigrid/place` (TeX) — pushed 2026-06-04

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)
Total APT across swarm: **20.344773 APT**

| World | Address | Balance (APT) |
|-------|---------|--------------|
| bob | 0x0a3c00c58fdf90... | 12.65700700 |
| F | 0x18a14b5b4bec11... | 1.96051600 |
| L | 0x7c2eaeafad9725... | 1.92726900 |
| J | 0x4d964db8f53837... | 1.89509300 |
| alice | 0xc793acdec12b4a... | 0.43643352 |
| O | 0x73252b6011a751... | 0.21013600 |
| K | 0xa732040a6b0d55... | 0.16196100 |
| P | 0x6218792de4a9bc... | 0.14013600 |
| M | 0x6fed37a7553ef1... | 0.11228500 |
| N | 0xe7dde6da0a65f5... | 0.10612100 |
| Q | 0xac40fa50b81b4c... | 0.10324000 |
| S | 0xb8753014e4888e... | 0.09178800 |
| R | 0x7ce605cc8fda4f... | 0.09021700 |
| T | 0x35781dc0e42fef... | 0.07371300 |
| U | 0x75860da47565f6... | 0.05577300 |
| A | 0x8699edc0960dd5... | 0.05176700 |
| V | 0xb59dd8170321df... | 0.04883299 |
| Y | 0xd8e32848f1dffa... | 0.04444900 |
| X | 0xa95cbbd116548a... | 0.04257700 |
| W | 0x5f32aef70f5ba5... | 0.04070500 |
| B | 0x3f892ebe6e4516... | 0.03625600 |
| Z | 0x7af0ef6e1bd706... | 0.02426800 |
| D | 0xf77656248f64d5... | 0.01162900 |
| C | 0x38b99e63ada9b6... | 0.01018500 |
| E | 0xdc1d9d533bac35... | 0.00937200 |
| H | 0xce67c327a7844e... | 0.00168100 |
| G | 0x69a394c0b0ac84... | 0.00068100 |
| I | 0x070fe5d74e4eda... | 0.00068100 |

### Multisig Contracts (5 probes)
All healthy — each requires 2-of-N signatures.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428a0c007... | 2 | ✅ |
| A-G | 0xf56c4a1c090621... | 2 | ✅ |
| Y-Z | 0xd3ffe1812b2df4... | 2 | ✅ |
| S-T | 0x3b1c3ae905d44c... | 2 | ✅ |
| V-W | 0x40fad7b423a843... | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)
**Status: Unavailable** — Vercel authentication wall, no bypass token available. Endpoint returns 401 HTML for unauthenticated agents.

---

## DuckDB Location
`packages/world-increment/ducklake/world-increments.duckdb`

Query example:
```sql
SELECT org_or_user, COUNT(*) as repos FROM repo_snapshots GROUP BY 1 ORDER BY 2 DESC;
SELECT world, balance_apt FROM aptos_snapshots ORDER BY balance_apt DESC;
```
