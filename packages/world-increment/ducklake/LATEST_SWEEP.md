# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-18

## Sweep Metadata
- **Date:** 2026-07-18
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (pip)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 70 | 83 |
| kubeflow | org | 35 | 34,226 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 39 | 213 |
| zubyul | user | 26 | 11 |
| migalkin | social-graph | 6 | 278 |
| AustinCStone | social-graph | 5 | 107 |
| wasita | social-graph | 4 | 4 |
| M1shaaa | social-graph | 3 | 0 |
| DJedamski | social-graph | 3 | 2 |
| kristinezheng | social-graph | 3 | 0 |
| **TOTAL** | | **199** | **34,926** |

### Notable Recent Activity (within 7 days of sweep)
- **plurigrid/gorj** (Clojure, ★1) — pushed 2026-07-18 — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **zubyul/from-possible-worlds** (TeX) — pushed 2026-07-18
- **kubeflow/mcp-server** (Python, ★26) — pushed 2026-07-18 — MCP Server for AI-Assisted Development with Kubeflow Tools
- **kubeflow/notebooks** — pushed 2026-07-18
- **kubeflow/sdk** (Python, ★125) — pushed 2026-07-18
- **kubeflow/trainer** (Go, ★2151) — pushed 2026-07-18
- **kubeflow/pipelines** (Python, ★4168) — pushed 2026-07-17
- **plurigrid/place** (TeX, ★1) — pushed 2026-07-14
- **plurigrid/eirobri** (Clojure) — pushed 2026-07-14 — EiRoBri replay world
- **bmorphism/Gay.jl** (Julia, ★2) — pushed 2026-07-14 — Wide-gamut color sampling with splittable determinism

### Top Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,780 | — | 2026-07-10 |
| kubeflow/pipelines | 4,168 | Python | 2026-07-17 |
| kubeflow/spark-operator | 3,138 | Python | 2026-07-17 |
| kubeflow/trainer | 2,151 | Go | 2026-07-18 |
| kubeflow/katib | 1,691 | Python | 2026-07-16 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-17 |
| kubeflow/arena | 815 | Go | 2026-07-17 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |

### Top Active Repos by Source

#### plurigrid (70 repos, 83★)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| asi-skills | Julia | 3 | 2026-04-26 |
| agent | Python | 5 | 2023-03-31 |

#### kubeflow (35 repos, 34226★)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,780 | 2026-07-10 |
| pipelines | Python | 4,168 | 2026-07-17 |
| spark-operator | Python | 3,138 | 2026-07-17 |
| trainer | Go | 2,151 | 2026-07-18 |
| katib | Python | 1,691 | 2026-07-16 |

#### bmorphism (39 repos, 213★)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 19 | 2025-01-05 |
| Gay.jl | Julia | 2 | 2026-07-14 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 addresses, queried 2026-07-18)
| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A–Z (26) | various | 0.0 each |

**Summary:** All 28 Hamming swarm addresses show 0.0 APT. Accounts unfunded on mainnet. Full addresses in `aptos_snapshots` table.

### Multisig Contract Probes (5 pairs)
| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | ✓ |
| A-G | 0xf56c4a... | 2 | ✓ |
| Y-Z | 0xd3ffe1... | 2 | ✓ |
| S-T | 0x3b1c3a... | 2 | ✓ |
| V-W | 0x40fad7... | 2 | ✓ |

All 5 multisig pairs healthy, all requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)
**Status:** UNAVAILABLE — Vercel deployment protection active. Authentication (OIDC or bypass token) required. No market data extractable.

---

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

GF(3) distribution across 199 increments: ERGODIC=67, PLUS=66, MINUS=66

## Database Summary
- **Tables:** world_increments (199), repo_snapshots (199), aptos_snapshots (28), multisig_probes (5), mnx_snapshots (0)
- **Schema unchanged** from prior sweep

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,780★ (+215 since Apr 12) — flagship ML platform for Kubernetes
- **kubeflow/trainer**: 2,151★ (+71 since Apr 12) — active development, pushed 2026-07-18
- **plurigrid/gorj**: 1,239 open issues — this very repo (world-increment home)
- **bmorphism/Gay.jl**: 187 open issues, actively pushed 2026-07-14
- **bmorphism/ocaml-mcp-sdk**: 61★ — OCaml SDK for MCP using Jane Street's oxcaml_effect
- All Hamming swarm multisigs healthy (2-of-N), balances at zero on mainnet
