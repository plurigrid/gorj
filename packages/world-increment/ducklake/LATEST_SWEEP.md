# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-25

## Sweep Metadata
- **Date:** 2026-07-25T05:09 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) Chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### This-Run Summary Counts

| Metric | Value |
|--------|-------|
| World Increments Added (this run) | 237 |
| GF(3) ERGODIC (#d3869b) | 78 |
| GF(3) PLUS (#b8bb26) | 80 |
| GF(3) MINUS (#cc241d) | 79 |
| Repo Snapshots (cumulative) | 1,158+ |
| Sources Covered | 3 orgs + 8 users |

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 50 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 12 |
| AustinCStone | social graph | 20 |
| DJedamski | social graph | 6 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| **TOTAL** | | **273** |

### Top Repos by Stars (Cumulative Ducklake)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,792 | — |
| kubeflow/pipelines | 4,169 | Python |
| kubeflow/spark-operator | 3,143 | Python |
| kubeflow/trainer | 2,153 | Go |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| migalkin/kgcourse2021 | 24 | HTML |

### Notable New Activity (2026 pushes)
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): crane-jank converged-IR hub, loopify pass spec, GF3 convergence maps
- **wasita/wasita.github.io** (Svelte, pushed 2026-07-21): active personal site
- **AustinCStone/byteruckus** (HTML, pushed 2026-07-15): latest AustinCStone repo
- **migalkin/kgcourse2021** (HTML, updated 2026-07-10): Knowledge Graphs course materials

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses queried (alice, bob, A–Z) via Aptos fullnode mainnet API with 1s sleep between calls.

| Metric | Value |
|--------|-------|
| Total addresses probed | 28 |
| Non-zero APT balance | 0 |
| Zero / unfunded | 28 |

All Hamming swarm wallets at **0.0 APT** on mainnet. CoinStore resources either unfunded or uninitialized for these addresses.

### Multisig Contract Probes

5 contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...4987003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a1c...c0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fad7b4...0eb6d | 2 | ✅ HEALTHY |

**All 5 multisig contracts healthy** — all require exactly 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

Status: **SPA — no JSON API publicly accessible.** `testnet.mnx.fi` serves a Next.js app. API paths `/api/markets`, `/api/v1/markets`, `/api/tickers` all return HTML. No market data extractable without browser execution. Recorded as unavailable in `mnx_snapshots` table.

---

## DuckDB Ducklake Schema

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
