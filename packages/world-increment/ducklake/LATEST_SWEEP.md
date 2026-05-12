# LATEST_SWEEP — 2026-05-12

Generated: 2026-05-12 15:11:48 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 16 (top) |
| zubyul | user | 8 (top) |
| migalkin | social graph | 3 (top) |
| wasita | social graph | 2 (top) |
| DJedamski | social graph | 1 (top) |
| M1shaaa | social graph | 1 (top) |
| AustinCStone | social graph | 1 (top) |
| kristinezheng | social graph | 1 (top) |

**Total repo snapshots stored: 185**

### GF(3) Color Chain

`id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d`

### Notable Repos (by stars)

| Repo | Stars | Language | Org/User |
|------|-------|----------|----------|
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | bmorphism |
| AustinCStone/TextGAN | 92 | Python | AustinCStone |
| migalkin/NodePiece | 144 | Python | migalkin |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | bmorphism |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | bmorphism |
| bmorphism/say-mcp-server | 20 | JavaScript | bmorphism |
| bmorphism/babashka-mcp-server | 18 | JavaScript | bmorphism |
| migalkin/StarE | 89 | Python | migalkin |
| migalkin/kgcourse2021 | 25 | HTML | migalkin |
| plurigrid/ontology | 8 | JavaScript | plurigrid |

### DuckDB Tables

- `world_increments`: 208 rows (GF3-colored event stream)
- `repo_snapshots`: 185 rows

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried via `0x1::coin::balance` view function.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| A      | `0x8699edc0960dd5b916...` | 0.05176700 |
| B      | `0x3f892ebe6e45164e63...` | 0.03625600 |
| C      | `0x38b99e63ada9b6fef1...` | 0.01018500 |
| D      | `0xf77656248f64d5dd00...` | 0.01162900 |
| E      | `0xdc1d9d533bac3507f9...` | 0.00937200 |
| F      | `0x18a14b5b4bec118c1c...` | 1.96051600 |
| G      | `0x69a394c0b0ac842127...` | 0.00068100 |
| H      | `0xce67c327a7844e5488...` | 0.00168100 |
| I      | `0x070fe5d74e4eda30e2...` | 0.00068100 |
| J      | `0x4d964db8f538374034...` | 1.89509300 |
| K      | `0xa732040a6b0d559041...` | 0.16196100 |
| L      | `0x7c2eaeafad9725492e...` | 1.92726900 |
| M      | `0x6fed37a7553ef16b2a...` | 0.11228500 |
| N      | `0xe7dde6da0a65f51062...` | 0.10612100 |
| O      | `0x73252b6011a75115a2...` | 0.21013600 |
| P      | `0x6218792de4a9bc3891...` | 0.14013600 |
| Q      | `0xac40fa50b81b4ca6b1...` | 0.10324000 |
| R      | `0x7ce605cc8fda4f8e4a...` | 0.09021700 |
| S      | `0xb8753014e4888ea48a...` | 0.09178800 |
| T      | `0x35781dc0e42fef3f25...` | 0.07371300 |
| U      | `0x75860da47565f6509b...` | 0.05577300 |
| V      | `0xb59dd8170321dfab5a...` | 0.04883299 |
| W      | `0x5f32aef70f5ba530d3...` | 0.04070500 |
| X      | `0xa95cbbd116548ac990...` | 0.04257700 |
| Y      | `0xd8e32848f1dffa811b...` | 0.04444900 |
| Z      | `0x7af0ef6e1bd706f4b3...` | 0.02426800 |
| alice  | `0xc793acdec12b4a6371...` | 0.43643352 |
| bob    | `0x0a3c00c58fdf9020b2...` | 12.65700700 |

**Total across swarm: 20.34477251 APT**

### Multisig Contract Probes

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B   | `0x0da4f428a0c007da0f...` | 2 | ✅ |
| A-G   | `0xf56c4a1c0906214f3f...` | 2 | ✅ |
| Y-Z   | `0xd3ffe1812b2df40622...` | 2 | ✅ |
| S-T   | `0x3b1c3ae905d44c3a49...` | 2 | ✅ |
| V-W   | `0x40fad7b423a843650f...` | 2 | ✅ |

**5/5 multisig contracts healthy** — all require 2-of-N signatures.

### MNX Testnet Markets

**Status: Unavailable** — `https://testnet.mnx.fi` is a Next.js SPA with no accessible REST API endpoints. Probed: `/api/markets`, `/api/v1/markets`, `/api/v2/markets`, `/api/tickers`. All returned 404 or rendered HTML. Logged as `category=unavailable` in `mnx_snapshots` table.

### DuckDB Tables

- `aptos_snapshots`: 28 rows
- `multisig_probes`: 5 rows  
- `mnx_snapshots`: 1 row (unavailable marker)

---

## Database Location

`packages/world-increment/ducklake/world-increments.duckdb`

## Schema Summary

```sql
world_increments   -- GF(3)-colored event stream (208 rows)
repo_snapshots     -- GitHub repo metadata (185 rows)
aptos_snapshots    -- Aptos wallet APT balances (28 rows)
multisig_probes    -- Multisig sig-threshold health (5 rows)
mnx_snapshots      -- MNX market data (1 row, unavailable)
```
