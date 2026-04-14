# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-14

## Sweep Metadata
- **Date:** 2026-04-14T16:08Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 427 |
| Total Repo Snapshots (cumulative) | 1,317 |
| New Increments This Sweep | 404 |
| New Repo Snapshots This Sweep | 373 |
| Sources Covered | 2 orgs + 9 users (plurigrid rate-limited) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy, 2-of-N) |
| MNX Markets | Unavailable (Next.js SPA) |

---

## GF(3) Color Chain

Rule: `id%3==0` → trit=0 ERGODIC `#d3869b` · `id%3==1` → trit=1 PLUS `#b8bb26` · `id%3==2` → trit=-1 MINUS `#cc241d`

| GF(3) State | Color | Count (this sweep) |
|-------------|-------|-------------------|
| ERGODIC | #d3869b | ~135 |
| PLUS | #b8bb26 | ~135 |
| MINUS | #cc241d | ~135 |

Sweep IDs 1–404 distributed evenly across GF(3) — balanced trit ergodicity confirmed.

---

## JOB 1: GitHub Social Graph Sweep

### Source Breakdown (this sweep)
| Source | Type | Increments |
|--------|------|-----------|
| bmorphism | user | 130 (100 repos + 30 events) |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| wasita | user | 31 |
| migalkin | user | 30 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| plurigrid | org | 1 (rate-limited placeholder) |

### Recent bmorphism Events (2026-04-14)
| Event Type | Repo |
|------------|------|
| CreateEvent | plurigrid/nash-portal |
| PushEvent | plurigrid/nash-portal |
| PullRequestEvent | plurigrid/nash-portal |
| IssuesEvent | plurigrid/nash-portal |
| PushEvent | plurigrid/asi |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances
Queried via `https://fullnode.mainnet.aptoslabs.com` — all 28 wallets returned **0.0 APT** (unfunded or CoinStore not registered). Addresses resolve as valid Aptos accounts.

| Label | Address (prefix) | APT |
|-------|-----------------|-----|
| alice | 0xc793ac… | 0.0 |
| bob | 0x0a3c00… | 0.0 |
| A–Z | 0x8699ed…–0x7af0ef… | 0.0 each |

### Multisig Contract Probes
`0x1::multisig_account::num_signatures_required` — all 5 returned **2-of-N**, healthy.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4… | 2 | HEALTHY |
| A-G | 0xf56c4a… | 2 | HEALTHY |
| Y-Z | 0xd3ffe1… | 2 | HEALTHY |
| S-T | 0x3b1c3a… | 2 | HEALTHY |
| V-W | 0x40fad7… | 2 | HEALTHY |

### MNX Markets
`https://testnet.mnx.fi` — **SPA (Next.js), no REST API endpoints accessible.** All `/api/*` paths return the frontend HTML bundle. Market data unavailable via HTTP scraping; noted as `N/A` in `mnx_snapshots` table.

---

## Top Repos by Source (from prior sweeps — plurigrid accessible)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4119 | 2026-04-10 |
| spark-operator | Python | 3111 | 2026-04-10 |
| trainer | Go | 2080 | 2026-04-10 |
| katib | Python | 1676 | 2026-04-02 |

### TeglonLabs (53 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (43 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

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
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-10)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark (pushed 2026-04-10)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
