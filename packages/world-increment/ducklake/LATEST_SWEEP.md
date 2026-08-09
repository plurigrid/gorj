# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-09  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|---|---|---|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| migalkin | social-graph | 6 |
| wasita | social-graph | 6 |
| TeglonLabs | org | 5 |
| AustinCStone | social-graph | 5 |
| DJedamski | social-graph | 4 |
| kristinezheng | social-graph | 3 |
| M1shaaa | social-graph | 3 |
| **TOTAL** | | **330** |

### GF(3) Color Chain Assignment

| id % 3 | Trit | Color | Name |
|---|---|---|---|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

### Notable Repos (recently pushed)

- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08) — crane-jank converged-IR hub, GF3 convergence maps
- **wasita/wm-cv** (Svelte, pushed 2026-08-07) — academic CV
- **wasita/xoxowasita-analysis** (Python, pushed 2026-08-06) — fresh analysis repo
- **migalkin/NodePiece** (Python, 144★) — ICLR'22 KG paper
- **AustinCStone/TextGAN** (Python, 92★) — TF text generation GAN
- **TeglonLabs/mathpix-gem** (Ruby, 2★) — mathematical OCR Ruby gem

### Events
- bmorphism and zubyul repos captured via user search (100 and 49 respectively)
- GitHub events API not queried (no `gh` CLI available; using MCP search)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-08-09)

Method: `POST /v1/view` → `0x1::coin::balance["0x1::aptos_coin::AptosCoin"]`

| World | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | 0xc793…4cc7b | 0.43643352 |
| bob | 0x0a3c…512d5d | 12.65700700 |
| A | 0x8699…be9d7a | 0.05176700 |
| B | 0x3f89…cb13 | 0.03625600 |
| C | 0x38b9…535e | 0.01018500 |
| D | 0xf776…cfdd1 | 0.01162900 |
| E | 0xdc1d…8d36 | 0.00937200 |
| F | 0x18a1…cf71 | 1.96051600 |
| G | 0x69a3…7f32 | 0.00068100 |
| H | 0xce67…5300f | 0.00168100 |
| I | 0x070f…1fc9 | 0.00068100 |
| J | 0x4d96…7f54 | 1.89509300 |
| K | 0xa732…25dc4 | 0.16196100 |
| L | 0x7c2e…eba9 | 1.92726900 |
| M | 0x6fed…f2e9 | 0.11228500 |
| N | 0xe7dd…51b2c | 0.10612100 |
| O | 0x7325…a89d | 0.21013600 |
| P | 0x6218…ec948 | 0.14013600 |
| Q | 0xac40…c89a9 | 0.10324000 |
| R | 0x7ce6…6e10 | 0.09021700 |
| S | 0xb875…d0386 | 0.09178800 |
| T | 0x3578…f4588 | 0.07371300 |
| U | 0x7586…f9956 | 0.05577300 |
| V | 0xb59d…af2c3 | 0.04883299 |
| W | 0x5f32…cc7b0 | 0.04070500 |
| X | 0xa95c…3047d | 0.04257700 |
| Y | 0xd8e3…444c4 | 0.04444900 |
| Z | 0x7af0…197c | 0.02426800 |

**Total Hamming Swarm APT: 20.3448**  
**Largest holder:** bob (12.6570 APT)  
**Notable balances:** F (1.9605), L (1.9273), J (1.8951)

### Multisig Contract Probes

All 5 multisig contracts healthy — all require **2-of-N** signatures.

| Pair | Address (truncated) | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4…7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c…0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff…b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c…7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa…eb6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is a React SPA that renders only `"MNX"` text. `/api/markets` returns HTTP 404. No market data extractable. Table left empty.

---

## DuckDB Schema Summary

| Table | Rows |
|---|---|
| world_increments | 11 |
| repo_snapshots | 330 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
