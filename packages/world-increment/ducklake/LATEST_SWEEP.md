# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-22

## Sweep Metadata
- **Date:** 2026-07-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found | Top Stars |
|--------|------|------------|-----------|
| plurigrid | org | 103 | vcg-auction (7★), ontology (8★), asi (31★) |
| kubeflow | org | 49 | kubeflow (15,789★), pipelines (4,169★) |
| TeglonLabs | org | 5 | mathpix-gem (2★) |
| bmorphism | user | 106 | Gay.jl (2★), ocaml-mcp-sdk (61★) |
| zubyul | user | 49 | gay-world (1★) |
| migalkin | social | 19 | NodePiece (144★), StarE (89★) |
| DJedamski | social | 6 | Kaggle (1★) |
| wasita | social | 12 | wasita.github.io (1★), magic-garden (2★) |
| kristinezheng | social | 5 | (0★) |
| M1shaaa | social | 8 | (0★) |
| AustinCStone | social | 41 | TextGAN (92★) |

### Notable Recent Activity (since last sweep 2026-04-12)

- **plurigrid/asi** (HTML, 31★ ↑ from 16★) — pushed 2026-07-17 — "everything is topological chemputer!"
- **plurigrid/gorj** (Clojure, 1★) — pushed 2026-07-07 — 1,318 open issues
- **plurigrid/shrimp** — pushed 2026-07-03 — new: "Jank worked example: shrimp"
- **bmorphism/Gay.jl** (Julia, 2★) — pushed 2026-07-21 — 187 open issues
- **bmorphism/gay-chat** — pushed 2026-07-14 — new: "gay://chat over Spritely Brassica Chat"
- **kubeflow/hub** (Go, 178★) — pushed 2026-07-22 — Model Registry
- **kubeflow/pipelines** (Python, 4,169★ ↑ from 4,119★) — pushed 2026-07-22
- **wasita/wasita.github.io** (Svelte, 1★) — pushed 2026-07-21
- **wasita/pnas-typst-template** — pushed 2026-07-16 — new repo
- **AustinCStone/byteruckus** (HTML) — pushed 2026-07-15 — new repo

### DuckDB Ducklake State (cumulative across all runs)

| Table | Accumulated Rows |
|-------|-----------------|
| world_increments | 99 |
| repo_snapshots | 1,020 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

### GF(3) Color Chain Distribution (this run, 76 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 32 |
| +1 | #b8bb26 | PLUS | 34 |
| -1 | #cc241d | MINUS | 33 |

Chain is balanced — divergence of 1 trit at closure.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-22)

All 28 addresses in the Hamming swarm (alice, bob, A–Z) returned
`resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
**Balance: 0.00 APT on all wallets.** Accounts exist on-chain but hold no APT in the
tracked coin store (may use FA store or never received APT).

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes (5 pairs)

All 5 multisig accounts are **healthy** and require exactly **2 signatures**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...4987003 | 2 | ✅ healthy |
| A-G | 0xf56c4a1c...bc0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ffe181...e75b883 | 2 | ✅ healthy |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✅ healthy |
| V-W | 0x40fad7b4...80eb6d | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable.** The MNX testnet frontend is a Next.js SPA serving only
a mobile orientation notice. API endpoints `/api/markets` and `/api/v1/markets`
return the SPA shell rather than JSON. `mnx_snapshots` table is empty.

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

## Key Highlights (2026-07-22)
- **kubeflow/kubeflow**: 15,789★ — flagship ML platform for Kubernetes (↑224 from Apr)
- **kubeflow/pipelines**: 4,169★ — most-pushed today (2026-07-22)
- **kubeflow/spark-operator**: 3,142★ — pushed 2026-07-21
- **bmorphism/anti-bullshit-mcp-server**: 22★ — active
- **migalkin/NodePiece**: 144★ — knowledge graph embeddings
- **AustinCStone/TextGAN**: 92★ — text generation with GANs
- **plurigrid/asi**: 31★ ↑ 15 stars since April sweep
- **plurigrid/gorj**: This repo — 1,318 open issues, GF(3) orchestration hub
- **All 5 multisigs**: 2-of-N, healthy as of 2026-07-22
- **28 Hamming swarm wallets**: 0 APT (no legacy coin store found)
