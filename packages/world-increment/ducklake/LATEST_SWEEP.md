# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-11  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** 1.5.4  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

GF(3) Chain: `id%3==0` → trit=0 ERGODIC `#d3869b` | `id%3==1` → trit=1 PLUS `#b8bb26` | `id%3==2` → trit=-1 MINUS `#cc241d`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 97 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 105 (100 fetched) |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |
| wasita | user (social graph) | 11 |
| DJedamski | user (social graph) | 6 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| AustinCStone | user (social graph) | 40 |

**61 representative repos stored in world_increments + repo_snapshots tables.**

### Top Repos by Stars

| Repo | Stars | Open Issues | Last Push |
|------|-------|-------------|-----------|
| kubeflow/kubeflow | 15,771 | 0 | 2026-07-10 |
| kubeflow/pipelines | 4,169 | 418 | 2026-07-11 |
| kubeflow/spark-operator | 3,137 | 110 | 2026-07-10 |
| kubeflow/trainer | 2,135 | 144 | 2026-07-10 |
| kubeflow/katib | 1,689 | 110 | 2026-07-10 |
| kubeflow/examples | 1,460 | 111 | 2025-04-14 |
| kubeflow/community-distribution | 1,029 | 31 | 2026-07-09 |
| AustinCStone/TextGAN | 92 | 5 | 2025-03-03 |
| migalkin/NodePiece | 144 | 0 | 2026-05-07 |
| migalkin/StarE | 89 | 1 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | 0 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | 1 | 2026-01-16 |
| plurigrid/asi | 30 | 4 | 2026-07-10 |

### Notable Activity (Pushed TODAY — 2026-07-11)

- **plurigrid/gorj** (this repo): 1,119 open issues — Rama topology nREPL routing + GF(3)
- **bmorphism/Gay.jl**: 187 open issues — core GF(3) wide-gamut color project
- **kubeflow/pipelines**: 418 open issues — active ML infrastructure
- **kubeflow/notebooks**: 180 open issues — Kubernetes notebook environment

### New / Notable Repos Since Last Sweep (April 2026)

- `TeglonLabs/jank-crane` (C++, 2026-06-08) — jank converged-IR hub with GF3 convergence maps
- `bmorphism/satreadout` (HTML/Lean, 2026-06-20) — machine-checked saturating perceptual readout
- `zubyul/voice-observatory` (Python, 2026-04-24) — companion to bmorphism/say-mcp-server
- `plurigrid/eirobri` (Clojure, 2026-06-30) — EiRoBri replay world, 30 issues
- `kubeflow/mcp-server` (Python, 20★) — AI-assisted dev with Kubeflow Tools
- `kubeflow/mcp-apache-spark-history-server` (Python, 182★) — Spark debug from AI agents

### GF(3) Increment Sample (first 12)

| ID | Source | Repo | GF3 Trit | Color | Name |
|----|--------|------|----------|-------|------|
| 1 | plurigrid | asi | +1 | `#b8bb26` | PLUS |
| 2 | plurigrid | gorj | -1 | `#cc241d` | MINUS |
| 3 | plurigrid | shrimp | 0 | `#d3869b` | ERGODIC |
| 4 | plurigrid | place | +1 | `#b8bb26` | PLUS |
| 5 | plurigrid | eirobri | -1 | `#cc241d` | MINUS |
| 6 | plurigrid | nash-portal | 0 | `#d3869b` | ERGODIC |
| 7 | plurigrid | zig-syrup | +1 | `#b8bb26` | PLUS |
| 8 | plurigrid | asi-skills | -1 | `#cc241d` | MINUS |
| 9 | plurigrid | nanoclj-zig | 0 | `#d3869b` | ERGODIC |
| 10 | plurigrid | ontology | +1 | `#b8bb26` | PLUS |
| 11 | plurigrid | microworlds | -1 | `#cc241d` | MINUS |
| 12 | plurigrid | vcg-auction | 0 | `#d3869b` | ERGODIC |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 addresses returned 0.0 APT** — addresses have no registered APT CoinStore resource. Addresses may hold other assets or are pre-funded via alternative mechanisms.

| Range | Count | Total APT |
|-------|-------|-----------|
| alice, bob | 2 | 0.0 |
| A–Z (26 worlds) | 26 | 0.0 |
| **Total** | **28** | **0.0** |

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | **2** | ✓ healthy |
| A-G | 0xf56c4a1c... | **2** | ✓ healthy |
| Y-Z | 0xd3ffe181... | **2** | ✓ healthy |
| S-T | 0x3b1c3ae9... | **2** | ✓ healthy |
| V-W | 0x40fad7b4... | **2** | ✓ healthy |

**All 5 multisig contracts healthy — uniform 2-of-2 threshold across all pairs.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection active (visitor password required). No market data extracted. `mnx_snapshots` table is empty for this sweep.

---

## DuckDB Table Summary

```
world_increments  : 61 rows  (GF3-colored repo push events)
repo_snapshots    : 61 rows  (org/user → repo metadata)
aptos_snapshots   : 28 rows  (Hamming swarm APT balances)
multisig_probes   :  5 rows  (2-of-2 on all 5 pairs)
mnx_snapshots     :  0 rows  (Vercel auth-gated)
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
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
