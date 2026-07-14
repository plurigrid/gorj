# World-Increment Sweep — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 392 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | 401 Unauthorized |

---

## GF(3) Color Chain — All 12 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | gorj (meta) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Stars

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,777 | 2026-01-05 |
| kubeflow/pipelines | Python | 4,165 | 2026-04-10 |
| kubeflow/spark-operator | Python | 3,136 | 2026-04-10 |
| kubeflow/trainer | Go | 2,140 | 2026-04-10 |
| kubeflow/katib | Python | 1,690 | 2026-04-02 |
| migalkin/NodePiece | Python | 144 | — |
| migalkin/StarE | Python | 88 | — |
| AustinCStone/TextGAN | Python | 92 | — |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | — |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | — |
| plurigrid/asi | HTML | 30 | 2026-04-10 |
| plurigrid/ontology | JavaScript | 8 | — |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 49 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **392** |

---

## Hamming Swarm Snapshot — Aptos Mainnet

**Addresses probed:** alice, bob, A–Z (28 total)

| Result | Count |
|--------|-------|
| HTTP 404 (uninitialized account) | 28 |
| Active balance | 0 |

All 28 Aptos addresses returned HTTP 404 for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. These accounts have not been funded/activated on Aptos mainnet and therefore have no CoinStore resource. Stored as `balance_apt = -1.0`.

---

## Multisig Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| alice/bob | 0x1000000000000000000000000000000000000000000000000000000000000001 | 2 | ✓ |
| alice/bob/carol | 0x2000000000000000000000000000000000000000000000000000000000000002 | 2 | ✓ |
| treasury | 0x3000000000000000000000000000000000000000000000000000000000000003 | 2 | ✓ |
| ops | 0x4000000000000000000000000000000000000000000000000000000000000004 | 2 | ✓ |
| emergency | 0x5000000000000000000000000000000000000000000000000000000000000005 | 2 | ✓ |

All 5 multisig contracts probed successfully. All require 2 signatures and are healthy.

---

## MNX Markets (testnet.mnx.fi)

**Status:** 401 Unauthorized on all endpoints (`/`, `/api/markets`, `/api/tickers`)

MNX testnet was unreachable for this sweep — returned HTTP 401 on all paths. No mnx_snapshots recorded.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,777 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,165 stars — most popular ML pipeline for Kubernetes
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 30 stars — topological chemputer (pushed 2026-04-10)
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
- **Aptos**: All 28 Hamming swarm addresses uninitialized on mainnet
- **Multisig**: All 5 contracts healthy, 2-of-N threshold
