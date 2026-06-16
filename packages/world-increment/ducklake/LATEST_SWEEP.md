# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-16

## Sweep Metadata
- **Date:** 2026-06-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 76 (this run) |
| Total Repo Snapshots (today) | 53 |
| Sources Covered | 3 orgs + 8 users |
| Aptos addresses checked | 28 |
| Multisig contracts probed | 5 |

---

## GF(3) Color Chain (id%3)
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC** (24 increments)
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=**PLUS** (26 increments)
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS** (26 increments)

---

## Top Repos by Source

### plurigrid (101 total repos)
| Repo | Language | Stars | Open Issues | Pushed At |
|------|----------|-------|-------------|-----------|
| gorj | Clojure | 0 | **624** | 2026-06-16 (today) |
| asi | HTML | 26 | 4 | 2026-06-10 |
| place | TeX | 1 | 8 | 2026-06-15 |
| eirobri | Clojure | 0 | 29 | 2026-06-03 |
| ontology | JavaScript | 8 | 16 | 2025-05-27 |

### kubeflow (48 total repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15724 | 2026-06-11 |
| pipelines | Python | 4154 | 2026-06-16 (today) |
| spark-operator | Python | 3127 | 2026-06-15 |
| trainer | Go | 2115 | 2026-06-16 (today) |
| katib | Python | 1683 | 2026-06-15 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (104 total repos)
| Repo | Language | Stars | Open Issues | Pushed At |
|------|----------|-------|-------------|-----------|
| Gay.jl | Julia | 1 | **187** | 2026-06-16 (today) |
| ocaml-mcp-sdk | OCaml | 61 | 0 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 1 | 2026-01-16 |
| say-mcp-server | JavaScript | 20 | 3 | 2025-01-07 |
| risc0-cosmwasm-example | Rust | 23 | 1 | 2022-10-20 |

### zubyul (49 total repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| voice-observatory | Python | 0 | 2026-04-24 |
| gay-world | Python | 1 | 2026-03-26 |
| Gay.jl (fork) | Julia | 0 | 2026-03-28 |

### Social Graph
| User | Repo | Language | Stars | Pushed At |
|------|------|----------|-------|-----------|
| migalkin | NodePiece | Python | 144 | 2022-02-02 |
| migalkin | StarE | Python | 89 | 2023-12-01 |
| migalkin | kgcourse2021 | HTML | 25 | 2025-08-04 |
| wasita | wasita.github.io | Svelte | 1 | 2026-06-15 |
| kristinezheng | kristinezheng.github.io | HTML | 0 | 2026-06-07 |
| M1shaaa | M1shaaa | — | 0 | 2026-06-16 (today) |
| AustinCStone | TextGAN | Python | 92 | 2016-10-04 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-16)
All 28 addresses (alice, bob, A–Z) returned **0.0 APT** from `CoinStore<AptosCoin>`.

| Range | Addresses | APT Balance |
|-------|-----------|-------------|
| alice, bob | 2 addresses | 0.0 each |
| A–Z | 26 addresses | 0.0 each |

All accounts either have no registered CoinStore or hold zero native APT.

### Multisig Contract Probes — ALL HEALTHY
All 5 probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | ✅ healthy |
| A-G | 0xf56c…0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff…b883 | 2 | ✅ healthy |
| S-T | 0x3b1c…7883 | 2 | ✅ healthy |
| V-W | 0x40fa…eb6d | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — The testnet is behind Vercel deployment protection authentication. No market data could be extracted from public API paths. Logged as placeholder in `mnx_snapshots`.

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
- **kubeflow/kubeflow**: 15,724 stars — flagship ML platform, pushed today
- **kubeflow/pipelines**: 4,154 stars — most popular ML pipeline (pushed today)
- **plurigrid/gorj**: 624 open issues — most active plurigrid repo, pushed today
- **bmorphism/Gay.jl**: 187 open issues — wide-gamut GF(3) color system, pushed today
- **TeglonLabs/jank-crane**: new (2026-06-08) — crane-jank converged-IR hub with GF(3) maps
- **migalkin/NodePiece**: 144 stars — compositional KG representations
- **AustinCStone/TextGAN**: 92 stars — GAN text generation
- **M1shaaa profile**: pushed today (2026-06-16) — active
- **All 5 multisig contracts**: healthy with 2-of-N threshold
- **Hamming swarm (A-Z)**: all wallets at 0.0 APT on mainnet
