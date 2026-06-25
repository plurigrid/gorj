# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-25

## Sweep Metadata
- **Date:** 2026-06-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (this run)

| Metric | Value |
|--------|-------|
| Repos ingested this run | 323 |
| World Increments in DB (total) | 346 |
| Repo Snapshots in DB (total) | 1267 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos addresses probed | 28 |
| Multisig contracts probed | 5 |

---

## GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 114 |
| +1 | PLUS | #b8bb26 | 116 |
| -1 | MINUS | #cc241d | 116 |

Assignment: `id%3==0 → ERGODIC`, `id%3==1 → PLUS`, `id%3==2 → MINUS`

---

## GitHub Social Graph — Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| TeglonLabs | org | 5 |
| migalkin | social graph | 19 |
| AustinCStone | social graph | 40 |
| wasita | social graph | 11 |
| DJedamski | social graph | 6 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| **TOTAL** | | **391** |

## Top Starred Repos (this run)

| Repo | Stars | Language | Source |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,743 | — | kubeflow |
| kubeflow/pipelines | 4,156 | Python | kubeflow |
| kubeflow/spark-operator | 3,128 | Python | kubeflow |
| kubeflow/trainer | 2,121 | Go | kubeflow |
| migalkin/NodePiece | 144 | Python | social:migalkin |
| AustinCStone/TextGAN | 92 | Python | social:AustinCStone |
| migalkin/StarE | 89 | Python | social:migalkin |
| TeglonLabs/mathpix-gem | 2 | Ruby | TeglonLabs |
| wasita/magic-garden | 2 | Python | social:wasita |

## Notable New Activity

- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"
- **wasita/wasita.github.io** (Svelte, pushed 2026-06-25): active personal site — pushed TODAY
- **migalkin/RWL** (Python, pushed 2026-05-28): Weisfeiler and Leman Go Relational (LOG 2022)
- **kristinezheng/kristinezheng.github.io** (HTML, pushed 2026-06-07): recently active

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All queried via `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 addresses (alice, bob, A–Z) return 0.0 APT.**

Addresses either unfunded on mainnet or CoinStore resource not initialized. No balance discrepancies detected.

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed on mainnet.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection active. All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) require authentication bypass token. No market data extracted. `mnx_snapshots` table is empty.

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
