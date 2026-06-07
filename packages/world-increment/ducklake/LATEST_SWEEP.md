# World-Increment Sweep + Hamming Snapshot — 2026-06-07

## Sweep Metadata
- **Date:** 2026-06-07 07:30:00 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 93 |
| Total Repo Snapshots | 93 |
| Sources Covered | 4 orgs/users + 7 social graph |

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 33 |
| kubeflow | org | 15 |
| bmorphism | user | 21 |
| zubyul | user | 22 |
| migalkin | user (social) | 1 |
| DJedamski | user (social) | 0 |
| wasita | user (social) | 0 |
| kristinezheng | user (social) | 0 |
| M1shaaa | user (social) | 0 |
| AustinCStone | user (social) | 0 |
| TeglonLabs | org | 0 |
| **TOTAL** | | **93** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 (ERGODIC) | `#d3869b` | ERGODIC | 31 |
| 1 (PLUS) | `#b8bb26` | PLUS | 31 |
| -1 (MINUS) | `#cc241d` | MINUS | 31 |

Chain rule: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`

### Notable Repos by Stars

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,706 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,153 | Python | ML Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,125 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,112 | Go | Distributed AI Model Training on Kubernetes |
| kubeflow/examples | 1,462 | Jsonnet | Extended examples and tutorials |
| kubeflow/katib | 1,685 | Python | Automated ML on Kubernetes |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | OCaml SDK for Model Context Protocol |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | MCP server for analyzing claims |
| plurigrid/asi | 25 | HTML | everything is topological chemputer |
| plurigrid/gorj | 413 issues | Clojure | forj + Rama topology nREPL + GF(3) trit coloring |

### Most Recently Pushed

| Repo | Pushed At | Source |
|------|-----------|--------|
| plurigrid/gorj | 2026-06-07 | plurigrid |
| bmorphism/Gay.jl | 2026-06-07 | bmorphism |
| kubeflow/pipelines | 2026-06-06 | kubeflow |
| kubeflow/trainer | 2026-06-06 | kubeflow |
| plurigrid/place | 2026-06-04 | plurigrid |
| plurigrid/eirobri | 2026-06-03 | plurigrid |
| bmorphism/world | 2026-06-02 | bmorphism |

### Language Landscape

**plurigrid:** Clojure, Rust, Zig, HTML, Julia, Haskell, Scheme, Racket, Go, Python  
**bmorphism:** Julia, OCaml, Python, JavaScript, Clojure, Zig, Move, Haskell, Java  
**zubyul:** Python, Rust, Clojure, Julia, GLSL, Move, TypeScript, Kotlin, Emacs Lisp  
**kubeflow:** Python, Go, YAML, TypeScript, HTML, Jsonnet, Jupyter Notebook

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 hamming-swarm addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on Aptos mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...512d | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B | 0x3f89...b13 | 0.00000000 |
| C | 0x38b9...35e | 0.00000000 |
| D | 0xf776...dd1 | 0.00000000 |
| E | 0xdc1d...d36 | 0.00000000 |
| F | 0x18a1...f71 | 0.00000000 |
| G | 0x69a3...f32 | 0.00000000 |
| H | 0xce67...00f | 0.00000000 |
| I | 0x070f...c9 | 0.00000000 |
| J | 0x4d96...f54 | 0.00000000 |
| K | 0xa732...dc4 | 0.00000000 |
| L | 0x7c2e...ba9 | 0.00000000 |
| M | 0x6fed...e9 | 0.00000000 |
| N | 0xe7dd...b2c | 0.00000000 |
| O | 0x7325...89d | 0.00000000 |
| P | 0x6218...948 | 0.00000000 |
| Q | 0xac40...a9 | 0.00000000 |
| R | 0x7ce6...e10 | 0.00000000 |
| S | 0xb875...386 | 0.00000000 |
| T | 0x3578...588 | 0.00000000 |
| U | 0x7586...956 | 0.00000000 |
| V | 0xb59d...b3 | 0.00000000 |
| W | 0x5f32...b0 | 0.00000000 |
| X | 0xa95c...47d | 0.00000000 |
| Y | 0xd8e3...c4 | 0.00000000 |
| Z | 0x7af0...97c | 0.00000000 |

**Total APT across swarm:** 0.00000000 APT  
**Note:** All addresses return 0 APT — CoinStore resources not initialized. These are fresh keypairs without funded accounts on mainnet.

### Multisig Contract Probes (5 pairs)

All probed via `0x1::multisig_account::num_signatures_required` POST to Aptos mainnet.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

**All 5 multisig contracts healthy — uniform 2-of-2 signature threshold.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE**  
`https://testnet.mnx.fi` and `https://testnet.mnx.fi/api/markets` both return Vercel authentication challenges. No market data accessible without deployment bypass token or trusted-source OIDC configuration.

---

## DuckDB Table Summary

```
world-increments.duckdb
├── world_increments    93 rows  — GF(3) trit-colored per-repo event log
├── repo_snapshots      93 rows  — repo metadata (stars, forks, issues, lang, pushed_at)
├── aptos_snapshots     28 rows  — hamming swarm wallet balances (all 0 APT)
├── multisig_probes      5 rows  — multisig contract health (all 2-of-2, healthy)
└── mnx_snapshots        1 row   — MNX market status (unavailable)
```

## Schema

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

## Notable Highlights

- **kubeflow/kubeflow**: 15,706 stars — flagship ML platform for Kubernetes (grown from 15,565 in April)
- **plurigrid/gorj**: This repo — active today (2026-06-07), 413 open issues, Clojure/GF(3)/Rama
- **bmorphism/Gay.jl**: Active today — wide-gamut splittable determinism, 189 open issues
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street oxcaml_effect
- **Multisig swarm**: All 5 contracts live and responding on Aptos mainnet (2-of-2)
- **Hamming addresses**: 28 fresh keypairs, no APT balances initialized yet
