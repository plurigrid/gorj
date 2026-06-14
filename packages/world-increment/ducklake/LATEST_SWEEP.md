# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-14

## Sweep Metadata
- **Date:** 2026-06-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source Type | Source | Repos Snapshotted |
|-------------|--------|--------------------|
| org | plurigrid | 28 |
| org | kubeflow | 14 |
| org | TeglonLabs | 5 |
| user | bmorphism | 17 |
| user | zubyul | 12 |
| social | migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone | 11 |
| **TOTAL** | | **87 new increments** |

### Top Repos by Stars (this sweep)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,720 | — | 2026-06-11 |
| kubeflow/pipelines | 4,153 | Python | 2026-06-14 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-12 |
| kubeflow/trainer | 2,115 | Go | 2026-06-13 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| plurigrid/ontology | 8 | JavaScript | 2025-05-27 |
| plurigrid/gorj | 0 | Clojure | 2026-06-14 ⭐ (570 issues, very active) |

### Most Recently Pushed

- `kubeflow/pipelines` — 2026-06-14T11:54 (4,153 stars, 479 open issues)
- `plurigrid/gorj` — 2026-06-14T11:21 (570 open issues)
- `bmorphism/Gay.jl` — 2026-06-14T00:43 (189 open issues)
- `kubeflow/website` — 2026-06-13T16:50
- `kubeflow/trainer` — 2026-06-13T03:19

### Notable Social Graph Highlights

- **migalkin**: Knowledge graph researcher (NodePiece 144★, StarE 89★, NBFNet_mlx 10★)
- **wasita**: Active developer (Svelte personal site, magic-garden bot 2★, vocoder)
- **AustinCStone**: ML researcher (TextGAN 92★, StereoVisionMRF 11★)
- **bmorphism**: Prolific MCP server author (ocaml-mcp-sdk 61★, say-mcp 20★, babashka-mcp 19★)
- **zubyul**: plurigrid collaborator (Gay.jl fork, nash-tui, gay-world, tilelang-kernels)

### GF(3) Color Chain Distribution (cumulative)

| GF3 Name | Color | Trit | Count (cumulative) |
|----------|-------|------|-------------------|
| ERGODIC | `#d3869b` | 0 | 36 |
| PLUS | `#b8bb26` | +1 | 37 |
| MINUS | `#cc241d` | -1 | 37 |

GF(3) rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z — 28 wallets)

All 28 addresses returned HTTP 404 from `fullnode.mainnet.aptoslabs.com`. This indicates the accounts have not initialized an `AptosCoin::CoinStore` resource on mainnet (uninitialized/zero-balance accounts). All recorded as `balance_apt = 0.0` in `aptos_snapshots`.

### Multisig Contract Probes — ALL HEALTHY ✅

All 5 Hamming-swarm multisig accounts are operational requiring 2 signatures.

| Pair | Address | Sigs Required | Status |
|------|---------|:-------------:|--------|
| A-B | 0x0da4f428a0c007da0f762... | 2 | ✅ healthy |
| A-G | 0xf56c4a1c0906214f3f859... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1812b2df4062281c... | 2 | ✅ healthy |
| S-T | 0x3b1c3ae905d44c3a49f0d... | 2 | ✅ healthy |
| V-W | 0x40fad7b423a843650fddc... | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable (HTTP 401 Unauthorized)** — All API paths require authentication. SPA likely needs session cookie or API key. `mnx_snapshots` table is empty for this run.

---

## DuckDB Table Summary

| Table | Rows (cumulative) |
|-------|:-----------------:|
| world_increments | 110 |
| repo_snapshots | 1031 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth required) |

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

## Action Items

- Aptos wallet 404s: accounts need APT funding + `register()` to initialize CoinStore
- MNX testnet: obtain API credentials for future market sweeps
- kubeflow/pipelines pushing hard (2026-06-14): worth monitoring for releases
- bmorphism/Gay.jl has 189 open issues — high velocity project
