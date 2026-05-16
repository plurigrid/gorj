# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-29  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos Captured | Total ★ | Top Repo |
|--------|------|---------------|---------|----------|
| plurigrid | org | 100 | 65 | asi (17★) |
| kubeflow | org | 10 (top active) | 27,973 | kubeflow/kubeflow (15,608★) |
| TeglonLabs | org | 4 | 2 | mathpix-gem (2★) |
| bmorphism | user | 15 (top active) | 197 | ocaml-mcp-sdk (60★) |
| zubyul | user | 9 (top active) | 5 | gay-world (2★) |
| migalkin | social | 5 | 274 | NodePiece (143★) |
| DJedamski | social | 3 | 2 | — |
| wasita | social | 4 | 3 | wasita.github.io (1★) |
| kristinezheng | social | 3 | 0 | — |
| M1shaaa | social | 2 | 0 | — |
| AustinCStone | social | 5 | 106 | TextGAN (92★) |

**Total repo snapshots:** 160  
**Total world-increment events:** 160

### GF(3) Color Chain

| Name | Color | Trit | Count |
|------|-------|------|-------|
| ERGODIC | `#d3869b` | 0 | 54 |
| PLUS | `#b8bb26` | +1 | 53 |
| MINUS | `#cc241d` | −1 | 53 |

### Top 15 Repos by Stars

| Repo | Language | ★ | Last Push |
|------|----------|---|-----------|
| kubeflow/kubeflow | — | 15,608 | 2026-04-29 |
| kubeflow/pipelines | Python | 4,128 | 2026-04-29 |
| kubeflow/spark-operator | Python | 3,121 | 2026-04-28 |
| kubeflow/trainer | Go | 2,094 | 2026-04-28 |
| kubeflow/manifests | YAML | 1,012 | 2026-04-27 |
| kubeflow/arena | Go | 810 | 2026-04-28 |
| kubeflow/kale | Python | 684 | 2026-04-29 |
| kubeflow/website | HTML | 184 | 2026-04-28 |
| kubeflow/hub | Go | 174 | 2026-04-29 |
| kubeflow/mcp-apache-spark-history-server | Python | 158 | 2026-04-29 |
| migalkin/NodePiece | Python | 143 | 2026-03-02 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | 2026-03-28 |
| migalkin/kgcourse2021 | HTML | 25 | 2026-02-16 |

### Notable Plurigrid Activity (recent pushes)
- `plurigrid/zig-syrup` (Zig) — 2026-04-26, OCapN Syrup high-perf impl
- `plurigrid/nash-portal` (Rust) — 2026-04-26
- `plurigrid/asi` (HTML, 17★) — 2026-04-26
- `plurigrid/gorj` (Clojure) — 2026-04-29 (this repo)
- `plurigrid/nanoclj-zig` (Zig) — 2026-04-25

### bmorphism Recent Activity
- `bmorphism/nanoclj-zig` (Zig) — 2026-04-25
- `bmorphism/Gay.jl` (Julia, 187 open issues) — 2026-04-17
- `bmorphism/whale` (MATLAB) — 2026-04-20, omniglot + sperm whale codas
- `bmorphism/anti-bullshit-mcp-server` (JS, 23★) — epistemological MCP

### zubyul Recent Activity
- `zubyul/voice-observatory` (Python) — 2026-04-24, companion to bmorphism/say-mcp-server
- `zubyul/ghostel-emacs-worlds` (GLSL) — 2026-04-24, terminal/emacs stack
- `zubyul/big-bad-plurigrid-quiz` (Emacs Lisp) — 2026-04-09

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet)

All 28 Hamming swarm addresses (alice, bob, A–Z) returned **0.000000 APT** — CoinStore resources not initialized or accounts unfunded on mainnet at snapshot time.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793…4cc7b | 0.0 |
| bob | 0x0a3c…512d5d | 0.0 |
| A–Z | 0x8699…→ 0x7af0… | 0.0 each |

### Multisig Probes (5 pairs, Aptos mainnet)

All 5 probed multisig contracts are **healthy** with 2-of-N signature requirements.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f4…987003 | 2 | ✓ |
| A-G | 0xf56c4a…bc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1…5b883 | 2 | ✓ |
| S-T | 0x3b1c3a…7883 | 2 | ✓ |
| V-W | 0x40fad7…0eb6d | 2 | ✓ |

**Interpretation:** All swarm multisig pairs require 2 signatures and responded successfully — swarm coordination contracts healthy.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — testnet.mnx.fi is a Next.js SPA; all API paths (`/api/markets`, `/api/v1/markets`) return the SPA HTML shell rather than JSON market data. No market data extractable without browser JS execution.

---

## DuckDB Schema Summary

```
world_increments   160 rows  — GF(3) color-chained event log
repo_snapshots     160 rows  — GitHub repo metadata
aptos_snapshots     28 rows  — Hamming swarm wallet balances
multisig_probes      5 rows  — Aptos multisig health
mnx_snapshots        1 row   — MNX testnet (unavailable marker)
```

Database: `packages/world-increment/ducklake/world-increments.duckdb`
