# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-16

## Sweep Metadata
- **Date:** 2026-05-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 117 |
| Total Repo Snapshots | 117 |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution (117 increments)

| GF3 Trit | Color | Name | Count |
|----------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 39 |
| +1 | `#b8bb26` | PLUS | 39 |
| -1 | `#cc241d` | MINUS | 39 |

GF(3) assignment rule:
- `id % 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id % 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id % 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

## Top Repos by Source

### plurigrid (34 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 23 | 2026-04-26 |
| StochFlow | Python | 4 | 2024-03-20 |
| ontology | JavaScript | 8 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-26 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| gorj | Clojure | 0 | 2026-05-16 (today, 215 open issues) |

### kubeflow (20 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,636 | 2026-05-07 |
| pipelines | Python | 4,139 | 2026-05-15 |
| spark-operator | Python | 3,125 | 2026-05-15 |
| trainer | Go | 2,098 | 2026-05-15 |
| katib | Python | 1,682 | 2026-05-09 |

### bmorphism (17 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| hypernym-mcp-server | JavaScript | 6 |
| open-location-code-zig | Zig | 3 |

### zubyul (16 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jonikas_lab_data_analysis_misc | Jupyter | 2 | 2023-08-16 |
| WGCNA | HTML | 2 | 2023-07-05 |
| gay-world | Python | 1 | 2026-03-26 |
| voice-observatory | Python | 0 | 2026-04-24 (most recent) |

### migalkin (6 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |
| NBFNet_mlx | Python | 10 |

### AustinCStone (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source (this sweep)

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 34 |
| kubeflow | org | 20 |
| bmorphism | user | 17 |
| zubyul | user | 16 |
| wasita | user (social graph) | 6 |
| migalkin | user (social graph) | 6 |
| AustinCStone | user (social graph) | 5 |
| TeglonLabs | org | 4 |
| DJedamski | user (social graph) | 4 |
| M1shaaa | user (social graph) | 3 |
| kristinezheng | user (social graph) | 2 |
| **TOTAL** | | **117** |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (ledger ~5,299,106,821)

All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
No APT balances on mainnet for any swarm address.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`. All healthy.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — `testnet.mnx.fi` is a Next.js SPA. Both `/api/markets` and `/api/tickers` return the HTML shell. No market data extractable without a headless browser. Sentinel row recorded in `mnx_snapshots`.

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
- **kubeflow/kubeflow**: 15,636 stars — flagship ML platform for Kubernetes (star growth +71 since Apr 12)
- **kubeflow/pipelines**: 4,139 stars — ML pipeline platform, pushed 2026-05-15
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **migalkin/NodePiece**: 144 stars — compositional KG embeddings (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — TF text generation GAN
- **plurigrid/asi**: 23 stars — topological chemputer (+7 since Apr 12)
- **plurigrid/gorj**: this repo — pushed today, 215 open issues
- **bmorphism/Gay.jl**: 188 open issues — GF(3) wide-gamut color library, most active bmorphism repo
- **Hamming swarm**: 5/5 multisigs healthy (all 2-of-N), wallet balances all 0 (accounts not initialized on mainnet)
- **MNX testnet**: SPA only, no REST API surface accessible
