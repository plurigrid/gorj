# World Increment Sweep + Hamming Snapshot

**Sweep Date:** 2026-08-04  
**Increment ID:** 13  
**GF(3) Color:** PLUS — trit=1, #b8bb26  
**Snapshot Hash:** `5b28fe016e0e3d0b0f22e35e01f7db0722d988e1`

---

## JOB 1: GitHub Social Graph Sweep

### Scope Note

GitHub API access in this session is proxy-restricted to `plurigrid/gorj` only. Calls to org/user repo listing endpoints for `plurigrid`, `kubeflow`, `TeglonLabs`, `bmorphism`, `zubyul`, and the zubyul social graph (`migalkin`, `DJedamski`, `wasita`, `kristinezheng`, `M1shaaa`, `AustinCStone`) were denied by the environment's network policy, which enforces repository-scoped access.

### plurigrid/gorj (in-scope)

| Field | Value |
|-------|-------|
| Repo | plurigrid/gorj |
| Language | Clojure |
| Latest Commit | `5b28fe0` — 2026-05-08 |
| Author | claude (noreply@anthropic.com) |
| Commit Message | `chore: ignore duckdb binary in repo root` |
| Active Sweep Branches | 51+ `world-increment/sweep-*` branches |
| Total Increments | 24 rows (IDs 1–13, some with multiple event_type rows) |
| Total Repo Snapshots | 945 |

### Recent Commits (plurigrid/gorj)

| SHA (short) | Date | Message |
|-------------|------|---------|
| `5b28fe0` | 2026-05-08 | chore: ignore duckdb binary in repo root |
| `ebf263f` | 2026-04-14 | world-increment ducklake: sync world.duckdb sweep state |
| `b434a43` | 2026-04-14 | Merge sweep state into master |
| `e76792f` | 2026-04-14 | world-increments.duckdb: sync latest sweep state |
| `6315180` | 2026-04-12 | world-increment sweep 2026-04-12: insert id=12 ERGODIC |

### GF(3) Chain State

| ID | GF3 | Color | Name | Event |
|----|-----|-------|------|-------|
| 10 | +1 | #b8bb26 | PLUS | repo_sweep |
| 11 | -1 | #cc241d | MINUS | repo_sweep |
| 12 | 0 | #d3869b | ERGODIC | sweep_complete |
| **13** | **+1** | **#b8bb26** | **PLUS** | **sweep_complete** ← _this run_ |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried via Aptos fullnode mainnet API. All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`, indicating no initialized APT balance on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...2d5d | 0.00000000 |
| A | 0x8699...e9d7a | 0.00000000 |
| B | 0x3f89...cb13 | 0.00000000 |
| C | 0x38b9...535e | 0.00000000 |
| D | 0xf776...fdd1 | 0.00000000 |
| E | 0xdc1d...8d36 | 0.00000000 |
| F | 0x18a1...cf71 | 0.00000000 |
| G | 0x69a3...7f32 | 0.00000000 |
| H | 0xce67...300f | 0.00000000 |
| I | 0x070f...1fc9 | 0.00000000 |
| J | 0x4d96...7f54 | 0.00000000 |
| K | 0xa732...25dc4 | 0.00000000 |
| L | 0x7c2e...eba9 | 0.00000000 |
| M | 0x6fed...f2e9 | 0.00000000 |
| N | 0xe7dd...1b2c | 0.00000000 |
| O | 0x7325...a89d | 0.00000000 |
| P | 0x6218...c948 | 0.00000000 |
| Q | 0xac40...c89a9 | 0.00000000 |
| R | 0x7ce6...6e10 | 0.00000000 |
| S | 0xb875...d386 | 0.00000000 |
| T | 0x3578...f588 | 0.00000000 |
| U | 0x7586...f956 | 0.00000000 |
| V | 0xb59d...af2c3 | 0.00000000 |
| W | 0x5f32...c7b0 | 0.00000000 |
| X | 0xa95c...047d | 0.00000000 |
| Y | 0xd8e3...44c4 | 0.00000000 |
| Z | 0x7af0...197c | 0.00000000 |

**Total wallets queried:** 28  
**Wallets with balance:** 0  
**Wallets with resource_not_found:** 28

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

**All 5 multisig contracts healthy** — each requires 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

Site is reachable (HTTP 200) but is a client-side Next.js SPA. No REST API endpoints found:

| Endpoint | Status |
|----------|--------|
| `/` | 200 (SPA shell) |
| `/api/markets` | 404 |
| `/api/v1/markets` | 404 |
| `/api/tickers` | 404 |
| `/ticker` | 200 (SPA shell) |
| `/markets` | 200 (SPA shell) |

**Result:** MNX testnet market data unavailable via static API — requires browser JS execution. Logged as `UNAVAILABLE` in mnx_snapshots.

---

## DuckDB State After This Sweep

| Table | Row Count |
|-------|-----------|
| world_increments | 24 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`
