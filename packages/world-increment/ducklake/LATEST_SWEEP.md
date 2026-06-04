# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-04

## Sweep Metadata
- **Date:** 2026-06-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 129 |
| Total Repo Snapshots | 129 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Market Snapshots | 0 (SPA — no JSON API) |

---

## GF(3) Color Chain

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=**PLUS**
- `id mod 3 == 2` → trit=2, color=#cc241d, name=**MINUS**

Cycle repeats across all 129 world increment IDs.

---

## Top Repos by Source

### plurigrid (28 repos, 48 total stars)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 24 | 2026-04-26 |
| ontology | JavaScript | 8 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-26 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| nash-portal | Rust | 2 | 2026-05-19 |
| gorj | Clojure | 0 | 2026-06-04 |

### kubeflow (20 repos, 33,161 total stars)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,705 | 2026-05-24 |
| pipelines | Python | 4,152 | 2026-06-03 |
| spark-operator | Python | 3,125 | 2026-06-03 |
| trainer | Go | 2,110 | 2026-06-03 |
| katib | Python | 1,685 | 2026-05-29 |
| examples | Jsonnet | 1,462 | 2025-04-14 |
| manifests | YAML | 1,020 | 2026-06-02 |

### TeglonLabs (4 repos, 2 total stars)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

### bmorphism (33 repos, 139 total stars)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| Gay.jl | Julia | 1 | 2026-06-04 |
| manifold-mcp-server | JavaScript | 14 | 2025-01-11 |
| penrose-mcp | JavaScript | 10 | 2025-01-20 |
| shitcoin | Python | 5 | 2026-04-08 |
| whale | MATLAB | 2 | 2025-09-04 |

### migalkin — zubyul social graph (6 repos, 279 total stars)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |
| NBFNet_mlx | Python | 10 |
| RWL | Python | 8 |
| rambo | Rust | 3 |

### AustinCStone — zubyul social graph (6 repos, 107 total stars)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |
| logisticRegressionHaskell | Haskell | 1 |

### zubyul (17 repos, 9 total stars)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gay-world | Python | 1 | 2026-03-26 |
| zubyul.github.io | CSS | 1 | 2026-01-27 |
| cascade-world | Python | 1 | 2025-09-19 |
| nash-tui | Rust | 0 | 2026-04-13 |
| nash-web | Rust | 0 | 2026-04-13 |
| voice-observatory | Python | 0 | 2026-04-24 |

---

## Repo Counts by Source

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| kubeflow | org | 20 | 33,161 |
| migalkin | user (social) | 6 | 279 |
| bmorphism | user | 33 | 139 |
| AustinCStone | user (social) | 6 | 107 |
| plurigrid | org | 28 | 48 |
| zubyul | user | 17 | 9 |
| wasita | user (social) | 6 | 5 |
| TeglonLabs | org | 4 | 2 |
| DJedamski | user (social) | 3 | 2 |
| kristinezheng | user (social) | 3 | 0 |
| M1shaaa | user (social) | 3 | 0 |
| **TOTAL** | | **129** | **33,752** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

Queried 28 wallets (alice, bob, A–Z) via Aptos fullnode mainnet.
**All balances: 0.00 APT** — CoinStore resource absent on all addresses; accounts are non-funded/non-initialized on mainnet.

### Multisig Contract Probes

All 5 multisig contracts are healthy (sigs_required=2 each).

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...987003 | 2 | true |
| A-G | 0xf56c4a1c...c0096 | 2 | true |
| Y-Z | 0xd3ffe181...75b883 | 2 | true |
| S-T | 0x3b1c3ae9...ed7883 | 2 | true |
| V-W | 0x40fad7b4...80eb6d | 2 | true |

**All multisigs operational.** 2-of-N threshold confirmed for all pairs.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable via REST API** — `testnet.mnx.fi` is a Next.js SPA.
All API path probes (`/api/markets`, `/api/v1/markets`, `/api/tickers`) returned HTML.
No market data extracted. `mnx_snapshots` table: 0 rows.

---

## DuckDB Schema
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
- **kubeflow/kubeflow**: 15,705 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,152 stars — most active push 2026-06-03
- **migalkin/NodePiece**: 144 stars — compositional KG representations (ICLR 2022)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK (Jane Street oxcaml_effect)
- **AustinCStone/TextGAN**: 92 stars — GAN text generation
- **plurigrid/gorj**: 0 stars, 336 open issues — this very repo, most active plurigrid project
- **bmorphism/Gay.jl**: 1 star, 189 open issues — pushed 2026-06-04 (today!)
- **Hamming swarm**: all 28 wallets at 0.0 APT; all 5 multisigs at threshold=2
