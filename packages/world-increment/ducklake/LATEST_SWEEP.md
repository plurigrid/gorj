# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-14

## Sweep Metadata
- **Date:** 2026-06-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 210 |
| Total Repo Snapshots (this run) | 187 |
| Sources Covered | 3 orgs + 2 users + 6 social graph |

### Sources Snapshotted

| Source | Type | Repos Sampled | Top Repo |
|--------|------|--------------|----------|
| plurigrid | org | 48 | plurigrid/* |
| kubeflow | org | 100 | kubeflow/pipelines (⭐4154) |
| TeglonLabs | org | 5 | TeglonLabs/jank-crane |
| bmorphism | user | 100+ | bmorphism/ocaml-mcp-sdk (⭐61) |
| zubyul | user | 49 | zubyul/gay-world |
| migalkin | social graph | 19 | migalkin/NodePiece (⭐144) |
| DJedamski | social graph | 6 | DJedamski/kaggle_ncaa18 |
| wasita | social graph | 11 | wasita/wasita.github.io |
| kristinezheng | social graph | 5 | kristinezheng/kristinezheng.github.io |
| M1shaaa | social graph | 8 | M1shaaa/lab-bookshelf- |
| AustinCStone | social graph | 40 | AustinCStone/TextGAN (⭐92) |

### Notable Activity (2026-06-14 window)
- `bmorphism/satreadout` — NEW: Lean 4.28 machine-checked saturating perceptual readout (pushed 2026-06-10)
- `bmorphism/Gay.jl` — Wide-gamut color sampling, 189 open issues (pushed 2026-06-10)
- `bmorphism/nanoclj-zig` — Zig NanoClj interpreter (pushed 2026-06-10)
- `bmorphism/babashka-mcp-server` — ⭐19, active (pushed 2026-06-05)
- `TeglonLabs/jank-crane` — NEW: crane-jank converged-IR hub with GF3 convergence maps (pushed 2026-06-08)
- `wasita/wasita.github.io` — personal site, 8 open issues (pushed 2026-06-01)
- `kristinezheng/kristinezheng.github.io` — updated 2026-06-07
- `kubeflow/pipelines` — ⭐4154, pushed 2026-06-14 (active)
- `kubeflow/trainer` — ⭐2115, pushed 2026-06-14 (active)
- `zubyul/voice-observatory` — macOS TUI voice-download observer (pushed 2026-04-24)

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 70 |
| +1 | #b8bb26 | PLUS | 70 |
| -1 | #cc241d | MINUS | 70 |

GF(3) rule: `id%3==0 → ERGODIC(#d3869b) | id%3==1 → PLUS(#b8bb26) | id%3==2 → MINUS(#cc241d)`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet)

All 28 Hamming swarm addresses (alice, bob, A–Z) returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. The accounts exist in the swarm mapping but have **no APT CoinStore registered** on Aptos mainnet at ledger version 5736253541.

**Status:** All 28 wallets → **0.00 APT** (CoinStore not initialized)

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.00 |
| bob   | 0x0a3c...512d | 0.00 |
| A–Z   | 0x8699...–0x7af0... | 0.00 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts responded, each requiring **2-of-N signatures**:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

**5/5 contracts live on Aptos mainnet. No anomalies.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection (password authentication required). No market data extractable without bypass token.

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)  -- 0 rows (unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/pipelines**: ⭐4,154 — active ML pipeline platform (pushed 2026-06-14)
- **migalkin/NodePiece**: ⭐144 — scalable KG embeddings, ICLR'22
- **bmorphism/ocaml-mcp-sdk**: ⭐61 — OCaml MCP SDK using Jane Street oxcaml_effect
- **AustinCStone/TextGAN**: ⭐92 — text generation GAN (2016, still referenced)
- **bmorphism/satreadout**: NEW Lean 4.28 perceptual readout proof (2026-06-10)
- **TeglonLabs/jank-crane**: NEW crane-jank IR hub with GF3 convergence maps (2026-06-08)
- **Multisig health**: All 5 Hamming-pair contracts live with 2-sig threshold
- **Hamming wallets**: All 28 at 0 APT — swarm accounts uninitialized on mainnet
