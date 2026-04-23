# World Increment Sweep + Hamming Snapshot

**Date:** 2026-04-23  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) Color Chain:** ERGODIC `#d3869b` (trit=0) · PLUS `#b8bb26` (trit=1) · MINUS `#cc241d` (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 48 |
| migalkin | user (zubyul social graph) | 19 |
| DJedamski | user (zubyul social graph) | 6 |
| wasita | user (zubyul social graph) | 10 |
| kristinezheng | user (zubyul social graph) | 6 |
| M1shaaa | user (zubyul social graph) | 8 |
| AustinCStone | user (zubyul social graph) | 40 |
| **TOTAL** | | **388** |

### Notable Repos

- `plurigrid/*` — 100 repos, broad Clojure/AI/energy systems portfolio
- `kubeflow/*` — 47 repos, ML platform on Kubernetes  
- `TeglonLabs/mathpix-gem` — Ruby gem for math OCR (Ruby, ★2, pushed 2026-01-01)
- `TeglonLabs/coin-flip-mcp` — MCP random coin flipper (JS, 2 forks)
- `bmorphism/*` — 100 repos, broad research/tools portfolio
- `wasita/wasita.github.io` — Svelte personal site (pushed 2026-04-22, most recent)
- `M1shaaa/M1shaaa` — profile repo (pushed 2026-04-23, today)
- `AustinCStone/*` — 40 repos, ML/CV research portfolio

### DuckDB Tables

- `world_increments` — GF(3)-colored event log (411 rows)
- `repo_snapshots` — full repo metadata with stars/forks/language

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 addresses (alice, bob, A–Z) queried via Aptos fullnode API.

**Result:** All addresses returned 0.0 APT — no `CoinStore<AptosCoin>` resource found on mainnet at these addresses. Addresses appear to be testnet/devnet addresses not holding mainnet APT.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A | 0x8699ed... | 0.0 |
| B–Z | ... | 0.0 each |

### Multisig Contracts (5 probes)

All probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | ✅ |
| A-G | 0xf56c4a... | 2 | ✅ |
| Y-Z | 0xd3ffe1... | 2 | ✅ |
| S-T | 0x3b1c3a... | 2 | ✅ |
| V-W | 0x40fad7... | 2 | ✅ |

**All 5 multisig contracts:** 2-of-2 threshold, contract responsive, marked healthy.

### MNX Markets (testnet.mnx.fi)

`/api/markets` → 404 (Next.js SPA, no server-rendered market data exposed). Market data **unavailable** via public API. `mnx_snapshots` table is empty.

### DuckDB Tables

- `aptos_snapshots` — 28 rows (all 0.0 APT)
- `multisig_probes` — 5 rows (all 2-of-2, healthy=true)
- `mnx_snapshots` — 0 rows (API unavailable)

---

## Summary

| Metric | Value |
|--------|-------|
| GitHub repos snapshotted | 388 |
| World increment events | 411 |
| Aptos addresses probed | 28 |
| Total APT across swarm | 0.0 |
| Multisig contracts probed | 5 |
| Multisig contracts healthy | 5/5 |
| MNX market data | Unavailable (404) |

