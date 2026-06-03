# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-03  
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
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 11 |
| kristinezheng | social graph | 6 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 10 |
| **TOTAL** | | **361** |

### Top 10 Most Recently Pushed

| repo | pushed_at | stars |
|------|-----------|-------|
| kubeflow/pipelines-components | 2026-06-03T02:22:37Z | 11 |
| plurigrid/gorj | 2026-06-03T02:17:06Z | 0 |
| bmorphism/Gay.jl | 2026-06-03T00:48:59Z | 1 |
| kubeflow/dashboard | 2026-06-02T20:32:22Z | 16 |
| kubeflow/notebooks | 2026-06-02T20:24:23Z | 73 |
| kubeflow/pipelines | 2026-06-02T19:02:03Z | 4151 |
| kubeflow/manifests | 2026-06-02T18:56:27Z | 1020 |
| kubeflow/hub | 2026-06-02T17:29:04Z | 175 |
| kubeflow/community | 2026-06-02T15:52:13Z | 195 |
| kubeflow/sdk | 2026-06-02T15:50:57Z | 120 |

### Top 10 by Stars

| repo | language | stars | forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | — | 15,704 | 2,668 |
| kubeflow/pipelines | Python | 4,151 | 2,004 |
| kubeflow/spark-operator | Python | 3,125 | 1,488 |
| kubeflow/trainer | Go | 2,110 | 963 |
| kubeflow/katib | Python | 1,685 | 525 |
| kubeflow/examples | Jsonnet | 1,462 | 755 |
| kubeflow/manifests | YAML | 1,020 | 1,065 |
| kubeflow/arena | Go | 811 | 191 |
| kubeflow/kale | Python | 691 | 155 |
| kubeflow/mpi-operator | Go | 528 | 235 |

### Stars by Org/User

| org_or_user | repos | total_stars |
|-------------|-------|-------------|
| kubeflow | 48 | 34,173 |
| migalkin | 19 | 280 |
| bmorphism | 100 | 246 |
| AustinCStone | 10 | 108 |
| plurigrid | 100 | 75 |
| zubyul | 49 | 14 |
| wasita | 11 | 5 |
| DJedamski | 6 | 3 |
| TeglonLabs | 4 | 2 |
| M1shaaa | 8 | 0 |
| kristinezheng | 6 | 0 |

### GF(3) Color Chain Distribution

| GF(3) Name | Color | Trit | Count |
|------------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 120 |
| PLUS | #b8bb26 | +1 | 121 |
| MINUS | #cc241d | -1 | 120 |

361 world-increments across the color chain. Distribution is near-uniform as expected (⌊361/3⌋ = 120, with 1 extra PLUS).

### Notable Signals

- **plurigrid/gorj** (this repo): 314 open issues, pushed today 2026-06-03 — most active plurigrid repo
- **bmorphism/Gay.jl**: 189 open issues, pushed today — wide-gamut GF(3) color library under heavy development
- **bmorphism/ocaml-mcp-sdk**: 61 stars — highest-starred bmorphism repo, OCaml SDK for MCP
- **migalkin/NodePiece**: 144 stars — ICLR'22 compositional KG representations
- **TeglonLabs/mathpix-gem**: Ruby gem for math OCR, 11 open issues
- **kubeflow/kubeflow**: 15,704 stars — dominant star count in the entire sweep

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (A–Z + alice/bob)

All 28 addresses queried against Aptos mainnet via  
`GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result:** All 28 addresses returned `resource_not_found` — the `CoinStore<AptosCoin>` resource is not initialized on any of these accounts at Ledger version 5,542,282,635. Accounts may use the FA (Fungible Asset) balance standard or have no APT deposits.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793acdec12b4a... | 0.0 (not initialized) |
| bob | 0x0a3c00c58fdf90... | 0.0 (not initialized) |
| A | 0x8699edc0960dd5... | 0.0 (not initialized) |
| B | 0x3f892ebe6e4516... | 0.0 (not initialized) |
| C | 0x38b99e63ada9b6... | 0.0 (not initialized) |
| D | 0xf77656248f64d5... | 0.0 (not initialized) |
| E | 0xdc1d9d533bac35... | 0.0 (not initialized) |
| F | 0x18a14b5b4bec11... | 0.0 (not initialized) |
| G | 0x69a394c0b0ac84... | 0.0 (not initialized) |
| H | 0xce67c327a7844e... | 0.0 (not initialized) |
| I | 0x070fe5d74e4eda... | 0.0 (not initialized) |
| J | 0x4d964db8f53837... | 0.0 (not initialized) |
| K | 0xa732040a6b0d55... | 0.0 (not initialized) |
| L | 0x7c2eaeafad9725... | 0.0 (not initialized) |
| M | 0x6fed37a7553ef1... | 0.0 (not initialized) |
| N | 0xe7dde6da0a65f5... | 0.0 (not initialized) |
| O | 0x73252b6011a751... | 0.0 (not initialized) |
| P | 0x6218792de4a9bc... | 0.0 (not initialized) |
| Q | 0xac40fa50b81b4c... | 0.0 (not initialized) |
| R | 0x7ce605cc8fda4f... | 0.0 (not initialized) |
| S | 0xb8753014e4888e... | 0.0 (not initialized) |
| T | 0x35781dc0e42fef... | 0.0 (not initialized) |
| U | 0x75860da47565f6... | 0.0 (not initialized) |
| V | 0xb59dd8170321df... | 0.0 (not initialized) |
| W | 0x5f32aef70f5ba5... | 0.0 (not initialized) |
| X | 0xa95cbbd116548a... | 0.0 (not initialized) |
| Y | 0xd8e32848f1dffa... | 0.0 (not initialized) |
| Z | 0x7af0ef6e1bd706... | 0.0 (not initialized) |

### Multisig Contract Probes

All 5 multisig accounts probed via `POST /v1/view` →  
`0x1::multisig_account::num_signatures_required`

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428a0c007... | 2 | ✅ |
| A-G | 0xf56c4a1c090621... | 2 | ✅ |
| Y-Z | 0xd3ffe1812b2df4... | 2 | ✅ |
| S-T | 0x3b1c3ae905d44c... | 2 | ✅ |
| V-W | 0x40fad7b423a843... | 2 | ✅ |

All 5 multisig contracts are healthy 2-of-2 threshold configurations.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi/api/markets` → **404 (SPA page)**  
`https://api.testnet.mnx.fi/markets` → **Cannot GET** (no public REST endpoint)

MNX is a Next.js SPA ("The AI Exchange") that fetches data from `wss://api.testnet.mnx.fi` over WebSocket and authenticated REST. No public market data endpoint is accessible without auth/WS session. Recorded as **unavailable** in `mnx_snapshots` (0 rows).

---

## DuckDB Schema Summary

```
world-increments.duckdb
├── world_increments  (361 rows) — GF(3)-colored event log
├── repo_snapshots    (361 rows) — GitHub repo metadata
├── aptos_snapshots    (28 rows) — Hamming swarm wallet balances
├── multisig_probes     (5 rows) — Aptos multisig health
└── mnx_snapshots       (0 rows) — MNX market data (unavailable)
```
