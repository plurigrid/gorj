# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-22

## Sweep Metadata
- **Date:** 2026-06-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 9 |
| Total Repo Snapshots | 191 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — All 9 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | social_graph (6 users) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | hamming_swarm (aptos) | balance_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | hamming_swarm (multisig) | multisig_health | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source

### plurigrid (59 repos snapshotted)
| Repo | Language | Stars | Open Issues | Pushed At |
|------|----------|-------|-------------|----------|
| gorj | Clojure | 0 | **745** | 2026-06-22 |
| asi | HTML | **26** | 4 | 2026-06-10 |
| ontology | JavaScript | 8 | 16 | 2025-05-27 |
| vcg-auction | Rust | 7 | 1 | 2023-03-16 |
| agent | Python | 5 | 6 | 2023-03-31 |

### kubeflow (24 repos snapshotted)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|----------|
| kubeflow | — | **15,740** | 2026-06-18 |
| pipelines | Python | **4,157** | 2026-06-22 |
| spark-operator | Python | **3,128** | 2026-06-22 |
| trainer | Go | 2,118 | 2026-06-22 |
| katib | Python | 1,685 | 2026-06-20 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (41 repos snapshotted)
| Repo | Language | Stars | Open Issues |
|------|----------|-------|-------------|
| Gay.jl | Julia | 2 | **187** |
| ocaml-mcp-sdk | OCaml | **61** | 0 |
| anti-bullshit-mcp-server | JavaScript | 23 | 1 |
| say-mcp-server | JavaScript | 20 | 3 |
| babashka-mcp-server | JavaScript | 19 | 3 |

### migalkin (6 repos snapshotted)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | **144** |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |

### Social Graph (DJedamski/wasita/kristinezheng/M1shaaa/AustinCStone)
| Repo | User | Stars | Notes |
|------|------|-------|-------|
| TextGAN | AustinCStone | **92** | GAN for text, TensorFlow |
| StereoVisionMRF | AustinCStone | 11 | MRF depth estimation |
| magic-garden | wasita | 2 | Discord bot |
| wins-search | wasita | 1 | Women in Network Science |

---

## Repo Counts by Source

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 59 |
| bmorphism | user | 41 |
| kubeflow | org | 24 |
| zubyul | user | 29 |
| AustinCStone | social | 7 |
| migalkin | user | 6 |
| wasita | social | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | social | 5 |
| M1shaaa | social | 5 |
| DJedamski | social | 4 |
| **TOTAL** | | **191** |

---

## Hamming Swarm — Aptos Snapshot

### Wallet Balances (alice, bob, A–Z = 28 addresses)

All 28 addresses queried against Aptos mainnet `fullnode.mainnet.aptoslabs.com`. The `CoinStore<AptosCoin>` resource was not found on any address — balances recorded as 0.0 APT. Wallets are likely uninitialized or use a non-standard coin type.

**Total APT across swarm: 0.0**

### Multisig Contract Health

| Pair | Contract | Sigs Required | Healthy |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts live — 2-of-2 threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — HTTP 401 Unauthorized on both `testnet.mnx.fi` and `testnet.mnx.fi/api/markets`. Testnet requires authentication; no market data captured.

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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights (2026-06-22 vs previous sweep 2026-04-12)
- **plurigrid/gorj**: 745 open issues (up from previous sweep) — active development in this very repo
- **plurigrid/asi**: 26★ (up from 16★) — topological chemputer growing
- **kubeflow/kubeflow**: 15,740★ (up from 15,565★)
- **kubeflow/pipelines**: 4,157★ (up from 4,119★) — active pushes 2026-06-22
- **bmorphism/Gay.jl**: 187 open issues — canonical GF(3) color library heavily developed
- **bmorphism/ocaml-mcp-sdk**: 61★ — OCaml SDK for MCP (Jane Street oxcaml_effect)
- **migalkin/NodePiece**: 144★ — knowledge graph embeddings (ICLR 2022)
- **All 5 Aptos multisig contracts** respond at 2-of-2; Hamming swarm wallet balances all 0 APT
