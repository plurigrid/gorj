# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-02

## Sweep Metadata
- **Date:** 2026-05-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment ID:** 13 · GF(3) trit=1 · **PLUS** · `#b8bb26`
- **Branch:** `world-increment/sweep-2026-05-02-0029`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 25 (max id=13) |
| Total Repo Snapshots | 945 |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Snapshots | 0 (SPA, no JSON API) |

---

## JOB 1: GitHub Social Graph Sweep

### Coverage This Run
- **plurigrid/gorj** — snapshotted via MCP (last push 2026-04-14T18:07:32Z)
- **plurigrid, kubeflow, TeglonLabs** (orgs) — GitHub unauthenticated API rate-limited; `gh` CLI not installed in environment
- **bmorphism, zubyul** (users) — same rate-limit constraint
- **Zubyul social graph** (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone) — same constraint

> Prior sweeps (IDs 1–12, 2026-04-07 through 2026-04-14) captured 944 snapshots across all 11 sources. Re-sweeping requires authenticated GitHub access.

### GF(3) Color Chain — All 13 Increments

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
| 12 | bmorphism (org) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |
| **13** | **world-increment-sweep** | **sweep_complete** | **+1** | **`#b8bb26`** | **PLUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

### Top Repos by Source (from prior sweeps)

| Source | Type | Repos | Notable |
|--------|------|-------|---------|
| plurigrid | org | 100 | asi (16★), zig-syrup, vivarium |
| bmorphism | user | 100 | ocaml-mcp-sdk (60★), anti-bullshit-mcp-server |
| TeglonLabs | org | 53 | mathpix-gem, vibespace |
| kubeflow | org | 47 | kubeflow (15565★), pipelines (4119★) |
| AustinCStone | user | 43 | TextGAN (92★) |
| migalkin | user | 30 | NodePiece (143★), StarE (88★) |
| wasita | user | 29 | — |
| zubyul | user | 24 | — |
| kristinezheng | user | 18 | — |
| M1shaaa | user | 16 | — |
| DJedamski | user | 11 | — |
| **TOTAL** | | **471** | (prior) + 1 gorj (this sweep) = 472 confirmed |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 wallets queried against `fullnode.mainnet.aptoslabs.com` (1s sleep between calls).  
All accounts returned **0.0 APT** — `CoinStore<AptosCoin>` resource absent or zero balance.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Total APT across swarm: 0.0**

### Multisig Contract Probes

All 5 probed via `POST /v1/view → 0x1::multisig_account::num_signatures_required`. All **healthy**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**5/5 multisig contracts healthy. All require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` serves a Next.js SPA. Probed `/api/markets` and `/api/v1/markets` — both return HTML (no JSON API). Market data requires client-side JS execution. `mnx_snapshots` table empty this sweep.

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

## Notable Highlights (cumulative)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — ML pipeline framework (pushed 2026-04-10)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer
- **Increment 13**: PLUS — opens the 5th GF(3) cycle; first Hamming swarm snapshot
