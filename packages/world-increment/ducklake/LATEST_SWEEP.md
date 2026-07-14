# World-Increment Sweep + Hamming Snapshot — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 84 |
| Total Repo Snapshots | 84 |
| Sources Covered | 3 orgs + 3 users + social graph |

### GF(3) Distribution (84 increments)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 28 |
| +1 | PLUS | `#b8bb26` | 28 |
| −1 | MINUS | `#cc241d` | 28 |

GF(3) rule: `id%3==0` → ERGODIC · `id%3==1` → PLUS · `id%3==2` → MINUS

---

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,777 | — | 2026-07-14 |
| kubeflow/pipelines | 4,165 | Python | 2026-07-14 |
| kubeflow/spark-operator | 3,135 | Python | 2026-07-13 |
| kubeflow/trainer | 2,139 | Go | 2026-07-14 |
| kubeflow/katib | 1,690 | Python | 2026-07-11 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-13 |
| kubeflow/mcp-apache-spark-history-server | 182 | Python | 2026-07-07 |
| kubeflow/hub | 177 | Go | 2026-07-13 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |

### Most Active Today (2026-07-14)

- `plurigrid/gorj` — Clojure — pushed 2026-07-14T05:12:55Z (this repo!)
- `plurigrid/eirobri` — Clojure — pushed 2026-07-14T02:23:51Z
- `bmorphism/Gay.jl` — Julia — pushed 2026-07-14T04:33:04Z (GF3-aware color sampling)
- `kubeflow/trainer` — Go — pushed 2026-07-14T04:08:24Z
- `wasita/wm-cv` — Svelte — pushed 2026-07-14T03:53:19Z
- `wasita/wasita.github.io` — Svelte — pushed 2026-07-14T03:31:01Z

### Repos by Source

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 50 |
| kubeflow | org | 10 |
| TeglonLabs | org | 5 |
| bmorphism | user | 7 |
| zubyul | user | 5 |
| social_graph | multi-user | 7 |
| **TOTAL** | | **84** |

### Social Graph Highlights

- **migalkin**: KG researcher — NodePiece (144★), StarE (89★), kgcourse2021 (24★), NBFNet_mlx active
- **wasita**: Active today — personal site + CV pushed; vocoder, send2kobo projects
- **zubyul**: voice-observatory, tilelang-kernels (GF3 trit classification GPU kernels), gay-world
- **bmorphism**: Gay.jl pushed today; satreadout, bci-preview, world launcher active

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances — alice, bob, A–Z (28 total)

All 28 wallets queried via `fullnode.mainnet.aptoslabs.com`. All returned **0.0 APT** — accounts are unfunded or have no CoinStore resource on mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | 0x8699…–0x7af0… | 0.0 each |

### Multisig Contract Probes — All Healthy ✅

All 5 multisig accounts exist on-chain and require **2-of-N signatures**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | ✅ healthy |
| A-G | 0xf56c…0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff…b883 | 2 | ✅ healthy |
| S-T | 0x3b1c…7883 | 2 | ✅ healthy |
| V-W | 0x40fa…eb6d | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — all routes return Vercel authentication required. No market data extracted.

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
