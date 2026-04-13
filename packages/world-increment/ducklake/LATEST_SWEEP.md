# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-13

## Sweep Metadata
- **Date:** 2026-04-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 350 |
| Total Repo Snapshots | 809 |
| Sources Covered | 3 orgs + 8 users + 6 social graph users |
| Aptos wallets probed | 28 (alice, bob, A–Z) |
| Multisig contracts probed | 5 (all healthy, 2-of-N) |
| MNX markets | unavailable (SPA, no REST API) |

---

## GF(3) Color Chain — 350 Increments

| GF3 Trit | Color | Name | Count |
|----------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 116 |
| +1 | `#b8bb26` | PLUS | 117 |
| -1 | `#cc241d` | MINUS | 117 |

GF(3) assignment rule: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`  
350 increments = 116.67 full GF(3) cycles — balanced ternary conservation.

---

## Top Repos by Source (2026-04-13 snapshot)

### kubeflow (94 repos, 67,721 total stars)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,570 | 2026-01-05 |
| pipelines | Python | 4,119 | 2026-04-13 |
| spark-operator | Python | 3,114 | 2026-04-13 |
| trainer | Go | 2,082 | 2026-04-10 |
| katib | Python | 1,678 | 2026-04-12 |
| examples | Jsonnet | 1,459 | 2025-04-14 |
| manifests | YAML | 1,010 | 2026-04-11 |
| arena | Go | 809 | 2026-04-13 |
| mcp-apache-spark-history-server | Python | 150 | 2026-04-08 |

### migalkin (37 repos, 553 total stars)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 143 | 2022-02-02 |
| StarE | Python | 88 | 2023-12-01 |
| kgcourse2021 | HTML | 25 | 2025-08-04 |
| NBFNet_mlx | Python | 10 | 2024-03-02 |

### bmorphism (199 repos, 378 total stars)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 60 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 18 | 2025-01-05 |
| manifold-mcp-server | JavaScript | 13 | 2025-01-11 |
| penrose-mcp | JavaScript | 10 | 2025-01-20 |
| shitcoin | Python | 5 | 2026-04-08 |
| boxxy | Move | 0 | 2026-04-09 |
| postweb | Go | 0 | 2026-04-09 |

### AustinCStone (48 repos, 212 total stars)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

### plurigrid (199 repos, 102 total stars)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-13 |
| ontology | JavaScript | 7 | 2025-05-27 |
| gorj | Clojure | 0 | 2026-04-13 |
| nash-portal | Rust | 0 | 2026-04-13 |

### zubyul (71 repos, 27 total stars)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| nash-tui | Rust | 0 | 2026-04-13 |
| nash-web | Rust | 0 | 2026-04-13 |
| gay-world | Python | 1 | 2026-03-26 |

---

## Repo Counts by Source (2026-04-13)

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 94 | 67,721 |
| bmorphism | user | 199 | 378 |
| migalkin | user (zubyul graph) | 37 | 553 |
| AustinCStone | user (zubyul graph) | 48 | 212 |
| plurigrid | org | 199 | 102 |
| TeglonLabs | org | 57 | 8 |
| zubyul | user | 71 | 27 |
| DJedamski | user (zubyul graph) | 17 | 10 |
| wasita | user (zubyul graph) | 39 | 5 |
| kristinezheng | user (zubyul graph) | 24 | 0 |
| M1shaaa | user (zubyul graph) | 24 | 0 |
| **TOTAL** | | **809** | **69,016** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — 28 Addresses
**Endpoint:** `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`  
**Ledger version probed:** 4,862,302,185

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for the legacy `CoinStore<AptosCoin>` resource. These accounts likely use the Aptos Fungible Asset standard or have zero APT balance in the legacy store.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | NULL |
| bob | 0x0a3c...12d5d | NULL |
| A–Z | 0x8699...–0x7af0... | NULL (×26) |

### Multisig Contract Probes
**Function:** `0x1::multisig_account::num_signatures_required`

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...87003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy** — 2-of-N threshold on all pairs.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Next.js SPA routes all requests to HTML shell. Endpoints tried: `/api/markets`, `/api/tickers`, `/api/pairs`, `/api/v1/markets`. No structured market data extractable without JS runtime.

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
- **kubeflow/kubeflow**: 15,570 stars — flagship ML platform for Kubernetes (pushed 2026-01-05)
- **kubeflow/spark-operator**: 3,114 stars — pushed 2026-04-13 (today!)
- **kubeflow/mpi-operator**: MPI-based distributed training — pushed 2026-04-13 (today!)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — GAN-based text generation in TensorFlow
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring (pushed today!)
- **zubyul/nash-web + nash-tui**: Both pushed 2026-04-13 — active NASH token WASM TUI development
- **Hamming swarm**: All 5 multisig contracts healthy, 2-of-N threshold — A-B, A-G, Y-Z, S-T, V-W
