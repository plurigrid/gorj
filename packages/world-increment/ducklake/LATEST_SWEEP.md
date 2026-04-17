# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-17

## Sweep Metadata
- **Date:** 2026-04-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.1.3 (Selene)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 86+ |
| Total Repo Snapshots (cumulative) | 1007+ (480 unique) |
| Sources Covered | 3 orgs + 8 users (this sweep: 9 sources, 62 new repos) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts | 5/5 healthy |
| MNX Markets Captured | 9 |

---

## GF(3) Color Chain (this sweep, 63 new increments — balanced 21/21/21)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 21 |
| +1 | `#b8bb26` | PLUS | 21 |
| -1 | `#cc241d` | MINUS | 21 |

GF(3) rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 20 |
| kubeflow | org | 13 |
| TeglonLabs | org | 4 |
| bmorphism | user | 13 |
| zubyul | user | 7 |
| migalkin | social graph | 4 |
| DJedamski | social graph | 1 |
| wasita | social graph | 3 |
| AustinCStone | social graph | 1 |

### Top Repos by Source (2026-04-17 snapshot)

#### plurigrid (org)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 0 | 2026-04-16 |
| reafference | HTML | 0 | 2026-04-16 |
| horse | TeX | 1 | 2026-04-16 |
| asi | HTML | 17 | 2026-04-13 |
| nanoclj-zig | Zig | 0 | 2026-04-09 |
| asi-skills | Julia | 3 | 2026-04-09 |
| ontology | JavaScript | 7 | 2025-05-27 |

#### kubeflow (org)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,579 | 2026-04-16 |
| pipelines | Python | 4,121 | 2026-04-16 |
| spark-operator | Python | 3,117 | 2026-04-16 |
| katib | Python | 1,679 | 2026-04-16 |
| trainer | Go | 2,085 | 2026-04-15 |
| mcp-apache-spark-history-server | Python | 151 | 2026-04-16 |

#### bmorphism (user)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 60 | 2026-03-28 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-02-05 |
| whale | MATLAB | 2 | 2026-01-21 |
| boxxy | Move | 0 | 2026-04-13 |
| postweb | Go | 0 | 2026-04-09 |

#### zubyul (user)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| nash-web | Rust | 0 | 2026-04-13 |
| nash-tui | Rust | 0 | 2026-04-13 |
| big-bad-plurigrid-quiz | Emacs Lisp | 0 | 2026-04-09 |
| gay-world | Python | 1 | 2026-04-05 |
| Gay.jl | Julia | 0 | 2026-03-28 |

#### Social Graph
| User | Repo | Stars | Language |
|------|------|-------|----------|
| migalkin | NodePiece | 143 | Python |
| migalkin | StarE | 89 | Python |
| migalkin | kgcourse2021 | 25 | HTML |
| wasita | wasita.github.io | 0 | Svelte |
| wasita | magic-garden | 1 | Python |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 wallets)
All 28 Hamming swarm addresses (alice, bob, A–Z) queried against Aptos mainnet.

**Result:** All 28 addresses returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
Wallets either hold no APT or use the newer `FungibleAsset` standard.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793…4cc7b | 0.0 |
| bob | 0x0a3c…512d | 0.0 |
| A | 0x8699…e9d7a | 0.0 |
| B | 0x3f89…cb13 | 0.0 |
| C–Z | (22 more) | 0.0 each |

### Multisig Contract Probes (5 pairs)
All queried via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

**All 5 multisig contracts healthy — unanimous 2-of-n threshold.**

### MNX Markets (testnet.mnx.fi)
9 markets captured from SPA frontend.

| Ticker | Name | Category | Price | Change |
|--------|------|----------|-------|--------|
| OAI26 | OpenAI Final 2026 Valuation | Valuations | $526B | +0.19% |
| ANT26 | Anthropic Final 2026 Valuation | Valuations | $419B | -1.18% |
| DPREZ | Democrat Elected President 2028 | Politics | 50% | +1.23% |
| H100 | SemiAnalysis H100 Rental Index | Compute | $2.76 | -0.72% |
| MSFT | Microsoft | Stocks | $421.46 | +1.17% |
| NVDA | NVIDIA | Stocks | $198.03 | -0.30% |
| TSLA | Tesla Inc | Stocks | $388.45 | -1.43% |
| SPX | S&P 500 Index | Financial | 7,037 | +0.33% |
| INVADE27 | China invades Taiwan (before 2027) | Politics | 16% | **-3.66%** |

**Top movers:** INVADE27 -3.66% · TSLA -1.43% · ANT26 -1.18% · DPREZ +1.23%

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
- **kubeflow/kubeflow**: 15,579 stars — flagship ML platform for Kubernetes (active 2026-04-16)
- **kubeflow/pipelines**: 4,121 stars — most popular ML pipeline for Kubernetes
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP via Jane Street's oxcaml_effect
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **ANT26 -1.18%**: Anthropic 2026 valuation down on MNX prediction markets
- **INVADE27 -3.66%**: Taiwan invasion probability falling on MNX (now at 16%)
- **Hamming swarm**: 28 wallets probed, 5 multisig pairs all healthy (2-of-n)
