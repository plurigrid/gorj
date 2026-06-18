# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-06-18  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos | Notable |
|--------|------|-------|---------|
| plurigrid | org | 100 | `asi` 26★, `ontology` 8★, `vcg-auction` 7★, `gorj` 642 open issues |
| kubeflow | org | 48 | `kubeflow` 15,730★, `pipelines` 4,154★, `spark-operator` 3,127★ |
| TeglonLabs | org | 5 | `jank-crane` (GF3 convergence maps), `mathpix-gem` 2★ |
| bmorphism | user | 78 | `ocaml-mcp-sdk` 61★, `anti-bullshit-mcp-server` 23★, `say-mcp-server` 20★ |
| zubyul | user | 30 | `gay-world` (goblin world builder), `plurigrid-site` (11 open issues) |
| migalkin | user | 14 | `NodePiece` 144★, `StarE` 89★ (knowledge graph research) |
| DJedamski | user | 6 | Academic/data science repos, mostly archived |
| wasita | user | 11 | `wasita.github.io` active, `magic-garden` 2★ |
| kristinezheng | user | 5 | Cognitive science / neuroscience research |
| M1shaaa | user | 8 | Yale/lab research projects |
| AustinCStone | user | 17 | `TextGAN` 92★, `StereoVisionMRF` 11★; recent `bmfork`/`bmforkupdate` links to bmorphism |

**Total repos snapshotted:** 322  
**World increments recorded:** 11

### GF(3) Color Chain

| ID | Source | Trit | Color | Name |
|----|--------|------|-------|------|
| 1 | plurigrid | 1 | #b8bb26 | PLUS |
| 2 | kubeflow | -1 | #cc241d | MINUS |
| 3 | TeglonLabs | 0 | #d3869b | ERGODIC |
| 4 | bmorphism | 1 | #b8bb26 | PLUS |
| 5 | zubyul | -1 | #cc241d | MINUS |
| 6 | migalkin | 0 | #d3869b | ERGODIC |
| 7 | DJedamski | 1 | #b8bb26 | PLUS |
| 8 | wasita | -1 | #cc241d | MINUS |
| 9 | kristinezheng | 0 | #d3869b | ERGODIC |
| 10 | M1shaaa | 1 | #b8bb26 | PLUS |
| 11 | AustinCStone | -1 | #cc241d | MINUS |

### Notable Activity

- **plurigrid/gorj** (this repo): 642 open issues, last pushed 2026-06-17 — very active
- **plurigrid/eirobri**: 29 open issues, last pushed 2026-06-03
- **plurigrid/place**: last pushed 2026-06-15
- **plurigrid/asi**: 26 stars, last pushed 2026-06-10
- **bmorphism/Gay.jl**: 187 open issues (likely automated/bot)
- **bmorphism/satreadout**: new repo 2026-06-10, machine-checked Lean 4 math
- **TeglonLabs/jank-crane**: new 2026-06-08, GF3 convergence maps (directly relevant)
- **kubeflow/trainer** and **kubeflow/community-distribution**: very active as of 2026-06-18

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses queried. **All wallets returned 0 APT.**  
The Aptos fullnode returned 0 for the CoinStore<AptosCoin> resource on all addresses,
indicating either unfunded accounts or accounts not yet initialized on mainnet.

| Label | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5d | 0.0 |
| A-Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...87003 | **2** | healthy |
| A-G | 0xf56c...0096 | **2** | healthy |
| Y-Z | 0xd3ff...b883 | **2** | healthy |
| S-T | 0x3b1c...7883 | **2** | healthy |
| V-W | 0x40fa...eb6d | **2** | healthy |

All 5 multisig accounts require 2-of-N signatures and are responsive on mainnet.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `https://testnet.mnx.fi` returns HTTP 401 (Vercel deployment protection).  
No market data accessible without Vercel bypass credentials.

---

## DuckDB Tables

```
world_increments  — 11 rows  (GF3 color-chained source sweeps)
repo_snapshots    — 322 rows (GitHub repo metadata)
aptos_snapshots   — 28 rows  (Hamming swarm wallet balances)
multisig_probes   —  5 rows  (Aptos multisig health)
mnx_snapshots     —  0 rows  (unavailable, auth-protected)
```
