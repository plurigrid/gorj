# World-Increment Sweep + Hamming Snapshot — 2026-08-01

## Sweep Metadata
- **Date:** 2026-08-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this run) | 306 |
| Sources Covered | 3 orgs + 8 users |

### Repo Counts by Source

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| bmorphism | user | 100 | 508 |
| plurigrid | org | 100 | 189 |
| zubyul | user | 49 | 40 |
| kubeflow | org | 49 | 96,040 |
| AustinCStone | user (social) | 41 | 319 |
| migalkin | user (social) | 19 | 832 |
| wasita | user (social) | 12 | 10 |
| M1shaaa | user (social) | 8 | 0 |
| kristinezheng | user (social) | 5 | 0 |
| TeglonLabs | org | 5 | 14 |

### GF(3) Color Chain Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**

### Notable Repos (2026-08-01 snapshot)
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,802 | 2026-08-01 |
| kubeflow/pipelines | Python | 4,172 | 2026-07-31 |
| kubeflow/spark-operator | Python | 3,141 | 2026-07-31 |
| kubeflow/trainer | Go | 2,165 | 2026-07-31 |
| kubeflow/katib | Python | 1,695 | 2026-07-31 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |
| plurigrid/asi | HTML | 57 | 2026-07-10 |
| plurigrid/gorj | Clojure | 1 | 2026-08-01 (THIS REPO, 1550 open issues) |
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet)

All 28 addresses (alice, bob, A–Z) queried via `fullnode.mainnet.aptoslabs.com`.  
**Result: All balances = 0 APT** — no `CoinStore<AptosCoin>` resource exists (accounts may be on-chain but hold no APT).

### Multisig Contract Probes

All 5 contracts healthy — all use 2-of-2 unanimous multisig:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4f4… | 2 | ✅ healthy |
| A-G | 0xf56c4a… | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1… | 2 | ✅ healthy |
| S-T | 0x3b1c3a… | 2 | ✅ healthy |
| V-W | 0x40fad7… | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)
**Status: Unavailable** — Next.js SPA, no public REST API endpoints accessible. No market data extractable.

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
