# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-25

## Sweep Metadata
- **Date:** 2026-04-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 34 |
| New Increments This Sweep | 11 |
| New Repo Snapshots This Sweep | 389 |
| Total Repo Snapshots (cumulative) | 1,333 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (SPA) |

---

## GF(3) Color Chain — This Sweep's 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Repo Snapshots by Source (This Sweep)

| Source | Type | Repos | Max Stars | Latest Push |
|--------|------|-------|-----------|-------------|
| plurigrid | org | 100 | 17 (asi) | 2026-04-25 |
| kubeflow | org | 47 | 15,600 | 2026-04-25 |
| TeglonLabs | org | 4 | 2 | 2026-01-01 |
| bmorphism | user | 100 | 60 | 2026-04-25 |
| zubyul | user | 49 | 2 | 2026-04-24 |
| migalkin | user | 19 | 143 | 2025-08-04 |
| DJedamski | user | 6 | 2 | 2018-03-07 |
| wasita | user | 10 | 2 | 2026-04-22 |
| kristinezheng | user | 6 | 0 | 2026-04-09 |
| M1shaaa | user | 8 | 0 | 2026-04-25 |
| AustinCStone | user | 40 | 92 | 2026-02-11 |

### Notable plurigrid Repos
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| asi | HTML | 17 | 2026-04-25 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |
| gorj | Clojure | 0 | 2026-04-25 |
| zig-syrup | Zig | 2 | 2026-04-24 |
| nash-portal | Rust | 1 | 2026-04-15 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |

---

## Hamming Swarm Snapshot — Aptos Mainnet

### Wallet Balances (alice, bob, A–Z)

All 28 addresses returned `resource_not_found` from `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
These accounts exist as Aptos address identifiers but have no funded APT CoinStore resource on mainnet.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793... | unfunded |
| bob   | 0x0a3c... | unfunded |
| A     | 0x8699... | unfunded |
| B     | 0x3f89... | unfunded |
| C     | 0x38b9... | unfunded |
| D     | 0xf776... | unfunded |
| E     | 0xdc1d... | unfunded |
| F     | 0x18a1... | unfunded |
| G     | 0x69a3... | unfunded |
| H     | 0xce67... | unfunded |
| I     | 0x070f... | unfunded |
| J     | 0x4d96... | unfunded |
| K     | 0xa732... | unfunded |
| L     | 0x7c2e... | unfunded |
| M     | 0x6fed... | unfunded |
| N     | 0xe7dd... | unfunded |
| O     | 0x7325... | unfunded |
| P     | 0x6218... | unfunded |
| Q     | 0xac40... | unfunded |
| R     | 0x7ce6... | unfunded |
| S     | 0xb875... | unfunded |
| T     | 0x3578... | unfunded |
| U     | 0x7586... | unfunded |
| V     | 0xb59d... | unfunded |
| W     | 0x5f32... | unfunded |
| X     | 0xa95c... | unfunded |
| Y     | 0xd8e3... | unfunded |
| Z     | 0x7af0... | unfunded |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** with 2-of-N threshold.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4... | 2 | HEALTHY |
| A-G | 0xf56c... | 2 | HEALTHY |
| Y-Z | 0xd3ff... | 2 | HEALTHY |
| S-T | 0x3b1c... | 2 | HEALTHY |
| V-W | 0x40fa... | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — `testnet.mnx.fi` is a Next.js SPA. No REST API endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) are publicly accessible. No data inserted into `mnx_snapshots`.

---

## DuckDB Schema Summary

```sql
world_increments  — 34 rows  (GF3 color chain of sweep events)
repo_snapshots    — 1,333 rows (GitHub repo metadata snapshots)
aptos_snapshots   — 28 rows  (Hamming swarm wallet balances)
multisig_probes   — 5 rows   (Aptos multisig health checks)
mnx_snapshots     — 0 rows   (SPA, unavailable)
```

---

## GF(3) Color Semantics

| Trit | Color | Name | Hex |
|------|-------|------|-----|
| 0 | Pink | ERGODIC | `#d3869b` |
| +1 | Green | PLUS | `#b8bb26` |
| -1 | Red | MINUS | `#cc241d` |

Colors derived from GF(3) Galois field arithmetic — `id % 3` maps each increment to an ergodic/plus/minus trit, forming a deterministic color chain across all world state transitions.
