# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-18  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.4  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Stored |
|--------|------|-------------|
| plurigrid | org | 50 |
| kubeflow | org | 15 |
| TeglonLabs | org | 5 |
| bmorphism | user | 13 |
| zubyul | user | 8 |
| migalkin | user (social) | 5 |
| DJedamski | user (social) | 3 |
| wasita | user (social) | 4 |
| kristinezheng | user (social) | 2 |
| M1shaaa | user (social) | 3 |
| AustinCStone | user (social) | 4 |

**Total world_increments inserted:** 112  
**Total repo_snapshots inserted:** 112

### GF(3) Color Chain
- `id%3==0` → trit=0 **ERGODIC** `#d3869b`
- `id%3==1` → trit=1 **PLUS** `#b8bb26`
- `id%3==2` → trit=-1 **MINUS** `#cc241d`

GF(3) assignment rule: `id mod 3 == 0 → ERGODIC, id mod 3 == 1 → PLUS, id mod 3 == 2 → MINUS`

### Notable Highlights

#### Most Active (pushed today, 2026-07-18)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| plurigrid/gorj | Clojure | 1 | 08:14 UTC |
| zubyul/from-possible-worlds | TeX | 0 | 07:34 UTC |
| kubeflow/sdk | Python | 125 | 03:01 UTC |
| kubeflow/trainer | Go | 2151 | 02:23 UTC |
| kubeflow/website | HTML | 184 | 02:07 UTC |

#### Top Stars in Sweep
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15780 | — |
| kubeflow/pipelines | 4168 | Python |
| kubeflow/spark-operator | 3138 | Python |
| kubeflow/trainer | 2151 | Go |
| kubeflow/katib | 1691 | Python |
| kubeflow/examples | 1460 | Jsonnet |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 31 | HTML |

#### New Since Last Sweep
- `TeglonLabs/jank-crane` (2026-06-08) — C++, crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps
- `plurigrid/gorj` — 1236 open issues (active!)
- `kubeflow/mcp-apache-spark-history-server` — 183★, new MCP server for Spark History

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-18)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A | 0x8699...9d7a | 0.0 |
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
| Q | 0xac40...9a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Summary:** All 28 Hamming-swarm wallets show **0 APT** balance on mainnet. Wallets may be unfunded, hold non-APT tokens, or operate on a separate environment.

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ Healthy |
| A-G | 0xf56c...096 | 2 | ✅ Healthy |
| Y-Z | 0xd3ff...883 | 2 | ✅ Healthy |
| S-T | 0x3b1c...883 | 2 | ✅ Healthy |
| V-W | 0x40fa...b6d | 2 | ✅ Healthy |

All 5 multisig contracts are **healthy** — all require 2-of-N signatures.

### MNX Markets

`https://testnet.mnx.fi` — **UNAVAILABLE**  
Site is behind Vercel deployment protection (authentication required). No market data could be extracted. `mnx_snapshots` table remains empty.

---

## DuckDB Tables Summary

| Table | Rows | Notes |
|-------|------|-------|
| world_increments | 112 | GF(3) colored repo push events |
| repo_snapshots | 112 | Full repo metadata |
| aptos_snapshots | 28 | alice + bob + A–Z, all 0 APT |
| multisig_probes | 5 | All healthy, 2-sig threshold |
| mnx_snapshots | 0 | Unavailable (Vercel auth) |

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
