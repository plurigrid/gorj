# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-10

## Sweep Metadata
- **Date:** 2026-07-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (via pip)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 405 (382 new this sweep) |
| Total Repo Snapshots | 1,326 (382 new this sweep) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — This Sweep (382 new increments, IDs 24–405)

GF(3) assignment: `id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d`

| GF3 Name | Color | Count (this sweep) |
|----------|-------|-------------------|
| ERGODIC | `#d3869b` | ~127 |
| PLUS | `#b8bb26` | ~128 |
| MINUS | `#cc241d` | ~127 |

GF(3) running cycle across 405 total increments: balanced trit distribution maintained.

---

## Top Repos by Source (2026-07-10 snapshot)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 30 | 2026-07-10 |
| ontology | JavaScript | 8 | 2026-05-27 |
| vcg-auction | Rust | 7 | 2025-11-12 |
| agent | Python | 5 | 2026-01-16 |
| gorj | Clojure | 1 | 2026-07-10 (today!) |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,771 | 2026-07-10 |
| pipelines | Python | 4,169 | 2026-07-10 |
| spark-operator | Python | 3,136 | 2026-07-10 |
| trainer | Go | 2,134 | 2026-07-09 |
| katib | Python | 1,689 | 2026-07-08 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| jank-crane | C++ | 0 | 2026-06-08 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| risc0-cosmwasm-example | Rust | 23 |
| say-mcp-server | JavaScript | 20 |
| babashka-mcp-server | JavaScript | 19 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |

### AustinCStone (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| AustinCStone | social graph | 30 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 11 |
| M1shaaa | social graph | 8 |
| DJedamski | social graph | 6 |
| kristinezheng | social graph | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **382** |

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
- **kubeflow/kubeflow**: 15,771 stars — flagship ML platform for Kubernetes (active today)
- **kubeflow/pipelines**: 4,169 stars — ML pipelines pushed today
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK using Jane Street oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 30 stars — topological chemputer (pushed today, doubled since Apr sweep)
- **plurigrid/gorj**: 1,101 open issues — active MCP + REPL orchestration work
- **M1shaaa/M1shaaa**: profile repo pushed TODAY (2026-07-10T14:14:51Z)
- **wasita/wasita.github.io**: Svelte personal site, pushed 2026-07-06
- **TeglonLabs/jank-crane**: GF3 convergence maps + crane-jank IR hub (pushed 2026-06-08)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice–Z, 28 addresses)

All 28 Hamming-swarm addresses queried against Aptos mainnet.  
Legacy `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource not found on any address.  
Accounts exist on-chain (resources present) but APT balance is 0 under the legacy coin standard.  
These addresses may hold APT via the newer Fungible Asset standard (not probed in this sweep).

| World | Address |
|-------|---------|
| alice | 0xc793...cc7b |
| bob | 0x0a3c...2d5d |
| A–Z | 26 addresses (see DuckDB aptos_snapshots) |

**Reported APT balance: 0.000 on all 28 addresses** (legacy CoinStore absent).

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts respond with `num_signatures_required = 2`. All healthy.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)

`GET /api/markets` → **HTTP 401 Unauthorized**.  
Market data unavailable without auth. `mnx_snapshots` table empty this sweep.
