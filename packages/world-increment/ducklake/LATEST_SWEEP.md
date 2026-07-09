# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-09

## Sweep Metadata
- **Date:** 2026-07-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment ID:** 24 (GF3: trit=0 ERGODIC #d3869b)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Total Repo Snapshots | 1,061 |
| New Repos This Sweep | 117 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (401) |

---

## Job 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Total | Snapshotted |
|--------|------|-------|-------------|
| plurigrid | org | 103 | 50 |
| kubeflow | org | 49 | 15 |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 105 | 13 |
| zubyul | user | 49 | 10 |
| migalkin | social graph | 19 | 5 |
| DJedamski | social graph | 6 | 4 |
| wasita | social graph | 11 | 4 |
| kristinezheng | social graph | 5 | 3 |
| M1shaaa | social graph | 8 | 3 |
| AustinCStone | social graph | 40 | 5 |

### Notable Repos (by stars, this sweep)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,768 | — | 2026-07-08 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-09 |
| kubeflow/spark-operator | 3,135 | Python | 2026-07-08 |
| kubeflow/trainer | 2,134 | Go | 2026-07-08 |
| kubeflow/katib | 1,689 | Python | 2026-07-08 |
| kubeflow/examples | 1,460 | Jsonnet | 2026-06-16 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-07 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |

### Most Recently Pushed (this sweep)

| Repo | Pushed At |
|------|-----------|
| plurigrid/gorj | 2026-07-09T04:14:06Z |
| bmorphism/Gay.jl | 2026-07-09T00:33:39Z |
| kubeflow/pipelines | 2026-07-09T01:06:13Z |
| kubeflow/kubeflow | 2026-07-08T21:43:08Z |
| kubeflow/trainer | 2026-07-08T20:26:42Z |

### TeglonLabs Highlights (2026-07-09)

- **jank-crane** (C++, 2026-06-08) — crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps
- **mathpix-gem** (Ruby, ⭐2) — math image → LaTeX, chemistry → SMILES, docs → markdown OCR
- **coin-flip-mcp** (JavaScript, 2 forks) — MCP server for random.org coin flips
- **topoi** (Python) — open issues: 1
- **monad-mcp-server** — Monad MCP Server

### Plurigrid Notable (gorj repo = this very sweep)

- **plurigrid/gorj** (Clojure, ⭐1, 1073 open issues) — forj + Rama topology nREPL routing + GF(3) gay trit coloring — pushed 2026-07-09
- **plurigrid/asi** (HTML, ⭐30, 9 forks) — everything is topological chemputer!
- **plurigrid/place** (TeX, ⭐1) — pushed 2026-07-07
- **plurigrid/eirobri** (Clojure, 30 open issues) — EiRoBri replay world

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

Queried Aptos mainnet via `fullnode.mainnet.aptoslabs.com` for CoinStore APT balances.

**Result: All 28 addresses returned "Resource not found"** — these wallets do not exist or hold no APT on Aptos mainnet as of 2026-07-09.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | null |
| bob | 0x0a3c...2d5d | null |
| A | 0x8699...9d7a | null |
| B | 0x3f89...b13 | null |
| C | 0x38b9...35e | null |
| D | 0xf776...dd1 | null |
| E–Z (22 more) | various | null |

### Multisig Contract Probes

All 5 probed Aptos multisig contracts are **healthy** (`num_signatures_required = 2`).

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` and `/api/markets` both return HTTP 401 Unauthorized. Market data not retrievable from this environment.

---

## GF(3) Assignment Rule

- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

Increment 24: 24 mod 3 = 0 → **ERGODIC #d3869b** — closes the 8th full GF(3) cycle.

---

## DB Schema

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
