# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-05-16  
**Sweep ID:** 13  
**GF(3):** trit=1 → **PLUS** `#b8bb26`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Targeted

| Source | Type | Notes |
|--------|------|-------|
| plurigrid | org | gorj, asi + ~100 repos |
| kubeflow | org | kubeflow, pipelines, spark-operator, trainer, katib |
| TeglonLabs | org | topologies |
| bmorphism | user | Gay.jl, ocaml-mcp-sdk, oxgame + ~100 repos |
| zubyul | user | active committer on gorj |
| migalkin | user | NodePiece (ICLR 2022) |
| DJedamski | user | social graph node |
| wasita | user | social graph node |
| kristinezheng | user | social graph node |
| M1shaaa | user | social graph node |
| AustinCStone | user | TextGAN |

> **Note:** Unauthenticated GitHub API rate-limited (60 req/hr). MCP tools scoped to `plurigrid/gorj`. Social graph nodes captured as sweep_note events with known star counts from prior sweeps. gorj repo snapshot captured via MCP commits API (20 recent commits).

### Notable Activity (2026-05-16)

- `plurigrid/gorj` (Clojure) — pushed 2026-05-08, 217 open issues, 9 open sweep PRs today (#499–#507)
- `bmorphism/Gay.jl` (Julia) — pushed 2026-05-16 00:32 UTC, 188 open issues
- `bmorphism/oxgame` (OCaml) — pushed 2026-05-15, open-game composition for OxCaml
- `bmorphism/ocaml-mcp-sdk` (OCaml) — 61 stars, Jane Street oxcaml_effect
- `kubeflow/kubeflow` — 15,636 stars, active ML-on-Kubernetes toolkit
- `migalkin/NodePiece` — 144 stars, ICLR 2022 compositional KG embeddings

### DuckDB State (post-sweep)

| Table | Rows |
|-------|------|
| world_increments | 42 (ids 1–13) |
| repo_snapshots | 957 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA) |

### GF(3) Color Chain — Sweep #13

| Trit | Name | Color | Count (cumulative) |
|------|------|-------|-------------------|
| 0 | ERGODIC | `#d3869b` | 7 |
| +1 | PLUS | `#b8bb26` | 27 |
| -1 | MINUS | `#cc241d` | 8 |

**Sweep #13 = PLUS** (13 mod 3 = 1 → trit=+1 → `#b8bb26`)

### Historical GF(3) Assignment Rule

```
id mod 3 == 0  →  trit=0,  ERGODIC  #d3869b
id mod 3 == 1  →  trit=+1, PLUS     #b8bb26
id mod 3 == 2  →  trit=-1, MINUS    #cc241d
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets (alice, bob, A–Z) queried against `fullnode.mainnet.aptoslabs.com` at ledger version ~5,300,448,576.

**Result: All 0.0 APT** — `CoinStore<AptosCoin>` resource not found on any address. Accounts exist on-chain but have no native APT coin store registered (using Fungible Assets framework or accounts are unfunded).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**5/5 contracts healthy** — all require 2-of-N signatures on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Next.js SPA returns HTML on all API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`). No machine-readable JSON surface accessible without JavaScript execution. `mnx_snapshots` table: 0 rows.

---

## Infrastructure

- **DuckDB:** v1.5.2 (Variegata)
- **DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos fullnode:** `fullnode.mainnet.aptoslabs.com` (ledger ~5.3B)
- **Sweep timestamp:** 2026-05-16 22:05 UTC

## Schema Reference

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
