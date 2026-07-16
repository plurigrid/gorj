# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-16

## Sweep Metadata
- **Date:** 2026-07-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Branch:** `world-increment/sweep-2026-07-16-1207`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| World Increments (today) | 245 |
| Repo Snapshots (today) | 245 |
| Total World Increments (all sweeps) | 268 |
| Total Repo Snapshots (all sweeps) | 1,189 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 10 |
| zubyul | user | 10 |
| TeglonLabs | org | 5 |
| migalkin | social-graph | 5 |
| AustinCStone | social-graph | 4 |
| wasita | social-graph | 4 |
| kristinezheng | social-graph | 3 |
| DJedamski | social-graph | 2 |
| M1shaaa | social-graph | 2 |
| **TOTAL** | | **245** |

### Top Repos by Stars (this sweep)
| Repo | Stars | Language | Pushed At |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,779 | — | 2026-07-16 |
| kubeflow/pipelines | 4,167 | Python | 2026-07-16 |
| kubeflow/spark-operator | 3,137 | Python | 2026-07-16 |
| kubeflow/trainer | 2,150 | Go | 2026-07-15 |
| kubeflow/katib | 1,690 | Python | 2026-07-15 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 22 | JavaScript | 2026-01-16 |

### Activity Highlights

**plurigrid** (100 repos):
- **gorj** (this repo) — pushed 2026-07-16, 1199 open issues, active GF(3)+REPL topology work
- **asi** — pushed 2026-07-10, 30★, topological chemputer HTML project
- **eirobri** — EiRoBri replay world (Clojure), pushed 2026-07-14
- **place** — TeX forester docs, pushed 2026-07-14
- **nanoclj-zig** — NaN-boxed Clojure in Zig 0.15 with GF(3) trit conservation

**bmorphism** (100 repos):
- **gay-chat** — `gay://chat` over Spritely Brassica Chat (Scheme), pushed 2026-07-14
- **Gay.jl** — Wide-gamut color sampling, 187 open issues, pushed 2026-07-14
- **satreadout** — Machine-checked saturating non-Riemannian perceptual readout, pushed 2026-06-20
- **ocaml-mcp-sdk** — OCaml SDK for MCP using Jane Street oxcaml_effect (61★)

**zubyul** (10 sampled):
- **voice-observatory** — macOS TUI for voice-download pathways, pushed 2026-04-24
- **ghostel-emacs-worlds** — Ghostty + alice/bob emacs-mods (GLSL), pushed 2026-04-24

**social graph**:
- wasita: wasita.github.io + wm-cv both pushed 2026-07-14 (active)
- AustinCStone: byteruckus (HTML) pushed 2026-07-15 (newest)
- migalkin: kgcourse2021 pushed 2026-07-10 (KG research active)

### GF(3) Color Chain Distribution (245 increments today)
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 81 |
| 1 | PLUS | #b8bb26 | 82 |
| -1 | MINUS | #cc241d | 82 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — 28 Addresses (alice, bob, A–Z)

**Result:** All 28 addresses returned HTTP 404 from `fullnode.mainnet.aptoslabs.com`.

These wallets have no initialized `0x1::coin::CoinStore<AptosCoin>` resource on Aptos mainnet — accounts have not received APT transactions. All stored in `aptos_snapshots` with `balance_apt = NULL`.

| Range | Count | Status |
|-------|-------|--------|
| alice, bob | 2 | 404 — not initialized |
| A through Z | 26 | 404 — not initialized |

### Multisig Contract Probes — 5 Pairs ✓ ALL HEALTHY

Probed via `POST /v1/view → 0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428… | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c… | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181… | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9… | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4… | 2 | ✓ HEALTHY |

All 5 multisig contracts require **2-of-N signatures** and are reachable on mainnet.

### MNX Testnet Markets

`https://testnet.mnx.fi/api/markets` → **401 Unauthorized** (API requires auth token).  
`mnx_snapshots` table is empty for this sweep.

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
