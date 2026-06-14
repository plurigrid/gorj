# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-14

## Sweep Metadata
- **Date:** 2026-06-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried This Run

| Source | Type | Repos in DB | Last Swept |
|--------|------|-------------|------------|
| plurigrid | org | 200 | 2026-04-14 (prior run) |
| kubeflow | org | 94 | 2026-04-14 (prior run) |
| TeglonLabs | org | 111 | 2026-06-14 ✅ |
| bmorphism | user | 200 | 2026-04-14 (prior run) |
| zubyul | user | 48 | 2026-04-14 (prior run) |
| migalkin | social | 67 | 2026-06-14 ✅ |
| DJedamski | social | 28 | 2026-06-14 ✅ |
| wasita | social | 68 | 2026-06-14 ✅ |
| kristinezheng | social | 41 | 2026-06-14 ✅ |
| M1shaaa | social | 40 | 2026-06-14 ✅ |
| AustinCStone | social | 92 | 2026-06-14 ✅ |

**Total repo snapshots in DB (all time):** 1,144 (989 historical + 155 today)  
**New increments added today:** 155 (45 social graph + 110 orgs/users refresh)

### Notable Repos — Full Sweep (Today)

| Repo | Stars | Lang | Last Pushed | Notes |
|------|-------|------|-------------|-------|
| kubeflow/kubeflow | 15,721 | — | 2026-06-11 | ML platform for K8s |
| kubeflow/pipelines | 4,154 | Python | 2026-06-14 | ML pipelines |
| kubeflow/spark-operator | 3,127 | Python | **2026-06-14** | Apache Spark on K8s |
| kubeflow/trainer | 2,115 | Go | 2026-06-13 | Distributed AI training |
| kubeflow/katib | 1,683 | Python | 2026-06-12 | AutoML on K8s |
| kubeflow/examples | 1,461 | Jsonnet | 2025-04-14 | Tutorials |
| migalkin/NodePiece | 144 | Python | 2026-05-07 | KG embeddings (ICLR'22) |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 | Text GAN in TensorFlow |
| migalkin/StarE | 89 | Python | 2026-04-16 | Hyper-relational KGs |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 | OxCaml MCP SDK |
| plurigrid/ontology | 8 | JavaScript | 2025-05-27 | autopoietic ergodicity |
| plurigrid/asi | **26** | HTML | **2026-06-10** | topological chemputer (+10★ since April) |
| plurigrid/gorj | 0 | Clojure | **2026-06-14** | **577 open issues** — very active |
| plurigrid/nanoclj-zig | 1 | Zig | 2026-04-25 | NaN-boxed Clojure in Zig, 20 open issues |
| bmorphism/Gay.jl | 1 | Julia | **2026-06-14** | Wide-gamut GF(3) colors, 189 open issues |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 | CosmWasm + zkVM |
| TeglonLabs/jank-crane | 0 | C++ | **2026-06-08** | crane-jank IR hub (newest TeglonLabs) |
| zubyul/gay-world | 1 | Python | 2026-03-26 | Goblin world builder |

### GF(3) Color Chain (68 total increments in DB)
- **ERGODIC** (trit=0, #d3869b): 22 increments
- **PLUS** (trit=1, #b8bb26): 23 increments
- **MINUS** (trit=-1, #cc241d): 23 increments

Chain rule: `id%3==0→ERGODIC | id%3==1→PLUS | id%3==2→MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-14)

Probed via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
The resource was **not found** for all 28 addresses — wallets are uninitialized or unfunded on mainnet.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | NULL |
| bob | 0x0a3c...2d5d | NULL |
| A–Z (26) | various | NULL (all 26) |

### Multisig Contract Probes

All 5 pairs returned `num_signatures_required = 2`. All contracts live and healthy.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✅ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — site is behind Vercel deployment protection. Returns 401 authentication page. No public API endpoint accessible without bypass token or OIDC credentials.

---

## DuckDB State Summary

```
world_increments:  223 rows   (GF3-keyed events, all sweeps)
repo_snapshots:  1,144 rows   (11 sources, history since 2026-04-10)
aptos_snapshots:    28 rows   (today: all NULL — wallets unfunded)
multisig_probes:     5 rows   (today: 2-of-N, all healthy)
mnx_snapshots:       0 rows   (unavailable, Vercel-protected)
```

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
