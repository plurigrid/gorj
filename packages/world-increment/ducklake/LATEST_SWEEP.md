# World-Increment Sweep + Hamming Snapshot

**Date:** 2026-05-19 00:16:31 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Unique Repos | Total Stars |
|--------|------|-------------|-------------|
| plurigrid | org | 167 | 154 |
| kubeflow | org | 49 | 101,802 |
| TeglonLabs | org | 53 | 14 |
| bmorphism | user | 165 | 509 |
| zubyul | user | 59 | 40 |
| migalkin | social | 30 | 833 |
| DJedamski | social | 11 | 17 |
| wasita | social | 32 | 10 |
| kristinezheng | social | 18 | 0 |
| M1shaaa | social | 16 | 0 |
| AustinCStone | social | 43 | 324 |

**Total unique repos tracked: 643**

### GF(3) Color Chain (world_increments)

| ID | Trit | Color | Name | Source |
|----|------|-------|------|--------|
| 1 | +1 | #b8bb26 | PLUS | plurigrid (org) |
| 2 | -1 | #cc241d | MINUS | kubeflow (org) |
| 3 | 0 | #d3869b | ERGODIC | TeglonLabs (org) |
| 4 | +1 | #b8bb26 | PLUS | bmorphism (user) |
| 5 | -1 | #cc241d | MINUS | zubyul (user) |
| 6 | 0 | #d3869b | ERGODIC | migalkin (social) |
| 7 | +1 | #b8bb26 | PLUS | DJedamski (social) |
| 8 | -1 | #cc241d | MINUS | wasita (social) |
| 9 | 0 | #d3869b | ERGODIC | kristinezheng (social) |
| 10 | +1 | #b8bb26 | PLUS | M1shaaa (social) |
| 11 | -1 | #cc241d | MINUS | AustinCStone (social) |

### Notable Repos

- **kubeflow**: 101,802 total stars — dominant ML infra org
- **migalkin/NodePiece**: 144 stars — ICLR'22 KG representation
- **migalkin/StarE**: 89 stars — EMNLP 2020 hyper-relational KGs
- **AustinCStone/TextGAN**: 92 stars — TF text GAN
- **TeglonLabs/mathpix-gem**: Ruby gem for LaTeX OCR (pushed 2026-01-01)
- **wasita/wasita.github.io**: Svelte personal site (pushed 2026-05-18, most recent)
- **bmorphism**: 165 unique repos, highly active user

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) returned **0 APT** — CoinStore resource not initialized on mainnet for any of these addresses.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793acde... | 0.0 |
| bob | 0x0a3c00c5... | 0.0 |
| A | 0x8699edc0... | 0.0 |
| B | 0x3f892ebe... | 0.0 |
| C | 0x38b99e63... | 0.0 |
| D | 0xf7765624... | 0.0 |
| E | 0xdc1d9d53... | 0.0 |
| F | 0x18a14b5b... | 0.0 |
| G | 0x69a394c0... | 0.0 |
| H | 0xce67c327... | 0.0 |
| I | 0x070fe5d7... | 0.0 |
| J | 0x4d964db8... | 0.0 |
| K | 0xa732040a... | 0.0 |
| L | 0x7c2eaeaf... | 0.0 |
| M | 0x6fed37a7... | 0.0 |
| N | 0xe7dde6da... | 0.0 |
| O | 0x73252b60... | 0.0 |
| P | 0x6218792d... | 0.0 |
| Q | 0xac40fa50... | 0.0 |
| R | 0x7ce605cc... | 0.0 |
| S | 0xb8753014... | 0.0 |
| T | 0x35781dc0... | 0.0 |
| U | 0x75860da4... | 0.0 |
| V | 0xb59dd817... | 0.0 |
| W | 0x5f32aef7... | 0.0 |
| X | 0xa95cbbd1... | 0.0 |
| Y | 0xd8e32848... | 0.0 |
| Z | 0x7af0ef6e... | 0.0 |

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig contracts healthy with 2-of-N threshold:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable.** All probed API paths returned no market data:
- `/`, `/api/markets`, `/api/v1/markets`, `/api/tickers`, `/markets`, `/api/v2/markets`

testnet.mnx.fi is a SPA; no REST/JSON market data endpoints responded.

---

## DuckDB Schema Summary

```
world_increments  — 11 sources tracked (GF3 chain)
repo_snapshots    — 643 unique repos across 11 sources
aptos_snapshots   — 28 addresses, all 0 APT
multisig_probes   — 5 pairs, all 2-sig threshold, all healthy
mnx_snapshots     — 0 rows (endpoint unavailable)
```
