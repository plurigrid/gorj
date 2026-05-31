# World Increment Sweep + Hamming Snapshot
**Timestamp:** 2026-05-31  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) World Increments (11 sources)

| ID | Source | Type | GF(3) | Color |
|----|--------|------|-------|-------|
| 1 | plurigrid | org | PLUS (trit=1) | #b8bb26 |
| 2 | kubeflow | org | MINUS (trit=-1) | #cc241d |
| 3 | TeglonLabs | org | ERGODIC (trit=0) | #d3869b |
| 4 | bmorphism | user | PLUS (trit=1) | #b8bb26 |
| 5 | zubyul | user | MINUS (trit=-1) | #cc241d |
| 6 | migalkin | user | ERGODIC (trit=0) | #d3869b |
| 7 | DJedamski | user | PLUS (trit=1) | #b8bb26 |
| 8 | wasita | user | MINUS (trit=-1) | #cc241d |
| 9 | kristinezheng | user | ERGODIC (trit=0) | #d3869b |
| 10 | M1shaaa | user | PLUS (trit=1) | #b8bb26 |
| 11 | AustinCStone | user | MINUS (trit=-1) | #cc241d |

### Repo Snapshot Summary (146 total repos)

| Source | Repos Snapped | Top Repo | Stars |
|--------|--------------|----------|-------|
| plurigrid | 100 | plurigrid/asi | 23 |
| kubeflow | 11 | kubeflow/kubeflow | 15,695 |
| TeglonLabs | 4 | TeglonLabs/mathpix-gem | 2 |
| bmorphism | 10 | bmorphism/anti-bullshit-mcp-server | 23 |
| zubyul | 5 | zubyul/gay-world | 1 |
| migalkin | 4 | migalkin/NodePiece | 144 |
| DJedamski | 2 | DJedamski/Kaggle | 1 |
| wasita | 3 | wasita/magic-garden | 2 |
| kristinezheng | 2 | kristinezheng/Green-Machine | 0 |
| M1shaaa | 2 | M1shaaa/M1shaaa | 0 |
| AustinCStone | 3 | AustinCStone/TextGAN | 92 |

### Notable Activity
- **plurigrid/gorj** pushed 2026-05-31 (today) — 279 open issues
- **plurigrid/eirobri** pushed 2026-05-26 — EiRoBri replay world (Clojure)
- **kubeflow/sdk** pushed 2026-05-31 — Universal Python SDK for AI workloads on Kubernetes
- **bmorphism/Gay.jl** — 189 open issues, Julia wide-gamut color + GF(3) trit work
- **zubyul/voice-observatory** pushed 2026-04-24 — companion to bmorphism/say-mcp-server

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All addresses queried against Aptos mainnet `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Balance (APT) | Address (truncated) |
|-------|--------------|---------------------|
| alice | 0.0 | 0xc793...cc7b |
| bob | 0.0 | 0x0a3c...2d5d |
| A | 0.0 | 0x8699...9d7a |
| B | 0.0 | 0x3f89...cb13 |
| C | 0.0 | 0x38b9...535e |
| D | 0.0 | 0xf776...fdd1 |
| E | 0.0 | 0xdc1d...8d36 |
| F | 0.0 | 0x18a1...cf71 |
| G | 0.0 | 0x69a3...f32 |
| H | 0.0 | 0xce67...300f |
| I | 0.0 | 0x070f...1fc9 |
| J | 0.0 | 0x4d96...7f54 |
| K | 0.0 | 0xa732...5dc4 |
| L | 0.0 | 0x7c2e...eba9 |
| M | 0.0 | 0x6fed...7f2e9 |
| N | 0.0 | 0xe7dd...1b2c |
| O | 0.0 | 0x7325...a89d |
| P | 0.0 | 0x6218...c948 |
| Q | 0.0 | 0xac40...c89a9 |
| R | 0.0 | 0x7ce6...6e10 |
| S | 0.0 | 0xb875...d386 |
| T | 0.0 | 0x3578...f588 |
| U | 0.0 | 0x7586...f956 |
| V | 0.0 | 0xb59d...af2c3 |
| W | 0.0 | 0x5f32...c7b0 |
| X | 0.0 | 0xa95c...047d |
| Y | 0.0 | 0xd8e3...444c4 |
| Z | 0.0 | 0x7af0...197c |

**Total swarm APT:** 0.0 APT — all accounts have zero CoinStore balance on mainnet.

### Multisig Contract Probes (5 pairs)

All probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4...003 | 2 | HEALTHY |
| A-G | 0xf56c...096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | HEALTHY |
| S-T | 0x3b1c...883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

All 5 multisig accounts live on Aptos mainnet, each requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

Status: **SPA-ONLY** — `https://testnet.mnx.fi` serves a Next.js client-side application. No REST API endpoints (`/api/markets`, `/api/tickers`) accessible server-side. Market data unavailable via HTTP scrape; requires browser JS execution.

---

## DuckDB Schema Summary

```
world_increments   — 11 rows  (GF(3) trit chain per source)
repo_snapshots     — 146 rows (repos from 11 sources)
aptos_snapshots    — 28 rows  (Hamming swarm wallets, all 0 APT)
multisig_probes    —  5 rows  (all healthy, 2-of-N)
mnx_snapshots      —  0 rows  (SPA, no accessible REST API)
```
