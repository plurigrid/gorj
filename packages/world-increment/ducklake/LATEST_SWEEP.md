# LATEST_SWEEP — 2026-06-01 20:13 UTC

## JOB 1: GitHub Social Graph Sweep

**Timestamp:** 2026-06-01 20:13 UTC  
**Total repos snapshotted:** 342  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

### Sources

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 101 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 102 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 5 |
| kristinezheng | user (social) | 3 |
| M1shaaa | user (social) | 3 |
| AustinCStone | user (social) | 5 |

### Notable Repos (by stars)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15700 | — | 2026-05-24 |
| kubeflow/pipelines | 4151 | Python | 2026-06-01 |
| kubeflow/spark-operator | 3125 | Python | 2026-06-01 |
| kubeflow/trainer | 2109 | Go | 2026-05-30 |
| kubeflow/katib | 1685 | Python | 2026-05-29 |
| kubeflow/examples | 1462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1019 | YAML | 2026-05-29 |
| kubeflow/arena | 811 | Go | 2026-05-07 |
| kubeflow/kale | 691 | Python | 2026-05-29 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 23 | HTML | 2026-04-26 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2025-01-07 |
| bmorphism/babashka-mcp-server | 18 | JavaScript | 2025-01-05 |
| bmorphism/manifold-mcp-server | 14 | JavaScript | 2025-01-11 |
| plurigrid/vcg-auction | 7 | Rust | 2023-03-16 |

### Recent Activity Highlights

- **plurigrid/gorj** (this repo): 292 open issues, pushed 2026-06-01 — forj + GF(3) trit coloring
- **plurigrid/eirobri**: 28 open issues — EiRoBri replay world
- **bmorphism/Gay.jl**: Wide-gamut color sampling, active 2026-06-01
- **zubyul/voice-observatory**: Passive macOS TUI, pushed 2026-04-24
- **wasita/wasita.github.io**: personal site, pushed 2026-06-01

---

## JOB 2: Hamming Swarm Snapshot

**Timestamp:** 2026-06-01 20:13 UTC

### Aptos Wallet Balances (Hamming Swarm A–Z + alice + bob)

All 28 addresses queried against `fullnode.mainnet.aptoslabs.com`.  
**Result: All balances = 0 APT** — no `0x1::coin::CoinStore<AptosCoin>` resources found. These appear to be uninitialized accounts on Aptos mainnet (no APT received/registered).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...cfdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...c7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...25dc4 | 0.0 |
| L | 0x7c2e...3eba9 | 0.0 |
| M | 0x6fed...7f2e9 | 0.0 |
| N | 0xe7dd...551b2c | 0.0 |
| O | 0x7325...5a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...76e10 | 0.0 |
| S | 0xb875...d0386 | 0.0 |
| T | 0x3578...3f4588 | 0.0 |
| U | 0x7586...f9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...3047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes (5 pairs)

All contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

All 5 multisig accounts are 2-of-N and responsive on mainnet.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` — HTTP 200 (Next.js SPA). REST API endpoints `/api/markets` and `/api/tickers` returned 404 (no server-side API surface exposed). Market data **unavailable** — SPA requires browser-side rendering to hydrate market state.

---

## DuckDB Schema Summary

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 342 | GF(3)-colored repo events |
| repo_snapshots | 342 | Full repo metadata |
| aptos_snapshots | 28 | Hamming swarm balances |
| multisig_probes | 5 | Multisig contract health |
| mnx_snapshots | 0 | MNX markets (unavailable) |

Database: `packages/world-increment/ducklake/world-increments.duckdb`
