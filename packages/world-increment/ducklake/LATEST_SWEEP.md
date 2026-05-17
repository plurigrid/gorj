# World Increment Sweep + Hamming Swarm Snapshot

**Sweep Date:** 2026-05-17 14:05 UTC  
**GF(3) Increment:** id=13, trit=1, color=#b8bb26 (PLUS)  
**Branch:** world-increment/sweep-2026-05-17

---

## JOB 1: GitHub Social Graph Sweep

### Sources Attempted
| Source | Type | Status |
|--------|------|--------|
| plurigrid | org | ✅ MCP tools (gorj repo) |
| kubeflow | org | ⚠️ API rate-limited (60 req/hr exhausted for shared IP) |
| TeglonLabs | org | ⚠️ API rate-limited |
| bmorphism | user | ⚠️ API rate-limited |
| zubyul | user | ⚠️ API rate-limited |
| migalkin | user (zubyul graph) | ⚠️ API rate-limited |
| DJedamski | user (zubyul graph) | ⚠️ API rate-limited |
| wasita | user (zubyul graph) | ⚠️ API rate-limited |
| kristinezheng | user (zubyul graph) | ⚠️ API rate-limited |
| M1shaaa | user (zubyul graph) | ⚠️ API rate-limited |
| AustinCStone | user (zubyul graph) | ⚠️ API rate-limited |

### plurigrid/gorj Snapshot (via GitHub MCP)
- **Branches:** 105 (including 100+ world-increment/sweep-* branches)
- **Latest Commit:** `5b28fe0` — chore: ignore duckdb binary in repo root (2026-05-08)
- **Description:** MCP server + hooks that give AI coding agents a Clojure REPL
- **Language:** Clojure

### DuckDB State After Sweep
| Table | Rows |
|-------|------|
| world_increments | 32 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`. All returned 0.0 APT — accounts hold no AptosCoin in CoinStore at time of snapshot.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A | 0x8699...be9d7a | 0.0 |
| B | 0x3f89...577cb13 | 0.0 |
| C | 0x38b9...91535e | 0.0 |
| D | 0xf776...fcfdd1 | 0.0 |
| E | 0xdc1d...958d36 | 0.0 |
| F | 0x18a1...3cf71 | 0.0 |
| G | 0x69a3...cc7f32 | 0.0 |
| H | 0xce67...5300f | 0.0 |
| I | 0x070f...c1fc9 | 0.0 |
| J | 0x4d96...87f54 | 0.0 |
| K | 0xa732...425dc4 | 0.0 |
| L | 0x7c2e...7eba9 | 0.0 |
| M | 0x6fed...7f2e9 | 0.0 |
| N | 0xe7dd...551b2c | 0.0 |
| O | 0x7325...5a89d | 0.0 |
| P | 0x6218...ec948 | 0.0 |
| Q | 0xac40...5c89a9 | 0.0 |
| R | 0x7ce6...76e10 | 0.0 |
| S | 0xb875...d0386 | 0.0 |
| T | 0x3578...f4588 | 0.0 |
| U | 0x7586...f9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...cc7b0 | 0.0 |
| X | 0xa95c...e33047d | 0.0 |
| Y | 0xd8e3...2444c4 | 0.0 |
| Z | 0x7af0...4e197c | 0.0 |

### Multisig Contract Probes
All 5 probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...87003 | 2 | ✅ |
| A-G | 0xf56c...c0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...d7883 | 2 | ✅ |
| V-W | 0x40fa...0eb6d | 2 | ✅ |

All 5 multisig contracts require **2-of-N** signatures and are healthy.

### MNX Markets (testnet.mnx.fi)
- SPA loaded (HTTP 200) — Next.js frontend
- `/api/markets`, `/api/v1/markets`, `/api/tickers` → all 404
- **Status: unavailable** — no public JSON API endpoints; market data not extractable from SPA

---

## GF(3) Color Chain

Current sweep: **id=13 → 13%3=1 → trit=1 → PLUS (#b8bb26)**

| trit | color | name |
|------|-------|------|
| 0 | #d3869b | ERGODIC |
| 1 | #b8bb26 | PLUS |
| -1 | #cc241d | MINUS |

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent · 2026-05-17*
