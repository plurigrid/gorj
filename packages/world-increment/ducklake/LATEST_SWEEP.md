# World-Increment Sweep + Hamming Snapshot — 2026-06-20

## Sweep Metadata
- **Date:** 2026-06-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (this run)

| Metric | Value |
|--------|-------|
| New World Increments | 149 (cumulative: 172) |
| New Repo Snapshots | 149 (cumulative: 1093) |
| Aptos wallets probed | 28 (all balance=0) |
| Multisig contracts probed | 5 (all healthy, 2-of-N) |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph

### Top Repos by Source (2026-06-20 snapshot)

#### plurigrid (44 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 26 | 2026-06-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| StochFlow | Python | 4 | 2024-03-20 |
| microworlds | Rust | 3 | 2023-05-13 |
| gorj | Clojure | 0 | **2026-06-20** (703 open issues!) |

#### kubeflow (33 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,737 | 2026-06-18 |
| pipelines | Python | 4,155 | **2026-06-20** |
| spark-operator | Python | 3,127 | 2026-06-18 |
| trainer | Go | 2,118 | 2026-06-19 |
| katib | Python | 1,683 | 2026-06-15 |

#### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| jank-crane | C++ | 0 | 2026-06-08 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

#### bmorphism (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 19 | 2025-01-05 |
| Gay.jl | Julia | 2 | **2026-06-20** (187 open issues) |
| satreadout | HTML | 0 | **2026-06-20** |

#### Zubyul social graph
| User | Notable Repos | Activity |
|------|---------------|----------|
| zubyul | gay-world, cascade-world, voice-observatory | Active to 2026-04 |
| migalkin | NodePiece (144★), StarE (89★), kgcourse2021 (25★) | KG/GNN researcher |
| wasita | magic-garden (2★) | Active to 2026-06 |
| AustinCStone | TextGAN (92★), StereoVisionMRF (11★) | ML researcher |
| DJedamski | School (1★), kaggle repos | Inactive since 2018 |
| kristinezheng | 5 MIT cog-sci repos | Inactive |
| M1shaaa | 6 Yale/Lookit repos | Inactive |

### GF(3) Color Chain Distribution (this run: 149 increments)
| GF(3) | Trit | Color | Count |
|-------|------|-------|-------|
| ERGODIC | 0 | #d3869b | 50 |
| PLUS | +1 | #b8bb26 | 50 |
| MINUS | -1 | #cc241d | 49 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, ledger v5838085875)

All 28 Hamming swarm addresses returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**All balances: 0 APT** — accounts appear unfunded or coins held in non-CoinStore resources.

| World | Address (prefix) | Balance |
|-------|-----------------|---------|
| alice | 0xc793ac... | 0 APT |
| bob | 0x0a3c00... | 0 APT |
| A–Z (26) | various | 0 APT each |

### Multisig Contract Probes

All 5 contracts called `0x1::multisig_account::num_signatures_required` — all healthy:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | **2** | ✓ healthy |
| A-G | 0xf56c4a... | **2** | ✓ healthy |
| Y-Z | 0xd3ffe1... | **2** | ✓ healthy |
| S-T | 0x3b1c3a... | **2** | ✓ healthy |
| V-W | 0x40fad7... | **2** | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — `testnet.mnx.fi` is Vercel-auth protected.  
Both root and `/api/markets` paths return authentication walls. No data.

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

## Notable Highlights (2026-06-20)
- **plurigrid/gorj**: pushed today (2026-06-20) with **703 open issues** — most active issue count
- **bmorphism/Gay.jl**: pushed today with **187 open issues** — deterministic color SPI very active
- **kubeflow/pipelines**: pushed today, 4,155 stars — flagship ML pipeline
- **kubeflow/kubeflow**: 15,737 stars (up from 15,565 in Apr snapshot)
- **migalkin/NodePiece**: 144 stars — top KG embedding library
- **AustinCStone/TextGAN**: 92 stars — most starred in social graph
- **All 5 Hamming multisig contracts**: 2-of-N, healthy
- **All 28 Aptos swarm wallets**: zero APT balance (resource_not_found)
