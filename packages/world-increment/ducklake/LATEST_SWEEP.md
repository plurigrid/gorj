# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-23

## Sweep Metadata
- **Date:** 2026-04-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 65 |
| kubeflow | org | 47 | 33,929 |
| TeglonLabs | org | 4 | 2 |
| bmorphism | user | 100 | 246 |
| zubyul | user | 47 | 14 |
| migalkin | user (social) | 5 | 274 |
| wasita | user (social) | 3 | 3 |
| DJedamski | user (social) | 3 | 2 |
| kristinezheng | user (social) | 3 | 0 |
| M1shaaa | user (social) | 3 | 0 |
| AustinCStone | user (social) | 3 | 103 |
| **TOTAL** | | **318** | **34,638** |

### Top 15 Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,596 | — | 2026-01-05 |
| kubeflow/pipelines | 4,125 | Python | 2026-04-23 |
| kubeflow/spark-operator | 3,117 | Python | 2026-04-21 |
| kubeflow/trainer | 2,088 | Go | 2026-04-22 |
| kubeflow/katib | 1,680 | Python | 2026-04-14 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,012 | YAML | 2026-04-11 |
| kubeflow/arena | 810 | Go | 2026-04-16 |
| kubeflow/kale | 684 | Python | 2026-04-22 |
| kubeflow/mpi-operator | 524 | Go | 2026-04-14 |
| kubeflow/fairing | 337 | Jsonnet | 2022-04-11 |
| kubeflow/pytorch-operator | 309 | Jsonnet | 2021-12-01 |
| migalkin/NodePiece | 143 | Python | 2026-03-02 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 106 |
| 1 | `#b8bb26` | PLUS | 106 |
| -1 | `#cc241d` | MINUS | 106 |

### Notable Activity (plurigrid — 100 repos)
- `plurigrid/gorj` — Clojure, 257 open issues, pushed 2026-04-23 (this repo)
- `plurigrid/asi` — HTML, 17 stars, 5 forks, pushed 2026-04-20
- `plurigrid/nanoclj-zig` — Zig NaN-boxed Clojure interpreter, 1★, pushed 2026-04-21
- `plurigrid/spi-race` — Swift splitmix parallel integrity, pushed 2026-04-21
- `plurigrid/nash-portal` — Rust WASM TUI + GeckoTerminal OHLCV, 1★, pushed 2026-04-15

### Notable Activity (bmorphism — 100 repos)
- `bmorphism/Gay.jl` — Julia wide-gamut SPI color sampling, 1★, 187 issues, pushed 2026-04-23
- `bmorphism/ocaml-mcp-sdk` — OCaml MCP SDK via Jane Street oxcaml_effect, 60★
- `bmorphism/anti-bullshit-mcp-server` — JS claim analysis MCP, 23★
- `bmorphism/nanoclj-zig` — Zig, pushed 2026-04-18

### Notable Activity (zubyul — 47 repos)
- `zubyul/nash-tui` + `zubyul/nash-web` — Rust NASH token TUIs, pushed 2026-04-13
- `zubyul/Gay.jl` — Julia fork, pushed 2026-03-28
- `zubyul/tilelang-kernels` — Python GPU kernels for GF(3) trit classification

### Social Graph (zubyul → migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)
- `migalkin/NodePiece` — 143★ KG embeddings (ICLR'22)
- `migalkin/StarE` — 89★ hyper-relational KG (EMNLP'20)
- `AustinCStone/TextGAN` — 92★ text generation GAN
- `wasita/wasita.github.io` — Svelte personal site, recently pushed
- `kristinezheng/lookit-jenga` — Jupyter cognitive science study
- `M1shaaa/lab-bookshelf-` — TypeScript, pushed 2024-12-31

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 Hamming swarm wallets (alice, bob, A–Z) returned **0.0 APT** from the Aptos mainnet fullnode (`fullnode.mainnet.aptoslabs.com`). Accounts exist on-chain but hold no `0x1::aptos_coin::AptosCoin` balance — either unfunded or balances held in other coin/token types.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…512d | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B | 0x3f89…b13 | 0.0 |
| C–Z | (see DB) | 0.0 each |

### Multisig Contract Probes (5 pairs) — ALL HEALTHY

All 5 multisig contracts responded successfully via `0x1::multisig_account::num_signatures_required`, each requiring **2-of-2** signatures.

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable (SPA).** The site returns a Next.js SPA (292 KB). No JSON API endpoints responded at `/api/markets`, `/api/v1/markets`, or `/api/tickers`. Market data is rendered client-side only and not accessible via server-side probe.

---

## DuckDB Table Summary

```
world_increments   318 rows  — GF(3)-colored repo snapshot events
repo_snapshots     318 rows  — full repo metadata per increment
aptos_snapshots     28 rows  — Hamming swarm wallet balances (A–Z + alice, bob)
multisig_probes      5 rows  — A-B, A-G, Y-Z, S-T, V-W (all 2-of-2, healthy)
mnx_snapshots        1 row   — MNX testnet (unavailable / SPA)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
