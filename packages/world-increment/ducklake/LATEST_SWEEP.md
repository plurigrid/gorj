# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-06-28  
**GF(3) color chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d (cycling)

---

## JOB 1: GitHub Social Graph Sweep

**Total repos snapshotted:** 381 across 11 sources

### Orgs

| Org | Repos | Top Repo | Stars |
|-----|-------|----------|-------|
| plurigrid | 100 | plurigrid/asi (HTML) | 26 |
| kubeflow | 48 | kubeflow/kubeflow | 15749 |
| TeglonLabs | 5 | TeglonLabs/mathpix-gem (Ruby) | 2 |

### Users (primary)

| User | Repos | Top Repo | Stars | Last Push |
|------|-------|----------|-------|-----------|
| bmorphism | 100 | bmorphism/ocaml-mcp-sdk (OCaml) | 61 | 2026-06-28 |
| zubyul | 49 | zubyul/WGCNA (HTML) | 2 | 2026-04-24 |

### Zubyul Social Graph

| User | Repos | Top Repo | Stars |
|------|-------|----------|-------|
| migalkin | 19 | migalkin/NodePiece (Python) | 144 |
| wasita | 11 | wasita/wasita.github.io (Svelte) | 1 |
| kristinezheng | 5 | kristinezheng/lookit-jenga (Jupyter) | 0 |
| M1shaaa | 8 | M1shaaa/M1shaaa | 0 |
| DJedamski | 6 | DJedamski/School (R) | 1 |
| AustinCStone | 30 | AustinCStone/TextGAN (Python) | 92 |

### GF(3) World Increment Records

| id | source | gf3_trit | color | name |
|----|--------|----------|-------|------|
| 1 | plurigrid | 1 | #b8bb26 | PLUS |
| 2 | kubeflow | 2 | #cc241d | MINUS |
| 3 | bmorphism | 0 | #d3869b | ERGODIC |
| 4 | zubyul | 1 | #b8bb26 | PLUS |
| 5 | migalkin | 2 | #cc241d | MINUS |
| 6 | wasita | 0 | #d3869b | ERGODIC |
| 7 | AustinCStone | 1 | #b8bb26 | PLUS |
| 8 | TeglonLabs | 2 | #cc241d | MINUS |
| 9 | DJedamski | 0 | #d3869b | ERGODIC |
| 10 | kristinezheng | 1 | #b8bb26 | PLUS |
| 11 | M1shaaa | 2 | #cc241d | MINUS |

**Notable recent activity:**
- `plurigrid/asi` pushed 2026-06-28 (stars: 26, "everything is topological chemputer!")
- `plurigrid/gorj` pushed 2026-06-28 (875 open issues — forj+Rama topology nREPL)
- `bmorphism/Gay.jl` (Julia) pushed 2026-06-28 (187 open issues)
- `M1shaaa/M1shaaa` pushed 2026-06-28
- `wasita/wasita.github.io` (Svelte) pushed 2026-06-25

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 addresses (alice, bob, A–Z) via Aptos fullnode mainnet.  
**Result:** All addresses returned 0 APT — CoinStore resource not found or accounts unfunded.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793acd... | 0.0 |
| bob | 0x0a3c00c... | 0.0 |
| A–Z | (26 addrs) | 0.0 each |

> Note: `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource absent for all addresses.  
> Addresses may be pre-funded or on a different layer.

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig contracts responded healthy with `num_signatures_required = 2`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | HEALTHY |
| A-G | 0xf56c4a1c... | 2 | HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | HEALTHY |
| V-W | 0x40fad7b4... | 2 | HEALTHY |

**Interpretation:** All pairs require 2-of-N signatures. Contract infrastructure operational.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` requires Vercel authentication (Protection Bypass token needed). API endpoints (`/api/markets`, `/api/v1/markets`) returned auth-gated SPA. No market data extractable without credentials.

---

## Database Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 381 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth-gated) |

**DuckDB version:** v1.5.4 (Variegata)  
**Sweep timestamp:** 2026-06-28
