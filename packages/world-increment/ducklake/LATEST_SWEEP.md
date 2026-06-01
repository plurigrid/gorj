# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-01

## Sweep Metadata
- **Date:** 2026-06-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repository Snapshot Summary

| Source | Type | Repos Captured |
|---|---|---|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph (zubyul) | 6 |
| DJedamski | social graph (zubyul) | 4 |
| wasita | social graph (zubyul) | 5 |
| kristinezheng | social graph (zubyul) | 4 |
| M1shaaa | social graph (zubyul) | 3 |
| AustinCStone | social graph (zubyul) | 6 |
| **TOTAL** | | **329** |

### GF(3) World-Increment Distribution

| GF(3) Name | Color | Trit | Count |
|---|---|---|---|
| ERGODIC | #d3869b | 0 | 109 |
| PLUS | #b8bb26 | 1 | 110 |
| MINUS | #cc241d | -1 | 110 |

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...` (329 increments)

### Notable Repos

**plurigrid** (100 repos) — polyglot research org (Clojure, Rust, Python, TypeScript, Julia, Zig, Haskell, Racket and more)
- `gorj` — 288 open issues; this very repo (forj + Rama topology nREPL routing)
- `asi` — 23 stars — topological chemputer
- `ontology` — 8 stars
- `vcg-auction` — 7 stars

**kubeflow** (48 repos) — ML platform for Kubernetes
- `kubeflow` — flagship repo ~15k+ stars
- `pipelines` — most active ML pipeline system
- `training-operator`, `spark-operator`, `katib` — top by activity

**bmorphism** (100 repos) — most recent push: `bmorphism/Gay.jl` (Julia, 2026-06-01)
- `ocaml-mcp-sdk` — OCaml MCP SDK using Jane Street oxcaml_effect
- `anti-bullshit-mcp-server` — 23 stars

**zubyul** (49 repos) — Python, Rust, Julia, Clojure, Move, Zig, Haskell; lab data analysis, WGCNA

**TeglonLabs** (4 repos)
- `mathpix-gem` (Ruby, 2 ★) — security-first LaTeX/SMILES/Markdown OCR gem
- `coin-flip-mcp` (JavaScript, 2 forks) — MCP server using random.org
- `monad-mcp-server` — Monad MCP Server
- `topoi` (Python) — topos theory

**Social graph highlights:**
- `migalkin/NodePiece` — 144 ★, 21 forks — large KG representation (ICLR'22)
- `migalkin/StarE` — 89 ★ — hyper-relational KG message passing (EMNLP'20)
- `AustinCStone/TextGAN` — 92 ★, 30 forks — GAN text generation (TensorFlow)
- `AustinCStone/StereoVisionMRF` — 11 ★ — MRF depth estimation from stereo
- `wasita/wasita.github.io` — pushed 2026-06-01 (today); active personal site (Svelte)
- `wasita/magic-garden` — 2 ★ — Discord game bot

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Sweep:** 28 addresses (alice, bob, A–Z), 1s delay between calls  
**Result:** All 28 wallets returned **0.00 APT** on mainnet at sweep time.  
The `CoinStore<AptosCoin>` resource was absent or zero for each — these addresses may be testnet/unfunded.

| World | Address | Balance (APT) |
|---|---|---|
| alice | 0xc793acdec12b4a…d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf90…d00e05512d | 0.0 |
| A | 0x8699edc0960dd5…0af6eaebe9d7a | 0.0 |
| B–Z | (see aptos_snapshots table) | 0.0 each |

### Multisig Contract Probes

All 5 contracts healthy — each requires **2-of-2** signatures.

| Pair | Contract Address | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4f428a0c007…e880def4987003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c090621…c5bee3fbc0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe1812b2df4…16df742638e75b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae905d44c…d3570060b23ded7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b423a843…81b0f9082c80eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA — no structured REST market data endpoint was accessible at sweep time. Probed: `/api/markets`, `/api/v1/markets`, `/markets` — all returned SPA HTML. Market data recorded as **unavailable** in `mnx_snapshots` table (0 rows).

---

## DuckDB Schema

```sql
world_increments   -- GF(3) color-chained increment log (329 rows)
repo_snapshots     -- GitHub repo metadata per increment (329 rows)
aptos_snapshots    -- Hamming swarm wallet balances (28 rows, all 0.0 APT)
multisig_probes    -- Aptos multisig contract health (5 rows, all 2-of-2)
mnx_snapshots      -- MNX market data (0 rows — SPA, unavailable)
```

### GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent, 2026-06-01*
