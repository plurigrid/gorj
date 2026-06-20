# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-20

**Date:** 2026-06-20  
**Run type:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.4 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) chain:** id%3==0 → trit=0 ERGODIC `#d3869b` | id%3==1 → trit=1 PLUS `#b8bb26` | id%3==2 → trit=-1 MINUS `#cc241d`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Covered

| Source | Type | Repos Snapshotted | Notes |
|--------|------|-------------------|-------|
| plurigrid | org | 24 | gorj (704 open issues!), asi 26★, active GF3/Clojure ecosystem |
| kubeflow | org | 18 | kubeflow 15.7k★, pipelines 4.1k★, actively maintained |
| TeglonLabs | org | 5 | jank-crane (C++/GF3), mathpix-gem, coin-flip-mcp |
| bmorphism | user | 13 | Gay.jl (187 open issues), ocaml-mcp-sdk 61★, satreadout new 2026-06-20 |
| zubyul | user | 9 | voice-observatory, nash-tui/nash-web, Gay.jl fork |
| migalkin | user | 4 | NodePiece 144★, StarE 89★ (KG research) |
| DJedamski | user | 2 | kaggle_ncaa18, Project_Euler |
| wasita | user | 3 | wasita.github.io, magic-garden, send2kobo |
| kristinezheng | user | 1 | kristinezheng.github.io (pushed 2026-06-07) |
| M1shaaa | user | 1 | M1shaaa config |
| AustinCStone | user | 3 | TextGAN 92★, StereoVisionMRF 11★, EpsteinSearch |
| **TOTAL** | | **83** | |

### Most Active (pushed 2026-06-20)

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/pipelines | 4,155 | Python | Machine Learning Pipelines for Kubeflow |
| kubeflow/sdk | 120 | Python | Universal Python SDK |
| kubeflow/kale | 694 | Python | Kubeflow superfood for Data Scientists |
| kubeflow/dashboard | 16 | TypeScript | Kubeflow Central Dashboard |
| kubeflow/pipelines-components | 11 | Python | Kubeflow Pipelines components |
| plurigrid/gorj | 0 | Clojure | forj + Rama topology nREPL + GF(3) |
| plurigrid/place | 1 | TeX | bci.place forester |
| bmorphism/Gay.jl | 2 | Julia | Wide-gamut color sampling GF(3) |
| bmorphism/satreadout | 0 | HTML | Machine-checked saturating perceptual readout |

### Notable Highlights

- **kubeflow/kubeflow**: 15,737★ — ML Toolkit for Kubernetes, last pushed 2026-06-18
- **kubeflow/mcp-apache-spark-history-server**: 177★ — new MCP tool for Spark debugging
- **plurigrid/gorj**: 704 open issues — this repo is the most issue-active in the plurigrid org
- **bmorphism/Gay.jl**: 187 open issues — GF(3) color sampler with SPI pattern, very active
- **bmorphism/ocaml-mcp-sdk**: 61★ — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **TeglonLabs/jank-crane**: C++/GF3 converged-IR hub, pushed 2026-06-08
- **migalkin/NodePiece**: 144★ — parameter-efficient KG representations (ICLR 2022)

### GF(3) Distribution (83 world increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 28 |
| 1 | `#b8bb26` | PLUS | 28 |
| -1 | `#cc241d` | MINUS | 27 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

**Endpoint:** `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

All 28 wallets (alice, bob, A–Z) returned **0.0 APT**. The `CoinStore` resource was absent for all addresses — these accounts exist on Aptos mainnet but have no registered native APT coin store (may hold other assets or are newly initialized).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793acde...cc7b | 0.0 |
| bob | 0x0a3c00c5...2d5d | 0.0 |
| A | 0x8699edc0...c7a | 0.0 |
| B | 0x3f892ebe...b13 | 0.0 |
| C | 0x38b99e63...35e | 0.0 |
| D | 0xf7765624...dd1 | 0.0 |
| E | 0xdc1d9d53...d36 | 0.0 |
| F | 0x18a14b5b...f71 | 0.0 |
| G | 0x69a394c0...f32 | 0.0 |
| H | 0xce67c327...00f | 0.0 |
| I–Z | (16 wallets) | 0.0 each |

### Multisig Contract Probes (5 pairs)

**Endpoint:** POST `https://fullnode.mainnet.aptoslabs.com/v1/view` → `0x1::multisig_account::num_signatures_required`

All 5 multisig accounts are live on mainnet with `sigs_required = 2` (2-of-N threshold):

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428...003 | 2 | ✅ |
| A-G | 0xf56c4a1c...096 | 2 | ✅ |
| Y-Z | 0xd3ffe181...883 | 2 | ✅ |
| S-T | 0x3b1c3ae9...883 | 2 | ✅ |
| V-W | 0x40fad7b4...b6d | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE**  
`https://testnet.mnx.fi/api/markets` returned no data. The site appears to be a SPA without a discoverable public API endpoint, or the testnet is currently down. No market data could be extracted.

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

## Table Counts

| Table | Rows |
|-------|------|
| world_increments | 83 |
| repo_snapshots | 83 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
