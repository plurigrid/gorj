# World-Increment Sweep + Hamming Swarm Snapshot

**Swept:** 2026-06-07  
**GF(3) Color Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | social graph | 40 |
| migalkin | social graph | 19 |
| M1shaaa | social graph | 8 |
| DJedamski | social graph | 6 |
| TeglonLabs | org | 4 |
| wasita | social graph | 0 (no public repos) |
| kristinezheng | social graph | 0 (no public repos) |

**Total unique repos snapshotted:** 643  
**DuckDB:** `world_increments` (397 entries), `repo_snapshots` (1318 rows), `aptos_snapshots` (28), `multisig_probes` (5)

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,706 | — |
| kubeflow/pipelines | 4,153 | Python |
| kubeflow/spark-operator | 3,126 | Python |
| kubeflow/trainer | 2,112 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,020 | YAML |
| kubeflow/arena | 811 | Go |
| plurigrid/asi | 25 | HTML |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |

### Recently Active Plurigrid Repos (2026)

- `plurigrid/place` — TeX, pushed 2026-06-04
- `plurigrid/eirobri` — Clojure (EiRoBri replay world), pushed 2026-06-03
- `plurigrid/gorj` — Clojure (forj + GF(3) trit coloring), 423 open issues, pushed 2026-06-07
- `plurigrid/nash-portal` — Rust (WASM TUI + GeckoTerminal candlesticks)

### bmorphism Activity Highlights

- `bmorphism/Gay.jl` — Julia, GF(3) SplitMix splittable coloring, active 2026-06-07
- `bmorphism/ocaml-mcp-sdk` — OCaml MCP SDK (Jane Street oxcaml_effect), ★61
- `bmorphism/anti-bullshit-mcp-server` — JavaScript claim analysis MCP, ★23
- `bmorphism/world` — Python local worlds launcher

### GF(3) Trit Distribution

| Trit | Name | Color | Entries |
|------|------|-------|---------|
| 0 | ERGODIC | #d3869b | 131 |
| +1 | PLUS | #b8bb26 | 133 |
| −1 | MINUS | #cc241d | 133 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Chain:** Aptos Mainnet `fullnode.mainnet.aptoslabs.com`

### Wallet Balances (28 worlds: alice, bob, A–Z)

All 28 addresses queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
**Result:** All wallets returned 0 APT — no `CoinStore` resource registered on-chain (uninitialized accounts).

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

Probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4…7003 | 2 | ✅ |
| A-G | 0xf56c…0096 | 2 | ✅ |
| Y-Z | 0xd3ff…b883 | 2 | ✅ |
| S-T | 0x3b1c…7883 | 2 | ✅ |
| V-W | 0x40fa…eb6d | 2 | ✅ |

All 5 multisig accounts are live with 2-of-N threshold.

### MNX Markets

**UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection. No market data extracted.

---

## DuckDB Path

`packages/world-increment/ducklake/world-increments.duckdb`

```
world_increments   397 rows  — GF(3)-colored repo event log
repo_snapshots    1318 rows  — GitHub repo metadata (9 sources)
aptos_snapshots     28 rows  — Hamming swarm APT balances
multisig_probes      5 rows  — Aptos multisig health
mnx_snapshots        0 rows  — MNX testnet (unavailable)
```
