# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep Timestamp:** 2026-05-13T14:13:41Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source Type | Name | Repos Captured |
|---|---|---|
| org | plurigrid | 100 |
| org | kubeflow | 48 |
| org | TeglonLabs | 4 |
| user | bmorphism | 100 |
| user | zubyul | 49 |
| social graph | migalkin | 0 (no public repos) |
| social graph | DJedamski | 0 (no public repos) |
| social graph | wasita | 0 (no public repos) |
| social graph | kristinezheng | 0 (no public repos) |
| social graph | M1shaaa | 0 (no public repos) |
| social graph | AustinCStone | 0 (no public repos) |

**Total repo snapshots captured: 301**

### TeglonLabs Repos (inline)

| Repo | Language | Stars | Forks | Issues | Last Push |
|---|---|---|---|---|---|
| mathpix-gem | Ruby | 2 | 0 | 11 | 2026-01-01 |
| monad-mcp-server | — | 0 | 0 | 0 | 2025-05-14 |
| topoi | Python | 0 | 0 | 1 | 2025-01-24 |
| coin-flip-mcp | JavaScript | 0 | 2 | 1 | 2025-09-21 |

### GF(3) World-Increment Color Chain

| Trit | Color | Name | Count |
|---|---|---|---|
| 0 | #d3869b | ERGODIC | 11 |
| +1 | #b8bb26 | PLUS | 13 |
| -1 | #cc241d | MINUS | 13 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

| World | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

> All 28 Hamming swarm wallets returned balance 0.0 APT. Accounts exist on-chain but hold no liquid APT in their CoinStore at time of sweep.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

> All 5 multisig contracts respond and require 2-of-N signatures. All healthy.

### MNX Markets (testnet.mnx.fi)

> Status: **Unavailable via API**. `testnet.mnx.fi` is a Next.js SPA; no JSON API endpoint found at `/api/markets`, `/api/v1/markets`, or `/markets`. Market data could not be extracted without browser-side JavaScript execution. Zero rows in `mnx_snapshots`.

---

## DuckDB Schema Summary

```
world_increments   : 37 rows   (GF3 color-chained sweep events)
repo_snapshots     : 1245 rows (GitHub repo metadata)
aptos_snapshots    : 28 rows   (Hamming swarm wallet balances)
multisig_probes    : 5 rows    (2-of-N multisig health checks)
mnx_snapshots      : 0 rows    (SPA — no API data available)
```
