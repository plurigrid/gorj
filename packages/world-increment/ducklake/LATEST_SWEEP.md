# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-11  
**Branch:** world-increment/sweep-$(date +%Y-%m-%d-%H%M)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| bmorphism | user | 100 | 509 |
| plurigrid | org | 100 | 156 |
| kubeflow | org | 48 | 101,916 |
| AustinCStone | user (zubyul graph) | 40 | 324 |
| TeglonLabs | org | 5 | 14 |
| zubyul | user | 49 | 40 |
| migalkin | user (zubyul graph) | 19 | 834 |
| wasita | user (zubyul graph) | 11 | 11 |
| kristinezheng | user (zubyul graph) | 5 | 0 |
| M1shaaa | user (zubyul graph) | 8 | 0 |
| DJedamski | user (zubyul graph) | 6 | 17 |

**Total repos snapshotted: 391** (stored as 1,335 rows with GF3 chain)

### GF(3) Color Chain Applied

| Trit | Name | Color | Sources |
|------|------|-------|---------|
| 0 | ERGODIC | #d3869b | plurigrid, wasita, kristinezheng, ... |
| 1 | PLUS | #b8bb26 | kubeflow, migalkin, DJedamski, ... |
| -1 | MINUS | #cc241d | bmorphism, zubyul, TeglonLabs, ... |

### Notable Repos

- **plurigrid/gorj** — 493 open issues, pushed 2026-06-11 (this repo!)
- **plurigrid/asi** — 25⭐ "everything is topological chemputer!"
- **bmorphism/ocaml-mcp-sdk** — 61⭐ OCaml SDK for MCP using Jane Street's oxcaml_effect
- **bmorphism/say-mcp-server** — 20⭐ macOS text-to-speech MCP
- **bmorphism/Gay.jl** — 1⭐, 189 open issues — wide-gamut color sampling
- **kubeflow** — 101,916 total stars across 48 repos (dominant by stars)
- **TeglonLabs/jank-crane** — pushed 2026-06-08, crane-jank GF3 convergence maps
- **migalkin** — 834 total stars, graph ML focus

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Timestamp:** 2026-06-11T06:11 UTC  
**Addresses probed:** 28 (alice, bob, A–Z)

| World | Balance (APT) | Status |
|-------|--------------|--------|
| alice | 0.00 | unfunded |
| bob | 0.00 | unfunded |
| A–Z | 0.00 each | unfunded |

All 28 addresses returned valid API responses (CoinStore resource exists), with 0 APT balance. Accounts are initialized on-chain but hold no APT.

### Multisig Contract Probes (5/5 healthy)

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428... | 2 | ✅ healthy |
| A-G | 0xf56c4a1c... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe181... | 2 | ✅ healthy |
| S-T | 0x3b1c3ae9... | 2 | ✅ healthy |
| V-W | 0x40fad7b4... | 2 | ✅ healthy |

All 5 multisig accounts respond with `num_signatures_required = 2` (2-of-N threshold confirmed healthy).

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Protected by Vercel deployment authentication. No market data extractable without bypass token or OIDC trusted source config.

---

## DuckDB Ducklake Schema

**Path:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1,335 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

---

## Summary

- **GitHub sweep:** 391 repos across 11 sources (3 orgs + 8 users), GF(3) trit coloring applied per source
- **Aptos Hamming swarm:** 28/28 wallets reachable, all 0 APT; 5/5 multisigs healthy at 2-of-N
- **MNX:** Auth-gated on Vercel, unavailable without credentials
