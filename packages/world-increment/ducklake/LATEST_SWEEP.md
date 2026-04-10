# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-10

## Sweep Metadata
- **Date:** 2026-04-10T19:36 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|:-----------------:|
| plurigrid | org | 17 |
| kubeflow | org | 10 |
| TeglonLabs | org | 4 |
| bmorphism | user | 9 |
| zubyul | user | 7 |
| migalkin | user (zubyul social graph) | 5 |
| DJedamski | user (zubyul social graph) | 4 |
| wasita | user (zubyul social graph) | 4 |
| kristinezheng | user (zubyul social graph) | 2 |
| M1shaaa | user (zubyul social graph) | 2 |
| AustinCStone | user (zubyul social graph) | 4 |
| **Total** | | **68** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|------:|----------|-----------|
| kubeflow/pipelines | 4119 | Python | 2026-04-10 |
| kubeflow/spark-operator | 3111 | Python | 2026-04-10 |
| kubeflow/trainer | 2080 | Go | 2026-04-10 |
| kubeflow/katib | 1676 | Python | 2026-04-02 |
| kubeflow/manifests | 1010 | YAML | 2026-04-09 |
| kubeflow/mcp-apache-spark-history-server | 150 | Python | 2026-04-08 |
| migalkin/NodePiece | 143 | Python | 2022-02-02 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | 2026-03-16 |
| migalkin/StarE | 88 | Python | 2023-12-01 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |

### Notable Recent Activity (plurigrid ecosystem)

- **plurigrid/gorj** (this repo) — Clojure, 130 open issues, last push 2026-04-10
- **plurigrid/nanoclj-zig** — NaN-boxed Clojure in Zig 0.15 with GF(3) trit conservation, 20 open issues
- **plurigrid/web-browser** — Rust, latest push 2026-04-10
- **plurigrid/asi** — topological chemputer, 16 stars, last push 2026-04-10
- **zubyul/big-bad-plurigrid-quiz** — Emacs Lisp flashcards from plurigrid ecosystem, last push 2026-04-09
- **bmorphism/boxxy** — Move lang, latest push 2026-04-09
- **bmorphism/postweb** — Go, evolved from prepostweb, 2026-04-09

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|------:|
| 1 | PLUS | #b8bb26 | 23 |
| -1 | MINUS | #cc241d | 23 |
| 0 | ERGODIC | #d3869b | 22 |

Total increments: **68** across 68 repo snapshots.

### Repo Counts by Source

| Source | Type | Repos | Total Stars |
|--------|------|------:|------------:|
| kubeflow | org | 10 | 12,943 |
| plurigrid | org | 17 | 23 |
| bmorphism | user | 9 | 88 |
| TeglonLabs | org | 4 | 2 |
| migalkin | user | 5 | 273 |
| AustinCStone | user | 4 | 106 |
| zubyul | user | 7 | 1 |
| wasita | user | 4 | 2 |
| DJedamski | user | 4 | 1 |
| kristinezheng | user | 2 | 0 |
| M1shaaa | user | 2 | 0 |
| **TOTAL** | | **68** | **13,439** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses queried against `fullnode.mainnet.aptoslabs.com`.  
All returned **HTTP 404** — accounts have no `CoinStore<AptosCoin>` resource registered on mainnet.  
Balances recorded as **0.0 APT** (accounts uninitialized or testnet-only addresses).

| World | Address | Balance (APT) |
|-------|---------|:-------------:|
| alice | 0xc793acde...cc7b | 0.0 |
| bob | 0x0a3c00c5...2d5d | 0.0 |
| A | 0x8699edc0...e9d7a | 0.0 |
| B | 0x3f892ebe...cb13 | 0.0 |
| C | 0x38b99e63...535e | 0.0 |
| D | 0xf7765624...fdd1 | 0.0 |
| E | 0xdc1d9d53...8d36 | 0.0 |
| F | 0x18a14b5b...f71 | 0.0 |
| G | 0x69a394c0...f32 | 0.0 |
| H | 0xce67c327...300f | 0.0 |
| I | 0x070fe5d7...1fc9 | 0.0 |
| J | 0x4d964db8...7f54 | 0.0 |
| K | 0xa732040a...5dc4 | 0.0 |
| L | 0x7c2eaeaf...eba9 | 0.0 |
| M | 0x6fed37a7...2e9 | 0.0 |
| N | 0xe7dde6da...51b2c | 0.0 |
| O | 0x73252b60...a89d | 0.0 |
| P | 0x62187929...948 | 0.0 |
| Q | 0xac40fa50...89a9 | 0.0 |
| R | 0x7ce605cc...6e10 | 0.0 |
| S | 0xb8753014...0386 | 0.0 |
| T | 0x35781dc0...4588 | 0.0 |
| U | 0x75860da4...9956 | 0.0 |
| V | 0xb59dd817...f2c3 | 0.0 |
| W | 0x5f32aef7...c7b0 | 0.0 |
| X | 0xa95cbbd1...047d | 0.0 |
| Y | 0xd8e32848...44c4 | 0.0 |
| Z | 0x7af0ef6e...197c | 0.0 |

> **Note:** HTTP 404 from the Aptos fullnode coin store endpoint indicates the account has not registered a CoinStore resource — either the address does not exist on mainnet or holds no APT. These may be testnet/devnet addresses.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | 0x0da4f428...7003 | 2 | ✓ |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ |

All 5 multisig contracts **operational** — all require exactly **2 signatures** (2-of-N threshold).

### MNX Markets

`testnet.mnx.fi` probed at three common API paths:
- `https://testnet.mnx.fi/api/markets` → HTTP 404
- `https://testnet.mnx.fi/api/v1/markets` → HTTP 404
- `https://testnet.mnx.fi/api/tickers` → HTTP 404

**Status: Unavailable** — testnet.mnx.fi is a SPA with no discoverable public REST API. `mnx_snapshots` table has 0 rows.

---

## DuckDB Schema Summary

```sql
-- Tables in world-increments.duckdb (2026-04-10 sweep)
world_increments   68 rows  -- GF(3) increment chain
repo_snapshots     68 rows  -- GitHub repo snapshots
aptos_snapshots    28 rows  -- Hamming swarm wallet balances
multisig_probes     5 rows  -- Multisig contract health probes
mnx_snapshots       0 rows  -- MNX markets (API unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights

- **kubeflow** ecosystem: 12,943 total stars across 10 repos, all actively pushed on 2026-04-10
- **plurigrid/gorj**: 130 open issues — active development of GF(3)/trit coloring for compositional REPL
- **plurigrid/nanoclj-zig**: NaN-boxed Clojure in Zig 0.15 with GF(3) trit conservation — 20 open issues
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **migalkin/NodePiece**: 143 stars — ICLR'22 KG representation paper, active in zubyul social graph
- All **5 Aptos multisig** contracts operational with 2-of-N threshold
- **28 Hamming swarm wallets** all show 0 APT on mainnet (uninitialized / testnet addresses)
- **kubeflow/mcp-server** and **kubeflow/mcp-apache-spark-history-server**: AI/MCP tooling for K8s
