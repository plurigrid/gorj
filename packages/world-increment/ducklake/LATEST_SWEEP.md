# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-31

## Sweep Metadata
- **Date:** 2026-05-31
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 391 |
| Total Repo Snapshots | 391 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts | 5 |

---

## GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|---|---|---|---|
| 0 | `#d3869b` | ERGODIC | 130 |
| +1 | `#b8bb26` | PLUS | 131 |
| -1 | `#cc241d` | MINUS | 130 |

GF(3) assignment: `id mod 3 == 0` → ERGODIC, `mod 3 == 1` → PLUS, `mod 3 == 2` → MINUS

---

## JOB 1 — GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 74 |
| bmorphism | user | 100 | 247 |
| kubeflow | org | 48 | 34,154 |
| zubyul | user | 49 | 14 |
| AustinCStone | user (social) | 40 | 108 |
| migalkin | user (social) | 19 | 280 |
| wasita | user (social) | 11 | 5 |
| M1shaaa | user (social) | 8 | 0 |
| DJedamski | user (social) | 6 | 3 |
| kristinezheng | user (social) | 6 | 0 |
| TeglonLabs | org | 4 | 2 |
| **TOTAL** | | **391** | **34,887** |

### Notable Repos
- **kubeflow/kubeflow**: flagship ML platform for Kubernetes
- **kubeflow/pipelines**: ML pipeline orchestration
- **kubeflow/spark-operator**: Kubernetes Spark operator
- **migalkin/NodePiece**: scalable knowledge-graph embeddings
- **bmorphism** (aggregate): OCaml MCP SDK, anti-bullshit MCP, open-location-code-zig
- **plurigrid** (aggregate): asi, vivarium, gorj, zig-syrup, ontology
- **TeglonLabs/mathpix-gem**: math OCR Ruby gem (Ruby, 2★)
- **wasita/wasita.github.io**: personal site in Svelte (pushed 2026-05-20)

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)
All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
Accounts are uninitialized on-chain or have no APT CoinStore registered.  
All balances recorded as `NULL`.

### Multisig Contract Probes (Aptos mainnet)
All 5 contracts are healthy, requiring 2-of-2 signatures.

| Pair | Address | Sigs Required | Healthy |
|---|---|---|---|
| A-B | `0x0da4f428…7003` | 2 | ✓ |
| A-G | `0xf56c4a1c…0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181…b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9…7883` | 2 | ✓ |
| V-W | `0x40fad7b4…eb6d` | 2 | ✓ |

### MNX Markets (`testnet.mnx.fi`)
**Unavailable** — SPA returns HTML shell; no JSON market data reachable at
`/api/markets` or `/api/v1/markets`. Recorded as `unavailable` in `mnx_snapshots`.

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)                          -- 391 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)                          -- 391 rows

aptos_snapshots(timestamp, world, address, balance_apt)         --  28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy) --  5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct) -- 1 row
```
