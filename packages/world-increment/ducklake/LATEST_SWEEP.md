# World Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-08-10 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 50 |
| kubeflow | org | 30 |
| TeglonLabs | org | 5 |
| bmorphism | user | 10 |
| zubyul | user | 8 |
| migalkin | social graph | 4 |
| M1shaaa | social graph | 2 |
| AustinCStone | social graph | 3 |
| DJedamski | social graph | 2 |
| wasita | social graph | 3 |
| kristinezheng | social graph | 3 |
| **Total** | | **120 repos this sweep** |

### Notable Repos (by stars)

| Org/User | Repo | Language | Stars |
|----------|------|----------|-------|
| kubeflow | kubeflow | Python | 15,807 |
| kubeflow | pipelines | Python | 4,180 |
| kubeflow | spark-operator | Go | 3,146 |
| bmorphism | ocaml-mcp-sdk | OCaml | 61 |
| bmorphism | anti-bullshit-mcp-server | JavaScript | 23 |
| migalkin | NodePiece | Python | 144 |
| migalkin | StarE | Python | 89 |
| bmorphism | Gay.jl | Julia | 2 |

### GF(3) Color Chain Distribution

| GF3 Name | Color | Count |
|----------|-------|-------|
| ERGODIC | #d3869b | 47 |
| PLUS | #b8bb26 | 48 |
| MINUS | #cc241d | 48 |

**Total world_increments in DB:** 143 (cumulative across sweeps)  
**Total repo_snapshots in DB:** 1,064 (cumulative historical record)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**Sweep timestamp:** 2026-08-10 UTC  
**Wallets queried:** 28 (alice, bob, A–Z)  
**Total APT across swarm:** 20.3448 APT

| World | Balance (APT) |
|-------|--------------|
| bob | 12.6570 |
| F | 1.9605 |
| L | 1.9273 |
| J | 1.8951 |
| alice | 0.4364 |
| O | 0.2101 |
| K | 0.1620 |
| P | 0.1401 |
| M | 0.1123 |
| N | 0.1061 |
| Q | 0.1032 |
| R | 0.0902 |
| S | 0.0918 |
| T | 0.0737 |
| U | 0.0558 |
| A | 0.0518 |
| X | 0.0426 |
| Y | 0.0444 |
| B | 0.0363 |
| V | 0.0488 |
| W | 0.0407 |
| Z | 0.0243 |
| C | 0.0102 |
| D | 0.0116 |
| E | 0.0094 |
| G | 0.0007 |
| H | 0.0017 |
| I | 0.0007 |

**Notes:** All balances queried via Aptos view function `0x1::coin::balance` (CoinStore resources not registered; view function required).

### Multisig Contract Probes

All 5 multisig contracts queried via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ healthy |
| A-G | 0xf56c4a1c... | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181... | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9... | 2 | ✓ healthy |
| V-W | 0x40fad7b4... | 2 | ✓ healthy |

All multisigs are 2-of-N and responding normally.

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — site returns a Next.js SPA shell. No REST/JSON API endpoint found at `/api/markets`, `/api/v1/markets`, or root. Market data requires JavaScript execution. Recorded as `unavailable` in `mnx_snapshots`.

---

## DuckDB Schema Summary

```
world_increments  — 143 rows  (GF3 color-tagged increment ledger)
repo_snapshots    — 1064 rows (GitHub repo state history)
aptos_snapshots   —   28 rows (Hamming swarm wallet balances)
multisig_probes   —    5 rows (multisig health checks)
mnx_snapshots     —    1 row  (MNX market: unavailable)
```
