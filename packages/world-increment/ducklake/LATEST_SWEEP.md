# World-Increment Sweep + Hamming Snapshot

**Date:** 2026-07-07
**Run:** world-increment-sweep + hamming-swarm-snapshot
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin (zubyul social) | user | 6 |
| DJedamski (zubyul social) | user | 4 |
| wasita (zubyul social) | user | 6 |
| kristinezheng (zubyul social) | user | 5 |
| M1shaaa (zubyul social) | user | 4 |
| AustinCStone (zubyul social) | user | 8 |
| **TOTAL** | | **336** |

### Notable Repos

**TeglonLabs** — `jank-crane` (C++, GF3 convergence maps, pushed 2026-06-08), `mathpix-gem` (Ruby, 2★)
**bmorphism** — `ocaml-mcp-sdk` (60★), `anti-bullshit-mcp-server` (23★)

Social graph highlights:
- `migalkin/NodePiece` — 144★ 21 forks (ICLR'22 KG representations)
- `migalkin/StarE` — 89★ 16 forks (EMNLP 2020)
- `AustinCStone/TextGAN` — 92★ 30 forks (TF text GAN)
- `wasita/wasita.github.io` — pushed 2026-07-06 (most recently active)

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 112 |
| +1 | `#b8bb26` | PLUS | 112 |
| -1 | `#cc241d` | MINUS | 112 |

Assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — 2026-07-07

All 28 addresses (alice, bob, A–Z) queried against mainnet CoinStore resource.
**All returned 0.00 APT** — accounts uninitialized or empty.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...87003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...0096 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...b883 | 2 | HEALTHY |

All 5 multisig contracts responsive — 2-of-N threshold confirmed.

### MNX Markets

`https://testnet.mnx.fi` — **UNAVAILABLE** (all API paths returned no JSON; testnet offline or SPA-only)

---

## DuckDB Row Counts

| Table | Rows | Notes |
|-------|------|-------|
| world_increments | 336 | GF3-tagged repo events |
| repo_snapshots | 336 | Full repo metadata |
| aptos_snapshots | 28 | All 0.0 APT |
| multisig_probes | 5 | All healthy |
| mnx_snapshots | 0 | Unavailable |
