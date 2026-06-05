# World-Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-06-05 UTC  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 35 |
| kubeflow | org | 20 |
| TeglonLabs | org | 4 |
| bmorphism | user | 21 |
| zubyul | user | 10 |
| migalkin | social graph | 6 |
| wasita | social graph | 5 |
| AustinCStone | social graph | 4 |
| DJedamski | social graph | 3 |
| kristinezheng | social graph | 2 |
| M1shaaa | social graph | 2 |
| **Total** | | **112** |

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | ★15,706 | — |
| kubeflow/pipelines | ★4,152 | Python |
| kubeflow/spark-operator | ★3,125 | Python |
| kubeflow/trainer | ★2,111 | Go |
| kubeflow/katib | ★1,684 | Python |
| kubeflow/examples | ★1,462 | Jsonnet |
| kubeflow/manifests | ★1,020 | YAML |
| migalkin/NodePiece | ★144 | Python |
| AustinCStone/TextGAN | ★92 | Python |
| migalkin/StarE | ★89 | Python |
| bmorphism/ocaml-mcp-sdk | ★61 | OCaml |

### Top Languages
| Language | Count |
|----------|-------|
| Python | 26 |
| JavaScript | 13 |
| Rust | 9 |
| HTML | 8 |
| Clojure | 6 |
| Go | 6 |
| Jupyter Notebook | 5 |
| TypeScript | 4 |
| Julia | 3 |
| Svelte | 3 |

### Notable Repos from Social Graph
- **plurigrid/gorj** — forj + Rama topology nREPL routing + GF(3) gay trit coloring (376 open issues — active!)
- **bmorphism/Gay.jl** — Wide-gamut color sampling with splittable determinism, 189 open issues
- **bmorphism/anti-bullshit-mcp-server** — MCP server for analyzing claims and detecting manipulation (★23)
- **bmorphism/risc0-cosmwasm-example** — CosmWasm + zkVM RISC-V EFI template (★23)
- **bmorphism/say-mcp-server** — macOS text-to-speech MCP (★20)
- **migalkin/NodePiece** — Compositional Knowledge Graph representations, ICLR 2022 (★144)
- **plurigrid/asi** — everything is topological chemputer! (★25)
- **zubyul/tilelang-kernels** — TileLang GPU kernels for GF(3) trit classification and Sinkhorn OT
- **bmorphism/ocaml-mcp-sdk** — OCaml SDK for MCP using Jane Street's oxcaml_effect (★61)

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 37 |
| -1 | `#cc241d` | MINUS | 37 |
| 1 | `#b8bb26` | PLUS | 38 |

Total world_increments: **112** (balanced across GF(3))

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z = 28 wallets)
All 28 Hamming swarm wallets returned **0.0 APT** — the `CoinStore<AptosCoin>` resource was not found on Aptos mainnet fullnode for any address. Accounts are either uninitialized or have never held APT.

| World | Address (prefix) | Balance APT |
|-------|------------------|-------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A | 0x8699...be9d7a | 0.0 |
| B | 0x3f89...77cb13 | 0.0 |
| C | 0x38b9...1535e | 0.0 |
| D | 0xf776...cfdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...3cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...5300f | 0.0 |
| I | 0x070f...c1fc9 | 0.0 |
| J | 0x4d96...87f54 | 0.0 |
| K | 0xa732...25dc4 | 0.0 |
| L | 0x7c2e...7eba9 | 0.0 |
| M | 0x6fed...7f2e9 | 0.0 |
| N | 0xe7dd...551b2c | 0.0 |
| O | 0x7325...5a89d | 0.0 |
| P | 0x6218...ec948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...76e10 | 0.0 |
| S | 0xb875...d0386 | 0.0 |
| T | 0x3578...3f4588 | 0.0 |
| U | 0x7586...ef9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...cc7b0 | 0.0 |
| X | 0xa95c...3047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes
All 5 multisig contracts are **healthy** (2-of-N signatures required):

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All multisig accounts respond to `0x1::multisig_account::num_signatures_required` on Aptos mainnet and require 2 signatures — the swarm's 2-of-N invariant holds across all probed pairs.

### MNX Markets
**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection (authentication required). The endpoint returns HTTP 200 with an auth challenge HTML page rather than market data. `mnx_snapshots` table is empty for this sweep.

---

## DuckDB Schema Summary
```
world_increments  — 112 rows  (GF3-colored repo snapshot events)
repo_snapshots    — 112 rows  (full repo metadata)
aptos_snapshots   —  28 rows  (Hamming swarm wallet balances, all 0.0 APT)
multisig_probes   —   5 rows  (2-of-N multisig health: all healthy, sigs=2)
mnx_snapshots     —   0 rows  (unavailable — Vercel auth protected)
```

## Query Examples
```sql
-- Top repos by stars
SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF(3) color distribution
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY 1, 2;

-- All healthy multisigs
SELECT pair, sigs_required FROM multisig_probes WHERE healthy = true;

-- Plurigrid ecosystem language breakdown
SELECT language, COUNT(*) FROM repo_snapshots
WHERE org_or_user IN ('plurigrid', 'bmorphism', 'zubyul')
  AND language IS NOT NULL
GROUP BY language ORDER BY 2 DESC;

-- Most recently pushed repos
SELECT full_name, pushed_at, org_or_user FROM repo_snapshots
ORDER BY pushed_at DESC LIMIT 10;
```
