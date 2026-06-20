# World Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-20  
**GF(3) color chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found | Notable |
|--------|------|-------------|---------|
| plurigrid | org | 101 | Gay.jl (187 issues), nanoclj-zig (Zig Clojure), zig-syrup, ontology (8★) |
| kubeflow | org | 48 | kubeflow/kubeflow (15736★), pipelines (4154★), spark-operator (3127★), trainer (2117★) |
| TeglonLabs | org | 5 | jank-crane (C++, GF3 convergence maps, pushed 2026-06-08) |
| bmorphism | user | 105 | Gay.jl (187 issues), anti-bullshit-mcp-server (23★), babashka-mcp-server (19★), world launcher |
| zubyul | user | 49 | gay-world, big-bad-plurigrid-quiz, ghosttel-emacs-worlds, nash-tui |
| migalkin | user | 19 | NodePiece (144★), StarE (89★), kgcourse2021 (25★) |
| DJedamski | user | 6 | R/Stats projects, Project_Euler |
| wasita | user | 11 | wasita.github.io (Svelte, pushed 2026-06-15), magic-garden, proj-template (pushed 2026-06-19) |
| kristinezheng | user | 5 | kristinezheng.github.io (pushed 2026-06-07) |
| M1shaaa | user | 8 | M1shaaa profile (pushed 2026-06-19) |
| AustinCStone | user | 40 | TextGAN (92★), EpsteinSearch (pushed 2026-02-11), bmfork |

### Recently Active Repos (pushed 2026-06)
- `kubeflow/internal-acls` – pushed 2026-06-19T19:50
- `kubeflow/pipelines-components` – pushed 2026-06-19T16:58
- `kubeflow/trainer` – pushed 2026-06-19T15:46
- `wasita/proj-template` – pushed 2026-06-19T21:22
- `M1shaaa/M1shaaa` – pushed 2026-06-19T14:57
- `bmorphism/Gay.jl` – pushed 2026-06-19T00:48 (187 open issues)
- `kubeflow/spark-operator` – pushed 2026-06-18T15:39
- `TeglonLabs/jank-crane` – pushed 2026-06-08T19:03 (GF3 convergence maps)
- `wasita/wasita.github.io` – pushed 2026-06-15T20:15

### GF(3) Increment Assignments (this sweep)

| ID | Source | Trit | Name | Color |
|----|--------|------|------|-------|
| 1 | plurigrid | 1 | PLUS | #b8bb26 |
| 2 | kubeflow | -1 | MINUS | #cc241d |
| 3 | TeglonLabs | 0 | ERGODIC | #d3869b |
| 4 | bmorphism | 1 | PLUS | #b8bb26 |
| 5 | zubyul | -1 | MINUS | #cc241d |
| 6 | migalkin | 0 | ERGODIC | #d3869b |
| 7 | DJedamski | 1 | PLUS | #b8bb26 |
| 8 | wasita | -1 | MINUS | #cc241d |
| 9 | kristinezheng | 0 | ERGODIC | #d3869b |
| 10 | M1shaaa | 1 | PLUS | #b8bb26 |
| 11 | AustinCStone | -1 | MINUS | #cc241d |

### DuckDB Schema
- `world_increments` – GF3-tagged sweep events
- `repo_snapshots` – per-repo metadata (stars, forks, issues, language, pushed_at)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm addresses (alice, bob, A–Z) queried against Aptos mainnet fullnode.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I–Z | (18 addresses) | 0.0 each |

**Observation:** All 28 addresses return 0 APT. The accounts may be unfunded, pre-funded via non-APT tokens, or the CoinStore resource is absent (accounts not yet on-chain in standard form).

### Multisig Contract Probes

All 5 multisig accounts queried via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

**All multisig contracts healthy — 2-of-2 threshold, all responding.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection requiring visitor password authentication. No market data extractable without bypass token.

---

## Database Summary

| Table | Rows |
|-------|------|
| world_increments | 34 (cumulative across sweeps) |
| repo_snapshots | 1037 (cumulative) |
| aptos_snapshots | 28 (this sweep) |
| multisig_probes | 5 (this sweep) |
| mnx_snapshots | 1 (unavailable marker) |

**DuckDB file:** `packages/world-increment/ducklake/world-increments.duckdb`
