# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-30

## Sweep Metadata
- **Date:** 2026-07-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Total on GitHub |
|--------|------|---------------|-----------------|
| plurigrid | org | 12 | 103 |
| kubeflow | org | 13 | 49 |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 6 | 106 |
| zubyul | user | 6 | 49 |
| migalkin | user (social) | 5 | 19 |
| wasita | user (social) | 4 | 12 |
| AustinCStone | user (social) | 3 | 41 |
| DJedamski | user (social) | 2 | 6 |
| kristinezheng | user (social) | 2 | 5 |
| M1shaaa | user (social) | 2 | 8 |
| **TOTAL** | | **58** | |

### Top Repos by Stars

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,796 | — | 2026-07-10 |
| kubeflow/pipelines | 4,171 | Python | 2026-07-29 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-29 |
| kubeflow/trainer | 2,162 | Go | 2026-07-30 |
| kubeflow/katib | 1,694 | Python | 2026-07-26 |
| kubeflow/examples | 1,461 | Jsonnet | 2025-04-14 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |

### Notable Activity (last 7 days, vs prior sweep 2026-04-12)

| Repo | Change | Note |
|------|--------|------|
| kubeflow/kubeflow | +231 ★ | 15,565 → 15,796 |
| kubeflow/pipelines | +52 ★ | 4,119 → 4,171 |
| kubeflow/spark-operator | +31 ★ | 3,111 → 3,142 |
| kubeflow/trainer | +82 ★ | 2,080 → 2,162 |
| plurigrid/asi | +40 ★ | 16 → 56 (big jump) |
| bmorphism/Gay.jl | — | 188 open issues; 106 total repos |
| plurigrid/gorj | — | 1,502 open issues; pushed 2026-07-30 |
| TeglonLabs/jank-crane | NEW | C++ GF3 convergence maps; pushed 2026-06-08 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 19 |
| 1 | `#b8bb26` | PLUS | 20 |
| -1 | `#cc241d` | MINUS | 19 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried 28 addresses (alice, bob, A–Z) via `https://fullnode.mainnet.aptoslabs.com`.

**Result: All 28 wallets = 0.0 APT** — addresses appear unfunded on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B | 0x3f89…b13 | 0.0 |
| C | 0x38b9…35e | 0.0 |
| D | 0xf776…fdd1 | 0.0 |
| E | 0xdc1d…d36 | 0.0 |
| F | 0x18a1…f71 | 0.0 |
| G | 0x69a3…f32 | 0.0 |
| H | 0xce67…00f | 0.0 |
| I | 0x070f…fc9 | 0.0 |
| J | 0x4d96…f54 | 0.0 |
| K | 0xa732…dc4 | 0.0 |
| L | 0x7c2e…ba9 | 0.0 |
| M | 0x6fed…2e9 | 0.0 |
| N | 0xe7dd…b2c | 0.0 |
| O | 0x7325…89d | 0.0 |
| P | 0x6218…948 | 0.0 |
| Q | 0xac40…89a9 | 0.0 |
| R | 0x7ce6…e10 | 0.0 |
| S | 0xb875…386 | 0.0 |
| T | 0x3578…588 | 0.0 |
| U | 0x7586…956 | 0.0 |
| V | 0xb59d…2c3 | 0.0 |
| W | 0x5f32…7b0 | 0.0 |
| X | 0xa95c…47d | 0.0 |
| Y | 0xd8e3…44c4 | 0.0 |
| Z | 0x7af0…97c | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts healthy — each requires **2-of-2 signatures**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…003 | 2 | ✓ |
| A-G | 0xf56c…096 | 2 | ✓ |
| Y-Z | 0xd3ff…883 | 2 | ✓ |
| S-T | 0x3b1c…883 | 2 | ✓ |
| V-W | 0x40fa…b6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no public REST API.** `https://testnet.mnx.fi` is a Next.js single-page application. Neither `/api/markets` nor `/api/v1/markets` returned structured data. `mnx_snapshots` table is empty this run.

---

## DuckDB Schema + Row Counts

```
world_increments   — 58 rows   (GF3-colored increment events)
repo_snapshots     — 58 rows   (GitHub repo snapshots)
aptos_snapshots    — 28 rows   (Hamming swarm wallet balances, all 0.0 APT)
multisig_probes    —  5 rows   (2-of-2 sigs, all healthy)
mnx_snapshots      —  0 rows   (SPA, no API data available)
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
