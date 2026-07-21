# World-Increment Sweep + Hamming Snapshot — 2026-07-21

## Sweep Metadata
- **Date:** 2026-07-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Crawled

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | ~90 repos |
| kubeflow | org | 49 repos |
| TeglonLabs | org | 5 repos |
| bmorphism | user | 106 repos |
| zubyul | user | 49 repos |
| wasita | social graph | 10+ repos |
| migalkin | social graph | 7 repos |
| AustinCStone | social graph | 8 repos |
| kristinezheng | social graph | 3 repos |
| M1shaaa | social graph | 4 repos |
| DJedamski | social graph | 1 repo |

### Top Repos by Stars (2026-07-21 snapshot)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,789 | — |
| kubeflow/pipelines | 4,169 | Python |
| kubeflow/spark-operator | 3,142 | Python |
| kubeflow/trainer | 2,152 | Go |
| kubeflow/katib | 1,692 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| kubeflow/community-distribution | 1,029 | YAML |
| kubeflow/arena | 815 | Go |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |
| bmorphism/anti-bullshit-mcp-server | 22 | JavaScript |
| plurigrid/asi | 31 | HTML |
| plurigrid/ontology | 8 | JavaScript |

### Plurigrid — Most Active (2026-07)

| Repo | Stars | Open Issues | Pushed |
|------|-------|-------------|--------|
| plurigrid/gorj | 1 | 1300 | 2026-07-21 |
| plurigrid/eirobri | 0 | 31 | 2026-07-21 |
| plurigrid/asi | 31 | 4 | 2026-07-10 |
| plurigrid/place | 1 | 14 | 2026-07-14 |

### bmorphism — Most Active (2026-07)

- `Gay.jl` — Wide-gamut color sampling, splittable determinism (⭐2, 187 open issues, updated 2026-07-21)
- `gay-chat` — gay://chat over Spritely Brassica Chat (updated 2026-07-14)
- `anti-bullshit-mcp-server` — multi-framework claim validation (⭐22, updated 2026-07-12)

### wasita — Most Active (2026-07)

- `wasita.github.io` — personal site, SvelteKit/Tailwind (updated 2026-07-21)
- `wm-cv` — Academic CV (updated 2026-07-14)

### GF(3) World Increments

105 new `world_increment` rows inserted, cycling:
```
id%3==0 → trit=0, #d3869b, ERGODIC
id%3==1 → trit=1, #b8bb26, PLUS
id%3==2 → trit=2, #cc241d, MINUS
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 wallets queried via `fullnode.mainnet.aptoslabs.com` (1s sleep between calls).

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac… | 0.0 |
| bob | 0x0a3c00… | 0.0 |
| A | 0x8699ed… | 0.0 |
| B | 0x3f892e… | 0.0 |
| C | 0x38b99e… | 0.0 |
| D | 0xf77656… | 0.0 |
| E | 0xdc1d9d… | 0.0 |
| F | 0x18a14b… | 0.0 |
| G | 0x69a394… | 0.0 |
| H | 0xce67c3… | 0.0 |
| I | 0x070fe5… | 0.0 |
| J | 0x4d964d… | 0.0 |
| K | 0xa73204… | 0.0 |
| L | 0x7c2eae… | 0.0 |
| M | 0x6fed37… | 0.0 |
| N | 0xe7dde6… | 0.0 |
| O | 0x73252b… | 0.0 |
| P | 0x621879… | 0.0 |
| Q | 0xac40fa… | 0.0 |
| R | 0x7ce605… | 0.0 |
| S | 0xb87530… | 0.0 |
| T | 0x35781d… | 0.0 |
| U | 0x75860d… | 0.0 |
| V | 0xb59dd8… | 0.0 |
| W | 0x5f32ae… | 0.0 |
| X | 0xa95cbb… | 0.0 |
| Y | 0xd8e328… | 0.0 |
| Z | 0x7af0ef… | 0.0 |

**Interpretation:** No CoinStore resources initialized on any swarm address. Addresses exist on-chain but hold 0 APT native balance. May hold other Aptos resources (Move objects, NFTs, custom tokens).

### Multisig Contract Probes

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4f4… | 2 | ✅ |
| A-G | 0xf56c4a… | 2 | ✅ |
| Y-Z | 0xd3ffe1… | 2 | ✅ |
| S-T | 0x3b1c3a… | 2 | ✅ |
| V-W | 0x40fad7… | 2 | ✅ |

All 5 multisig contracts **healthy**, all requiring **2-of-N signatures**.

### MNX Markets (testnet.mnx.fi)

- All API paths (`/api/markets`, `/api/v1/markets`) → HTTP 401
- Root → HTTP 401 (authentication required)
- **Status:** Unavailable from public/unauthenticated endpoints

---

## DuckDB Summary

**Path:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows Added This Run |
|-------|---------------------|
| world_increments | 105 |
| repo_snapshots | 105 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (API gated) |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=2, color=#cc241d, name=MINUS

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
