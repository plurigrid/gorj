# World Increment Sweep + Hamming Snapshot
**Timestamp:** 2026-04-22T05:11:52Z  
**GF(3) color chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage
| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| kubeflow | org | 47 | 33,923 | 2026-04-21 |
| migalkin | user (social) | 19 | 278 | 2025-08-04 |
| bmorphism | user | 100 | 246 | 2026-04-22 |
| AustinCStone | user (social) | 40 | 108 | 2026-02-11 |
| plurigrid | org | 100 | 65 | 2026-04-21 |
| zubyul | user | 47 | 14 | 2026-04-13 |
| wasita | user (social) | 7 | 3 | 2026-04-22 |
| DJedamski | user (social) | 5 | 3 | 2018-03-07 |
| TeglonLabs | org | 4 | 2 | 2026-01-01 |
| M1shaaa | user (social) | 7 | 0 | 2026-04-22 |
| kristinezheng | user (social) | 5 | 0 | 2026-04-09 |
| **TOTAL** | | **381** | **34,642** | |

### Hot Repos (recently active)
- `plurigrid/gorj` — Clojure, 250 open issues, pushed 2026-04-21 — forj + Rama topology nREPL routing
- `bmorphism/Gay.jl` — Julia, 187 open issues, pushed 2026-04-22 — Wide-gamut color sampling with GF(3) trits
- `plurigrid/nanoclj-zig` — Zig, pushed 2026-04-21 — NaN-boxed Clojure interpreter in Zig
- `wasita/wasita.github.io` — Svelte, pushed 2026-04-22 — active personal site
- `M1shaaa/M1shaaa` — pushed 2026-04-22 — profile config (active today)
- `kubeflow/pipelines` — Python, 4125 stars — ML Pipelines for Kubernetes

### GF(3) Trit Distribution
- ERGODIC (trit=0, #d3869b): 127 increments
- PLUS (trit=1, #b8bb26): 127 increments
- MINUS (trit=-1, #cc241d): 127 increments
- **Conservation check: perfectly balanced** ✓

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All balances queried via `0x1::coin::balance` view function.

| World | Balance (APT) | Address (truncated) |
|-------|--------------|---------------------|
| bob | 12.6570 | 0x0a3c...512d5d |
| F | 1.9605 | 0x18a1...3cf71 |
| L | 1.9273 | 0x7c2e...7eba9 |
| J | 1.8951 | 0x4d96...7f54 |
| alice | 0.4364 | 0xc793...4cc7b |
| O | 0.2101 | 0x7325...5a89d |
| K | 0.1620 | 0xa732...25dc4 |
| P | 0.1401 | 0x6218...ec948 |
| M | 0.1123 | 0x6fed...7f2e9 |
| N | 0.1061 | 0xe7dd...551b2c |
| Q | 0.1032 | 0xac40...c89a9 |
| S | 0.0918 | 0xb875...d0386 |
| R | 0.0902 | 0x7ce6...76e10 |
| T | 0.0737 | 0x3578...3f4588 |
| U | 0.0558 | 0x7586...ef9956 |
| A | 0.0518 | 0x8699...4cc7b |
| V | 0.0488 | 0xb59d...af2c3 |
| Y | 0.0444 | 0xd8e3...2444c4 |
| X | 0.0426 | 0xa95c...3047d |
| W | 0.0407 | 0x5f32...cc7b0 |
| B | 0.0363 | 0x3f89...77cb13 |
| Z | 0.0243 | 0x7af0...197c |
| D | 0.0116 | 0xf776...cfdd1 |
| C | 0.0102 | 0x38b9...91535e |
| E | 0.0094 | 0xdc1d...958d36 |
| H | 0.0017 | 0xce67...5300f |
| I | 0.0007 | 0x070f...1fc9 |
| G | 0.0007 | 0x69a3...7f32 |

**Total swarm APT: ~20.63 APT**  
**Top holder:** bob (12.66 APT, 61% of swarm)

### Multisig Probes (all 5 healthy, 2-of-N)
| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All multisig accounts require exactly 2 signatures. All respond healthy.

### MNX Markets (testnet.mnx.fi)
Status: **Unavailable** — site is a Next.js SPA with no public JSON API endpoints.  
`/api/markets` and `/api/tickers` return HTML shell only. Logged as placeholder row.

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name, source_type,
                 source_name, event_type, repo_name, actor, snapshot_hash)
repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name, full_name,
               language, stars, forks, open_issues, pushed_at, description)
aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```
