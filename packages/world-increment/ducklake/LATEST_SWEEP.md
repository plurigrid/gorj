# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-31 UTC  
**Branch:** world-increment sweep  
**GF(3) chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d → …

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned

| Source | Type | Repos Snapshotted | Max Stars |
|--------|------|-------------------|-----------|
| kubeflow | org | 17 | 15,800 (kubeflow/kubeflow) |
| migalkin | user | 6 | 144 (NodePiece) |
| AustinCStone | user (social) | 6 | 92 (TextGAN) |
| bmorphism | user | 17 | 61 (ocaml-mcp-sdk) |
| plurigrid | org | 17 | 56 (asi) |
| TeglonLabs | org | 5 | 2 (mathpix-gem) |
| zubyul | user | 11 | 1 (gay-world) |

**Total repos snapshotted:** 79  
**Social graph users not scanned:** DJedamski, wasita, kristinezheng, M1shaaa (queued for next sweep)

### Notable Activity (most recently pushed)

- `plurigrid/gorj` — pushed 2026-07-31 (1,540 open issues)
- `kubeflow/pipelines` — pushed 2026-07-31 (4,172 stars, 505 open issues)
- `kubeflow/spark-operator` — pushed 2026-07-31 (3,142 stars)
- `bmorphism/Gay.jl` — pushed 2026-07-31 (188 open issues)
- `kubeflow/community` — pushed 2026-07-31
- `AustinCStone/byteruckus` — pushed 2026-07-15
- `zubyul/from-possible-worlds` — pushed 2026-07-18

### Language Distribution (top 10)

| Language | Repos |
|----------|-------|
| Python | 24 |
| JavaScript | 11 |
| Rust | 7 |
| Clojure | 6 |
| HTML | 5 |
| Go | 4 |
| Julia | 3 |
| Zig | 2 |
| TeX | 2 |
| Jsonnet | 2 |

### GF(3) World Increment Chain

| Increment ID | Source | GF3 Trit | Color | Name |
|---|---|---|---|---|
| 1 | plurigrid | 1 | #b8bb26 | PLUS |
| 2 | kubeflow | -1 | #cc241d | MINUS |
| 3 | bmorphism | 0 | #d3869b | ERGODIC |
| 4 | zubyul | 1 | #b8bb26 | PLUS |
| 5 | TeglonLabs | -1 | #cc241d | MINUS |
| 6 | migalkin | 0 | #d3869b | ERGODIC |
| 7 | AustinCStone | 1 | #b8bb26 | PLUS |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses: alice, bob, A-Z)

All 28 queried addresses returned **0.0 APT** from the Aptos mainnet CoinStore resource.  
This indicates the wallets have not received mainnet APT (no CoinStore resource initialized).  
The accounts exist as entries in the Aptos address space but have zero on-chain balance.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428...87003 | 2 | YES |
| A-G | 0xf56c4a1c...0096 | 2 | YES |
| Y-Z | 0xd3ffe181...b883 | 2 | YES |
| S-T | 0x3b1c3ae9...7883 | 2 | YES |
| V-W | 0x40fad7b4...eb6d | 2 | YES |

**All 5 multisig contracts healthy** — each requires 2-of-N signatures. Contracts are active and responding on mainnet.

### MNX Markets (testnet.mnx.fi)

Status: **SPA only** — `testnet.mnx.fi` serves a Next.js SPA. All routes (`/`, `/api/markets`, `/api/v1/markets`) return the same HTML shell with no market data in the response body. Market data is loaded client-side via browser JavaScript. No ticker data available from server-side probe.

---

## DuckDB Schema Summary

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 7 |
| repo_snapshots | 79 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA unavailable) |
