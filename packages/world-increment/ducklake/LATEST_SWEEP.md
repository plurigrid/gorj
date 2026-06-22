# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-22

**Date:** 2026-06-22  
**DuckDB:** `world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Snapshotted

| ID | GF3 Trit | Color | Name | Source | Repos Found |
|----|----------|-------|------|--------|-------------|
| 1 | +1 PLUS | #b8bb26 | plurigrid | org | 101 |
| 2 | −1 MINUS | #cc241d | kubeflow | org | 48 |
| 3 | 0 ERGODIC | #d3869b | TeglonLabs | org | 5 |
| 4 | +1 PLUS | #b8bb26 | bmorphism | user | 105 |
| 5 | −1 MINUS | #cc241d | zubyul | user | 49 |
| 6 | 0 ERGODIC | #d3869b | social graph | multi | 89 |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

**Total repositories indexed:** 397 across all sources (59 stored in ducklake)

### Notable Activity (recent pushes 2026)

**plurigrid:**
- `gorj` (Clojure, 738 open issues) — last push 2026-05-08; this repo
- `eirobri` (Clojure, 29 open issues) — EiRoBri replay world, 2026-05-19
- `nash-portal` (Rust) — NASH token TUI in browser, ⭐2, 2026-05-19
- `nanoclj-zig` (Zig, ⭐1, 20 open issues) — NaN-boxed Clojure, GF(3) trit conservation
- `asi` (HTML, ⭐26) — top star repo, "everything is topological chemputer!"
- `place` (TeX, ⭐1, 9 open issues) — 2026-06-04

**kubeflow:**
- `pipelines` (Python, ⭐4157, 449 open issues) — updated 2026-06-22
- `spark-operator` (Python, ⭐3128, 104 open issues) — updated 2026-06-22
- `mcp-apache-spark-history-server` (Python, ⭐177) — MCP for Spark debugging
- `notebooks` — 184 open issues, active
- `sdk` (Python, ⭐120, 133 open issues) — Universal Python SDK for AI workloads on K8s

**TeglonLabs:**
- `jank-crane` (C++) — crane-jank converged-IR hub, GF3 convergence maps, 2026-06-08 (newest)
- `mathpix-gem` (Ruby, ⭐2) — math image to LaTeX with security-first design

**bmorphism:**
- `ocaml-mcp-sdk` (OCaml, ⭐61) — top star; OCaml SDK for MCP using Jane Street's oxcaml_effect
- `Gay.jl` (Julia, ⭐2, 187 open issues) — wide-gamut SPI color sampling, 2026-06-20
- `bci-preview` (HTML) — Stable redirect for bci.place forester preview, 2026-06-20
- `satreadout` (HTML) — Machine-checked Lean 4.28 saturating readout, 2026-06-20
- `world` (Python) — Local worlds launcher for SA3/jank/world proofs, 2026-06-02

**zubyul:**
- `gay-world` (Python, ⭐1) — Goblin world builder with MLX task decomposition
- `ghostel-emacs-worlds` (GLSL) — Ghostty config + ghostel family, 2026-04-24
- `tilelang-kernels` (Python) — GPU kernels for SplitMix64/GF(3)/flash attention
- `big-bad-plurigrid-quiz` (Emacs Lisp) — 27 flashcards from plurigrid/bmorphism activity

**Social Graph (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone):**
- `migalkin/NodePiece` (Python, ⭐144) — Compositional KG representations, ICLR'22
- `AustinCStone/TextGAN` (Python, ⭐92) — text GAN in TensorFlow
- `migalkin/StarE` (Python, ⭐89) — hyper-relational KG message passing, EMNLP 2020
- `wasita/wasita.github.io` (Svelte, 8 open issues) — personal website, updated 2026-06-15
- `wasita/send2kobo` (TypeScript) — send books to Kobo, updated 2026-05-19
- `wasita/proj-template` — updated 2026-06-19

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 wallets)

All queried via `fullnode.mainnet.aptoslabs.com` REST API. All wallets returned **0 APT** — no `CoinStore<AptosCoin>` resource found on any address. These wallets are either unfunded, hold other resource types, or the API returned no coin store.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | 0.0 |
| bob   | 0x0a3c…12d5 | 0.0 |
| A     | 0x8699…9d7a | 0.0 |
| B     | 0x3f89…b13  | 0.0 |
| C–Z   | (24 addresses)     | 0.0 each |

### Multisig Contract Probes (5 contracts)

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`. **All healthy — 2-of-2 multisig.**

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…3003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — `testnet.mnx.fi` is behind Vercel deployment authentication (visitor password required). Both `/api/markets` and `/api/v1/markets` endpoints return the Vercel auth wall. No market data could be extracted without credentials. Stored as placeholder in mnx_snapshots.

---

## DuckDB Schema Summary

```
world_increments  — 6 rows  (GF3 color chain: PLUS→MINUS→ERGODIC×2)
repo_snapshots    — 59 rows  (sampled from 397 indexed repos)
aptos_snapshots   — 28 rows  (alice, bob, A–Z; all 0.0 APT)
multisig_probes   —  5 rows  (all 2-of-2, all healthy)
mnx_snapshots     —  1 row   (unavailable placeholder)
```

## GF(3) Color Chain Reference

```
id%3==0 → trit= 0  ERGODIC  #d3869b  (pink)
id%3==1 → trit=+1  PLUS     #b8bb26  (yellow-green)
id%3==2 → trit=-1  MINUS    #cc241d  (red)
```

Sweep completed: 2026-06-22. Next sweep recommended in 24h.
