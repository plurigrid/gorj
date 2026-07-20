# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-20

## Sweep Metadata

- **Date:** 2026-07-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** 1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos This Sweep |
|--------|------|-----------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin (social graph) | user | 19 |
| DJedamski (social graph) | user | 6 |
| wasita (social graph) | user | 12 |
| kristinezheng (social graph) | user | 5 |
| M1shaaa (social graph) | user | 8 |
| AustinCStone (social graph) | user | 41 |
| **TOTAL THIS SWEEP** | | **394** |

### GF(3) Color Chain Rule

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

### Top Repos by Stars (this sweep)

| Repo | Lang | Stars | Last Push |
|------|------|-------|-----------|
| kubeflow/kubeflow | — | 15785 | 2026-07-10 |
| kubeflow/pipelines | Python | 4169 | 2026-07-20 |
| kubeflow/spark-operator | Python | 3140 | 2026-07-17 |
| kubeflow/trainer | Go | 2152 | 2026-07-20 |
| kubeflow/katib | Python | 1691 | 2026-07-16 |
| kubeflow/community-distribution | YAML | 1029 | 2026-07-20 |
| kubeflow/arena | Go | 815 | 2026-07-17 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | JS | 22 | 2026-01-16 |
| plurigrid/asi | HTML | 31 | 2026-07-10 |
| plurigrid/asi-skills | Julia | 3 | 2026-04-26 |

### Most Active (pushed 2026-07-20)

- `kubeflow/hub`, `kubeflow/pipelines`, `kubeflow/trainer`, `kubeflow/sdk`
- `kubeflow/notebooks`, `kubeflow/mcp-server`, `kubeflow/community-distribution`
- `kubeflow/mpi-operator`, `kubeflow/internal-acls`
- `plurigrid/gorj` — this repo (Clojure/GF3 nREPL routing)
- `bmorphism/Gay.jl` — wide-gamut color sampling (Julia)
- `wasita/wasita.github.io` — personal website (Svelte)

### Notable Signals

- **kubeflow/mcp-server** (★28, Python): New MCP server for Kubeflow tooling — active today
- **plurigrid/gorj** (★1): This repo — forj + Rama topology nREPL routing + GF(3) coloring — pushed today
- **plurigrid/asi** (★31, HTML): "Everything is topological chemputer" — most-starred plurigrid repo
- **bmorphism/Gay.jl** active today — wide-gamut color sampling with splittable determinism (Pigeonhole)
- **TeglonLabs/jank-crane** (C++): crane-jank converged-IR hub with GF3 convergence maps (pushed 2026-06-08)
- **migalkin** social graph: Knowledge graph ML researcher; NodePiece (★144) + StarE (★89)
- **wasita** social graph: Active network scientist / SvelteKit developer; site active today
- **AustinCStone** social graph: ML/vision researcher; TextGAN (★92), byteruckus pushed 2026-07-15

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

Queried 28 addresses (alice, bob, A–Z) via Aptos fullnode mainnet API.

**Result: All 28 accounts return `resource_not_found`** for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
Accounts exist on-chain but CoinStore is not initialized — zero APT balance for all.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793ac... | NULL (no CoinStore) |
| bob | 0x0a3c00... | NULL (no CoinStore) |
| A–Z | various | NULL (no CoinStore) |

*All 28 addresses stored in `aptos_snapshots` table with `balance_apt = NULL`.*

### Multisig Contract Probes

Probed 5 multisig contracts via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✅ |
| A-G | 0xf56c4a1c... | 2 | ✅ |
| Y-Z | 0xd3ffe181... | 2 | ✅ |
| S-T | 0x3b1c3ae9... | 2 | ✅ |
| V-W | 0x40fad7b4... | 2 | ✅ |

**All 5 multisigs healthy — 2-of-2 signature threshold confirmed on all pairs.**

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — the testnet frontend requires Vercel deployment authentication.  
No market data was accessible. `mnx_snapshots` table remains empty this sweep.

---

## DuckDB Ducklake State

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (cumulative) | Notes |
|-------|-------------------|-------|
| world_increments | 331 | Includes prior sweep runs |
| repo_snapshots | 1252 | Cumulative history |
| aptos_snapshots | 28 | This sweep: all NULL |
| multisig_probes | 5 | All healthy |
| mnx_snapshots | 0 | Auth-blocked |

History is preserved across sweeps by design (append-only ducklake).

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
