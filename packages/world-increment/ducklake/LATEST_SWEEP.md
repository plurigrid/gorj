# World-Increment Sweep — 2026-04-26

## Sweep Metadata
- **Date:** 2026-04-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 (cumulative, ids 1–13) |
| Total Repo Snapshots | 945 (cumulative) |
| Sources Covered | 11 distinct sources |
| Aptos Addresses Snapshotted | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — Recent Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (org) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |
| **13** | **plurigrid/gorj** | **sweep_complete** | **+1** | **`#b8bb26`** | **PLUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## JOB 1: GitHub Social Graph Sweep

### Status

| Source | Type | Result |
|--------|------|--------|
| plurigrid/gorj | MCP tools (scoped) | ✅ 20 commits, 50 branches |
| plurigrid (org) | GitHub API (unauthenticated) | ❌ rate limit exhausted |
| kubeflow (org) | GitHub API (unauthenticated) | ❌ rate limit exhausted |
| TeglonLabs (org) | GitHub API (unauthenticated) | ❌ rate limit exhausted |
| bmorphism (user) | GitHub API (unauthenticated) | ❌ rate limit exhausted |
| zubyul + social graph (6) | GitHub API (unauthenticated) | ❌ rate limit exhausted |

> No `GITHUB_TOKEN` in environment; unauthenticated rate limit (60 req/hr) was 0 at sweep start. MCP tools are scoped to `plurigrid/gorj` only.

### plurigrid/gorj Snapshot

- **Latest commit:** `ebf263f` — "world-increment ducklake: sync world.duckdb sweep state" (2026-04-14)
- **Active branches:** 50 (`world-increment/sweep-*` pattern, ranging 2026-03-26 → 2026-04-14)
- **Language:** Clojure
- **Description:** MCP server + hooks that give AI coding agents a Clojure REPL

### Prior Sweep Data (ids 1–12, from 2026-04-12)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

### Notable Repos (from prior sweep)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **plurigrid/asi**: 16 stars — topological chemputer

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-04-26)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com/v1`.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A–Z (26) | — | 0.0 each |

**Total APT across swarm:** 0.0 APT  
**Non-zero balances:** 0 / 28

### Multisig Contract Probes (2026-04-26)

All probed via `0x1::multisig_account::num_signatures_required` view function.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**All 5 multisig contracts healthy** — 2-of-N threshold confirmed on all pairs.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` is a Next.js SPA. Paths probed: `/api/markets`, `/api/v1/markets`, `/`. All return HTML shell, no JSON market data available without browser JS execution.

**Status:** Unavailable — `mnx_snapshots` table remains empty this sweep.

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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
