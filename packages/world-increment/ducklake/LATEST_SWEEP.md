# World Increment Sweep + Hamming Swarm Snapshot — 2026-07-31

## Sweep Metadata
- **Date:** 2026-07-31
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| kubeflow | org | 49 | 102,167 | 2026-07-31 |
| migalkin | user (social graph) | 19 | 554 | 2026-07-10 |
| bmorphism | user | 100 | 508 | 2026-07-31 |
| AustinCStone | user (social graph) | 41 | 216 | 2026-07-15 |
| plurigrid | org | 100 | 188 | 2026-07-31 |
| zubyul | user | 49 | 40 | 2026-07-18 |
| DJedamski | user (social graph) | 6 | 14 | 2018-03-07 |
| TeglonLabs | org | 5 | 12 | 2026-06-08 |
| wasita | user (social graph) | 12 | 6 | 2026-07-21 |
| kristinezheng | user (social graph) | 5 | 0 | 2026-07-01 |
| M1shaaa | user (social graph) | 8 | 0 | 2026-02-04 |
| **TOTAL** | | **394** | **103,705** | |

### Notable Activity (2026-07-31)

- **kubeflow/pipelines** — 4171★, Python ML pipelines, pushed today
- **kubeflow/spark-operator** — 3142★, K8s Spark operator, pushed today
- **kubeflow/trainer** — 2165★, distributed training, pushed today
- **plurigrid/gorj** — This repo, 1532 open issues, pushed today
- **bmorphism/Gay.jl** — Wide-gamut Julia color lib, 188 open issues, pushed today
- **plurigrid/zig-syrup** — OCapN Syrup in Zig (2★), pushed 2026-07-28
- **TeglonLabs/jank-crane** — crane-jank GF3 convergence maps, C++, pushed 2026-06-08
- **migalkin/NodePiece** — ICLR'22 KG embeddings, 144★
- **bmorphism/ocaml-mcp-sdk** — OCaml MCP SDK, 61★

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 106 |
| 1 | `#b8bb26` | PLUS | 108 |
| -1 | `#cc241d` | MINUS | 107 |

**Total world_increments this run:** 298 new records  
**Cumulative world_increments in DB:** 321  
**Cumulative repo_snapshots in DB:** 1,242

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

Queried 28 Hamming swarm addresses (alice, bob, A–Z) via Aptos mainnet fullnode.

| Metric | Value |
|--------|-------|
| Addresses queried | 28 |
| APT CoinStore found | 0 |
| Total APT balance | 0.0 APT |

All 28 addresses returned no `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource. Wallets are either unfunded on mainnet or use FA (Fungible Asset) standard rather than legacy CoinStore. API was reachable and responded successfully for all queries.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...cfdd | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...7f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...76e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4...7003` | 2 | ✓ healthy |
| A-G | `0xf56c...0096` | 2 | ✓ healthy |
| Y-Z | `0xd3ff...b883` | 2 | ✓ healthy |
| S-T | `0x3b1c...7883` | 2 | ✓ healthy |
| V-W | `0x40fa...eb6d` | 2 | ✓ healthy |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed on mainnet.**

### MNX Markets (testnet.mnx.fi)

- `https://testnet.mnx.fi/api/markets` → HTTP 404
- `https://testnet.mnx.fi/markets` → HTTP 200 (SPA shell, no server-rendered data)

**Status: UNAVAILABLE** — Testnet MNX is a single-page app; no market data is served in the HTML response. No mnx_snapshots rows inserted.

---

## DuckDB Schema & Counts

```
world_increments   321 rows  (GF3-colored repo snapshot events, cumulative)
repo_snapshots    1242 rows  (full repo metadata, cumulative)
aptos_snapshots     28 rows  (A-Z + alice/bob, this run)
multisig_probes      5 rows  (all healthy, 2-sig threshold, this run)
mnx_snapshots        0 rows  (SPA unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
