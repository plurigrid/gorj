# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-04-20  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 20 (top active) |
| TeglonLabs | org | 4 |
| bmorphism | user | 20 |
| zubyul | user | 17 |
| migalkin | user (zubyul social graph) | 7 |
| wasita | user (zubyul social graph) | 6 |
| AustinCStone | user (zubyul social graph) | 8 |
| DJedamski | user (zubyul social graph) | 4 |
| kristinezheng | user (zubyul social graph) | 4 |
| M1shaaa | user (zubyul social graph) | 4 |
| **TOTAL** | | **194** |

### Top Repos by Stars

| Org/User | Repo | Stars |
|----------|------|-------|
| kubeflow | kubeflow | 15,585 |
| kubeflow | pipelines | 4,123 |
| kubeflow | spark-operator | 3,116 |
| kubeflow | trainer | 2,086 |
| kubeflow | katib | 1,680 |
| kubeflow | examples | 1,460 |
| kubeflow | manifests | 1,012 |
| kubeflow | arena | 810 |
| bmorphism | ocaml-mcp-sdk | 60 |
| bmorphism | anti-bullshit-mcp-server | 23 |
| migalkin | NodePiece | 143 |
| migalkin | StarE | 89 |
| plurigrid | asi | 17 |

### GF(3) Trit Color Chain (world_increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 72 |
| 1 | `#b8bb26` | PLUS | 73 |
| -1 | `#cc241d` | MINUS | 72 |
| **Total** | | | **217** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A-Z) probed via Aptos fullnode mainnet API.  
**Result:** All addresses return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — wallets hold no APT in native coin store (unfunded or using other token stores).

| World | Total APT |
|-------|-----------|
| All 28 (alice, bob, A-Z) | 0.00 APT |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428...987003` | 2 | HEALTHY |
| A-G | `0xf56c4a1c...0096` | 2 | HEALTHY |
| Y-Z | `0xd3ffe181...b883` | 2 | HEALTHY |
| S-T | `0x3b1c3ae9...7883` | 2 | HEALTHY |
| V-W | `0x40fad7b4...eb6d` | 2 | HEALTHY |

All 5 multisig accounts require **2-of-N signatures** and respond normally.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** - DNS resolution failed. No market data fetched. Recorded as unavailable in `mnx_snapshots`.

---

## DuckDB Schema Summary

```
world_increments  : 217 rows  (GF3 trit-colored event log)
repo_snapshots    : 194 unique repos inserted this sweep
aptos_snapshots   : 28 rows   (Hamming swarm A-Z + alice + bob)
multisig_probes   : 5 rows    (all healthy, 2-of-N)
mnx_snapshots     : 1 row     (unavailable)
```

---

## Notable Activity

- **plurigrid/gorj**: 232 open issues, Clojure, pushed 2026-04-19
- **plurigrid/nanoclj-zig**: Zig Clojure interpreter with GF(3) trit conservation, 21 issues
- **plurigrid/bci-blue-share**: BCI signal infrastructure pushed 2026-04-19
- **plurigrid/nash-portal**: NASH token TUI (ratzilla WASM + GeckoTerminal), pushed 2026-04-15
- **bmorphism/Gay.jl**: Wide-gamut color sampling, 187 open issues - highly active
- **kubeflow/mcp-apache-spark-history-server**: New MCP+Spark bridge, 151 stars (2025-06-26)
- **zubyul/tilelang-kernels**: GPU kernels for GF(3) trit classification + Sinkhorn OT
- **migalkin/NodePiece**: 143 stars, compositional KG representations (ICLR 2022)
- **wasita/wasita.github.io**: Personal site (Svelte), active 2026-04-13
