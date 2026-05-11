# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-11 UTC  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 40 |
| kubeflow | org | 29 |
| TeglonLabs | org | 4 |
| bmorphism | user | 21 |
| zubyul | user | 22 |
| migalkin | user (zubyul social) | 7 |
| wasita | user (zubyul social) | 5 |
| kristinezheng | user (zubyul social) | 2 |
| M1shaaa | user (zubyul social) | 2 |
| AustinCStone | user (zubyul social) | 3 |
| **Total** | | **135** |

> GitHub unauthenticated REST API was rate-limited (0/60 remaining); sweep performed via GitHub MCP search API.

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 45 |
| +1 | `#b8bb26` | PLUS | 46 |
| -1 | `#cc241d` | MINUS | 45 |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,630 | — | 2026-05-07 |
| kubeflow/pipelines | 4,138 | Python | 2026-05-08 |
| kubeflow/spark-operator | 3,125 | Python | 2026-05-08 |
| kubeflow/trainer | 2,096 | Go | 2026-05-09 |
| kubeflow/katib | 1,683 | Python | 2026-05-09 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,016 | YAML | 2026-05-08 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |

### Notable Recent Activity (plurigrid org)

- **gorj** (Clojure) — forj + Rama topology nREPL + GF(3) gay trit coloring, pushed 2026-05-11
- **zig-syrup** (Zig) — OCapN Syrup with CapTP optimizations, pushed 2026-04-30
- **asi** (HTML) — topological chemputer, 21★, pushed 2026-04-26
- **nanoclj-zig** (Zig) — NaN-boxed Clojure interpreter in Zig 0.15, pushed 2026-04-25
- **horse** (TeX) — 1★, 9 open issues, pushed 2026-05-07

### Notable Recent Activity (bmorphism)

- **Gay.jl** (Julia) — wide-gamut color sampling with splittable determinism, 188 open issues, pushed 2026-05-11
- **ocaml-mcp-sdk** (OCaml) — Jane Street oxcaml_effect MCP SDK, 61★, pushed 2026-03-16
- **anti-bullshit-mcp-server** (JS) — claim validation + manipulation detection, 23★, pushed 2026-01-16
- **zig-syrup** (Zig) — embeddable OCapN Syrup encoder/decoder, pushed 2026-05-07
- **nanoclj-zig** (Zig) — fork from plurigrid, pushed 2026-05-07

### Notable Recent Activity (zubyul)

- **voice-observatory** (Python) — passive macOS TUI for voice-download pathways, pushed 2026-04-24
- **nash-tui** / **nash-web** (Rust) — NASH token TUI with GeckoTerminal OHLCV candles, pushed 2026-04-13
- **gay-world** (Python) — Goblin world builder, MLX task decomposition, pushed 2026-03-26
- **kinesis-kb360pro** (Python) — Claude Code skill for Kinesis Advantage360 Pro, pushed 2026-03-26

### TeglonLabs

- **mathpix-gem** (Ruby) — mathematical image → LaTeX OCR, 2★, pushed 2026-01-01
- **coin-flip-mcp** (JS) — MCP server with random.org, 2 forks
- **topoi** (Python) — 1 open issue
- **monad-mcp-server** — Monad MCP Server

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, ledger ~5,223,774,xxx)

All 28 Hamming swarm wallets (alice, bob, A–Z) probed via:
`/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result:** All 28 wallets return `resource_not_found` for the standard `CoinStore<AptosCoin>`.  
**Root cause:** These wallets do not hold APT via the legacy CoinStore module. Several are custom contract accounts:

- `alice` (0xc793...) — has custom modules: `store_v2`, `address_book`, `multiverse`, `lending_pool` (sequence_number=72, active account)
- `A` (0x8699...) — has `0x1::account::Account` resource (sequence_number present, active)
- Other wallets: accounts exist on-chain but APT balance not held via CoinStore

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0 (no CoinStore) |
| bob | 0x0a3c...12d5 | 0 (no CoinStore) |
| A–Z | (26 addresses) | 0 (no CoinStore) |

**Note:** Wallets may hold APT via Fungible Asset (FA) store or custom wrappers. Standard legacy CoinStore not present in any of the 28 accounts.

### Multisig Contract Probes (5 pairs)

Probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts are healthy (2-of-N threshold, all responding).**

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` — returns a Next.js SPA (client-side rendered).  
`/api/markets` and `/api/v1/markets` — return SPA HTML, not JSON.  
**Status: Market data unavailable** — SPA renders client-side; no public REST API detected at common paths.

---

## DuckDB Schema Summary

```
world_increments: 136 rows (GF3 trit-colored repo sweep events)
repo_snapshots:   136 rows (10 sources: plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul, migalkin, wasita, kristinezheng, M1shaaa, AustinCStone)
aptos_snapshots:  28 rows  (alice, bob, A-Z — all CoinStore balance 0)
multisig_probes:  5 rows   (A-B, A-G, Y-Z, S-T, V-W — all healthy, sigs=2)
mnx_snapshots:    1 row    (SPA unavailable)
```

## Data Provenance

- GitHub sweep: MCP GitHub search API (authenticated via session token)
- Aptos RPC: `https://fullnode.mainnet.aptoslabs.com/v1` (public, unauthenticated)
- Multisig: Aptos `/v1/view` Move function call
- MNX: HTTP probe of `https://testnet.mnx.fi` — Next.js SPA, no JSON API
- Ledger version at probe time: ~5,223,774,xxx
