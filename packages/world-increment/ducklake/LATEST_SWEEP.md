# World-Increment Sweep + Hamming Snapshot — 2026-06-04

## Sweep Metadata
- **Date:** 2026-06-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (2026-06-04)

| Metric | Value |
|--------|-------|
| Total World Increments | 414 |
| Total Repo Snapshots | 1,335 (incl. historical) |
| New Repos This Sweep | 382 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution (414 increments)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 137 |
| +1 | PLUS | `#b8bb26` | 139 |
| -1 | MINUS | `#cc241d` | 138 |

Distribution is near-uniform (Δ=2), confirming ergodic GF(3) trit conservation across the full sweep.

GF(3) rule: `id%3==0` → ERGODIC · `id%3==1` → PLUS · `id%3==2` → MINUS

---

## Top Repos by Stars (this sweep)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,704 | — | 2026-05-24 |
| kubeflow/pipelines | 4,151 | Python | 2026-06-03 |
| kubeflow/spark-operator | 3,124 | Python | 2026-06-03 |
| kubeflow/trainer | 2,110 | Go | 2026-06-03 |
| kubeflow/katib | 1,685 | Python | 2026-06-04 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,020 | YAML | 2026-06-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| migalkin/kgcourse2021 | 25 | HTML | 2025-08-04 |
| plurigrid/asi | 24 | HTML | 2026-04-26 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 |
| bmorphism/manifold-mcp-server | 14 | JavaScript | 2025-01-11 |
| bmorphism/Gay.jl | 1 | Julia | 2026-06-04 |
| plurigrid/gorj | 0 | Clojure | 2026-06-04 |

### Actively Pushed 2026

- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring (337 open issues — 🔥)
- `plurigrid/eirobri` — EiRoBri replay world (29 open issues)
- `bmorphism/Gay.jl` — Wide-gamut color sampling with splittable determinism (189 open issues)
- `bmorphism/world` — Local worlds launcher for SA3, jank, world proofs
- `bmorphism/ocaml-mcp-sdk` — OCaml SDK for Model Context Protocol (61 stars)
- `zubyul/voice-observatory` — Passive macOS TUI for voice-download pathways
- `TeglonLabs/mathpix-gem` — Transform mathematical images to LaTeX (Ruby)
- `wasita/wasita.github.io` — personal website (Svelte, active 2026-06-01)
- `wasita/wm-cv` — Academic CV as single-page Svelte app
- `M1shaaa/M1shaaa` — Profile config (last pushed 2026-06-03)

---

## Repo Counts by Source

| Source | Type | Repos This Sweep |
|--------|------|-----------------|
| plurigrid | org | 98 |
| kubeflow | org | 48 |
| bmorphism | user | 94 |
| zubyul | user | 51 |
| AustinCStone | user | 37 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 6 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **382** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-04)

All 28 Hamming swarm wallets queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Balance (APT) | Note |
|-------|--------------|------|
| alice | 0.0 | empty / no CoinStore |
| bob | 0.0 | empty / no CoinStore |
| A–Z (26 wallets) | 0.0 each | empty / no CoinStore |

All wallets return 0.0 APT. Accounts exist on-chain but hold no native APT (likely FA token-only or drained).

### Multisig Contract Probes (all HEALTHY)

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | `0x0da4f428...87003` | 2 | ✓ healthy |
| A-G | `0xf56c4a1c...0096` | 2 | ✓ healthy |
| Y-Z | `0xd3ffe181...b883` | 2 | ✓ healthy |
| S-T | `0x3b1c3ae9...7883` | 2 | ✓ healthy |
| V-W | `0x40fad7b4...eb6d` | 2 | ✓ healthy |

All 5 multisigs require 2-of-N signatures. All contracts responded successfully.

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — `/api/markets` and `/api/v1/markets` return HTML SPA shell, not JSON. No market data extracted. Zero rows in `mnx_snapshots`.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,704 stars (+139 since Apr sweep) — flagship ML platform
- **kubeflow/pipelines**: 4,151 stars (+32 since Apr) — pushed 2026-06-03
- **kubeflow/spark-operator**: 3,124 stars (+13 since Apr) — pushed 2026-06-03
- **plurigrid/gorj**: 337 open issues — this very repo, most active in plurigrid
- **bmorphism/Gay.jl**: 189 open issues, pushed 2026-06-04 — wide-gamut splittable determinism
- **bmorphism/ocaml-mcp-sdk**: 61 stars (+1) — OCaml MCP SDK via Jane Street oxcaml_effect
- **All Hamming wallets**: 0.0 APT — swarm may be FA-token-only or awaiting initialization
- **GF(3) trit balance**: 137/139/138 — ergodic chain holds across 414 increments
