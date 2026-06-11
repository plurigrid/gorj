# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-11 UTC  
**DuckDB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| AustinCStone | user | 40 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| **Total** | | **391** |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 130 |
| 1 | PLUS | `#b8bb26` | 131 |
| -1 | MINUS | `#cc241d` | 130 |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,714 | — |
| kubeflow/pipelines | 4,152 | Python |
| kubeflow/spark-operator | 3,126 | Python |
| kubeflow/trainer | 2,111 | Go |
| kubeflow/katib | 1,683 | Python |
| migalkin/NodePiece | 144 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 25 | HTML |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |

### Most Open Issues

| Repo | Issues |
|------|--------|
| plurigrid/gorj | 504 |
| bmorphism/Gay.jl | 189 |
| plurigrid/eirobri | 29 |
| plurigrid/ontology | 16 |
| bmorphism/infinity-topos-impossibility | 14 |

### Notable Activity (2026-06-11 UTC)

- `plurigrid/gorj` — pushed today; 504 open issues; this very repo
- `M1shaaa/M1shaaa` — pushed today (profile config)
- `kubeflow/kubeflow` — pushed today; 15,714 stars
- `bmorphism/Gay.jl` — pushed today; GF(3) color library

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming-swarm wallets (alice, bob, A–Z) queried against Aptos mainnet
via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 wallets returned 0 APT** (accounts unfunded / empty CoinStore).

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793acdec12b4a63… | 0.0 APT |
| bob | 0x0a3c00c58fdf9020… | 0.0 APT |
| A | 0x8699edc0960dd5b9… | 0.0 APT |
| B–Z | (22 more addresses) | 0.0 APT each |

### Multisig Contract Probes (5 pairs)

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da… | 2 | healthy |
| A-G | 0xf56c4a1c0906214f… | 2 | healthy |
| Y-Z | 0xd3ffe1812b2df406… | 2 | healthy |
| S-T | 0x3b1c3ae905d44c3a… | 2 | healthy |
| V-W | 0x40fad7b423a84365… | 2 | healthy |

**All 5 multisig contracts healthy** — 2-of-N threshold confirmed on each pair.

### MNX Markets

`https://testnet.mnx.fi` — **UNAVAILABLE**: Vercel deployment auth gate.
Both `/api/markets` and `/api/v1/markets` return 401/auth HTML.
`mnx_snapshots` table: 0 rows.

---

## DuckDB Schema Summary

```
world_increments  : 391 rows  (GF3-colored repo event log, id%3 chain)
repo_snapshots    : 391 rows  (full repo metadata snapshot)
aptos_snapshots   :  28 rows  (Hamming swarm wallet balances)
multisig_probes   :   5 rows  (2-of-N multisig health)
mnx_snapshots     :   0 rows  (MNX testnet unavailable)
```

### GF(3) Legend

- **trit=0 ERGODIC** `#d3869b` — pink/rose: identity/fixed point
- **trit=1 PLUS** `#b8bb26` — yellow-green: additive
- **trit=-1 MINUS** `#cc241d` — red: subtractive
