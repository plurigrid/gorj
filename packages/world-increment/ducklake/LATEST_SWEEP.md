# World-Increment Sweep — 2026-06-01

## Sweep Metadata
- **Date:** 2026-06-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 356 |
| Total Repo Snapshots | 356 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — 356 Increments

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=**MINUS**

```
ERGODIC #d3869b: 118 increments
PLUS    #b8bb26: 119 increments
MINUS   #cc241d: 119 increments
```

---

## Top Repos by Source

### plurigrid org (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 23 | 2026-04-26 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| gorj | Clojure | 0 | 2026-06-01 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| nash-portal | Rust | 2 | 2026-05-19 |

Notable: `gorj` (this repo!) pushed 2026-06-01 with 287 open issues — forj + Rama nREPL + GF(3) gay trit coloring.

### kubeflow org (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,697 | 2026-05-24 |
| pipelines | Python | 4,149 | 2026-06-01 |
| spark-operator | Python | 3,124 | 2026-05-29 |
| trainer | Go | 2,109 | 2026-05-30 |
| katib | Python | 1,685 | 2026-05-29 |
| mcp-apache-spark-history-server | Python | 173 | 2026-05-29 |

### bmorphism user (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 18 | 2025-01-05 |
| manifold-mcp-server | JavaScript | 14 | 2025-01-11 |
| Gay.jl | Julia | 1 | 2026-06-01 |

### zubyul user (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gay-world | Python | 1 | 2026-03-26 |
| WGCNA | HTML | 2 | 2023-07-05 |
| jonikas_lab_data_analysis_misc | Jupyter | 2 | 2023-08-16 |
| Nikolova_lab_data_analysis | R | 2 | 2023-06-16 |
| nash-tui | Rust | 0 | 2026-04-13 |

### TeglonLabs org (4 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

### migalkin user (9 repos — social graph)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |
| NBFNet_mlx | Python | 10 |
| RWL | Python | 8 |

### AustinCStone user (15 repos — social graph)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

### wasita user (11 repos — social graph)
Active through 2026-06-01. Primarily Svelte/TypeScript web apps.

### DJedamski user (6 repos — social graph)
Data science and Kaggle competitions. R/Python.

### kristinezheng user (6 repos — social graph)
MIT student, neuroscience + HackMIT projects.

### M1shaaa user (8 repos — social graph)
Yale/MIT student, Lookit studies + TypeScript.

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user | 15 |
| migalkin | user | 9 |
| wasita | user | 11 |
| kristinezheng | user | 6 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **356** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm addresses probed via Aptos mainnet fullnode API.  
`GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Note:** All addresses returned 0 APT. Accounts may be uninitialized or hold no `aptos_coin` resources.

### Multisig Contracts (5 probed)

All probed via `POST /v1/view` with `0x1::multisig_account::num_signatures_required`.

| Pair | Contract Address | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✅ HEALTHY |

All 5 multisig contracts healthy: 2-of-N signature threshold confirmed.

### MNX Markets

`https://testnet.mnx.fi` is a Next.js SPA. No REST API accessible via crawl (`/api/markets`, `/api/v1/markets`). `mnx_snapshots` table empty — requires browser JS execution.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,697 ⭐ — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,149 ⭐ — pushed 2026-06-01 (active today)
- **kubeflow/spark-operator**: 3,124 ⭐ — K8s operator for Apache Spark
- **migalkin/NodePiece**: 144 ⭐ — scalable KG representations (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 61 ⭐ — OCaml MCP SDK using oxcaml_effect
- **AustinCStone/TextGAN**: 92 ⭐ — text GAN in TensorFlow
- **plurigrid/gorj**: This repo — forj + Rama nREPL + GF(3) coloring (pushed today!)
- **bmorphism/Gay.jl**: Wide-gamut GF(3) color library, 189 open issues
- **All 5 multisig contracts**: 2-of-N threshold, fully healthy
