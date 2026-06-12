# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-12

## Sweep Metadata
- **Date:** 2026-06-12
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Swept — GF(3) Color Chain

| ID | GF(3) | Color | Source | Type | Repos |
|----|-------|-------|--------|------|-------|
| 1 | trit=0 | `#d3869b` ERGODIC | plurigrid | org | 100 |
| 2 | trit=1 | `#b8bb26` PLUS | kubeflow | org | 48 |
| 3 | trit=-1 | `#cc241d` MINUS | TeglonLabs | org | 5 |
| 4 | trit=0 | `#d3869b` ERGODIC | bmorphism | user | 100 |
| 5 | trit=1 | `#b8bb26` PLUS | zubyul | user | 49 |
| 6 | trit=-1 | `#cc241d` MINUS | migalkin | user | 19 |
| 7 | trit=0 | `#d3869b` ERGODIC | DJedamski | user | 6 |
| 8 | trit=1 | `#b8bb26` PLUS | wasita | user | 11 |
| 9 | trit=-1 | `#cc241d` MINUS | kristinezheng | user | 5 |
| 10 | trit=0 | `#d3869b` ERGODIC | M1shaaa | user | 8 |
| 11 | trit=1 | `#b8bb26` PLUS | AustinCStone | user | 40 |

**Total repos snapshotted: 391**

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

### Top Repos by Stars (snapshot 2026-06-12)
| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15718 | — | 2026-06-11 |
| kubeflow/pipelines | 4152 | Python | 2026-06-12 |
| kubeflow/spark-operator | 3127 | Python | 2026-06-09 |
| kubeflow/trainer | 2112 | Go | 2026-06-12 |
| kubeflow/katib | 1683 | Python | 2026-06-05 |
| kubeflow/examples | 1461 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1023 | YAML | 2026-06-12 |
| plurigrid/asi | 26 | HTML | 2026-06-10 |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |

### Language Distribution (top 15)
| Language | Repos |
|----------|-------|
| Python | 235 |
| Rust | 57 |
| JavaScript | 53 |
| Go | 51 |
| HTML | 51 |
| TypeScript | 47 |
| Jupyter Notebook | 40 |
| Clojure | 30 |
| Jsonnet | 23 |
| R | 22 |
| Julia | 19 |
| Java | 18 |
| C | 15 |
| Zig | 15 |
| TeX | 15 |

### Notable Recent Activity (pushed since 2026-06-01)
- **plurigrid/gorj** — 2026-06-12 — "forj + Rama topology nREPL routing + GF(3) gay trit coloring" (527 open issues, active today)
- **M1shaaa/M1shaaa** — 2026-06-12 — profile config, active today
- **kubeflow/trainer** — 2026-06-12 — Go, 2112⭐
- **kubeflow/pipelines** — 2026-06-12 — Python, 4152⭐
- **kubeflow/community-distribution** — 2026-06-12 — YAML, 1023⭐
- **kristinezheng/kristinezheng.github.io** — 2026-06-07 — HTML portfolio
- **TeglonLabs/jank-crane** — 2026-06-08 — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps" (C++)
- **plurigrid/asi** — 2026-06-10 — "everything is topological chemputer!" 26⭐
- **wasita/wasita.github.io** — 2026-06-01 — Svelte personal site

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-12)

Queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` with 1s sleep between calls.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z (26 wallets) | 0x8699...→ 0x7af0... | 0.0 each |

**Total: 28 wallets queried — all return 0.0 APT.**

> All accounts returned resource-not-found on mainnet. The CoinStore resource is absent, indicating these wallets have not been funded or initialized with APT on mainnet.

### Multisig Contract Probes (Aptos Mainnet)

Probed via `POST https://fullnode.mainnet.aptoslabs.com/v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | **2** | ✅ |
| A-G | 0xf56c...0096 | **2** | ✅ |
| Y-Z | 0xd3ff...b883 | **2** | ✅ |
| S-T | 0x3b1c...7883 | **2** | ✅ |
| V-W | 0x40fa...eb6d | **2** | ✅ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed on mainnet.**

### MNX Markets (`testnet.mnx.fi`)

**Status: Unavailable** — `testnet.mnx.fi` and `testnet.mnx.fi/api/markets` are behind Vercel deployment protection. Both endpoints return HTTP 401 with authentication challenge. No market data accessible without a bypass token or OIDC trusted-source configuration.

---

## DuckDB Ducklake Summary

```
Database: packages/world-increment/ducklake/world-increments.duckdb
  world_increments : 11 rows  (GF3 color-chained sweep records)
  repo_snapshots   : 391 rows (GitHub repos across 11 sources)
  aptos_snapshots  :  28 rows (Hamming swarm wallet balances — all 0 APT)
  multisig_probes  :   5 rows (Aptos 2-of-N multisig health — all ✅)
  mnx_snapshots    :   1 row  (MNX testnet — unavailable/Vercel-auth-gated)
```

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)
repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
