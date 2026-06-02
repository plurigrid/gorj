# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-02  
**Sweep IDs:** 1–100 (GF3 color chain applied)  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Sampled | Notes |
|--------|------|--------------|-------|
| plurigrid | org | 24 | Active Clojure/Zig/Rust ecosystem |
| kubeflow | org | 20 | ML platform, 15.7k⭐ flagship |
| TeglonLabs | org | 6 | MCP servers, mathpix-gem |
| bmorphism | user | 18 | OCaml MCP SDK (61⭐), anti-bullshit-mcp |
| zubyul | user | 15 | Gay.jl, NASH TUI, OpenBCI |
| migalkin | social | 3 | Knowledge graph / GNN research |
| wasita | social | 3 | Personal site (Svelte, active 2026-06-01) |
| M1shaaa | social | 4 | Lab research, Yale |
| AustinCStone | social | 3 | Profile sweep |
| kristinezheng | social | 2 | Social node |
| DJedamski | social | 2 | Social node |

**Total increments:** 100  
**GF(3) color chain distribution:**

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 32 |
| +1 | `#b8bb26` | PLUS | 34 |
| -1 | `#cc241d` | MINUS | 34 |

### Top Repos by Stars (this sweep)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,700 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,151 | 2026-06-01 |
| kubeflow/spark-operator | Python | 3,125 | 2026-06-01 |
| kubeflow/trainer | Go | 2,109 | 2026-05-30 |
| kubeflow/katib | Python | 1,685 | 2026-05-29 |
| kubeflow/examples | Jsonnet | 1,462 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,019 | 2026-05-29 |
| kubeflow/arena | Go | 811 | 2026-05-07 |
| kubeflow/kale | Python | 691 | 2026-06-01 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| plurigrid/asi | HTML | 24 | 2026-04-26 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| bmorphism/risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| bmorphism/say-mcp-server | JavaScript | 20 | 2025-01-07 |
| bmorphism/babashka-mcp-server | JavaScript | 18 | 2025-01-05 |
| plurigrid/vcg-auction | Rust | 7 | 2023-03-16 |
| plurigrid/ontology | JavaScript | 8 | 2025-05-27 |
| plurigrid/gorj | Clojure | 0 | 2026-06-01 (296 open issues) |

### Notable Activity

- **plurigrid/gorj** (this repo): 296 open issues, pushed 2026-06-01 — highest issue velocity in plurigrid
- **plurigrid/eirobri**: 28 open issues, EiRoBri replay world
- **bmorphism/Gay.jl**: 189 open issues, wide-gamut color sampling — primary Gay.jl hub
- **kubeflow/mcp-apache-spark-history-server**: 173⭐ new MCP integration for Spark
- **wasita/wasita.github.io**: active personal site, pushed 2026-06-01

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 addresses (alice, bob, A–Z) via Aptos fullnode mainnet API.

| Result | Count |
|--------|-------|
| Wallets queried | 28 |
| Funded wallets (> 0 APT) | 0 |
| Total APT across all wallets | 0.0 |

All 28 addresses returned no `CoinStore<AptosCoin>` resource — addresses exist on-chain but hold no APT balance (likely test/swarm addresses not yet funded on mainnet).

### Multisig Contract Probes (5/5 Healthy)

| Pair | Contract Address | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | `0x0da4f428...4987003` | 2 | ✓ healthy |
| A-G | `0xf56c4a1c...fbc0096` | 2 | ✓ healthy |
| Y-Z | `0xd3ffe181...e75b883` | 2 | ✓ healthy |
| S-T | `0x3b1c3ae9...ded7883` | 2 | ✓ healthy |
| V-W | `0x40fad7b4...c80eb6d` | 2 | ✓ healthy |

All 5 multisig contracts respond with `num_signatures_required = 2`. Swarm ring is **100% operational**.

### MNX Markets

`testnet.mnx.fi/api/markets` returned **HTTP 404** — testnet API endpoint unavailable at sweep time. No market data captured.

---

## DuckDB Schema Summary

```sql
world_increments  -- 100 rows (this sweep)
repo_snapshots    -- current sweep + historical (504 unique repos)
aptos_snapshots   -- 28 rows
multisig_probes   -- 5 rows
mnx_snapshots     -- 0 rows (unavailable)
```

## GF(3) Color Chain Legend

- **ERGODIC** `#d3869b` (trit=0): id mod 3 == 0 — stationary distribution node
- **PLUS** `#b8bb26` (trit=+1): id mod 3 == 1 — positive increment
- **MINUS** `#cc241d` (trit=-1): id mod 3 == 2 — negative increment
