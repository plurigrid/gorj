# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-01

## Sweep Metadata
- **Date:** 2026-08-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (Cumulative DB State)

| Metric | Value |
|--------|-------|
| Total World Increments | 49 |
| Total Repo Snapshots | 972 |
| Aptos Wallets Probed (this run) | 28 |
| Multisig Contracts Probed (this run) | 5 |
| MNX Markets | unavailable |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted (2026-08-01)

| Source | Type | Notable Repos | Stars |
|--------|------|---------------|-------|
| plurigrid | org | gorj (active 2026-08-01), zig-syrup, asi | 58, 2, 1 |
| kubeflow | org | kubeflow (15802★), pipelines (4173★), spark-operator (3141★) | active 2026-08-01 |
| TeglonLabs | org | jank-crane (C++/GF3), mathpix-gem (Ruby) | 0, 2 |
| bmorphism | user | Gay.jl (Julia, 188 issues), ocaml-mcp-sdk (61★), anti-bullshit-mcp-server (22★) | active 2026-07-21 |
| zubyul | user | voice-observatory, ghostel-emacs-worlds, gay-world | active 2026-04-24 |
| migalkin | user | NodePiece (144★ ICLR'22), StarE (89★), kgcourse2021 | active 2026-07-10 |
| DJedamski | user | Kaggle/Coursera data science repos | inactive (2018) |
| AustinCStone | user | byteruckus (2026-07-15), bmfork tools | 41 repos total |
| wasita | user | in historical DB | — |
| kristinezheng | user | in historical DB | — |
| M1shaaa | user | in historical DB | — |

### Recently Active (pushed within 7 days of 2026-08-01)

- **plurigrid/gorj**: 2026-08-01 — forj MCP + GF(3) nREPL routing (this repo)
- **plurigrid/zig-syrup**: 2026-07-28 — OCapN Syrup Zig implementation
- **kubeflow/pipelines**: 2026-08-01 — ML Pipelines for Kubernetes
- **kubeflow/mcp-server**: 2026-08-01 — Kubeflow AI-assisted dev tools
- **kubeflow/kale**: 2026-08-01 — Data Scientist superfood (699★)
- **bmorphism/Gay.jl**: 2026-07-21 — wide-gamut GF(3) color sampling
- **bmorphism/gay-chat**: 2026-07-14 — Spritely Brassica chat
- **AustinCStone/byteruckus**: 2026-07-15 — new HTML repo

### GF(3) Color Chain (this run's increments, IDs 24–49)

GF(3) assignment: `id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (all 28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) returned **0.0 APT** balance.
Accounts appear unfunded or CoinStore not initialized on mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | 0x8699…7af0 | 0.0 each |

### Multisig Contract Probes — ALL HEALTHY ✅

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

All 5 multisig contracts respond correctly with 2-of-2 signature threshold.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `/api/markets` returns HTTP 404; base URL is a minimal SPA with no market data. Testnet may be offline or API routes changed.

---

---

## Top Repos by Source (2026-08-01)

### plurigrid (50+ repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 58 | 2026-07-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-26 |
| zig-syrup | Zig | 2 | 2026-07-28 |
| nash-portal | Rust | 2 | 2026-05-19 |
| gorj | Clojure | 1 | 2026-08-01 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15802 | 2026-08-01 |
| pipelines | Python | 4173 | 2026-08-01 |
| spark-operator | Python | 3141 | 2026-07-31 |
| trainer | Go | 2165 | 2026-07-31 |
| katib | Python | 1695 | 2026-07-31 |
| mcp-apache-spark-history-server | Python | 185 | 2026-08-01 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (30+ repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 22 |
| Gay.jl | Julia | 2 (188 open issues) |
| gay-chat | Scheme | 0 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |

### AustinCStone (41 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| byteruckus | HTML | 0 | 2026-07-15 |
| EpsteinSearch | Python | 0 | 2026-02-11 |

---

## DuckDB Tables (Cumulative)

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 49 | GF(3) colored event log |
| `repo_snapshots` | 972 | GitHub repo metadata (all orgs/users) |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances (this run) |
| `multisig_probes` | 5 | Aptos 2-of-2 multisig health (this run) |
| `mnx_snapshots` | 0 | MNX market data (unavailable) |

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
- **kubeflow/kubeflow**: 15,802 stars (+237 since April) — active 2026-08-01
- **kubeflow/pipelines**: 4,173 stars — pushed 2026-08-01
- **plurigrid/asi**: 58 stars (up from 16 in April sweep) — topological chemputer
- **migalkin/NodePiece**: 144 stars — ICLR'22 knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK, Jane Street oxcaml_effect
- **bmorphism/Gay.jl**: 188 open issues — active GF(3) color sampling work
- **plurigrid/gorj**: pushed 2026-08-01 — this repo, forj MCP + GF(3) routing
- **All 5 multisig contracts**: healthy, 2-of-2 threshold
- **MNX testnet**: offline/unavailable as of 2026-08-01
