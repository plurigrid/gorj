# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-15

## Sweep Metadata
- **Date:** 2026-06-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 391 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (Vercel auth) |

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name | Repos |
|----|--------|------|----------|-------|------|-------|
| 1 | plurigrid | org | +1 | `#b8bb26` | **PLUS** | 100 |
| 2 | kubeflow | org | -1 | `#cc241d` | **MINUS** | 48 |
| 3 | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** | 5 |
| 4 | bmorphism | user | +1 | `#b8bb26` | **PLUS** | 100 |
| 5 | zubyul | user | -1 | `#cc241d` | **MINUS** | 49 |
| 6 | migalkin | user | 0 | `#d3869b` | **ERGODIC** | 19 |
| 7 | DJedamski | user | +1 | `#b8bb26` | **PLUS** | 6 |
| 8 | wasita | user | -1 | `#cc241d` | **MINUS** | 11 |
| 9 | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** | 5 |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** | 8 |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** | 40 |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Stars

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15725 | 2026-06-11 |
| kubeflow/pipelines | Python | 4154 | 2026-06-15 |
| kubeflow/spark-operator | Python | 3127 | 2026-06-14 |
| kubeflow/trainer | Go | 2115 | 2026-06-15 |
| kubeflow/katib | Python | 1683 | 2026-06-12 |
| kubeflow/examples | Jsonnet | 1461 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1023 | 2026-06-15 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| plurigrid/asi | HTML | 26 | 2026-06-10 |
| plurigrid/gorj | Clojure | 0 | 2026-06-15 (596 open issues) |

---

## Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets (alice, bob, A–Z) queried via `fullnode.mainnet.aptoslabs.com/v1`.  
**Result: 0.0 APT across all 28 addresses** — `CoinStore<AptosCoin>` resource not initialized.

### Multisig Probes — All HEALTHY

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

### MNX Markets

`testnet.mnx.fi` requires Vercel visitor authentication — no market data accessible. Table `mnx_snapshots` has 0 rows.

---

## Schema
```sql
world_increments(id, ts, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, meta, actor, snapshot_hash)

repo_snapshots(id, ts, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(ts, world, address, balance_apt)
multisig_probes(ts, pair, address, sigs_required, healthy)
mnx_snapshots(ts, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
