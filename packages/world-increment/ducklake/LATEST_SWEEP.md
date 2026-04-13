# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-13

## Sweep Metadata
- **Date:** 2026-04-13T23:45:00Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Source | Type | Repos | Total Stars | Languages |
|--------|------|-------|-------------|-----------|
| plurigrid | org | 100 | 40 | Clojure, Go, Zig, Rust, Julia, Python, Scheme, Racket, ... |
| kubeflow | org | 47 | 33,872 | TypeScript, Go, Python, Jupyter Notebook, YAML, Jsonnet |
| TeglonLabs | org | 53 | 6 | HTML, Ruby, Python, Rust, TypeScript, JavaScript |
| bmorphism | user | 100 | 131 | Python, Go, Zig, Clojure, Solidity, Move, OCaml, TypeScript, Rust |
| zubyul | user | 24 | 13 | Python, R, Julia, Go, Emacs Lisp, JavaScript |
| migalkin | user (social) | 30 | 277 | Rust, JavaScript, Java, Python, R, Jupyter Notebook |
| DJedamski | user (social) | 11 | 7 | Jupyter Notebook, R, Python |
| wasita | user (social) | 31 | 3 | Typst, Python, Svelte, TypeScript, MATLAB |
| kristinezheng | user (social) | 18 | 0 | JavaScript, CSS, Python, HTML |
| M1shaaa | user (social) | 16 | 0 | TypeScript, JavaScript, HTML, Python |
| AustinCStone | user (social) | 43 | 108 | HTML, C, Haskell, C++, TeX, Python, MATLAB, JavaScript |
| **TOTAL** | | **473** | **34,457** | |

### World Increments (60 events — bmorphism + zubyul recent public events)
| Event Type | Count |
|-----------|-------|
| PushEvent | 28 |
| PullRequestEvent | 14 |
| CreateEvent | 13 |
| IssuesEvent | 2 |
| ForkEvent | 1 |
| WatchEvent | 1 |
| ReleaseEvent | 1 |

**GF(3) Distribution:** PLUS(#b8bb26)=20 | MINUS(#cc241d)=20 | ERGODIC(#d3869b)=20

### Top Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,572 | — | 2026-01-05 |
| kubeflow/pipelines | 4,119 | Python | 2026-04-13 |
| kubeflow/spark-operator | 3,114 | Python | 2026-04-13 |
| kubeflow/trainer | 2,082 | Go | 2026-04-13 |
| kubeflow/katib | 1,678 | Python | 2026-04-13 |
| kubeflow/examples | 1,459 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,010 | YAML | 2026-04-11 |
| kubeflow/arena | 809 | Go | 2026-04-13 |
| kubeflow/kale | 683 | Python | 2026-04-13 |
| kubeflow/mpi-operator | 523 | Go | 2026-04-13 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet — 28 wallets)
All wallets returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~4,864,602,200. Wallets are unfunded on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793acd...24cc7b | — |
| bob | 0x0a3c00c...12d5d | — |
| A | 0x8699edc...e9d7a | — |
| B | 0x3f892eb...cb13 | — |
| C | 0x38b99e6...535e | — |
| D | 0xf77656...cfdd1 | — |
| E | 0xdc1d9d...8d36 | — |
| F | 0x18a14b...3cf71 | — |
| G | 0x69a394...7f32 | — |
| H | 0xce67c3...300f | — |
| I | 0x070fe5...1fc9 | — |
| J | 0x4d964d...7f54 | — |
| K | 0xa73204...25dc4 | — |
| L | 0x7c2eae...eba9 | — |
| M | 0x6fed37...7f2e9 | — |
| N | 0xe7dde6...51b2c | — |
| O | 0x73252b...a89d | — |
| P | 0x621879...ec948 | — |
| Q | 0xac40fa...c89a9 | — |
| R | 0x7ce605...76e10 | — |
| S | 0xb87530...d0386 | — |
| T | 0x35781d...4588 | — |
| U | 0x75860d...f9956 | — |
| V | 0xb59dd8...af2c3 | — |
| W | 0x5f32ae...c7b0 | — |
| X | 0xa95cbb...3047d | — |
| Y | 0xd8e328...444c4 | — |
| Z | 0x7af0ef...197c | — |

### Multisig Contract Probes — 5/5 HEALTHY
All probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428...4987003 | 2-of-2 | HEALTHY |
| A-G | 0xf56c4a1c...bc0096 | 2-of-2 | HEALTHY |
| Y-Z | 0xd3ffe181...75b883 | 2-of-2 | HEALTHY |
| S-T | 0x3b1c3ae9...ed7883 | 2-of-2 | HEALTHY |
| V-W | 0x40fad7b4...80eb6d | 2-of-2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE via REST**  
MNX is a Next.js SPA backed by a WebSocket-only API (`wss://api.testnet.mnx.fi`). No REST market endpoints respond — all return 404. Market data is accessible only via browser WebSocket.

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)        -- 60 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)        -- 473 rows

aptos_snapshots(timestamp, world, address, balance_apt)   -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct) -- 1 row
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,572 stars — flagship ML platform for Kubernetes, active as of 2026
- **kubeflow/pipelines**: 4,119 stars — pushed 2026-04-13 (today)
- **kubeflow/trainer**: 2,082 stars — pushed 2026-04-13 (today)
- **migalkin/NodePiece**: top star in zubyul social graph (277 stars) — scalable KG embeddings
- **bmorphism**: 28 PushEvents today across plurigrid/asi, plurigrid/gorj, and more
- **All 5 multisig pairs** (A-B, A-G, Y-Z, S-T, V-W) confirmed 2-of-2 on Aptos mainnet
- **Hamming swarm**: 28 wallets probed, all unfunded at current ledger height
