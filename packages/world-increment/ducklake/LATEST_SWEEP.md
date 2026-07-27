# World Increment + Hamming Swarm Snapshot — 2026-07-27

## Sweep Metadata
- **Date:** 2026-07-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 83 |
| Total Repo Snapshots (cumulative) | 1,004 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried This Run
| Source | Type | Total Repos | Stars |
|--------|------|-------------|-------|
| kubeflow | org | 49 (sampled 13) | ~82k |
| plurigrid | org | 103 | 153 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 106 | 355 |
| zubyul | user | 49 | 27 |
| migalkin | user | 19 | 821 |
| wasita | user | 12 | 10 |
| kristinezheng | user | 5 | 0 |
| AustinCStone | user | 41 | 319 |
| DJedamski | user | 6 | 15 |
| M1shaaa | user | 8 | 0 |

### Top Active Repos (by pushed_at)

**plurigrid/gorj** — Clojure, pushed 2026-07-27, ⭐1, 🐛1444
→ forj + Rama topology nREPL routing + GF(3) gay trit coloring

**bmorphism/Gay.jl** — Julia, pushed 2026-07-27, ⭐2, 🐛188
→ Wide-gamut color sampling with splittable determinism (Pigeons.jl SPI)

**kubeflow/pipelines** — Python, pushed 2026-07-27, ⭐4171, 🍴2067
→ Machine Learning Pipelines for Kubeflow

**kubeflow/mcp-server** — Python, pushed 2026-07-27, ⭐29
→ MCP Server for AI-Assisted Development with Kubeflow Tools

**wasita/wasita.github.io** — Svelte, pushed 2026-07-21, 🐛8
→ personal website (SvelteKit + Tailwind)

**plurigrid/eirobri** — Clojure, pushed 2026-07-21, 🐛31
→ EiRoBri replay world

**zubyul/from-possible-worlds** — TeX, pushed 2026-07-18
→ active paper/book project

**bmorphism/gay-chat** — Scheme, pushed 2026-07-14
→ gay://chat operationalization over Spritely Brassica Chat

**migalkin/kgcourse2021** — HTML, pushed 2026-07-10, ⭐24
→ Knowledge Graphs course (Russian-language)

**plurigrid/asi** — HTML, pushed 2026-07-10, ⭐52
→ everything is topological chemputer!

### GF(3) Color Chain (this run — 60 new repo increments)

| Trit | Color | Name | Count (this run) |
|------|-------|------|-----------------|
| 0 | #d3869b | ERGODIC | 22 |
| +1 | #b8bb26 | PLUS | 24 |
| -1 | #cc241d | MINUS | 24 |

Chain rule: `id mod 3 == 0 → ERGODIC | 1 → PLUS | 2 → MINUS`

### Notable Repos
- **bmorphism/ocaml-mcp-sdk** (OCaml, ⭐61) — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **migalkin/NodePiece** (Python, ⭐144) — Compositional KG embeddings (ICLR 2022)
- **migalkin/StarE** (Python, ⭐89) — Message Passing for Hyper-Relational KGs (EMNLP 2020)
- **AustinCStone/TextGAN** (Python, ⭐92) — GAN for text generation in TensorFlow
- **bmorphism/anti-bullshit-mcp-server** (JS, ⭐22) — Claims analysis MCP server
- **TeglonLabs/jank-crane** (C++, 2026-06-08) — crane-jank converged-IR hub with GF3 convergence maps
- **zubyul/nash-tui** (Rust) — NASH token TUI: real-time candles + GeckoTerminal OHLCV

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All wallets queried against `fullnode.mainnet.aptoslabs.com`.

| World | Address (last 8 chars) | APT Balance |
|-------|------------------------|-------------|
| alice | ...24cc7b | 0.0 APT |
| bob | ...12d5 | 0.0 APT |
| A | ...ebe9d7a | 0.0 APT |
| B | ...577cb13 | 0.0 APT |
| C | ...691535e | 0.0 APT |
| D | ...fcfdd1 | 0.0 APT |
| E | ...0958d36 | 0.0 APT |
| F | ...74c3cf71 | 0.0 APT |
| G | ...dbcc7f32 | 0.0 APT |
| H | ...4e5300f | 0.0 APT |
| I | ...fc00c1fc9 | 0.0 APT |
| J | ...293e87f54 | 0.0 APT |
| K | ...7a425dc4 | 0.0 APT |
| L | ...6337eba9 | 0.0 APT |
| M | ...b49b7f2e9 | 0.0 APT |
| N | ...9a11551b2c | 0.0 APT |
| O | ...4a525a89d | 0.0 APT |
| P | ...13621ec948 | 0.0 APT |
| Q | ...525e5c89a9 | 0.0 APT |
| R | ...6d76e10 | 0.0 APT |
| S | ...bf99d0386 | 0.0 APT |
| T | ...5f2d3f4588 | 0.0 APT |
| U | ...f395ef9956 | 0.0 APT |
| V | ...8a89af2c3 | 0.0 APT |
| W | ...6ccc7b0 | 0.0 APT |
| X | ...2cbe33047d | 0.0 APT |
| Y | ...0fa2444c4 | 0.0 APT |
| Z | ...6e4e197c | 0.0 APT |

**Status:** All 28 accounts return 0 APT. CoinStore resource not initialized on mainnet —
consistent with prior sweeps. Addresses are registered stubs not yet funded.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

All 5 multisig contracts respond to `0x1::multisig_account::num_signatures_required`
with `2`. **All healthy — 2-of-N signing threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

- Endpoint `https://testnet.mnx.fi` is a Next.js SPA.
- `/api/markets` and `/api/v1/markets` return HTML shell, not JSON.
- Market data requires browser JS execution — not accessible via unauthenticated REST.
- **Status: Unavailable** — noting as SPA with no REST API probe endpoint.

---

## DuckDB Schema (world-increments.duckdb)

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

Database is **append-only** — rows accumulate across sweeps for temporal analysis.
