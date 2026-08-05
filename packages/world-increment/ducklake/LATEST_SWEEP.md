# World-Increment Sweep — 2026-08-05

## Sweep Metadata
- **Date:** 2026-08-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 227 |
| Total Repo Snapshots | 227 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Sampled | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 75 |
| 1 | `#b8bb26` | PLUS | 76 |
| -1 | `#cc241d` | MINUS | 76 |

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 50 |
| kubeflow | org | 49 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | social graph | 6 |
| TeglonLabs | org | 5 |
| wasita | social graph | 5 |
| AustinCStone | social graph | 4 |
| kristinezheng | social graph | 3 |
| DJedamski | social graph | 3 |
| M1shaaa | social graph | 3 |
| **TOTAL** | | **227** |

### Top Repos by Stars

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15805 | 2026-07-10 |
| kubeflow/pipelines | Python | 4177 | 2026-08-05 |
| kubeflow/spark-operator | Python | 3143 | 2026-08-05 |
| kubeflow/trainer | Go | 2170 | 2026-08-04 |
| kubeflow/katib | Python | 1694 | 2026-08-05 |
| kubeflow/examples | Jsonnet | 1461 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1029 | 2026-08-04 |
| kubeflow/arena | Go | 816 | 2026-07-29 |
| kubeflow/kale | Python | 699 | 2026-08-05 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| plurigrid/asi | HTML | 59 | 2026-07-10 |
| bmorphism/anti-bullshit-mcp-server | JS | 23 | 2026-01-16 |
| migalkin/kgcourse2021 | HTML | 24 | 2026-07-10 |

### Notable Activity (pushed within last 7 days of 2026-08-05)

- **kubeflow/sdk** — pushed 2026-08-05T14:45 (Universal Python SDK for AI on K8s)
- **kubeflow/kale** — pushed 2026-08-05T14:52
- **kubeflow/pipelines** — pushed 2026-08-05T13:48
- **plurigrid/gorj** — pushed 2026-08-05T14:21 (this repo, 1650 open issues)
- **bmorphism/Gay.jl** — pushed 2026-08-05T02:24 (188 open issues, active)
- **wasita/xoxowasita-analysis** — pushed 2026-08-04T21:50 (brand new repo)
- **wasita/joint-planning-lit** — pushed 2026-08-04T03:30 (brand new repo)
- **plurigrid/eirobri** — pushed 2026-08-04T02:23

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 addresses (alice, bob, A–Z) are **live accounts** with non-zero sequence numbers (alice: seq=72, A: seq=58), but have **no CoinStore resource**. Balances recorded as 0.0 APT. Accounts use the Fungible Asset (FA) standard rather than the legacy `0x1::coin::CoinStore` API, or hold no native APT.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793ac...4cc7b | 0.0 |
| bob | 0x0a3c00...512d5d | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Probes

All 5 contracts healthy — `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f4...87003 | 2 | ✓ healthy |
| A-G | 0xf56c4a...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe1...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3a...7883 | 2 | ✓ healthy |
| V-W | 0x40fad7...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

Site is a **Next.js SPA** — no market data exposed via REST API endpoints. Recorded as unavailable in `mnx_snapshots`.

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
