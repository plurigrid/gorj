# World-Increment Sweep — 2026-06-21

## Sweep Metadata
- **Date:** 2026-06-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Prior sweep:** 2026-04-12 (accumulated in DB)

---

## Summary Counts (cumulative DB state)

| Metric | Value |
|--------|-------|
| Total World Increments | 34 (accumulated) |
| Total Repo Snapshots | 1,325 (accumulated) |
| Aptos Snapshots (this run) | 28 |
| Multisig Probes (this run) | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — This Sweep's 11 Increments

| Source | Event Type | GF3 Trit | Color | Name |
|--------|------------|-----------|-------|------|
| plurigrid | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| kubeflow | repo_snapshot | 1 | `#b8bb26` | **PLUS** |
| bmorphism | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| zubyul | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| migalkin | repo_snapshot | 1 | `#b8bb26` | **PLUS** |
| AustinCStone | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| wasita | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| TeglonLabs | repo_snapshot | 1 | `#b8bb26` | **PLUS** |
| DJedamski | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| kristinezheng | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| M1shaaa | repo_snapshot | 1 | `#b8bb26` | **PLUS** |

GF(3) assignment rule: `id%3==0 → trit=0 ERGODIC #d3869b`, `id%3==1 → trit=1 PLUS #b8bb26`, `id%3==2 → trit=-1 MINUS #cc241d`

---

### Repo Counts — This Sweep

| Source | Type | Repos Fetched | Stars (this sweep) |
|--------|------|---------------|--------------------|
| plurigrid | org | 100 | ~157 |
| kubeflow | org | 48 | ~101,962 |
| bmorphism | user | 100 | ~510 |
| zubyul | user | 49 | ~40 |
| AustinCStone | user | 30 | ~324 |
| migalkin | user | 19 | ~834 |
| wasita | user | 11 | ~11 |
| TeglonLabs | org | 5 | ~14 |
| kristinezheng | user | 5 | 0 |
| M1shaaa | user | 8 | 0 |
| DJedamski | user | 6 | ~17 |
| **TOTAL** | | **381** | **~103,869** |

---

### Top Repos by Stars (from DB)

| Repo | Stars | Language | Pushed At |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,739 | — | 2026-06-18 |
| kubeflow/pipelines | 4,156 | Python | 2026-06-20 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-18 |
| kubeflow/trainer | 2,118 | Go | 2026-06-19 |
| kubeflow/katib | 1,684 | Python | 2026-06-20 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |

### Notable Changes Since 2026-04-12

- **plurigrid/asi** grew from 16 → 26 ⭐ (+10 in ~70 days)
- **kubeflow/kubeflow** grew from 15,565 → 15,739 ⭐ (+174)
- **kubeflow/mcp-apache-spark-history-server** appeared (177 ⭐) — new MCP server for Spark debugging
- **TeglonLabs/jank-crane** is new (2026-06-08) — C++, crane-jank converged-IR hub with GF3 convergence maps
- **bmorphism/Gay.jl** is new — Julia wide-gamut color sampling, 187 open issues
- **plurigrid/gorj** pushed 2026-06-21 (today) — this very sweep

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (A–Z, alice, bob)

**Status: BLOCKED (Vercel authentication gate)**

The Aptos fullnode endpoint `fullnode.mainnet.aptoslabs.com` is gated behind Vercel auth in this execution environment. All 28 Hamming swarm addresses returned `NULL` balance. The addresses and NULL values have been stored in `aptos_snapshots` for tracking.

| World | Address (prefix→suffix) | Balance (APT) |
|-------|------------------------|---------------|
| alice | 0xc793...4cc7b | NULL |
| bob | 0x0a3c...512d5d | NULL |
| A | 0x8699...e9d7a | NULL |
| B | 0x3f89...cb13 | NULL |
| C | 0x38b9...535e | NULL |
| D | 0xf776...cfdd1 | NULL |
| E | 0xdc1d...8d36 | NULL |
| F | 0x18a1...3cf71 | NULL |
| G | 0x69a3...7f32 | NULL |
| H | 0xce67...300f | NULL |
| I | 0x070f...1fc9 | NULL |
| J | 0x4d96...7f54 | NULL |
| K | 0xa732...5dc4 | NULL |
| L | 0x7c2e...eba9 | NULL |
| M | 0x6fed...7f2e9 | NULL |
| N | 0xe7dd...551b2c | NULL |
| O | 0x7325...a89d | NULL |
| P | 0x6218...c948 | NULL |
| Q | 0xac40...c89a9 | NULL |
| R | 0x7ce6...76e10 | NULL |
| S | 0xb875...d0386 | NULL |
| T | 0x3578...f4588 | NULL |
| U | 0x7586...f9956 | NULL |
| V | 0xb59d...af2c3 | NULL |
| W | 0x5f32...c7b0 | NULL |
| X | 0xa95c...3047d | NULL |
| Y | 0xd8e3...444c4 | NULL |
| Z | 0x7af0...197c | NULL |

**Fix needed:** Set `APTOS_API_KEY` env var or use a proxy endpoint in session config.

### Multisig Contract Probes

**Status: BLOCKED (same Vercel auth gate)**

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...7003 | NULL | false |
| A-G | 0xf56c...0096 | NULL | false |
| Y-Z | 0xd3ff...b883 | NULL | false |
| S-T | 0x3b1c...7883 | NULL | false |
| V-W | 0x40fa...eb6d | NULL | false |

### MNX Markets

**Status: UNAVAILABLE**

`testnet.mnx.fi` returns Vercel auth. No market data fetched. `mnx_snapshots` table is empty.

---

## DuckDB Schema (for reference)

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

1. **Aptos/multisig access:** Add `APTOS_API_KEY` or allow-list `fullnode.mainnet.aptoslabs.com` in session network policy.
2. **MNX Markets:** Needs direct API key or alternative endpoint — `testnet.mnx.fi` is Vercel-auth gated.
3. **TeglonLabs/jank-crane** (new 2026-06-08): C++ crane-jank IR hub with GF3 maps — may be relevant to gorj's GF(3) trit coloring infrastructure.
4. **kubeflow/mcp-apache-spark-history-server** (177 ⭐ new): MCP server pattern potentially useful for forj tooling.
