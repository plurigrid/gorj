# World-Increment Sweep — 2026-06-27

## Sweep Metadata
- **Date:** 2026-06-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New Repo Snapshots This Run | 60 |
| Total Repo Snapshots (Cumulative) | 1,004 |
| Sources Covered | 3 orgs + 8 users + 6 social-graph users |
| Aptos Wallets Queried | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — This Run (60 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 20 |
| +1 | `#b8bb26` | PLUS | 20 |
| -1 | `#cc241d` | MINUS | 20 |

GF(3) chain cycles: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...` (20 full cycles)

---

## Top Repos by Source (This Run)

### plurigrid (19 repos snapshotted)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 0 (855 issues) | 2026-06-27 |
| asi | HTML | 26 | 2026-06-26 |
| eirobri | Clojure | 0 | 2026-06-23 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |
| ontology | JavaScript | 8 | 2025-05-27 |

### kubeflow (10 repos snapshotted)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,747 | 2026-06-18 |
| pipelines | Python | 4,156 | 2026-06-26 |
| spark-operator | Python | 3,128 | 2026-06-26 |
| trainer | Go | 2,123 | 2026-06-26 |
| katib | Python | 1,687 | 2026-06-23 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (10 repos snapshotted)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 (187 issues) | 2026-06-27 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| hypernym-mcp-server | JavaScript | 6 | 2025-04-02 |
| shitcoin | Python | 5 | 2026-04-08 |

### zubyul (8 repos snapshotted)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| voice-observatory | Python | 0 | 2026-04-24 |
| nash-tui | Rust | 0 | 2026-04-13 |
| gay-world | Python | 1 | 2026-03-26 |
| tilelang-kernels | Python | 0 | 2026-03-16 |

### Social Graph (8 repos)
| Repo | User | Stars | Pushed At |
|------|------|-------|-----------|
| migalkin/StarE | migalkin | 89 | 2023-12-01 |
| migalkin/kgcourse2021 | migalkin | 25 | 2025-08-04 |
| wasita/wasita.github.io | wasita | 1 | 2026-06-25 |
| kristinezheng/IntPhys2 | kristinezheng | 0 | 2026-06-03 |
| M1shaaa/M1shaaa | M1shaaa | 0 | 2026-06-27 |

---

## Repo Counts by Source (This Run)

| Source | Type | Repos This Run |
|--------|------|----------------|
| plurigrid | org | 19 |
| kubeflow | org | 10 |
| TeglonLabs | org | 5 |
| bmorphism | user | 10 |
| zubyul | user | 8 |
| migalkin | social | 2 |
| wasita | social | 2 |
| kristinezheng | social | 1 |
| M1shaaa | social | 1 |
| DJedamski | social | 1 |
| AustinCStone | social | 1 |
| **TOTAL** | | **60** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, Mainnet)

All 28 hamming swarm wallets queried via `https://fullnode.mainnet.aptoslabs.com`.

**Result: All 28 wallets returned 0.0 APT.** The `0x1::coin::CoinStore<AptosCoin>` resource is absent for these addresses — they are either unfunded on mainnet or use a different token mechanism.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z (26 addresses) | — | 0.0 each |

### Multisig Contract Probes (5 pairs)

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig accounts are live with 2-of-2 signature requirement.

### MNX Markets

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection authentication. Both `/api/markets` and `/api/v1/markets` return Vercel auth walls. No market data extracted.

---

---

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
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,747 stars (↑182 since April sweep) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,156 stars (↑37) — pushed 2026-06-26
- **kubeflow/spark-operator**: 3,128 stars (↑17) — pushed 2026-06-26
- **plurigrid/gorj**: 855 open issues (up from prior sweep) — very active
- **bmorphism/Gay.jl**: 187 open issues — GF(3) color system extremely active
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for Model Context Protocol
- **plurigrid/asi**: 26 stars (↑10 since April) — topological chemputer, pushed 2026-06-26
- **TeglonLabs/jank-crane**: new C++ repo for GF3 convergence maps (pushed 2026-06-08)
- **kubeflow/mcp-apache-spark-history-server**: 178 stars — new MCP integration
- **All 5 multisig pairs healthy** at 2-of-2 threshold on Aptos mainnet
- **All 28 hamming wallets empty** (0.0 APT) — consistent with unfunded testnet wallets

*Generated by world-increment-sweep + hamming-swarm-snapshot agent, 2026-06-27*
