# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-05  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| AustinCStone | user (social) | 30 |
| wasita | user (social) | 11 |
| DJedamski | user (social) | 2 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| **TOTAL** | | **372** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 124 |
| 1 | `#b8bb26` | PLUS | 124 |
| -1 | `#cc241d` | MINUS | 124 |

### Top Languages (across all repos)

| Language | Repos |
|----------|-------|
| Python | 77 |
| Rust | 26 |
| JavaScript | 24 |
| TypeScript | 22 |
| HTML | 16 |
| Go | 15 |
| Jupyter Notebook | 14 |
| Clojure | 14 |

### Notable Recent Activity

- **plurigrid/shrimp** — pushed 2026-07-03 (most recent plurigrid)
- **bmorphism/Gay.jl** — Julia, pushed 2026-07-05
- **M1shaaa/M1shaaa** — pushed 2026-07-05
- **wasita/wasita.github.io** — Svelte, pushed 2026-07-05
- **kubeflow/pipelines** — Python, 4169 stars, pushed 2026-07-05
- **TeglonLabs/jank-crane** — C++, crane-jank converged-IR hub with GF3 convergence maps

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, coin::balance view)

Note: All addresses are active on chain. Legacy CoinStore not used — queried via coin::balance view function (FA-compatible).

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| bob | 0x0a3c00c5... | 12.6570 |
| F | 0x18a14b5b... | 1.9605 |
| L | 0x7c2eaeaf... | 1.9273 |
| J | 0x4d964db8... | 1.8951 |
| alice | 0xc793acde... | 0.4364 |
| K | 0xa732040a... | 0.1620 |
| O | 0x73252b60... | 0.2101 |
| P | 0x62187929... | 0.1401 |
| M | 0x6fed37a7... | 0.1123 |
| N | 0xe7dde6da... | 0.1061 |
| Q | 0xac40fa50... | 0.1032 |
| S | 0xb8753014... | 0.0918 |
| R | 0x7ce605cc... | 0.0902 |
| T | 0x35781dc0... | 0.0737 |
| U | 0x75860da4... | 0.0558 |
| A | 0x8699edc0... | 0.0518 |
| V | 0xb59dd817... | 0.0488 |
| X | 0xa95cbbd1... | 0.0426 |
| Y | 0xd8e32848... | 0.0444 |
| W | 0x5f32aef7... | 0.0407 |
| B | 0x3f892ebe... | 0.0363 |
| Z | 0x7af0ef6e... | 0.0243 |
| D | 0xf7765624... | 0.0116 |
| C | 0x38b99e63... | 0.0102 |
| E | 0xdc1d9d53... | 0.0094 |
| H | 0xce67c327... | 0.0017 |
| G | 0x69a394c0... | 0.0007 |
| I | 0x070fe5d7... | 0.0007 |

**Total APT tracked: 20.3448 APT**  
**Largest holder: bob (12.657 APT, 62.2% of swarm)**

### Multisig Contract Probes

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4f428... | 2 | YES |
| A-G | 0xf56c4a1c... | 2 | YES |
| Y-Z | 0xd3ffe181... | 2 | YES |
| S-T | 0x3b1c3ae9... | 2 | YES |
| V-W | 0x40fad7b4... | 2 | YES |

All 5 multisig accounts require 2-of-N signatures. All probes healthy.

### MNX Markets

Status: UNAVAILABLE  
`https://testnet.mnx.fi` returns Vercel authentication gate — no market data accessible without credentials.

---

## Database Summary

| Table | Rows |
|-------|------|
| world_increments | 372 |
| repo_snapshots | 372 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (sentinel) |
