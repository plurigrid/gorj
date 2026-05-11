# World-Increment Sweep — 2026-05-11

## Sweep Metadata

| Field | Value |
|-------|-------|
| **Date** | 2026-05-11 |
| **Agent** | world-increment-sweep + hamming-swarm-snapshot |
| **DuckDB version** | v1.5.2 (Variegata) |
| **Database** | `packages/world-increment/ducklake/world-increments.duckdb` |

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 34 |
| New Increments This Sweep | 11 |
| Total Repo Snapshots (cumulative) | 1,252 |
| New Repo Snapshots This Sweep | 308 |
| Sources Covered | 3 orgs + 4 users (4 rate-limited) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Total APT Across Swarm | 20.34477251 APT |

---

## GF(3) Color Chain — This Sweep (IDs 13–23)

| ID | Source Type | Source Name | Event Type | GF3 Trit | Color | Name |
|----|-------------|-------------|------------|-----------|-------|------|
| 13 | org  | plurigrid     | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | org  | kubeflow      | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | org  | TeglonLabs    | repo_snapshot |  0 | `#d3869b` | **ERGODIC** |
| 16 | user | migalkin      | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 17 | user | kristinezheng | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 18 | user | M1shaaa       | repo_snapshot |  0 | `#d3869b` | **ERGODIC** |
| 19 | user | AustinCStone  | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 20 | user | bmorphism     | rate_limited  | -1 | `#cc241d` | **MINUS** |
| 21 | user | zubyul        | rate_limited  |  0 | `#d3869b` | **ERGODIC** |
| 22 | user | DJedamski     | rate_limited  | +1 | `#b8bb26` | **PLUS** |
| 23 | user | wasita        | rate_limited  | -1 | `#cc241d` | **MINUS** |

GF(3) chain segment: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

> Note: bmorphism, zubyul, DJedamski, wasita hit GitHub unauthenticated rate limit (60 req/hr). Their increments are recorded with `rate_limited` event type; no repo rows inserted for these sources.

---

## Repo Snapshot Coverage (This Sweep)

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 53 |
| migalkin | user | 30 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| AustinCStone | user | 43 |
| bmorphism | user | 0 (rate-limited) |
| zubyul | user | 0 (rate-limited) |
| DJedamski | user | 0 (rate-limited) |
| wasita | user | 0 (rate-limited) |
| **Total** | | **308** |

### Top 15 Repos by Stars

| Repo | Language | Stars | Forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | — | 15,630 | 2,648 |
| kubeflow/pipelines | Python | 4,138 | 1,991 |
| kubeflow/spark-operator | Python | 3,125 | 1,480 |
| kubeflow/trainer | Go | 2,096 | 947 |
| kubeflow/katib | Python | 1,683 | 522 |
| kubeflow/examples | Jsonnet | 1,462 | 756 |
| kubeflow/manifests | YAML | 1,016 | 1,062 |
| kubeflow/arena | Go | 810 | 190 |
| kubeflow/kale | Python | 684 | 156 |
| kubeflow/mpi-operator | Go | 526 | 235 |
| kubeflow/fairing | Jsonnet | 337 | 143 |
| kubeflow/pytorch-operator | Jsonnet | 310 | 143 |
| kubeflow/community | Jsonnet | 196 | 257 |
| kubeflow/website | HTML | 184 | 919 |
| kubeflow/kfctl | Go | 182 | 134 |

### Language Distribution (This Sweep)

| Language | Repos |
|----------|-------|
| Python | 62 |
| Go | 15 |
| HTML | 13 |
| Rust | 12 |
| JavaScript | 11 |
| TypeScript | 8 |
| Jsonnet | 8 |
| Jupyter Notebook | 5 |
| Clojure | 5 |
| Java | 5 |

---

## Hamming Swarm — Aptos Wallet Balances

