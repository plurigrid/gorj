# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-27T19:30Z  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 11 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 30 |
| **TOTAL** | | **381** |

### GF(3) Color Chain Distribution

| GF3 Trit | Color | Name | Count |
|----------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 127 |
| +1 | `#b8bb26` | PLUS | 127 |
| -1 | `#cc241d` | MINUS | 127 |

### Top Starred Repos

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,749 | 2026-06-18 |
| kubeflow/pipelines | Python | 4,158 | 2026-06-27 |
| kubeflow/spark-operator | Python | 3,129 | 2026-06-26 |
| kubeflow/trainer | Go | 2,125 | 2026-06-26 |
| kubeflow/katib | Python | 1,687 | 2026-06-23 |
| migalkin/StarE | Python | 89 | 2023-12-01 |

### Most Recently Active (June 2026)

| Repo | Language | Last Push |
|------|----------|-----------|
| plurigrid/gorj | Clojure | 2026-06-27 19:11Z |
| kubeflow/hub | Go | 2026-06-27 17:16Z |
| kubeflow/pipelines | Python | 2026-06-27 15:18Z |
| M1shaaa/M1shaaa | — | 2026-06-27 13:25Z |
| plurigrid/place | TeX | 2026-06-27 05:53Z |
| bmorphism/Gay.jl | Julia | 2026-06-27 00:38Z |
| wasita/wasita.github.io | Svelte | 2026-06-25 16:23Z |
| TeglonLabs/jank-crane | C++ | 2026-06-08 19:03Z |

### Notable TeglonLabs Repos

- **jank-crane** (C++): "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow" — pushed 2026-06-08
- **mathpix-gem** (Ruby, 2 stars): Mathematical OCR gem — pushed 2026-01-01
- **coin-flip-mcp** (JavaScript, 2 forks): MCP server for random.org coin flips

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

**Date:** 2026-06-27  
**All 28 addresses queried** (alice, bob, A-Z)  
**Result: All wallets show 0 APT** — no initialized `0x1::coin::CoinStore` resource found on mainnet for any address in the hamming swarm. This indicates the wallets have not been seeded with APT or have never executed a coin-store initialization transaction.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793ac... | 0.00 |
| bob | 0x0a3c00... | 0.00 |
| A-Z (26) | various | 0.00 each |

### Multisig Contract Probes

All 5 multisig accounts are **healthy** and require **2 signatures**.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | healthy |
| A-G | 0xf56c4a... | 2 | healthy |
| Y-Z | 0xd3ffe1... | 2 | healthy |
| S-T | 0x3b1c3a... | 2 | healthy |
| V-W | 0x40fad7... | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — testnet.mnx.fi requires Vercel deployment protection authentication (HTTP 401). Market data could not be retrieved without a bypass token or Trusted Source OIDC configuration.

---

## DuckDB Schema Summary

```
world_increments: 381 rows  (GF3-tagged github events)
repo_snapshots:   381 rows  (per-repo metadata snapshot)
aptos_snapshots:   28 rows  (hamming swarm wallet balances)
multisig_probes:    5 rows  (2-of-N multisig health)
mnx_snapshots:      0 rows  (unavailable - Vercel auth gate)
```
