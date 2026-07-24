# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Indexed |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 106 (top 9 sampled) |
| zubyul | user | 49 (top 8 sampled) |
| migalkin | social | 19 |
| AustinCStone | social | 41 |
| wasita | social | 12 |
| M1shaaa | social | 8 |
| DJedamski | social | 6 |
| kristinezheng | social | 5 |
| **TOTAL this run** | | **183 new rows** |

### Notable Activity (pushed ≥ 2026-07)

| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| plurigrid/gorj | Clojure | 1 | 2026-07-24 |
| kubeflow/pipelines | Python | 4169 | 2026-07-24 |
| kubeflow/hub | Go | 178 | 2026-07-24 |
| kubeflow/mcp-server | Python | 29 | 2026-07-24 |
| kubeflow/notebooks | — | 74 | 2026-07-24 |
| kubeflow/community-distribution | YAML | 1029 | 2026-07-24 |
| plurigrid/eirobri | Clojure | 0 | 2026-07-21 |
| wasita/wasita.github.io | Svelte | 1 | 2026-07-21 |
| bmorphism/Gay.jl | Julia | 2 | 2026-07-21 |
| plurigrid/place | TeX | 1 | 2026-07-14 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| migalkin/kgcourse2021 | HTML | 24 | 2026-07-10 |
| plurigrid/asi | HTML | 31 | 2026-07-10 |
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |

### Top Stars per Source

| Source | Top Repo | Stars |
|--------|----------|-------|
| kubeflow | pipelines | 4169 |
| migalkin | NodePiece | 144 |
| AustinCStone | TextGAN | 92 |
| bmorphism | ocaml-mcp-sdk | 61 |
| plurigrid | asi | 31 |
| wasita | wasita.github.io | 1 |

### GF(3) Color Chain Rule

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

183 new increment rows added cycling `PLUS → MINUS → ERGODIC → ...` (61 full GF(3) cycles).

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses, 2026-07-24)

All 28 wallets queried via `fullnode.mainnet.aptoslabs.com`. All returned **0 APT** — accounts appear unfunded or their `CoinStore<AptosCoin>` resource does not exist on mainnet.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793ac... | 0.000000 |
| bob | 0x0a3c00... | 0.000000 |
| A–Z (26 wallets) | various | 0.000000 each |

**Total swarm balance: 0.000000 APT**

### Multisig Contract Probes (5 contracts)

All 5 multisig accounts are **healthy** — each requires 2-of-N signatures.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | ✓ |
| A-G | 0xf56c4a... | 2 | ✓ |
| Y-Z | 0xd3ffe1... | 2 | ✓ |
| S-T | 0x3b1c3a... | 2 | ✓ |
| V-W | 0x40fad7... | 2 | ✓ |

All multisig contracts online. Quorum intact (5/5).

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no JSON API data extractable.**  
`/api/markets` and `/api/v1/markets` both returned the Next.js SPA HTML shell. No headless browser available. Recorded as unavailable in `mnx_snapshots`.

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

## Highlights

- **gorj (this repo)** was pushed today (2026-07-24) — 1372 open issues, active Clojure/GF(3) dev
- **kubeflow/pipelines** continues as highest-activity ML repo (4169 stars, pushed today)
- **All 5 multisigs** respond with 2-sig quorum — Hamming swarm governance intact
- **28 Aptos wallets** currently at 0 APT — no liquidity on mainnet addresses
- **MNX testnet** is live (SPA loads) but exposes no REST API for market data extraction
