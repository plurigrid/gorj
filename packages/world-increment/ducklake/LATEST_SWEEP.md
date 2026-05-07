# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-07

## Sweep Metadata
- **Date:** 2026-05-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 10 |
| Total Repo Snapshots | 206 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 5 users + 2 aptos |

---

## GF(3) Color Chain — All 10 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | user_events | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 7  | wasita (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 8  | M1shaaa (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 9  | hamming_swarm (aptos) | balance_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | multisig_probes (aptos) | contract_probe | +1 | `#b8bb26` | **PLUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## Top Repos by Source

### plurigrid (50 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 20 | 2026-04-26 |
| ontology | JavaScript | 7 | 2025-05-27 |
| StochFlow | Python | 4 | 2024-03-20 |
| act | Python | 3 | 2024-07-26 |
| asi-skills | Julia | 3 | 2026-04-26 |
| horse | TeX | 1 | 2026-05-07 |
| gorj | Clojure | 0 | 2026-05-07 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,624 | 2026-04-29 |
| pipelines | Python | 4,135 | 2026-05-07 |
| spark-operator | Python | 3,124 | 2026-05-05 |
| trainer | Go | 2,095 | 2026-05-07 |
| katib | Python | 1,683 | 2026-05-06 |
| mcp-apache-spark-history-server | Python | 165 | 2026-05-05 |

### TeglonLabs (4 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| topoi | Python | 0 | 2025-01-24 |
| monad-mcp-server | — | 0 | 2025-05-14 |

### migalkin (30 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2022-02-02 |
| StarE | Python | 89 | 2023-12-01 |
| kgcourse2021 | HTML | 25 | 2025-08-04 |
| NBFNet_mlx | Python | 10 | 2024-03-02 |

### zubyul (27 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | Python | 0 | 2026-04-30 |
| voice-observatory | Python | 0 | 2026-04-24 |
| ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |
| say-mcp-server | — | 0 | 2026-04-23 |
| big-bad-plurigrid-quiz | Emacs Lisp | 0 | 2026-04-09 |
| gay-world | Python | 1 | 2026-03-26 |
| Gay.jl | Julia | 0 | 2026-03-28 |

### wasita (32 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| vocoder | JavaScript | 0 | 2026-05-06 |
| wasita.github.io | Svelte | 1 | 2026-04-28 |
| ch3-lib | Typst | 0 | 2026-04-12 |
| wm-cv | Svelte | 0 | 2026-04-12 |
| magic-garden | Python | 2 | 2026-01-13 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 50 |
| kubeflow | org | 47 |
| wasita | user | 32 |
| migalkin | user | 30 |
| zubyul | user | 27 |
| M1shaaa | user | 16 |
| TeglonLabs | org | 4 |
| bmorphism, DJedamski, kristinezheng, AustinCStone | user | 0 (rate-limited) |
| **TOTAL** | | **206** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
All returned `resource_not_found` — accounts are registered on-chain but have no initialized APT CoinStore, or balances are zero.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A–H | (8 addresses) | 0.0 each |
| I–R | (10 addresses) | 0.0 each |
| S–Z | (8 addresses) | 0.0 each |

**Total APT across swarm: 0.0** | **Swarm size: 28 wallets**

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy: 2-of-N signatures required.**

### MNX Markets (testnet.mnx.fi)

Status: **SPA (Next.js) — no REST API endpoint returning JSON data.**
Paths `/api/markets` and `/api/v1/markets` return the HTML shell.
Market data: **unavailable** at time of sweep.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC

## Notable Highlights
- **kubeflow/kubeflow**: 15,624 stars — flagship ML platform for Kubernetes (active 2026-04-29)
- **kubeflow/pipelines**: 4,135 stars — most active repo, pushed 2026-05-07
- **kubeflow/mcp-apache-spark-history-server**: 165 stars — new MCP integration
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings, GNN researcher
- **plurigrid/asi**: 20 stars — "everything is topological chemputer!" (pushed 2026-04-26)
- **plurigrid/gorj**: This repo — forj + REPL + GF(3) trit coloring (pushed 2026-05-07)
- **zubyul/gay-world** + **zubyul/Gay.jl**: active plurigrid social graph nodes
- **Hamming swarm**: 28 wallets, all zero APT on mainnet (CoinStore not initialized)
- **All multisigs**: 2-of-N, healthy across A-B, A-G, Y-Z, S-T, V-W pairs

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent.*
