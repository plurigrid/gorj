# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 15 (top active) |
| TeglonLabs | org | 5 |
| bmorphism | user | 10 |
| zubyul | user | 8 |
| migalkin | user | 5 |
| AustinCStone | user | 5 |
| **Total** | | **148** |

> Note: Session GitHub API is repository-scoped; org-level listing endpoints unavailable. Repos captured via MCP `search_repositories`. DJedamski, wasita, kristinezheng, M1shaaa not returned by search (no public repos visible or search constraint). bmorphism/zubyul events not accessible via API scope.

### GF(3) Color Chain Distribution (148 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 49 |
| +1 | `#b8bb26` | PLUS | 50 |
| -1 | `#cc241d` | MINUS | 49 |

Chain: `PLUS → MINUS → ERGODIC → ...` cycling 148 times across all repo snapshots.

### Top Starred Repos (2026-07-24 snapshot)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,792 | — | 2026-07-24 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-24 |
| kubeflow/spark-operator | 3,143 | Python | 2026-07-23 |
| kubeflow/trainer | 2,153 | Go | 2026-07-24 |
| kubeflow/katib | 1,692 | Python | 2026-07-20 |
| kubeflow/examples | 1,461 | Jsonnet | 2026-07-22 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-23 |
| kubeflow/arena | 815 | Go | 2026-07-21 |
| kubeflow/kale | 695 | Python | 2026-07-22 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| bmorphism/anti-bullshit-mcp-server | 22 | JavaScript | 2026-07-12 |
| plurigrid/asi | 31 | HTML | 2026-07-17 |
| plurigrid/gorj | 1 | Clojure | 2026-07-07 |

### Most Recently Pushed (plurigrid)

| Repo | Pushed At | Description |
|------|-----------|-------------|
| plurigrid/asi | 2026-07-17 | everything is topological chemputer! |
| plurigrid/gorj | 2026-07-07 | forj + Rama topology nREPL routing + GF(3) gay trit coloring |
| plurigrid/shrimp | 2026-07-03 | Jank worked example: shrimp |
| plurigrid/place | 2026-06-27 | BCI forester preview |
| plurigrid/eirobri | 2026-05-19 | EiRoBri replay world |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-24)

**Addresses surveyed:** 28 (alice, bob, A–Z)

All wallets returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~6,437,755,165. These addresses have never registered/funded the APT CoinStore resource on mainnet.

**Total APT across all 28 wallets: 0.0 APT**

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ Healthy |
| A-G | 0xf56c4a1c... | 2 | ✓ Healthy |
| Y-Z | 0xd3ffe181... | 2 | ✓ Healthy |
| S-T | 0x3b1c3ae9... | 2 | ✓ Healthy |
| V-W | 0x40fad7b4... | 2 | ✓ Healthy |

All 5 multisig contracts require **2-of-N signatures** and responded to view calls — all live on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` is a **Next.js SPA** — all API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return the rendered HTML shell with no JSON data accessible unauthenticated. Recorded as `unavailable` in `mnx_snapshots`.

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

## Row Counts

```
world_increments  — 148 rows
repo_snapshots    — 148 rows
aptos_snapshots   —  28 rows (all 0.0 APT)
multisig_probes   —   5 rows (all healthy, sigs_required=2)
mnx_snapshots     —   1 row  (unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
