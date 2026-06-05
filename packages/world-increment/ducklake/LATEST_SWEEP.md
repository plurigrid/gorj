# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-05
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul social graph) | 7 |
| wasita | user (zubyul social graph) | 5 |
| AustinCStone | user (zubyul social graph) | 6 |
| DJedamski | user (zubyul social graph) | 5 |
| kristinezheng | user (zubyul social graph) | 3 |
| M1shaaa | user (zubyul social graph) | 3 |
| **TOTAL** | | **330** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 110 |
| 1 | `#b8bb26` | PLUS | 110 |
| -1 | `#cc241d` | MINUS | 110 |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15706 | — | 2026-05-24 |
| kubeflow/pipelines | 4152 | Python | 2026-06-05 |
| kubeflow/spark-operator | 3125 | Python | 2026-06-04 |
| kubeflow/trainer | 2111 | Go | 2026-06-05 |
| kubeflow/katib | 1684 | Python | 2026-06-04 |
| kubeflow/examples | 1462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1020 | YAML | 2026-06-05 |
| kubeflow/arena | 811 | Go | 2026-05-07 |
| kubeflow/kale | 690 | Python | 2026-06-04 |
| kubeflow/mpi-operator | 528 | Go | 2026-06-02 |

### Notable plurigrid Activity (most recently pushed)

| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| gorj | Clojure | 0 | forj + Rama topology nREPL routing + GF(3) gay trit coloring |
| eirobri | Clojure | 0 | EiRoBri replay world |
| place | TeX | 1 | — |
| nash-portal | Rust | 2 | NASH token TUI — ratzilla WASM + GeckoTerminal OHLCV |
| zig-syrup | Zig | 2 | High-performance OCapN Syrup with CapTP optimizations |
| asi | HTML | 25 | everything is topological chemputer! |

### Notable bmorphism Activity (most recently pushed)

| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| world | Python | 0 | Local worlds launcher for SA3, jank, and world proofs |
| Gay.jl | Julia | 1 | Wide-gamut color sampling with splittable determinism |
| ocaml-mcp-sdk | OCaml | 61 | OCaml SDK for MCP using Jane Street's oxcaml_effect |
| anti-bullshit-mcp-server | JavaScript | 23 | MCP server for analyzing claims + detecting manipulation |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 wallets queried via `https://fullnode.mainnet.aptoslabs.com/v1/`.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A | 0x8699ed... | 0.0 |
| B | 0x3f892e... | 0.0 |
| C | 0x38b99e... | 0.0 |
| D | 0xf77656... | 0.0 |
| E | 0xdc1d9d... | 0.0 |
| F | 0x18a14b... | 0.0 |
| G | 0x69a394... | 0.0 |
| H | 0xce67c3... | 0.0 |
| I | 0x070fe5... | 0.0 |
| J | 0x4d964d... | 0.0 |
| K | 0xa73204... | 0.0 |
| L | 0x7c2eae... | 0.0 |
| M | 0x6fed37... | 0.0 |
| N | 0xe7dde6... | 0.0 |
| O | 0x73252b... | 0.0 |
| P | 0x621879... | 0.0 |
| Q | 0xac40fa... | 0.0 |
| R | 0x7ce605... | 0.0 |
| S | 0xb87530... | 0.0 |
| T | 0x35781d... | 0.0 |
| U | 0x75860d... | 0.0 |
| V | 0xb59dd8... | 0.0 |
| W | 0x5f32ae... | 0.0 |
| X | 0xa95cbb... | 0.0 |
| Y | 0xd8e328... | 0.0 |
| Z | 0x7af0ef... | 0.0 |

> All CoinStore resources returned empty — wallets exist on-chain but hold 0 APT or have not registered the native coin store.

### Multisig Contract Probes

All probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | ✓ |
| A-G | 0xf56c4a... | 2 | ✓ |
| Y-Z | 0xd3ffe1... | 2 | ✓ |
| S-T | 0x3b1c3a... | 2 | ✓ |
| V-W | 0x40fad7... | 2 | ✓ |

> All 5 multisig accounts require 2-of-N signatures. All respond as healthy.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `https://testnet.mnx.fi` is deployed behind Vercel Deployment Protection (visitor password required). All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) redirect to the auth wall. No market data extractable without bypass token.

---

## DuckDB Schema

```
world-increments.duckdb
├── world_increments    (330 rows)  — GF(3) trit-colored increment log
├── repo_snapshots      (330 rows)  — GitHub repo metadata by increment
├── aptos_snapshots     (28 rows)   — Hamming swarm APT balances
├── multisig_probes     (5 rows)    — Multisig 2-of-N health checks
└── mnx_snapshots       (1 row)     — MNX exchange (unavailable)
```

### Sample Queries

```sql
-- Top sources by repo count
SELECT source_name, COUNT(*) as repos
FROM world_increments
GROUP BY source_name ORDER BY repos DESC;

-- GF(3) color distribution
SELECT gf3_color, gf3_name, gf3_trit, COUNT(*)
FROM world_increments GROUP BY 1,2,3;

-- Multisig health summary
SELECT pair, sigs_required, healthy FROM multisig_probes;
```
