# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-26 UTC  
**DuckDB:** v1.5.5 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) color chain:** ERGODIC #d3869b | PLUS #b8bb26 | MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|------:|------------:|-------------|
| kubeflow | org | 49 | 34,414 | 2026-07-26T07:30Z |
| plurigrid | org | 100 | 83 | 2026-07-26T08:12Z |
| bmorphism | user | 100 | 246 | 2026-07-26T02:38Z |
| zubyul | user | 49 | 14 | 2026-07-18T12:02Z |
| AustinCStone | user (social) | 41 | 108 | 2026-07-15T05:19Z |
| migalkin | user (social) | 19 | 279 | 2025-08-04T03:01Z |
| wasita | user (social) | 12 | 5 | 2026-07-21T15:52Z |
| kristinezheng | user (social) | 5 | 0 | 2026-07-01T20:57Z |
| TeglonLabs | org | 5 | 2 | 2026-06-08T19:03Z |

**Total repos snapshotted: 370**

### Top 10 Repos by Stars

| Repo | Stars | Language | Last Push |
|------|------:|----------|-----------|
| kubeflow/kubeflow | 15,794 | — | 2026-07-10 |
| kubeflow/pipelines | 4,170 | Python | 2026-07-26 |
| kubeflow/spark-operator | 3,143 | Python | 2026-07-25 |
| kubeflow/trainer | 2,153 | Go | 2026-07-25 |
| kubeflow/katib | 1,692 | Python | 2026-07-22 |
| kubeflow/examples | 1,461 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-24 |
| kubeflow/arena | 815 | Go | 2026-07-24 |
| kubeflow/kale | 697 | Python | 2026-07-25 |
| kubeflow/mpi-operator | 530 | Go | 2026-07-23 |

### Notable Non-kubeflow Activity

- **migalkin/NodePiece**: 143★ Python — scalable KG embeddings (last push 2025-08)
- **bmorphism** repos: active through 2026-07-26, mixed OCaml/Clojure/Zig/TypeScript
- **plurigrid/gorj**: this repo — forj + GF(3) trit coloring (pushed 2026-07-26)
- **wasita/wasita.github.io**: Svelte personal site pushed 2026-07-21
- **TeglonLabs/jank-crane**: C++ jank+crane converged-IR hub (GF3 convergence maps, pushed 2026-06-08)

### GF(3) World-Increment Distribution (this run)

| Trit | Name | Color | Count |
|-----:|------|-------|------:|
| 0 | ERGODIC | #d3869b | 124 |
| 1 | PLUS | #b8bb26 | 123 |
| -1 | MINUS | #cc241d | 123 |

**370 repo snapshots → 370 world-increment records. 123+ complete GF(3) cycles.**

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

28 wallets queried: alice, bob, A–Z via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**All 28 wallets: 0.0 APT**

The `AptosCoin::CoinStore` resource is uninitialized or zero on all addresses. These accounts may hold other FA tokens or have never received APT directly via the legacy CoinStore path.

### Multisig Contract Probes

All 5 probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|:-------------:|--------|
| A-B | 0x0da4f428…7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a1c…0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe181…b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3ae9…7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fad7b4…eb6d | 2 | ✅ HEALTHY |

**5/5 multisig contracts healthy — all require 2-of-N signatures.**

### MNX Testnet Markets

`https://testnet.mnx.fi` is a Next.js SPA. All API paths return the client-side HTML shell. No JSON market data is accessible without in-browser JS execution.

**Status: UNAVAILABLE (SPA, no public JSON REST API)**

---

## DuckDB Table Counts (cumulative)

| Table | Records |
|-------|--------:|
| world_increments | 393 |
| repo_snapshots | 1,314 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
