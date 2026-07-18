# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-18

## Sweep Metadata
- **Date:** 2026-07-18
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source Type | Name | Repos Snapshotted |
|-------------|------|-------------------|
| org | plurigrid | 13 (from 100 total) |
| org | kubeflow | 7 (from 49 total) |
| org | TeglonLabs | 5 |
| user | bmorphism | 7 (from 100 total) |
| user | zubyul | 5 (from 48 total) |
| user | migalkin | 3 (from 19 total) |
| user | wasita | 3 (from 12 total) |
| user | AustinCStone | 3 (from 41 total) |
| user | DJedamski | 2 (from 6 total) |
| user | kristinezheng | 2 (from 5 total) |
| user | M1shaaa | 2 (from 8 total) |

**Total world_increments inserted:** 52  
**Total repo_snapshots inserted:** 52

### Notable Repos (Most Active / Most Starred)

| Repo | Stars | Lang | Last Push |
|------|-------|------|-----------|
| kubeflow/kubeflow | 15,780 | — | 2026-07-18 |
| kubeflow/pipelines | 4,168 | Python | 2026-07-17 |
| kubeflow/spark-operator | 3,138 | Python | 2026-07-18 |
| kubeflow/mcp-server | 26 | Python | 2026-07-18 (most recent) |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| plurigrid/asi | 31 | HTML | 2026-07-10 |
| plurigrid/gorj | 1 | Clojure | **2026-07-18 (today)** |
| zubyul/from-possible-worlds | 0 | TeX | **2026-07-18 (today)** |

### GF(3) Color Chain

- **trit=0 (ERGODIC #d3869b):** id % 3 == 0
- **trit=+1 (PLUS #b8bb26):** id % 3 == 1  
- **trit=-1 (MINUS #cc241d):** id % 3 == 2

52 increments → 17 full GF(3) cycles + 1 remainder (id 52: PLUS)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A–Z) confirmed to exist on Aptos mainnet. No legacy `0x1::coin::CoinStore<AptosCoin>` resource found on any account — consistent with the Fungible Asset (FA) model or zero APT balance. All recorded as `0.0000 APT`.

**Status: all accounts exist, no APT CoinStore resources detected**

### Multisig Contract Probes — ALL HEALTHY ✓

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig contracts require exactly 2 signatures — Hamming swarm topology intact.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `https://testnet.mnx.fi/api/markets` returned HTTP 401 Unauthorized. No market data retrieved this sweep.

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)
-- 52 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
-- 52 rows

aptos_snapshots(timestamp, world, address, balance_apt)
-- 28 rows (all 0.0 APT — FA model or empty)

multisig_probes(timestamp, pair, address, sigs_required, healthy)
-- 5 rows (all healthy, 2-of-2)

mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
-- 1 row (sentinel: MNX_UNAVAILABLE)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
