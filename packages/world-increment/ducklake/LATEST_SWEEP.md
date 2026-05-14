# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-14

## Sweep Metadata
- **Date:** 2026-05-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul graph) | 19 |
| wasita | user (zubyul graph) | 11 |
| DJedamski | user (zubyul graph) | 6 |
| kristinezheng | user (zubyul graph) | 6 |
| M1shaaa | user (zubyul graph) | 8 |
| AustinCStone | user (zubyul graph) | 40 |
| **TOTAL** | | **391** |

### GF(3) Increment Distribution (per-repo color chain)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 130 |
| 1 | #b8bb26 | PLUS | 131 |
| -1 | #cc241d | MINUS | 130 |

Assignment: `id%3==0 → ERGODIC` · `id%3==1 → PLUS` · `id%3==2 → MINUS`

### Top 15 Repos by Stars

| Repo | Stars | Language |
|------|-------|---------|
| kubeflow/kubeflow | 15,629 | — |
| kubeflow/pipelines | 4,140 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,098 | Go |
| kubeflow/katib | 1,682 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,017 | YAML |
| kubeflow/arena | 810 | Go |
| kubeflow/kale | 686 | Python |
| kubeflow/mpi-operator | 526 | Go |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |

### Notable Highlights

**plurigrid** (100 repos): Most active today: `plurigrid/gorj` (188 open issues, pushed 2026-05-14).
Top-starred: `plurigrid/asi` (21 ⭐), `plurigrid/ontology` (8 ⭐), `plurigrid/vcg-auction` (7 ⭐).
Active themes: Gay.jl GF(3) color semantics, Zig/Clojure/Rust runtimes, OCapN/Goblins, categorical type theory, NASH portal, zig-syrup OCapN.

**kubeflow** (48 repos): Flagship `kubeflow/kubeflow` (15,629 ⭐, pushed 2026-05-07). Trainer, spark-operator, katib, pipelines all pushed 2026-05-12–13.
New: `kubeflow/mcp-apache-spark-history-server` (168 ⭐), `kubeflow/mcp-server` (7 ⭐).

**bmorphism** (100 repos): `bmorphism/Gay.jl` (188 open issues, pushed today 2026-05-14).
Top MCP servers: `say-mcp-server` (20 ⭐, 9 forks), `anti-bullshit-mcp-server` (23 ⭐), `babashka-mcp-server` (18 ⭐), `ocaml-mcp-sdk` (61 ⭐).
Recent: `nanoclj-zig`, `zig-syrup` pushed 2026-05-07.

**zubyul** (49 repos): `tilelang-kernels` (GPU GF(3)/SplitMix64 kernels for NVIDIA GB10 Blackwell CUDA 13.0), `nash-tui` (NASH token TUI GeckoTerminal), `ghostel-emacs-worlds` (Ghostty + Emacs stack), `kinesis-kb360pro` (GF(3) keyboard).

**TeglonLabs** (4 repos): `topoi` (Python), `mathpix-gem` (Ruby, 2 ⭐), `monad-mcp-server`, `coin-flip-mcp`.

**Social graph** (migalkin/wasita/DJedamski/kristinezheng/M1shaaa/AustinCStone): KG research (NodePiece 144 ⭐ ICLR'22, StarE 89 ⭐ EMNLP'20), ML/DL, neuroscience lookit studies.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming-swarm addresses (alice, bob, A–Z) queried via Aptos mainnet fullnode.
All returned **0.0 APT** — CoinStore resources not initialized or accounts hold zero balance.

| World | Short Address | APT Balance |
|-------|--------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (5 pairs)

All probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`. All **2-of-N**, all healthy.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | **2** | ✅ HEALTHY |
| A-G | 0xf56c...0096 | **2** | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | **2** | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | **2** | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | **2** | ✅ HEALTHY |

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` returns HTTP 200 (Next.js SPA). No JSON API endpoint accessible server-side (`/api/markets`, `/api/v1/markets`, `/markets` all return HTML). **mnx_snapshots table is empty** — data is loaded client-side via JS bundles only.

---

## Database Summary

```
world_increments : 391 rows  (GF3 color-chained repo sweep events)
repo_snapshots   : 391 rows  (full repo metadata — stars, forks, language, pushed_at)
aptos_snapshots  : 28 rows   (Hamming swarm wallet balances, all 0.0 APT)
multisig_probes  : 5 rows    (A-B, A-G, Y-Z, S-T, V-W — all 2-sig, healthy)
mnx_snapshots    : 0 rows    (SPA only — no accessible JSON API)
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

## GF(3) Assignment Rule
- `id % 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id % 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id % 3 == 2` → trit=-1, color=#cc241d, name=MINUS
