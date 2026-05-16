# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-16T00:00 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**DuckDB version:** v1.5.2 (Variegata)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| migalkin | user (social graph) | 8 |
| wasita | user (social graph) | 7 |
| AustinCStone | user (social graph) | 6 |
| M1shaaa | user (social graph) | 5 |
| TeglonLabs | org | 4 |
| kristinezheng | user (social graph) | 4 |
| DJedamski | user (social graph) | 4 |
| **TOTAL** | | **335** |

### GF(3) Color Chain Distribution (world_increments)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 111 |
| 1 | PLUS | `#b8bb26` | 112 |
| -1 | MINUS | `#cc241d` | 112 |

Assignment: `id % 3 == 0` → ERGODIC, `id % 3 == 1` → PLUS, `id % 3 == 2` → MINUS

### Top Starred Repositories

| Repo | Language | Stars | Forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | — | 15,633 | 2,648 |
| kubeflow/pipelines | Python | 4,139 | 1,992 |
| kubeflow/spark-operator | Python | 3,125 | 1,482 |
| kubeflow/trainer | Go | 2,098 | 949 |
| kubeflow/katib | Python | 1,682 | 522 |
| kubeflow/examples | Jsonnet | 1,463 | 757 |
| kubeflow/manifests | YAML | 1,017 | 1,064 |
| kubeflow/arena | Go | 810 | 190 |
| kubeflow/kale | Python | 687 | 156 |
| migalkin/NodePiece | Python | 144 | 21 |
| AustinCStone/TextGAN | Python | 92 | 30 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 |
| plurigrid/asi | HTML | 23 | 5 |

### Notable Plurigrid Repos (recent activity)
- `plurigrid/gorj` (Clojure) — forj + Rama topology nREPL routing + GF(3) gay trit coloring (209 open issues, pushed 2026-05-16)
- `plurigrid/nanoclj-zig` (Zig) — NaN-boxed Clojure interpreter, interaction nets, fuel-bounded eval, GF(3) trit conservation (pushed 2026-04-25)
- `plurigrid/zig-syrup` (Zig) — OCapN Syrup high-perf impl (★2, pushed 2026-04-30)
- `plurigrid/asi-skills` (Julia) — 69 skills with Galois Hole Type accessibility (★3, pushed 2026-04-26)
- `plurigrid/nash-portal` (Rust) — NASH token TUI in browser, ratzilla WASM (★2, pushed 2026-04-26)
- `plurigrid/horse` (TeX) — (★1, 9 open issues, pushed 2026-05-07)

### Notable bmorphism Repos (recent activity)
- `bmorphism/Gay.jl` (Julia) — Wide-gamut color sampling, GF(3), Pigeons.jl SPI (188 open issues, pushed 2026-05-16)
- `bmorphism/oxgame` (OCaml) — Stellar resolution and open-game composition (pushed 2026-05-15)
- `bmorphism/nanoclj-zig` (Zig) — pushed 2026-05-07
- `bmorphism/ocaml-mcp-sdk` (OCaml) — Jane Street oxcaml_effect (★61, pushed 2026-03-16)
- `bmorphism/risc0-cosmwasm-example` (Rust) — zkVM + CosmWasm (★23)

### Zubyul Social Graph (zubyul-connected users)
- `migalkin/NodePiece` (Python) — ICLR'22 KG representations (★144, pushed 2026-05-07)
- `migalkin/StarE` (Python) — EMNLP 2020 hyper-relational KG (★89)
- `AustinCStone/TextGAN` (Python) — GAN text generation in TensorFlow (★92)
- `wasita/wasita.github.io` (Svelte) — personal site, active (8 open issues, pushed 2026-05-14)
- `wasita/magic-garden` (Python) — Discord bot (★2, pushed 2026-04-22)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All wallets returned 0 APT.** The Aptos mainnet API returned `resource_not_found` for all addresses — accounts are not yet initialized on-chain with APT (CoinStore resource not registered).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0xc793...cc7b | 0.00 |
| bob | 0x0a3c...512d | 0.00 |
| A | 0x8699...9d7a | 0.00 |
| B | 0x3f89...b13 | 0.00 |
| C | 0x38b9...35e | 0.00 |
| D | 0xf776...fdd1 | 0.00 |
| E | 0xdc1d...8d36 | 0.00 |
| F | 0x18a1...cf71 | 0.00 |
| G | 0x69a3...7f32 | 0.00 |
| H | 0xce67...300f | 0.00 |
| I | 0x070f...1fc9 | 0.00 |
| J | 0x4d96...7f54 | 0.00 |
| K | 0xa732...5dc4 | 0.00 |
| L | 0x7c2e...eba9 | 0.00 |
| M | 0x6fed...7f2e9 | 0.00 |
| N | 0xe7dd...51b2c | 0.00 |
| O | 0x7325...a89d | 0.00 |
| P | 0x6218...c948 | 0.00 |
| Q | 0xac40...c89a9 | 0.00 |
| R | 0x7ce6...76e10 | 0.00 |
| S | 0xb875...d0386 | 0.00 |
| T | 0x3578...f4588 | 0.00 |
| U | 0x7586...f9956 | 0.00 |
| V | 0xb59d...af2c3 | 0.00 |
| W | 0x5f32...cc7b0 | 0.00 |
| X | 0xa95c...3047d | 0.00 |
| Y | 0xd8e3...444c4 | 0.00 |
| Z | 0x7af0...197c | 0.00 |

**Total Hamming swarm APT:** 0.00 APT  
**Active wallets:** 0 / 28

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts responded successfully. All require **2 signatures** (2-of-N).

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | `0x0da4...7003` | 2 | HEALTHY |
| A-G | `0xf56c...0096` | 2 | HEALTHY |
| Y-Z | `0xd3ff...b883` | 2 | HEALTHY |
| S-T | `0x3b1c...7883` | 2 | HEALTHY |
| V-W | `0x40fa...eb6d` | 2 | HEALTHY |

**Multisig health:** 5/5 (100%)

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE**  
`https://testnet.mnx.fi/api/markets` returned HTTP 404 (Vercel CDN, cached April 28 2026). No market data retrieved.

---

## DuckDB Schema Summary

```
world_increments: 335 rows   (GF3 color chain of all repo events)
repo_snapshots:   335 rows   (full repo metadata)
aptos_snapshots:   28 rows   (all 0.00 APT, accounts uninitialized on-chain)
multisig_probes:    5 rows   (all healthy, 2-of-N)
mnx_snapshots:      0 rows   (endpoint unavailable)
```

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent | 2026-05-16*
