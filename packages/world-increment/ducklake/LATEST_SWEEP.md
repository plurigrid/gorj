# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-22

## Sweep Metadata
- **Date:** 2026-04-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 69 |
| Total Repo Snapshots | 473 |
| Sources Covered | 3 orgs + 8 users |
| Events Captured | 58 (bmorphism + zubyul) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts | 5 (all healthy, sigs=2) |
| MNX Markets | unavailable (503) |

---

## GF(3) Color Chain — 69 World Increments

11 repo-source increments + 58 event increments = 69 total. Perfectly balanced at 23 per trit.

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 23 |
| +1 | PLUS | `#b8bb26` | 23 |
| −1 | MINUS | `#cc241d` | 23 |

GF(3) rule: `id mod 3 == 0 → ERGODIC`, `id mod 3 == 1 → PLUS`, `id mod 3 == 2 → MINUS`

### Repo-Source Increments (IDs 1–11)

| ID | Source | Type | Trit | Color | Name |
|----|--------|------|------|-------|------|
| 1  | plurigrid | org | 0 | `#d3869b` | ERGODIC |
| 2  | kubeflow | org | +1 | `#b8bb26` | PLUS |
| 3  | TeglonLabs | org | -1 | `#cc241d` | MINUS |
| 4  | bmorphism | user | 0 | `#d3869b` | ERGODIC |
| 5  | zubyul | user | +1 | `#b8bb26` | PLUS |
| 6  | migalkin | user | -1 | `#cc241d` | MINUS |
| 7  | DJedamski | user | 0 | `#d3869b` | ERGODIC |
| 8  | wasita | user | +1 | `#b8bb26` | PLUS |
| 9  | kristinezheng | user | -1 | `#cc241d` | MINUS |
| 10 | M1shaaa | user | 0 | `#d3869b` | ERGODIC |
| 11 | AustinCStone | user | +1 | `#b8bb26` | PLUS |

Events (IDs 12–69): 28 bmorphism + 30 zubyul public events — PushEvent (29), CreateEvent (9), PullRequestEvent (6), WatchEvent (3), ForkEvent (3), PullRequestReviewEvent (3), other (5).

---

## Top Repos by Source

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

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| plurigrid | org | 100 | 43 |
| bmorphism | user | 100 | 128 |
| TeglonLabs | org | 53 | 6 |
| kubeflow | org | 47 | 33,923 |
| AustinCStone | user | 43 | 108 |
| migalkin | user | 30 | 278 |
| wasita | user | 31 | 4 |
| zubyul | user | 24 | 13 |
| kristinezheng | user | 18 | 0 |
| M1shaaa | user | 16 | 0 |
| DJedamski | user | 11 | 7 |
| **TOTAL** | | **473** | **34,510** |

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
- **kubeflow/kubeflow**: 15,594 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,125 stars — most popular ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,117 stars — Kubernetes operator for Apache Spark
- **kubeflow/trainer**: 2,085 stars — distributed training operator
- **migalkin/NodePiece**: scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: OCaml SDK for Model Context Protocol
- **AustinCStone/TextGAN**: text generation with GANs
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) trit coloring
- **69 increments**: closes 23 full GF(3) cycles (perfectly balanced trit distribution)

## Hamming Swarm — Aptos Mainnet

All 28 swarm addresses (alice, bob, A–Z) have no initialized APT CoinStore resource at mainnet ledger ~4.97B. Accounts exist on-chain but hold no APT balance.

## Multisig Health

All 5 Hamming-pair multisig contracts (A-B, A-G, Y-Z, S-T, V-W) are live with `num_signatures_required = 2`. No degradation detected.

## MNX Markets

`testnet.mnx.fi` returned 503 Service Unavailable / DNS failures on all probed endpoints. No market data captured.
