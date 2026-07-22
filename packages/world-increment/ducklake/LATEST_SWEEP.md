# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-22

## Sweep Metadata
- **Date:** 2026-07-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** duckdb Python 1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 84 |
| Total Repo Snapshots | 84 |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | 0 (SPA — no JSON API) |

---

## GF(3) Color Chain

- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

Chain repeats: `PLUS → MINUS → ERGODIC → ...` (28 full cycles across 84 increments)

---

## JOB 1: GitHub Social Graph

### Sources Covered

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 23 |
| kubeflow | org | 18 |
| TeglonLabs | org | 5 |
| bmorphism | user | 16 |
| zubyul | user | 10 |
| migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone | social-graph | 12 |
| **TOTAL** | | **84** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,789 | — | 2026-07-10 |
| kubeflow/pipelines | 4,168 | Python | 2026-07-21 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-17 |
| kubeflow/trainer | 2,152 | Go | 2026-07-21 |
| kubeflow/katib | 1,692 | Python | 2026-07-21 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |

### Most Recently Active

- `bmorphism/Gay.jl` — pushed **2026-07-22** (187 open issues, active)
- `plurigrid/gorj` — pushed **2026-07-22** (1310 open issues)
- `plurigrid/eirobri` — pushed 2026-07-21
- `wasita/wasita.github.io` — pushed 2026-07-21
- `kubeflow/trainer` — pushed 2026-07-21

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

28 wallets probed: alice, bob, A–Z via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**All 28 wallets: 0.0 APT** — CoinStore resource not initialized or zero balance at snapshot time.

### Multisig Contract Probes

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✅ |
| A-G | 0xf56c...096 | 2 | ✅ |
| Y-Z | 0xd3ff...883 | 2 | ✅ |
| S-T | 0x3b1c...883 | 2 | ✅ |
| V-W | 0x40fa...b6d | 2 | ✅ |

All 5 multisig contracts healthy, each requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi/api/markets` returns HTML SPA shell (Next.js). No JSON data extractable without browser execution. `mnx_snapshots` table has 0 rows.

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
