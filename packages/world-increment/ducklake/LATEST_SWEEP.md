# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-11

## Sweep Metadata
- **Date:** 2026-07-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** 1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (this run)

| Metric | Value |
|--------|-------|
| New World Increments | 64 |
| New Repo Snapshots | 64 |
| Aptos Snapshots | 28 |
| Multisig Probes | 5 |
| MNX Snapshots | 0 (auth-gated) |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain

Assignment rule: `id mod 3 == 0` → trit=0 ERGODIC #d3869b | `id mod 3 == 1` → trit=1 PLUS #b8bb26 | `id mod 3 == 2` → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 60 total, 10 inserted |
| kubeflow | org | 40+ total, 10 inserted |
| TeglonLabs | org | 5 |
| bmorphism | user | 40+ total, 10 inserted |
| zubyul | user | 30+ total, 10 inserted |
| migalkin | user (zubyul graph) | 10 total, 4 inserted |
| wasita | user (zubyul graph) | 11 total, 3 inserted |
| kristinezheng | user (zubyul graph) | 5 |
| DJedamski | user (zubyul graph) | 6 total, 3 inserted |
| M1shaaa | user (zubyul graph) | 8 total, 3 inserted |
| AustinCStone | user (zubyul graph) | 40 total, 4 inserted |

### Notable Repos (by stars, this run)

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,771 | — | 2026-07-10 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-11 |
| kubeflow/spark-operator | 3,137 | Python | 2026-07-10 |
| kubeflow/trainer | 2,135 | Go | 2026-07-10 |
| kubeflow/katib | 1,689 | Python | 2026-07-10 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 30 | HTML | 2026-07-10 |

### Active Plurigrid Repos (last 30 days)
- **plurigrid/gorj** — Clojure, 1115 open issues — GF(3) nREPL routing (pushed 2026-07-11)
- **plurigrid/asi** — HTML, 30★ — topological chemputer (pushed 2026-07-10)
- **plurigrid/shrimp** — Jank worked example (pushed 2026-07-03)
- **plurigrid/eirobri** — Clojure, EiRoBri replay world (pushed 2026-06-30)

### TeglonLabs Activity (5 repos)
- **jank-crane** — C++, crane-jank converged-IR hub with GF3 maps (pushed 2026-06-08)
- **mathpix-gem** — Ruby 2★, math OCR gem

### bmorphism Highlights
- **Gay.jl** — Julia, 187 open issues, 2★ — wide-gamut splittable color sampling (pushed 2026-07-11, most active)
- **satreadout** — Lean 4.28 machine-checked perceptual readout (pushed 2026-06-20)
- **ocaml-mcp-sdk** — OCaml, 61★ — first-class MCP SDK (pushed 2026-03-16)
- **anti-bullshit-mcp-server** — JS, 23★ — epistemic validation MCP

### zubyul Highlights
- **nash-tui / nash-web** — Rust — NASH token TUI + browser WASM (pushed 2026-04-13)
- **tilelang-kernels** — Python — TileLang GPU kernels for GF(3) (pushed 2026-03-16)
- **gay-world** — Python, 1★ — Goblin world builder with MLX decomposition

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Status:** All 28 addresses → `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger v6,223,528,667.

No Hamming swarm address has an initialized APT coin store on mainnet. Accounts may be unfunded/non-existent on mainnet.

### Multisig Contract Probes — ALL HEALTHY ✓

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | **2** | ✓ healthy |
| A-G | 0xf56c4a1c... | **2** | ✓ healthy |
| Y-Z | 0xd3ffe181... | **2** | ✓ healthy |
| S-T | 0x3b1c3ae9... | **2** | ✓ healthy |
| V-W | 0x40fad7b4... | **2** | ✓ healthy |

All 5 multisig contracts respond with `num_signatures_required = 2`.

### MNX Markets (testnet.mnx.fi)

**Status:** Vercel deployment protection — "Authentication Required" (visitor password needed). Market data unavailable without credentials.

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
