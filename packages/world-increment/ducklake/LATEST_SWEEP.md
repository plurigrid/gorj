# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-04-13  
**Branch:** world-increment/sweep  
**GF(3) Color Chain:** trit=0 → ERGODIC #d3869b | trit=1 → PLUS #b8bb26 | trit=-1 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Fetched | Status |
|--------|------|--------------|--------|
| plurigrid | org | 100 | captured |
| kubeflow | org | — | rate-limited |
| TeglonLabs | org | — | rate-limited |
| bmorphism | user | — | rate-limited |
| zubyul | user | — | rate-limited |
| migalkin | user (social) | — | rate-limited |
| DJedamski | user (social) | — | rate-limited |
| wasita | user (social) | — | rate-limited |
| kristinezheng | user (social) | — | rate-limited |
| M1shaaa | user (social) | — | rate-limited |
| AustinCStone | user (social) | — | rate-limited |

> GitHub unauthenticated API rate limit (60 req/hr) exhausted after plurigrid fetch. Reset at 14:42 UTC.

### Top Plurigrid Repos (by stars)

| Repo | Language | Stars | Forks | Open Issues | Last Push |
|------|----------|-------|-------|-------------|-----------|
| plurigrid/asi | HTML | 16 | 5 | 3 | 2026-04-10 |
| plurigrid/ontology | JavaScript | 7 | 9 | 16 | 2025-05-27 |
| plurigrid/asi-skills | Julia | 3 | 1 | 2 | 2026-04-09 |
| plurigrid/zig-syrup | Zig | 2 | 2 | 2 | 2026-04-09 |
| plurigrid/horse | TeX | 1 | 1 | 7 | 2026-04-10 |
| plurigrid/gorj | Clojure | 0 | 0 | 168 | 2026-04-13 |

### Language Distribution (plurigrid, this sweep)

| Language | Repos | Total Stars |
|----------|-------|-------------|
| Python | 84 | cumulative |
| Rust | 24 | 8 |
| HTML | 21 | 245 |
| Go | 21 | 3,969 |
| JavaScript | 15 | 45 |
| Clojure | 13 | 3 |
| TypeScript | 12 | 331 |

### GF(3) World-Increment Chain (latest 5)

| ID | Trit | Color | Name | Source | Event |
|----|------|-------|------|--------|-------|
| 17 | +1 | #b8bb26 | PLUS | org/plurigrid | repo_sweep |
| 16 | -1 | #cc241d | MINUS | org/kubeflow | repo_sweep_ratelimited |
| 15 | 0 | #d3869b | ERGODIC | org/TeglonLabs | repo_sweep_ratelimited |
| 14 | +1 | #b8bb26 | PLUS | user/bmorphism | repo_sweep_ratelimited |
| 13 | -1 | #cc241d | MINUS | user/zubyul | repo_sweep_ratelimited |

### DuckDB Table State

| Table | Rows |
|-------|------|
| world_increments | 17 |
| repo_snapshots | 571 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, ledger v4860475943)

All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
Result: **resource_not_found** for all — accounts exist (address A: seq=58) but use Fungible Asset (FA)
module rather than legacy CoinStore. Legacy CoinStore balance = 0.0 APT for all.

| World | Address (truncated) | CoinStore APT |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...51b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...ec948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...d0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

> Note: To query FA balances use `0x1::primary_fungible_store::balance` view function.

### Multisig Contract Probes

All 5 multisig contracts responded healthy with **2-of-N threshold**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...7003 | 2 | true |
| A-G | 0xf56c4a1c...0096 | 2 | true |
| Y-Z | 0xd3ffe181...b883 | 2 | true |
| S-T | 0x3b1c3ae9...7883 | 2 | true |
| V-W | 0x40fad7b4...eb6d | 2 | true |

**Swarm health: 5/5 multisig contracts operational**

### MNX Markets (testnet.mnx.fi)

Status: **SPA — no public REST API endpoints accessible**. Site returned 292KB JS bundle with no
`/api/*` routes responding. Market data loads client-side via WebSocket or authenticated session.
Recorded as `SPA_UNAVAILABLE` in `mnx_snapshots`.

---

## Storage

```
packages/world-increment/ducklake/
  world-increments.duckdb    # DuckDB v1.5.2 ducklake (5 tables, 622 rows total)
  LATEST_SWEEP.md            # This file
  schema.sql                 # Schema reference
```

**Aptos ledger version:** 4860475943  
**Sweep timestamp:** 2026-04-13T~14:42 UTC  
**GF(3) increment IDs this sweep:** 13-17
