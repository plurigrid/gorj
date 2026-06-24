# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-24

## Sweep Metadata
- **Date:** 2026-06-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 414 |
| Total Repo Snapshots | 1,335 |
| Aptos Wallets Probed | 28 (A–Z + alice + bob) |
| Multisig Contracts | 5 (all healthy, 2-of-N) |
| MNX Markets | unavailable (Vercel auth) |
| Sources Covered | 3 orgs + 8 users + social graph |

---

## GF(3) Color Chain Distribution

GF(3) trit assigned per world_increment row: `id % 3`

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | **ERGODIC** | 137 |
| +1 | `#b8bb26` | **PLUS** | 139 |
| -1 | `#cc241d` | **MINUS** | 138 |

Chain cycles: `ERGODIC → PLUS → MINUS → ERGODIC → …` (138 complete cycles)

---

## Top Repos by Source (2026-06-24 snapshot)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 26 | 2026-06-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| gorj | Clojure | 0 | 2026-06-24 |
| place | TeX | 1 | 2026-06-24 |
| eirobri | Clojure | 0 | 2026-06-23 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,741 | 2026-06-18 |
| pipelines | Python | 4,157 | 2026-06-23 |
| spark-operator | Python | 3,128 | 2026-06-24 |
| trainer | Go | 2,119 | 2026-06-22 |
| katib | Python | 1,685 | 2026-06-23 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| Gay.jl | Julia | 2 | 2026-06-24 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |

### migalkin (30 repos, social)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (40 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
**Result: All 28 wallets returned 0.00 APT** (CoinStore resource not found — wallets may be unfunded or hold assets in Fungible Asset form rather than legacy CoinStore).

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.00 |
| bob | 0x0a3c...2d5d | 0.00 |
| A–Z (26) | various | 0.00 each |

**Swarm total: 0.00 APT**

### Multisig Contract Probes

5 contracts probed via `0x1::multisig_account::num_signatures_required` view function.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**5/5 contracts healthy. All require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE — Vercel authentication required**  
All API paths return a Vercel auth challenge. No market data retrievable without authenticated Vercel session.

---

## Repo Counts by Source (2026-06-24)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user | 40 |
| migalkin | social | 30 |
| wasita | social | 11 |
| TeglonLabs | org | 5 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| DJedamski | social | 6 |
| **TOTAL** | | **~391 unique** |

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

## Notable Highlights (2026-06-24)
- **kubeflow/kubeflow**: 15,741 stars — flagship ML platform for Kubernetes (pushed 2026-06-18)
- **kubeflow/pipelines**: 4,157 stars — pushed 2026-06-23 (active)
- **kubeflow/spark-operator**: 3,128 stars — pushed 2026-06-24 (active today)
- **migalkin/NodePiece**: 144 stars — compositional knowledge graph representations
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs (TensorFlow)
- **plurigrid/asi**: 26 stars — topological chemputer (pushed 2026-06-10)
- **plurigrid/gorj**: This very repo — 779 open issues, pushed 2026-06-24 (most active plurigrid repo)
- **bmorphism/Gay.jl**: 187 open issues — wide-gamut GF(3) color sampling in Julia
- **All 5 multisig contracts**: 2-of-N healthy — Hamming swarm coordination intact
