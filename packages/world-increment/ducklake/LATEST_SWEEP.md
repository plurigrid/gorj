# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-05-02T07:08 UTC  
**World increment id:** 13  
**GF(3) position:** trit=1 · PLUS · `#b8bb26`  
**Session:** https://claude.ai/code/session_012vWCeQkrNm1dqw6ng7Xw79

---

## JOB 1 — GitHub Social Graph Sweep

### Status

| Source | Type | Repos captured | Note |
|--------|------|---------------|------|
| plurigrid/gorj | org repo | 1 | Via MCP GitHub tool (restricted scope) |
| kubeflow | org | 0 | GitHub API rate-limited (0/60 remaining) |
| TeglonLabs | org | 0 | GitHub API rate-limited |
| bmorphism | user | 0 | GitHub API rate-limited |
| zubyul | user | 0 | GitHub API rate-limited |
| migalkin | user (zubyul graph) | 0 | GitHub API rate-limited |
| DJedamski | user (zubyul graph) | 0 | GitHub API rate-limited |
| wasita | user (zubyul graph) | 0 | GitHub API rate-limited |
| kristinezheng | user (zubyul graph) | 0 | GitHub API rate-limited |
| M1shaaa | user (zubyul graph) | 0 | GitHub API rate-limited |
| AustinCStone | user (zubyul graph) | 0 | GitHub API rate-limited |

**GitHub API constraint:** unauthenticated public API exhausted (60 req/hr cap); `gh` CLI not installed; MCP tools scoped to `plurigrid/gorj` only. Rate limit resets at next UTC hour.

### plurigrid/gorj snapshot

- **Full name:** plurigrid/gorj  
- **Language:** Clojure  
- **Description:** MCP server + hooks that give AI coding agents a Clojure REPL  
- **Last pushed:** 2026-04-14T18:07:32Z  
- **Recent commits (20):** world-increment ducklake sweeps, hamming snapshots, GF3 color chain

### DuckDB state

| Table | Total rows |
|-------|-----------|
| world_increments | 24 (13 increment ids) |
| repo_snapshots | 955 |
| aptos_snapshots | 28+ |
| multisig_probes | 5+ |
| mnx_snapshots | 1+ |

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-05-02)

All 28 addresses queried against `fullnode.mainnet.aptoslabs.com`. All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — indicating accounts have no APT CoinStore resource (zero balance or uninitialized).

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...12d5 | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts responded healthy with `num_signatures_required = 2`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...003 | 2 | true |
| A-G | 0xf56c...096 | 2 | true |
| Y-Z | 0xd3ff...883 | 2 | true |
| S-T | 0x3b1c...883 | 2 | true |
| V-W | 0x40fa...b6d | 2 | true |

All multisigs: **2-of-2 threshold, all healthy**.

### MNX Markets (testnet.mnx.fi)

Site reachable (HTTP 200 at `/markets`). Pure Next.js SPA — market data loads client-side after wallet connection. No public JSON API endpoints found (`/api/markets`, `/api/v1/markets`, `/api/tickers` all 404). **Market data: unavailable without wallet auth.**

---

## GF(3) Color Chain — Increment History

| id | GF3 | Color | Name | Source | Event |
|----|-----|-------|------|--------|-------|
| 1 | +1 | `#b8bb26` | PLUS | plurigrid | repo_sweep |
| 2 | -1 | `#cc241d` | MINUS | kubeflow | repo_sweep |
| 3 | 0 | `#d3869b` | ERGODIC | TeglonLabs | repo_sweep |
| 4 | +1 | `#b8bb26` | PLUS | bmorphism | repo_sweep |
| 5 | -1 | `#cc241d` | MINUS | zubyul | repo_sweep |
| ... | ... | ... | ... | ... | ... |
| 12 | 0 | `#d3869b` | ERGODIC | bmorphism | sweep_complete |
| **13** | **+1** | **`#b8bb26`** | **PLUS** | **plurigrid** | **world_sweep** |

Next increment: id=14 → `14%3=2` → trit=-1 → **MINUS `#cc241d`**
