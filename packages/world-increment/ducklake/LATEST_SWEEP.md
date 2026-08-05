# World-Increment Sweep + Hamming Snapshot — 2026-08-05

## Sweep Metadata
- **Date:** 2026-08-05T06:19 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Captured | Notable Stars |
|--------|------|---------------|--------------|
| plurigrid | org | 42 | asi 58★, ontology 8★, gorj 1★ |
| kubeflow | org | 20 | kubeflow 15805★, pipelines 4176★, trainer 2170★ |
| TeglonLabs | org | 5 | mathpix-gem 2★, coin-flip-mcp 2★ |
| bmorphism | user | 10 | ocaml-mcp-sdk 61★, anti-bullshit-mcp-server 23★ |
| zubyul | user | 10 | Gay.jl (188 issues open), gay-world 1★ |
| migalkin | social | 6 | NodePiece 144★, StarE 89★, kgcourse2021 24★ |
| DJedamski | social | 4 | Kaggle, School, Getting-and-Cleaning-Data |
| wasita | social | 6 | xoxowasita-analysis (new 2026-08-04!), magic-garden 2★ |
| kristinezheng | social | 4 | kristinezheng.github.io, lookit-jenga |
| M1shaaa | social | 3 | lab-bookshelf-, Python-Lookit-Uploads |
| AustinCStone | social | 11 | TextGAN 92★, StereoVisionMRF 11★, byteruckus |
| **TOTAL** | | **121** | |

**World-increments inserted this run:** 116  
**GF(3) color chain:** id%3==0→ERGODIC #d3869b | id%3==1→PLUS #b8bb26 | id%3==2→MINUS #cc241d

### Notable Activity (2026-08-05)
- **plurigrid/gorj** (this repo): pushed TODAY, 1641 open issues — highest activity
- **plurigrid/eirobri**: pushed 2026-08-04 — EiRoBri replay world
- **plurigrid/place**: pushed 2026-08-02, 15 issues
- **bmorphism/Gay.jl**: 188 open issues — high velocity GF(3) color library
- **wasita/xoxowasita-analysis**: CREATED 2026-08-04 (yesterday) — brand new
- **wasita/joint-planning-lit**: CREATED 2026-08-04 — new literature repo
- **kubeflow/spark-operator**: pushed 2026-08-05 TODAY, 3143★, 110 issues
- **kubeflow/pipelines**: 4176★, 517 open issues — very active
- **kubeflow/sdk**: pushed TODAY, 132★, 242 issues

### GF(3) Summary (116 increments)
- trit=1 PLUS #b8bb26: 39 repos (ids 1,4,7,...)
- trit=-1 MINUS #cc241d: 39 repos (ids 2,5,8,...)
- trit=0 ERGODIC #d3869b: 38 repos (ids 3,6,9,...)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 wallets: alice, bob, A–Z)

All wallets queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 wallets return 0 APT** — no APT CoinStore resource registered on any address. Accounts may exist on-chain but no native APT balance is recorded.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (5 contracts)

Probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

**All 5 multisig contracts healthy — 2-of-2 signature threshold intact.**

### MNX Markets (testnet.mnx.fi)

MNX is a Next.js SPA (title: "The AI Exchange", description: "The AI Exchange"). REST API returns 404 for `/api/markets` and `/api/v1/markets`. CSP header reveals actual backend runs over WebSocket (`wss://api.testnet.mnx.fi`). **MNX market data: unavailable from this environment — SPA/WebSocket only, no accessible REST API.**

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)
-- 116+ records this sweep, cumulative across runs

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
-- 116 new records this sweep

aptos_snapshots(timestamp, world, address, balance_apt)
-- 28 records (alice, bob, A–Z) — all 0 APT

multisig_probes(timestamp, pair, address, sigs_required, healthy)
-- 5 records — A-B, A-G, Y-Z, S-T, V-W — all 2-of-2, healthy

mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
-- 0 records — SPA/WebSocket only, unavailable
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
