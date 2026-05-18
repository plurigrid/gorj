# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-18
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC `#d3869b` | id%3==1 → trit=1 PLUS `#b8bb26` | id%3==2 → trit=-1 MINUS `#cc241d`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 20 | 32,657 |
| migalkin | user (zubyul social) | 4 | 268 |
| bmorphism | user | 11 | 174 |
| AustinCStone | user (zubyul social) | 3 | 103 |
| plurigrid | org | 36 | 68 |
| wasita | user (zubyul social) | 3 | 3 |
| DJedamski | user (zubyul social) | 4 | 3 |
| TeglonLabs | org | 4 | 2 |
| zubyul | user | 6 | 2 |
| kristinezheng | user (zubyul social) | 3 | 0 |
| M1shaaa | user (zubyul social) | 1 | 0 |
| **TOTAL** | | **95** | **33,280** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,646 | — | 2026-05-07 |
| kubeflow/pipelines | 4,139 | Python | 2026-05-17 |
| kubeflow/spark-operator | 3,126 | Python | 2026-05-15 |
| kubeflow/trainer | 2,100 | Go | 2026-05-15 |
| kubeflow/katib | 1,682 | Python | 2026-05-09 |
| kubeflow/examples | 1,463 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,017 | YAML | 2026-05-16 |
| kubeflow/arena | 810 | Go | 2026-05-07 |
| kubeflow/kale | 687 | Python | 2026-05-15 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |

### GF(3) Trit Distribution (95 increments)

| GF3 Name | Color | Count | Trit |
|----------|-------|-------|------|
| ERGODIC | #d3869b | 31 | 0 |
| PLUS | #b8bb26 | 32 | +1 |
| MINUS | #cc241d | 32 | -1 |

### Notable Recent Activity

- **plurigrid/gorj** (Clojure, 237 issues): forj + Rama topology nREPL routing — pushed 2026-05-18
- **bmorphism/Gay.jl** (Julia, 189 issues): Wide-gamut color sampling with splittable determinism — pushed 2026-05-18
- **wasita/wasita.github.io** (Svelte): personal website — pushed 2026-05-18
- **kubeflow/pipelines** (Python, 4139*): ML Pipelines — pushed 2026-05-17
- **kubeflow/manifests** (YAML, 1017*): AI Reference Platform Manifests — pushed 2026-05-16
- **bmorphism/ocaml-mcp-sdk** (OCaml, 61*): OCaml SDK for MCP — active development
- **TeglonLabs**: mathpix-gem (Ruby/LaTeX OCR), coin-flip-mcp (JS), monad-mcp-server, topoi (Python)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 28 addresses)

All 28 addresses returned **0.0 APT** — no active CoinStore resource found on mainnet for any swarm member at sweep time.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C–Z | (24 more addresses) | 0.0 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** — each requires 2-of-N signatures.

| Pair | Contract Address | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428...87003 | 2 | YES |
| A-G | 0xf56c4a1c...0096 | 2 | YES |
| Y-Z | 0xd3ffe181...b883 | 2 | YES |
| S-T | 0x3b1c3ae9...7883 | 2 | YES |
| V-W | 0x40fad7b4...eb6d | 2 | YES |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Endpoint serves a JavaScript SPA with no accessible JSON API at `/api/markets`. No market data extractable at sweep time.

---

## DuckDB Schema

```
world_increments  — 95 rows  (GF3 trit-colored event log)
repo_snapshots    — 95 rows  (GitHub repo state at sweep time)
aptos_snapshots   — 28 rows  (Hamming swarm wallet balances)
multisig_probes   —  5 rows  (2-of-N multisig health checks)
mnx_snapshots     —  0 rows  (unavailable at sweep time)
```

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent on 2026-05-18.*
