# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-06  
**Increment ID:** 13  
**GF(3) Color:** PLUS · trit=1 · #b8bb26  
**Sweep hash:** 5b28fe016e0e3d0b0f22e35e01f7db0722d988e1 (plurigrid/gorj HEAD)

---

## JOB 1: GitHub Social Graph Sweep

### Access Status

The GitHub REST API (`api.github.com`) is proxy-blocked in this environment for repositories outside the session scope (`plurigrid/gorj`). Direct curl to `/orgs/{org}/repos` returned:
> "This GitHub API path is not available: sessions are bound to their configured repositories."

Confirmed accessible: **plurigrid/gorj** (via GitHub MCP).

### Repo Snapshot

| id  | org/user  | repo | language | pushed_at |
|-----|-----------|------|----------|-----------|
| 474 | plurigrid | gorj | Clojure  | 2026-05-08T14:04:34Z |

**Total repo snapshots in DB:** 945 (944 from prior sweeps + 1 this run)  
**Total world increments:** 13 (completing 4th GF(3) cycle + 1 into 5th)

### GF(3) Color Chain

| id%3 | trit | color   | name    |
|------|------|---------|---------|
|  0   |  0   | #d3869b | ERGODIC |
|  1   |  1   | #b8bb26 | PLUS    |
|  2   | -1   | #cc241d | MINUS   |

Increment 13 → 13%3=1 → **PLUS** (#b8bb26)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-08-06)

All 28 addresses (alice, bob, A–Z) queried against Aptos mainnet at ledger v6641347083+.  
**Result:** All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

This indicates these accounts either:
- Hold APT via the newer **FungibleAsset** store (not legacy CoinStore), or
- Have zero on-chain activity under the legacy resource

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 (resource_not_found) |
| bob   | 0x0a3c...2d5d | 0.0 (resource_not_found) |
| A     | 0x8699...9d7a | 0.0 (resource_not_found) |
| B     | 0x3f89...b13  | 0.0 (resource_not_found) |
| C     | 0x38b9...35e  | 0.0 (resource_not_found) |
| D     | 0xf776...dd1  | 0.0 (resource_not_found) |
| E     | 0xdc1d...d36  | 0.0 (resource_not_found) |
| F     | 0x18a1...f71  | 0.0 (resource_not_found) |
| G     | 0x69a3...f32  | 0.0 (resource_not_found) |
| H     | 0xce67...00f  | 0.0 (resource_not_found) |
| I     | 0x070f...fc9  | 0.0 (resource_not_found) |
| J     | 0x4d96...f54  | 0.0 (resource_not_found) |
| K     | 0xa732...dc4  | 0.0 (resource_not_found) |
| L     | 0x7c2e...ba9  | 0.0 (resource_not_found) |
| M     | 0x6fed...2e9  | 0.0 (resource_not_found) |
| N     | 0xe7dd...b2c  | 0.0 (resource_not_found) |
| O     | 0x7325...89d  | 0.0 (resource_not_found) |
| P     | 0x6218...948  | 0.0 (resource_not_found) |
| Q     | 0xac40...89a9 | 0.0 (resource_not_found) |
| R     | 0x7ce6...e10  | 0.0 (resource_not_found) |
| S     | 0xb875...386  | 0.0 (resource_not_found) |
| T     | 0x3578...588  | 0.0 (resource_not_found) |
| U     | 0x7586...956  | 0.0 (resource_not_found) |
| V     | 0xb59d...2c3  | 0.0 (resource_not_found) |
| W     | 0x5f32...7b0  | 0.0 (resource_not_found) |
| X     | 0xa95c...47d  | 0.0 (resource_not_found) |
| Y     | 0xd8e3...44c4 | 0.0 (resource_not_found) |
| Z     | 0x7af0...97c  | 0.0 (resource_not_found) |

### Multisig Probes (5/5 HEALTHY)

All 5 multisig contracts returned `num_signatures_required = 2`. All healthy.

| Pair | Address (truncated) | sigs_required | Status |
|------|---------------------|---------------|--------|
| A-B  | 0x0da4...003 | 2 | ✓ HEALTHY |
| A-G  | 0xf56c...096 | 2 | ✓ HEALTHY |
| Y-Z  | 0xd3ff...883 | 2 | ✓ HEALTHY |
| S-T  | 0x3b1c...883 | 2 | ✓ HEALTHY |
| V-W  | 0x40fa...b6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

Testnet MNX is a Next.js SPA — no REST API endpoints responded with JSON data (`/api/markets`, `/api/v1/markets`, `/api/tickers` all returned HTML). Market data **unavailable** via server-side scraping.

---

## DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 13 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
