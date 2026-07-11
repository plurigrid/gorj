# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-11

## Sweep Metadata
- **Date:** 2026-07-11 03:14 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 111 |
| Total Repo Snapshots (cumulative) | 1,032 |
| New increments this run | 38 (IDs 62–99) |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain (this run, newest)

| ID | Source | Repo | GF3 | Color |
|----|--------|------|-----|-------|
| 99 | migalkin | migalkin.github.io | ERGODIC | #d3869b |
| 98 | migalkin | SMJoin-experiments | MINUS | #cc241d |
| 97 | migalkin | rambo | PLUS | #b8bb26 |
| 96 | migalkin | NBFNet_mlx | ERGODIC | #d3869b |
| 95 | migalkin | RWL | MINUS | #cc241d |
| 94 | migalkin | kgcourse2021 | PLUS | #b8bb26 |
| 93 | migalkin | StarE | ERGODIC | #d3869b |
| 92 | migalkin | NodePiece | MINUS | #cc241d |
| 91 | zubyul | chromatic-vrf | PLUS | #b8bb26 |
| 90 | zubyul | cat-world | ERGODIC | #d3869b |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet (ledger epoch 16,491, block 890,544,607)

**All 28 Hamming swarm wallets (alice, bob, A–Z):** `resource_not_found`  
The Aptos mainnet is live and reachable; these addresses hold no APT in `0x1::coin::CoinStore<AptosCoin>` at ledger version 6,221,728,576.

### Multisig Contract Probes — ALL HEALTHY

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...7003 | 2 | ✅ |
| A-G | 0xf56c4a1c...0096 | 2 | ✅ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✅ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✅ |
| V-W | 0x40fad7b4...eb6d | 2 | ✅ |

### MNX Markets (testnet.mnx.fi) — UNAVAILABLE (HTTP 401)

---

## Top Repos by Source

### plurigrid (103 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 30 | 2026-07-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-26 |
| gorj | Clojure | 1 | 2026-07-11 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,771 | 2026-07-10 |
| pipelines | Python | 4,169 | 2026-07-11 |
| spark-operator | Python | 3,137 | 2026-07-10 |
| trainer | Go | 2,135 | 2026-07-10 |
| katib | Python | 1,689 | 2026-07-10 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| Gay.jl | Julia | 2 (187 issues) |
| open-location-code-zig | Zig | 3 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |

### AustinCStone (40 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |

---

## Repo Counts by Source

| Source | Type | Repos Found |
|--------|------|-------------|
| bmorphism | user | 100 |
| plurigrid | org | 103 |
| kubeflow | org | 49 |
| AustinCStone | user | 40 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **395** |

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
- **kubeflow/kubeflow**: 15,771 stars — flagship ML platform for Kubernetes (pushed 2026-07-10)
- **kubeflow/pipelines**: 4,169 stars — pushed 2026-07-11 (active today)
- **kubeflow/mcp-server**: new! MCP server for AI-assisted Kubeflow dev (20★, 28 forks)
- **migalkin/NodePiece**: 144 stars — ICLR'22 KG representation paper
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **bmorphism/Gay.jl**: 187 open issues — most active bmorphism repo, pushed 2026-07-11
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 30 stars — topological chemputer (pushed 2026-07-10)
- **plurigrid/gorj**: 1,112 open issues — this repo, pushed 2026-07-11
- **TeglonLabs/jank-crane**: new (Jun 2026) — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"
- **Hamming swarm**: all 5 multisig contracts healthy (2-of-N), all wallet APT balances unfunded
- **GF(3)**: 111 total world increments, 37 ERGODIC / 37 PLUS / 37 MINUS across cumulative history
