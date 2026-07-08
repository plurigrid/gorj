# World-Increment Sweep + Hamming Snapshot — 2026-07-08

## Sweep Metadata
- **Date:** 2026-07-08
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (Cumulative DB)

| Metric | Value |
|--------|-------|
| Total World Increments | 34 |
| Total Repo Snapshots | 1000 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users (social graph) |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Crawled

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 103 total |
| kubeflow | org | 49 total |
| TeglonLabs | org | 5 total |
| bmorphism | user | 105 total |
| zubyul | user | 49 total |
| migalkin | social graph | 19 total |
| DJedamski | social graph | 6 total |
| wasita | social graph | 11 total |
| kristinezheng | social graph | 5 total |
| M1shaaa | social graph | 8 total |
| AustinCStone | social graph | 40 total |

### Top Repos by Stars (2026-07-08 Snapshot)

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15770 | — | 2026-07-08 |
| kubeflow/pipelines | 4170 | Python | 2026-07-08 |
| kubeflow/spark-operator | 3134 | Python | 2026-07-08 |
| kubeflow/trainer | 2131 | Go | 2026-07-08 |
| kubeflow/katib | 1690 | Python | 2026-07-06 |
| kubeflow/arena | 815 | Go | 2026-07-04 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-02-05 |
| plurigrid/asi | 30 | HTML | 2026-07-07 |
| plurigrid/ontology | 8 | JavaScript | 2026-05-09 |

### Notable New Activity (since last sweep 2026-04-12)

- **plurigrid/gorj**: 1053 open issues (was ~0), pushed 2026-07-07 — Rama/REPL very active
- **plurigrid/asi** grew 16→30 stars, topological chemputer active
- **plurigrid/shrimp**: new repo (2026-07-03) — Jank worked example
- **TeglonLabs/jank-crane**: new (2026-06-08) — crane-jank converged-IR hub with GF3 convergence maps
- **bmorphism/satreadout**: new (2026-06-10) — Lean 4.28 machine-checked saturating readout
- **bmorphism/Gay.jl**: now 187 open issues (was 0), active Julia color SPI dev
- **bmorphism/bci-preview**: new (2026-06-19) — stable redirect for bci.place forester
- **zubyul/voice-observatory**: new (2026-04-24), companion to bmorphism/say-mcp-server
- **kubeflow/kale** now active again (pushed 2026-07-08) — Kubeflow's superfood for Data Scientists
- **kubeflow/sdk**: 123★ new repo (2025-04-23) for universal Python SDK

### GF(3) Color Chain — Latest Increments (IDs 23–34)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 23 | plurigrid | 2 | `#cc241d` | MINUS |
| 24 | kubeflow | 0 | `#d3869b` | ERGODIC |
| 25 | TeglonLabs | 1 | `#b8bb26` | PLUS |
| 26 | bmorphism | 2 | `#cc241d` | MINUS |
| 27 | zubyul | 0 | `#d3869b` | ERGODIC |
| 28 | migalkin | 1 | `#b8bb26` | PLUS |
| 29 | DJedamski | 2 | `#cc241d` | MINUS |
| 30 | wasita | 0 | `#d3869b` | ERGODIC |
| 31 | kristinezheng | 1 | `#b8bb26` | PLUS |
| 32 | M1shaaa | 2 | `#cc241d` | MINUS |
| 33 | AustinCStone | 0 | `#d3869b` | ERGODIC |
| 34 | sweep_complete | 1 | `#b8bb26` | PLUS |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming-swarm addresses queried against Aptos mainnet fullnode.  
**Result:** All addresses return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
Recorded as 0.0 APT — no CoinStore initialized / no APT balance on any address.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C–Z | various | 0.0 × 24 |

### Multisig Contract Probes

5 pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

**All 5/5 multisigs healthy — 2-of-2 threshold confirmed on all pairs.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection active.  
API paths `/api/markets`, `/api/v1/markets`, `/api/tickers` all gate behind Vercel auth.  
mnx_snapshots table empty this run.

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
