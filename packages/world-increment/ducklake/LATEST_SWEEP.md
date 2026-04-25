# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-04-25 04:12 UTC
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| plurigrid | org | 100 | 65 |
| kubeflow | org | 47 | 33,939 |
| TeglonLabs | org | 4 | 2 |
| bmorphism | user | 100 | 246 |
| zubyul | user | 49 | 14 |
| migalkin | user (zubyul social) | 19 | 278 |
| DJedamski | user (zubyul social) | 6 | 3 |
| wasita | user (zubyul social) | 10 | 4 |
| kristinezheng | user (zubyul social) | 6 | 0 |
| M1shaaa | user (zubyul social) | 8 | 0 |
| AustinCStone | user (zubyul social) | 40 | 108 |
| **TOTAL** | | **389** | **34,659** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 129 |
| 1 | `#b8bb26` | PLUS | 130 |
| -1 | `#cc241d` | MINUS | 130 |

### Notes
- GitHub API direct curl: blocked 403 in sandbox; used MCP search_repositories
- Events for bmorphism/zubyul: unavailable (no API token)
- M1shaaa profile repo pushed 2026-04-25 02:05 (active today)
- wasita/wasita.github.io pushed 2026-04-22 (recently active)
- kristinezheng/kristinezheng.github.io pushed 2026-04-09 (recently active)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Aptos mainnet node reached (ledger version 4,997,493,731 / epoch 15,564 / block 731,960,868).

All 28 probed addresses (alice, bob, A-Z) returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — addresses are defined but
have zero APT (coin store not initialized = never received APT).

| Range | Count | Total APT |
|-------|-------|-----------|
| alice, bob | 2 | 0.0 |
| A through Z | 26 | 0.0 |
| **Total** | **28** | **0.0** |

### Multisig Contracts

All probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

All 5 multisig contracts are live on Aptos mainnet, each requiring 2-of-N signatures.

### MNX Markets

`testnet.mnx.fi` — HTTP 503 "DNS cache overflow" — **unavailable** from this network.

---

## DuckDB Schema

```sql
world_increments  -- 389 rows (GF3 color-tagged repo events)
repo_snapshots    -- 389 rows (full metadata: org, language, stars, forks)
aptos_snapshots   -- 28 rows (all zero APT, uninitialized addresses)
multisig_probes   -- 5 rows (all require 2 sigs, all healthy)
mnx_snapshots     -- 0 rows (503 unavailable)
```

---

*Next sweep recommended: 2026-04-26 04:12 UTC*
