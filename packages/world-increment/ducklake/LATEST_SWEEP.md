# World-Increment Sweep + Hamming Snapshot — 2026-07-06

## Sweep Metadata
- **Date:** 2026-07-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python SDK)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts (this run)

| Metric | Value |
|--------|-------|
| New World Increments | 110 |
| Cumulative Repo Snapshots | 1031 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 36 |
| +1 | PLUS | `#b8bb26` | 37 |
| -1 | MINUS | `#cc241d` | 37 |

Chain rule: `id mod 3 == 0 → ERGODIC`, `id mod 3 == 1 → PLUS`, `id mod 3 == 2 → MINUS`

---

## Top Repos by Stars (2026-07-06 snapshot)

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,764 | 2026-06-18 |
| kubeflow/pipelines | Python | 4,169 | 2026-07-05 |
| kubeflow/spark-operator | Python | 3,132 | 2026-07-02 |
| kubeflow/trainer | Go | 2,129 | 2026-07-03 |
| kubeflow/katib | Python | 1,689 | 2026-07-01 |
| kubeflow/kale | Python | 696 | 2026-07-01 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |

---

## Repo Counts by Source (this run)

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 20 |
| kubeflow | org | 13 |
| TeglonLabs | org | 5 |
| bmorphism | user | 14 |
| zubyul | user | 9 |
| migalkin | social | 5 |
| DJedamski | social | 4 |
| wasita | social | 5 |
| kristinezheng | social | 3 |
| M1shaaa | social | 3 |
| AustinCStone | social | 6 |
| **TOTAL** | | **87** |

---

## Notable Activity (most recently pushed)

- **plurigrid/gorj** (Clojure, 999 open issues) — pushed 2026-07-06 ← this repo
- **wasita/wasita.github.io** (Svelte) — pushed 2026-07-05
- **kubeflow/pipelines** (Python, 4169★) — pushed 2026-07-05
- **kubeflow/community-distribution** (YAML) — pushed 2026-07-05
- **plurigrid/eirobri** (Clojure, 30 open issues) — pushed 2026-06-30
- **plurigrid/asi** (HTML, 28★) — pushed 2026-06-29
- **bmorphism/Gay.jl** (Julia, 187 open issues) — pushed 2026-06-20
- **bmorphism/satreadout** — machine-checked saturating perceptual readout — pushed 2026-06-20
- **TeglonLabs/jank-crane** (C++) — GF3 convergence maps — pushed 2026-06-08

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A–Z)

**All 28 wallets: 0.0 APT**

Accounts appear uninitialized on mainnet — no `CoinStore<AptosCoin>` resource registered. Aptos fullnode API (`fullnode.mainnet.aptoslabs.com`) was reachable and returned valid (zero) responses for all addresses.

### Multisig Contract Probes (5 pairs)

All probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4f428...987003 | **2** | ✓ HEALTHY |
| A-G | 0xf56c4a1c...c0096 | **2** | ✓ HEALTHY |
| Y-Z | 0xd3ffe181...5b883 | **2** | ✓ HEALTHY |
| S-T | 0x3b1c3ae9...7883 | **2** | ✓ HEALTHY |
| V-W | 0x40fad7b4...eb6d | **2** | ✓ HEALTHY |

All multisig accounts require 2-of-N signatures. No anomalies detected.

### MNX Markets (`testnet.mnx.fi`)

**UNAVAILABLE** — Endpoint requires Vercel deployment-protection authentication. All probed paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return an auth challenge. Market data could not be extracted without a bypass token.

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

## DuckDB Table Sizes (cumulative)
| Table | Rows |
|-------|------|
| world_increments | 110 |
| repo_snapshots | 1031 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (error placeholder) |
