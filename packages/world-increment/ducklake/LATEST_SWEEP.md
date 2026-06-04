# World-Increment Sweep — 2026-05-06

## Sweep Metadata
- **Date:** 2026-05-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 270 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Swarm Addresses | 28 (alice, bob, A–Z) |
| Multisig Probes | 5 |
| MNX Market Data | unavailable (SPA, no public API) |

---

## GF(3) Color Chain — 11 World Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## GitHub Social Graph — Repo Counts

| Source | Type | Repos Snapshotted | Stars (top repo) | Top Repo |
|--------|------|-------------------|------------------|----------|
| kubeflow | org | 38 | 15,622 | kubeflow/kubeflow |
| plurigrid | org | 50 | 19 | plurigrid/asi |
| TeglonLabs | org | 4 | 2 | TeglonLabs/mathpix-gem |
| bmorphism | user | 50 | 60 | bmorphism/ocaml-mcp-sdk |
| zubyul | user | 49 | 2 | zubyul/WGCNA |
| migalkin | user | 19 | 143 | migalkin/NodePiece |
| DJedamski | user | 6 | 1 | DJedamski/School |
| wasita | user | 11 | 2 | wasita/magic-garden |
| kristinezheng | user | 6 | 0 | — |
| M1shaaa | user | 8 | 0 | — |
| AustinCStone | user | 30 | 92 | AustinCStone/TextGAN |
| **TOTAL** | | **271** | | |

### Top Repos by Stars

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,622 | 2026-05-06 |
| kubeflow/pipelines | Python | 4,133 | 2026-05-06 |
| kubeflow/spark-operator | Python | 3,123 | 2026-05-05 |
| kubeflow/trainer | Go | 2,096 | 2026-05-06 |
| kubeflow/katib | Python | 1,683 | 2026-05-05 |
| kubeflow/examples | Jsonnet | 1,460 | 2026-04-14 |
| kubeflow/manifests | YAML | 1,015 | 2026-05-05 |
| kubeflow/arena | Go | 810 | 2026-04-28 |
| kubeflow/kale | Python | 684 | 2026-05-05 |
| migalkin/NodePiece | Python | 143 | 2026-03-02 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | 2026-03-16 |
| plurigrid/gorj | Clojure | 0 (80 issues) | 2026-05-06 |

### Notable Recent Activity (last 30 days)
- **kubeflow/pipelines** (4,133★): pushed 2026-05-06 — active ML pipeline platform
- **bmorphism/Gay.jl** (187 open issues): pushed 2026-05-06 — wide-gamut color sampling
- **wasita/vocoder**: pushed 2026-05-06 — new repo created same day
- **plurigrid/gorj**: pushed 2026-05-06 — this very repo
- **plurigrid/zig-syrup**: 2026-04-30 — high-perf OCapN Syrup in Zig

---

## Hamming Swarm Snapshot — Aptos Mainnet

**Sweep timestamp:** 2026-05-06 UTC  
**Method:** `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

All 28 addresses returned **0.0 APT**. The `error_code` field in the API response indicates these accounts have no initialized CoinStore resource on mainnet (accounts not funded or resource not registered).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…512d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

**Total swarm balance:** 0.0 APT

---

## Multisig Contract Probes — Aptos Mainnet

All 5 multisig contracts respond healthy with `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✅ |
| A-G | 0xf56c…0096 | 2 | ✅ |
| Y-Z | 0xd3ff…b883 | 2 | ✅ |
| S-T | 0x3b1c…7883 | 2 | ✅ |
| V-W | 0x40fa…eb6d | 2 | ✅ |

**All multisig contracts nominal — 2-of-N threshold consistent across all pairs.**

---

## MNX Markets (testnet.mnx.fi)

**Status:** Unavailable for programmatic extraction.  
The endpoint returns a valid SPA shell (292 KB HTML). Neither `/api/markets` nor `/api/v1/markets` returned JSON. No embedded `window.__INITIAL_STATE__` or similar bootstrap data detected in the page source. No rows inserted into `mnx_snapshots`.

---

## DuckDB Tables Updated

| Table | Rows inserted (2026-05-06) |
|-------|---------------------------|
| `world_increments` | 11 |
| `repo_snapshots` | 270 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 |

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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
