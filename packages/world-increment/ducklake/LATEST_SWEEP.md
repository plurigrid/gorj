# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-11  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.1 (Variegata) — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 98 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 99 |
| zubyul | user | 45 |
| migalkin | user (zubyul social) | 6 |
| wasita | user (zubyul social) | 4 |
| AustinCStone | user (zubyul social) | 4 |
| DJedamski | user (zubyul social) | 3 |
| kristinezheng | user (zubyul social) | 3 |
| M1shaaa | user (zubyul social) | 3 |
| **TOTAL** | | **316** |

### GF(3) Trit Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 105 |
| +1 | `#b8bb26` | PLUS | 106 |
| -1 | `#cc241d` | MINUS | 105 |

### Top Repos by Stars

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,565 | 2026-01-05 |
| kubeflow/pipelines | Python | 4,119 | 2026-04-11 |
| kubeflow/spark-operator | Python | 3,111 | 2026-04-10 |
| kubeflow/trainer | Go | 2,080 | 2026-04-10 |
| kubeflow/katib | Python | 1,676 | 2026-04-02 |
| kubeflow/manifests | YAML | 1,010 | 2026-04-09 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 88 | 2026-02-22 |
| AustinCStone/StereoVisionMRF | Python | 11 | 2026-04-01 |
| migalkin/NBFNet_mlx | Python | 10 | 2026-03-11 |
| plurigrid/asi | HTML | 16 | 2026-04-10 |
| plurigrid/asi-skills | Julia | 3 | 2026-04-09 |

### Recently Active plurigrid Highlights

- **gorj** (Clojure) — forj + Rama topology nREPL routing + GF(3) gay trit coloring — pushed 2026-04-11
- **nanoclj-zig** (Zig) — NaN-boxed Clojure interpreter + interaction nets + GF(3) trit conservation — pushed 2026-04-09
- **zig-syrup** (Zig) — High-performance OCapN Syrup with CapTP optimizations — pushed 2026-04-09
- **asi-skills** (Julia) — 69 skills with Galois Hole Type accessibility — pushed 2026-04-09
- **web-browser** (Rust) — from prepostweb lineage (monaduck1069) — pushed 2026-04-10

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Result:** All 28 addresses returned HTTP 404 on `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
Accounts exist on-chain at ledger version 4,837,841,856 but CoinStore resources are not initialized (APT not deposited via legacy coin interface). Balance recorded as 0.0 APT for all worlds.

| Worlds | Status |
|--------|--------|
| alice, bob | CoinStore not initialized — 0.0 APT |
| A through Z (26 addresses) | CoinStore not initialized — 0.0 APT |

### Multisig Contract Probes

All 5 contracts probed via `POST /v1/view → 0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428…87003` | 2 | ✓ |
| A-G | `0xf56c4a1c…0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181…b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9…7883` | 2 | ✓ |
| V-W | `0x40fad7b4…eb6d` | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable. `https://testnet.mnx.fi/api/markets` → HTTP 404.  
The site is a Next.js SPA with no publicly accessible REST market data endpoints at standard paths. Recorded as unavailable in `mnx_snapshots`.

---

## DuckDB Schema Summary

```
world-increments.duckdb
├── world_increments     316 rows  (GF3-colored repo events)
├── repo_snapshots       316 rows  (full repo metadata)
├── aptos_snapshots       28 rows  (alice+bob+A–Z, all 0.0 APT)
├── multisig_probes        5 rows  (all healthy, sigs_required=2)
└── mnx_snapshots          1 row   (unavailable)
```

---

## GF(3) Trit Legend

```
id % 3 == 0  →  trit=0   ERGODIC  #d3869b  (pink/rose)
id % 3 == 1  →  trit=+1  PLUS     #b8bb26  (green)
id % 3 == 2  →  trit=-1  MINUS    #cc241d  (red)
```

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
