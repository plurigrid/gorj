# World-Increment Sweep + Hamming Snapshot — 2026-06-06

## Sweep Metadata
- **Date:** 2026-06-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts — This Run (2026-06-06)

| Metric | Value |
|--------|-------|
| World Increments This Run | 11 |
| Repo Snapshots This Run | 312 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Market Data | unavailable (Vercel auth) |

---

## GF(3) Color Chain — This Run's 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | social | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | social | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | social | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | social | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | social | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | social | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

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

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet)
All 28 Hamming swarm addresses (alice, bob, A–Z) returned **0.0 APT** — CoinStore resources not initialized on mainnet.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|:---:|:---:|
| A-B | 0x0da4f428...987003 | 2 | ✓ |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ |

**All 5 multisig accounts healthy** — 2-of-2 threshold, all responded.

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — Vercel deployment protection active; no bypass token available.

---

## Notable Highlights — 2026-06-06 Run
- **kubeflow/kubeflow**: 15,706 stars (flagship ML for Kubernetes)
- **kubeflow/pipelines**: 4,152 stars, pushed 2026-06-06 (most active kubeflow repo)
- **plurigrid/gorj**: 402 open issues, pushed 2026-06-06 (this repo!)
- **bmorphism/Gay.jl**: 189 open issues, pushed 2026-06-06 (most active bmorphism)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK via Jane Street oxcaml_effect
- **migalkin/NodePiece**: 144 stars — ICLR'22 knowledge graph paper
- **AustinCStone/TextGAN**: 92 stars — text GAN in TensorFlow
- **plurigrid/asi**: 25 stars — topological chemputer
- **5/5 multisig healthy** — all Hamming swarm multisigs at 2-of-2
