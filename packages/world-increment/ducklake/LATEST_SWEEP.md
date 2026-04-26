# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-26

## Sweep Metadata
- **Date:** 2026-04-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 389 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — All 11 Increments

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 1  | AustinCStone | user | 40 | +1 | `#b8bb26` | **PLUS** |
| 2  | DJedamski | user | 6 | -1 | `#cc241d` | **MINUS** |
| 3  | M1shaaa | user | 8 | 0 | `#d3869b` | **ERGODIC** |
| 4  | TeglonLabs | org | 4 | +1 | `#b8bb26` | **PLUS** |
| 5  | bmorphism | user | 100 | -1 | `#cc241d` | **MINUS** |
| 6  | kristinezheng | user | 6 | 0 | `#d3869b` | **ERGODIC** |
| 7  | kubeflow | org | 47 | +1 | `#b8bb26` | **PLUS** |
| 8  | migalkin | user | 19 | -1 | `#cc241d` | **MINUS** |
| 9  | plurigrid | org | 100 | 0 | `#d3869b` | **ERGODIC** |
| 10 | wasita | user | 10 | +1 | `#b8bb26` | **PLUS** |
| 11 | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

### Top Repos by Stars

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,600 | — | 2026-01-05 |
| kubeflow/pipelines | 4,125 | Python | 2026-04-24 |
| kubeflow/spark-operator | 3,120 | Python | 2026-04-24 |
| kubeflow/trainer | 2,092 | Go | 2026-04-25 |
| kubeflow/katib | 1,679 | Python | 2026-04-14 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,012 | YAML | 2026-04-11 |
| kubeflow/arena | 810 | Go | 2026-04-16 |
| kubeflow/kale | 685 | Python | 2026-04-24 |
| kubeflow/mpi-operator | 524 | Go | 2026-04-14 |

### Repo Counts by Source

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| bmorphism | user | 100 | 508 |
| plurigrid | org | 100 | 145 |
| kubeflow | org | 47 | 101,663 |
| zubyul | user | 49 | 40 |
| AustinCStone | user | 40 | 324 |
| migalkin | user | 19 | 832 |
| wasita | user | 10 | 10 |
| M1shaaa | user | 8 | 0 |
| kristinezheng | user | 6 | 0 |
| DJedamski | user | 6 | 17 |
| TeglonLabs | org | 4 | 14 |
| **TOTAL** | | **389** | **103,553** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-04-26)

All 28 addresses probed via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All addresses returned `resource_not_found` — CoinStore not initialized on mainnet. Balances recorded as 0.0 APT.

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793…cc7b | 0.0 APT |
| bob | 0x0a3c…512d | 0.0 APT |
| A | 0x8699…9d7a | 0.0 APT |
| B | 0x3f89…b13 | 0.0 APT |
| C | 0x38b9…35e | 0.0 APT |
| D | 0xf776…dd1 | 0.0 APT |
| E | 0xdc1d…d36 | 0.0 APT |
| F | 0x18a1…f71 | 0.0 APT |
| G | 0x69a3…f32 | 0.0 APT |
| H | 0xce67…30f | 0.0 APT |
| I | 0x070f…fc9 | 0.0 APT |
| J | 0x4d96…f54 | 0.0 APT |
| K | 0xa732…dc4 | 0.0 APT |
| L | 0x7c2e…ba9 | 0.0 APT |
| M | 0x6fed…2e9 | 0.0 APT |
| N | 0xe7dd…b2c | 0.0 APT |
| O | 0x7325…89d | 0.0 APT |
| P | 0x6218…948 | 0.0 APT |
| Q | 0xac40…89a | 0.0 APT |
| R | 0x7ce6…e10 | 0.0 APT |
| S | 0xb875…386 | 0.0 APT |
| T | 0x3578…588 | 0.0 APT |
| U | 0x7586…956 | 0.0 APT |
| V | 0xb59d…2c3 | 0.0 APT |
| W | 0x5f32…7b0 | 0.0 APT |
| X | 0xa95c…47d | 0.0 APT |
| Y | 0xd8e3…4c4 | 0.0 APT |
| Z | 0x7af0…97c | 0.0 APT |

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✅ true |
| A-G | 0xf56c…0096 | 2 | ✅ true |
| Y-Z | 0xd3ff…b883 | 2 | ✅ true |
| S-T | 0x3b1c…7883 | 2 | ✅ true |
| V-W | 0x40fa…eb6d | 2 | ✅ true |

**All 5 multisig contracts healthy — all 2-of-N threshold.**

### MNX Markets (testnet.mnx.fi)

**Status: SPA — data unavailable via static fetch.**

`testnet.mnx.fi` is a client-rendered Next.js app. All API paths (`/api/markets`, `/api/tickers`, `/api/v1/markets`, `/api/pairs`) return the HTML bundle. Market data requires JavaScript execution. Recorded as `unavailable` in `mnx_snapshots`.

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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,600 stars — flagship ML orchestration platform, still actively pushed 2026
- **kubeflow/pipelines**: 4,125 stars — ML pipeline system, pushed 2026-04-24
- **kubeflow/spark-operator**: 3,120 stars — Kubernetes Spark operator, pushed 2026-04-24
- **migalkin** sweep: 19 repos, 832 total stars — KG embedding research (NodePiece, StarE, ULTRA)
- **bmorphism** sweep: 100 repos, 508 total stars — wide ML/systems portfolio
- **plurigrid** sweep: 100 repos, 145 total stars — ASI/vivarium/gorj topology work
- **TeglonLabs**: mathpix-gem (Ruby, 2 stars), monad-mcp-server, topoi, coin-flip-mcp
- **All 5 Aptos multisig contracts**: 2-of-N threshold, confirmed healthy on mainnet
- **All 28 Aptos wallet addresses**: CoinStore not initialized — 0.0 APT each
