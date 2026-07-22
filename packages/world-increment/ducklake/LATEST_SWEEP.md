# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-22

## Sweep Metadata
- **Date:** 2026-07-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 103 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 106 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 12 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 41 |
| **TOTAL** | | **403** |

### Summary Counts (this run)

| Metric | Value |
|--------|-------|
| World Increments inserted | 71 |
| Repo Snapshots (cumulative) | 992 |
| Aptos wallets snapshotted | 28 |
| Multisig probes | 5 |
| Sources covered | 3 orgs + 8 users |

### GF(3) Color Chain Distribution (this run)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 23 |
| +1 | `#b8bb26` | PLUS | 24 |
| -1 | `#cc241d` | MINUS | 24 |

### Top Repos by Source (2026-07-22 snapshot)

#### plurigrid (103 repos)
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-17 |
| gorj | Clojure | 1 | 2026-07-07 |
| ontology | JavaScript | 8 | 2026-05-09 |
| Plurigraph | JavaScript | 3 | 2026-05-12 |
| vcg-auction | Rust | 7 | 2025-12-16 |

#### kubeflow (49 repos)
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow | — | 15,788 | 2026-07-22 |
| pipelines | Python | 4,169 | 2026-07-22 |
| spark-operator | Python | 3,142 | 2026-07-21 |
| trainer | Go | 2,153 | 2026-07-22 |
| katib | Python | 1,692 | 2026-07-20 |
| kale | Python | 695 | 2026-07-22 |
| examples | Jsonnet | 1,461 | 2026-07-22 |
| mcp-server | Python | 29 | 2026-07-21 (**new**) |

#### TeglonLabs (5 repos)
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |

#### bmorphism (106 repos)
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | 2026-07-21 (187 open issues) |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| gay-chat | Scheme | 0 | 2026-07-14 (**new**) |
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| risc0-cosmwasm-example | Rust | 23 | 2025-05-21 |

#### Social Graph
| User | Repo | Stars | Last Push |
|------|------|-------|-----------|
| migalkin | NodePiece | 144 | 2026-05-07 |
| migalkin | StarE | 89 | 2026-04-16 |
| wasita | wasita.github.io | 1 | 2026-07-21 |
| AustinCStone | TextGAN | 92 | 2025-03-03 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, ledger ~6,406,416,535)

All 28 addresses returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
Accounts may be using the Fungible Asset (FA) coin standard, or are unfunded.

| World | Balance (APT) |
|-------|---------------|
| alice, bob | 0.0 each |
| A–Z (26) | 0.0 each |
| **Total** | **0.0 APT** |

### Multisig Contract Probes (`0x1::multisig_account::num_signatures_required`)

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a1c... | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | ✅ HEALTHY |
| V-W | 0x40fad7b4... | 2 | ✅ HEALTHY |

All 5 multisig contracts: **2-of-N, live and responsive**.

### MNX Markets (testnet.mnx.fi)

MNX testnet is a Next.js SPA. No public API endpoints available:
- `GET /api/markets` → 404
- `GET /api/v1/markets` → SPA HTML fallback

**Status: UNAVAILABLE** — no market data extractable via REST.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Key Findings (2026-07-22)
- **kubeflow** is the highest-velocity org: `examples`, `trainer`, `pipelines`, `kale` all pushed today
- **kubeflow/mcp-server** is a new MCP integration (29★, 36 forks, 42 open issues) added 2026-04-08
- **bmorphism/Gay.jl** has 187 open issues — highly active development
- **bmorphism/gay-chat** is new (created 2026-07-14): gay://chat over Spritely Brassica
- **wasita** is recently active (personal site updated 2026-07-21)
- **Hamming swarm wallets** all at 0 APT — CoinStore legacy resource not initialized
- **All 5 multisig contracts** live, healthy, requiring 2-of-N signatures
- **MNX testnet** SPA only, no REST API surface found
