# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-10

## Sweep Metadata
- **Date:** 2026-06-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 391 |
| Total Repo Snapshots | 391 |
| Sources Covered | 3 orgs + 8 users |
| Aptos wallets probed | 28 |
| Multisig contracts probed | 5 |

---

## GF(3) Color Chain Distribution (391 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 130 |
| 1 | `#b8bb26` | PLUS | 131 |
| -1 | `#cc241d` | MINUS | 130 |

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 25 | 2026-04-26 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |
| StochFlow | Python | 4 | 2024-03-20 |
| gorj | Clojure | 0 | 2026-06-10 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,713 | 2026-05-24 |
| pipelines | Python | 4,153 | 2026-06-09 |
| spark-operator | Python | 3,126 | 2026-06-09 |
| trainer | Go | 2,112 | 2026-06-10 |
| katib | Python | 1,685 | 2026-06-05 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| jank-crane | C++ | 0 | 2026-06-08 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (97 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 19 | 2025-01-05 |
| Gay.jl | Julia | 1 | 2026-06-10 |

### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 25 | 2026-02-16 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |

### AustinCStone (40 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TextGAN | Python | 92 | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |
| SpectralClustering | Python | 3 | 2021-04-16 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 97 |
| kubeflow | org | 48 |
| AustinCStone | social | 40 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| wasita | social | 11 |
| M1shaaa | social | 8 |
| DJedamski | social | 6 |
| kristinezheng | social | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **391** |

---

## Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` on Aptos mainnet.
Accounts have no `CoinStore<AptosCoin>` initialized — either unused on mainnet or testnet-only.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | null (uninitialized) |
| bob | 0x0a3c...2d5d | null (uninitialized) |
| A–Z | 0x8699...–0x7af0... | null (uninitialized) |

### Multisig Contract Probes (5/5 healthy)

All 5 multisig contracts are reachable on Aptos mainnet. Each requires exactly **2 signatures**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Vercel deployment is password-protected. Both `/` and `/api/markets` return an authentication challenge. No market data accessible without credentials.

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
- **kubeflow/kubeflow**: 15,713 stars — flagship ML platform for Kubernetes
- **kubeflow/trainer**: pushed 2026-06-10 (same day as this sweep) — Distributed AI + LLM fine-tuning on K8s
- **plurigrid/gorj**: 469 open issues, pushed 2026-06-10 — this very repo
- **bmorphism/Gay.jl**: pushed 2026-06-10, 189 open issues — wide-gamut SPI color sampling
- **migalkin/NodePiece**: 144 stars — compositional KG representations (ICLR 2022)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP via Jane Street oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — TensorFlow text generation GAN
- **All 5 multisig contracts**: healthy, 2-of-N on Aptos mainnet
- **28 Hamming wallets**: uninitialized on mainnet (no CoinStore)