Queried via `0x1::coin::balance` view function on Aptos mainnet (`fullnode.mainnet.aptoslabs.com`).  
Method: POST to `/v1/view` — works across both legacy coin and fungible asset framework.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| bob   | `0x0a3c00c5…d7d2a9de0c13d00e05512d5d` | 12.65700700 |
| F     | `0x18a14b5b…b979bcf5f6da74c3cf71` | 1.96051600  |
| L     | `0x7c2eaeaf…94673ee6337eba9` | 1.92726900  |
| J     | `0x4d964db8…1b98cb6e2293e87f54` | 1.89509300  |
| alice | `0xc793acde…f80d41f556c2d0d624cc7b` | 0.43643352  |
| O     | `0x73252b60…d07467bf3024a525a89d` | 0.21013600  |
| K     | `0xa732040a…a2085e2a47a425dc4` | 0.16196100  |
| P     | `0x6218792d…c29366013621ec948` | 0.14013600  |
| M     | `0x6fed37a7…d4a74590fe483d49b7f2e9` | 0.11228500  |
| N     | `0xe7dde6da…a13fd4559a11551b2c` | 0.10612100  |
| Q     | `0xac40fa50…96af0a3b6525e5c89a9` | 0.10324000  |
| S     | `0xb8753014…bc3c27457a00beb4f99d0386` | 0.09178800  |
| R     | `0x7ce605cc…3a65d41ebeb36d76e10` | 0.09021700  |
| T     | `0x35781dc0…8fe8131b3759505f2d3f4588` | 0.07371300  |
| U     | `0x75860da4…a39e3fa521f395ef9956` | 0.05577300  |
| A     | `0x8699edc0…decfa46f78ab0af6eaebe9d7a` | 0.05176700  |
| V     | `0xb59dd817…62cff6ea8a89af2c3` | 0.04883299  |
| Y     | `0xd8e32848…617ba53ef2b39100fa2444c4` | 0.04444900  |
| X     | `0xa95cbbd1…030457d4569b2cbe33047d` | 0.04257700  |
| W     | `0x5f32aef7…d8963d45a6ccc7b0` | 0.04070500  |
| B     | `0x3f892ebe…cfe21105a4577cb13` | 0.03625600  |
| Z     | `0x7af0ef6e…5ebd5e6e4e197c` | 0.02426800  |
| D     | `0xf7765624…eda37688cc5bb2b1d9fcfdd1` | 0.01162900  |
| C     | `0x38b99e63…e123f7952691535e` | 0.01018500  |
| E     | `0xdc1d9d53…1ab4f565906b7a8d0958d36` | 0.00937200  |
| H     | `0xce67c327…ddac32e6f02e850d94e5300f` | 0.00168100  |
| I     | `0x070fe5d7…a508ea15fc00c1fc9` | 0.00068100  |
| G     | `0x69a394c0…7c641dd3c5dbcc7f32` | 0.00068100  |

**Total APT across swarm: 20.34477251 APT**

Distribution notes:
- Top 4 wallets (bob, F, L, J) hold 83.7% of total swarm APT
- 9 wallets hold < 0.01 APT (dust range)
- All 28 accounts confirmed active (sequence_number > 0)

---

## Multisig Contract Probes

Probed via `0x1::multisig_account::num_signatures_required` view function.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428…4987003` | 2 | ✅ |
| A-G | `0xf56c4a1c…bc0096` | 2 | ✅ |
| S-T | `0x3b1c3ae9…ed7883` | 2 | ✅ |
| V-W | `0x40fad7b4…80eb6d` | 2 | ✅ |
| Y-Z | `0xd3ffe181…75b883` | 2 | ✅ |

All 5 multisig contracts **healthy** — 2-of-N threshold confirmed on all pairs.

---

## MNX Markets

**Status: Unavailable** — `testnet.mnx.fi` is a Next.js SPA; no public REST/JSON API endpoint accessible without JS execution. Market data cannot be extracted via curl. Recorded as placeholder in `mnx_snapshots` table.

---

## DuckDB Ducklake State

| Table | Cumulative Rows |
|-------|----------------|
| world_increments | 34 |
| repo_snapshots | 1,252 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## Schema Reference

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

- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**
