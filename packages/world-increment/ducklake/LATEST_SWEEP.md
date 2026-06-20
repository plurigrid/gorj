# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-20T10:30:00Z  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d (18/18/18 split)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept
| Source | Type | Notable Repos | Latest Push |
|--------|------|---------------|-------------|
| plurigrid | org | gorj, place, eirobri, asi | 2026-06-20 |
| kubeflow | org | pipelines (4155★), kubeflow (15736★), trainer | 2026-06-20 |
| TeglonLabs | org | jank-crane (GF3+C++) | 2026-06-08 |
| bmorphism | user | Gay.jl, satreadout, ocaml-mcp-sdk (61★) | 2026-06-20 |
| zubyul | user | voice-observatory, nash-tui, gay-world | 2026-04-24 |
| migalkin | social graph | NodePiece (144★), StarE (89★) | 2025-08-04 |
| wasita | social graph | wasita.github.io, magic-garden | 2026-06-19 |
| AustinCStone | social graph | TextGAN (92★), EpsteinSearch | 2026-02-11 |
| kristinezheng | social graph | kristinezheng.github.io | 2026-06-07 |
| M1shaaa | social graph | M1shaaa (profile), lab-bookshelf | 2026-06-20 |
| DJedamski | social graph | (no public repos found) | — |

### Hot Repos Pushed 2026-06-20
- **plurigrid/gorj** `Clojure` — forj + Rama topology nREPL routing + GF(3) gay trit coloring (693 open issues)
- **plurigrid/place** `TeX` — 9 open issues
- **bmorphism/satreadout** `HTML` — Machine-checked saturating non-Riemannian perceptual readout
- **bmorphism/Gay.jl** `Julia` — Wide-gamut color sampling with splittable determinism (187 open issues)
- **kubeflow/pipelines** `Python` — 4155 stars, 450 open issues
- **kubeflow/dashboard** `TypeScript` — Kubeflow Central Dashboard
- **M1shaaa/M1shaaa** — profile repo, pushed today

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15736 | — |
| kubeflow/pipelines | 4155 | Python |
| kubeflow/spark-operator | 3127 | Python |
| kubeflow/trainer | 2118 | Go |
| kubeflow/katib | 1683 | Python |
| kubeflow/arena | 813 | Go |
| kubeflow/mcp-apache-spark-history-server | 177 | Python |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 26 | HTML |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |

### GF(3) Increment Distribution (54 new increments this sweep)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 18 |
| +1 | `#b8bb26` | PLUS | 18 |
| -1 | `#cc241d` | MINUS | 18 |

### DuckDB Tables
- `world_increments`: 77 total rows (54 new this sweep)
- `repo_snapshots`: 998 total rows (54 new this sweep; 944 from prior sweeps)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
**Sweep timestamp:** 2026-06-20T10:20:00Z  
**Ledger version:** ~5,831,256,123  
**Method:** `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

> **Result:** All 28 hamming world addresses return `resource_not_found` for native APT CoinStore. These accounts either hold FA-standard tokens or are not initialized with APT.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I–Z (18 addrs) | various | 0.0 |

### Multisig Contract Probes
**Method:** `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

All 5 multisig contracts healthy — each requires 2-of-N signatures.

### MNX Markets (`testnet.mnx.fi`)
**Status:** UNAVAILABLE — Vercel deployment protection (HTTP 401). No bypass token available.

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

---

## Run Summary

| Job | Status | Notes |
|-----|--------|-------|
| GitHub sweep (3 orgs) | COMPLETE | kubeflow most active (pipelines+dashboard pushed today) |
| GitHub sweep (2 users) | COMPLETE | bmorphism Gay.jl + satreadout pushed today |
| GitHub social graph (6 users) | COMPLETE | migalkin/NodePiece 144 stars top find |
| Aptos balances (28 addrs) | COMPLETE | All 0 APT — no CoinStore registered |
| Multisig probes (5 contracts) | COMPLETE | All healthy, 2-of-N sigs |
| MNX Markets | BLOCKED | Vercel auth required (HTTP 401) |
| DuckDB persist | COMPLETE | packages/world-increment/ducklake/world-increments.duckdb |
