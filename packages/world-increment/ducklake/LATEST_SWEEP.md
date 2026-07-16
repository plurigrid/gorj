# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-16

## Sweep Metadata
- **Date:** 2026-07-16 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (duckdb 1.5.4)
- **Increment ID:** 25 → GF3 trit=**1** (PLUS) color **#b8bb26**

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 25 |
| Total Repo Snapshots | 984 |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

**Proxy scope note:** External GitHub REST API is blocked; only `plurigrid/gorj` is in scope. Repo data collected via MCP GitHub search (plurigrid org, 50 of 55 repos returned). kubeflow, TeglonLabs, bmorphism, zubyul, and social graph users (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone) were unreachable this run.

### plurigrid org — Top repos by recency (this run: 20 inserted)

| Repo | Language | Stars | Forks | Open Issues | Pushed |
|------|----------|-------|-------|-------------|--------|
| gorj | Clojure | 1 | 0 | **1202** | 2026-07-16 |
| asi | HTML | **30** | **10** | 4 | 2026-07-10 |
| place | TeX | 1 | 1 | 13 | 2026-07-14 |
| eirobri | Clojure | 0 | 0 | 30 | 2026-07-14 |
| shrimp | — | 0 | 0 | 0 | 2026-07-03 |
| nash-portal | Rust | 2 | 3 | 1 | 2026-05-19 |
| zig-syrup | Zig | 2 | 2 | 0 | 2026-04-30 |
| asi-skills | Julia | 3 | 0 | 0 | 2026-04-26 |
| nanoclj-zig | Zig | 1 | 1 | 20 | 2026-04-25 |
| ontology | JavaScript | 8 | 9 | 16 | 2025-05-27 |

### Social graph coverage

| Source | Status |
|--------|--------|
| plurigrid org | ✅ 50 repos fetched (MCP search) |
| kubeflow, TeglonLabs orgs | ❌ proxy blocked this session |
| bmorphism, zubyul + 6 social users | ❌ proxy blocked this session |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-07-16)

All 28 addresses queried against `fullnode.mainnet.aptoslabs.com/v1`. All returned `resource_not_found` — no `CoinStore<AptosCoin>` resource on mainnet for any Hamming world address.

| Range | Count | Total APT |
|-------|-------|-----------|
| alice, bob | 2 | 0.000 |
| A–Z (26 worlds) | 26 | 0.000 |
| **Grand total** | **28** | **0.000 APT** |

Status: addresses are unfunded on mainnet (Aptos API reachable, ledger version ~6.3B).

### Multisig Contract Probes — All 5 Healthy ✅

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | `0x0da4f428…` | 2 | ✅ |
| A-G | `0xf56c4a1c…` | 2 | ✅ |
| Y-Z | `0xd3ffe181…` | 2 | ✅ |
| S-T | `0x3b1c3ae9…` | 2 | ✅ |
| V-W | `0x40fad7b4…` | 2 | ✅ |

All contracts respond correctly with `num_signatures_required = 2`.

### MNX Markets (testnet.mnx.fi)

All probed endpoints returned **HTTP 401 Unauthorized** — market data requires authentication. Recorded as unavailable in mnx_snapshots.

---

## GF(3) Color Chain

- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=**MINUS**

Increment #25 → **PLUS** (#b8bb26) — 8th PLUS in the chain.

---

## Prior Run Highlights (from DB history)
- **kubeflow/kubeflow**: 15,565 stars (from 2026-04-12 sweep)
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK
- **migalkin/NodePiece**: 143 stars — scalable KG embeddings
- **plurigrid/asi**: grew from 16→30 stars since April 2026 sweep
