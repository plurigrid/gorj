# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-11
**Agent:** world-increment-sweep + hamming-swarm-snapshot
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 76 |
| bmorphism | user | 100 | 247 |
| zubyul | user | 49 | 14 |
| kubeflow | org | 48 | 34,190 |
| AustinCStone | user (social graph) | 30 | 108 |
| migalkin | user (social graph) | 19 | 280 |
| wasita | user (social graph) | 11 | 5 |
| M1shaaa | user (social graph) | 8 | 0 |
| DJedamski | user (social graph) | 6 | 3 |
| TeglonLabs | org | 5 | 2 |
| kristinezheng | user (social graph) | 5 | 0 |

**Total:** 381 repos snapshotted across 11 sources

### Top Repos by Stars

| Repo | Language | Stars | Forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | — | 15,714 | 2,671 |
| kubeflow/pipelines | Python | 4,152 | 2,005 |
| kubeflow/spark-operator | Python | 3,126 | 1,489 |
| kubeflow/trainer | Go | 2,111 | 964 |
| kubeflow/katib | Python | 1,683 | 525 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 |
| plurigrid/asi | HTML | 25 | 7 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 |
| bmorphism/Gay.jl | Julia | 1 | 1 (189 open issues) |
| plurigrid/gorj | Clojure | 0 | 0 (506 open issues) |

### Notable Plurigrid Activity (Most Recent Pushes)

- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring (2026-06-11)
- `plurigrid/asi` — topological chemputer (2026-06-10)
- `plurigrid/place` — TeX (2026-06-10)
- `plurigrid/eirobri` — EiRoBri replay world, Clojure (2026-06-03)
- `plurigrid/nash-portal` — NASH token TUI in browser, Rust (2026-05-19)

### Notable bmorphism Activity

- `bmorphism/Gay.jl` — Wide-gamut color sampling with splittable determinism, Julia (2026-06-11)
- `bmorphism/satreadout` — Machine-checked saturating non-Riemannian perceptual readout, Lean (2026-06-10)
- `bmorphism/world` — Local worlds launcher for SA3, jank, world proofs, Python (2026-06-02)
- `bmorphism/ocaml-mcp-sdk` — OCaml SDK for MCP (61 stars), OCaml (2026-03-16)

### GF(3) Color Chain Distribution

| Name | Hex | Count |
|------|-----|-------|
| ERGODIC (trit=0) | #d3869b | 127 |
| PLUS (trit=1) | #b8bb26 | 127 |
| MINUS (trit=-1) | #cc241d | 127 |

381 world-increments with balanced GF(3) trit assignment (id%3 in {0,1,2}).

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**Queried:** 28 wallets (alice, bob, A-Z)
**Result:** All 28 wallets: `resource_not_found` — no CoinStore<AptosCoin> registered.

| Range | Count | Total APT |
|-------|-------|-----------|
| alice, bob | 2 | 0.0 |
| A-Z (26 addresses) | 26 | 0.0 |
| **Total** | **28** | **0.0 APT** |

All addresses exist in the Aptos address space but have not initialized an APT coin store at ledger version 5,686,137,237.

### Multisig Contract Probes

| Pair | Contract (truncated) | Sigs Required | Healthy |
|------|----------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

All 5 multisig contracts are live and require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

Status: UNAVAILABLE — Vercel Deployment Protection (HTTP 401).
No market data extractable without Vercel visitor password or OIDC bypass token.
`mnx_snapshots` table remains empty.

---

## DuckDB Schema

```
world_increments  381 rows  (one per repo, GF(3) trit colored)
repo_snapshots    381 rows  (full repo metadata)
aptos_snapshots    28 rows  (all 0.0 APT, resource_not_found)
multisig_probes     5 rows  (all healthy, 2-of-N)
mnx_snapshots       0 rows  (auth-protected)
```

File: `packages/world-increment/ducklake/world-increments.duckdb`
