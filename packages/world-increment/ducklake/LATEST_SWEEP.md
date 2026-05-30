# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-05-30T21:xx UTC
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| kristinezheng | user | 6 |
| DJedamski | user | 6 |
| **Total** | | **391** |

### GF(3) Trit Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 130 |
| 1 | PLUS | `#b8bb26` | 131 |
| -1 | MINUS | `#cc241d` | 130 |

### Top Repos by Stars (cross-source)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,693 | -- |
| kubeflow/pipelines | 4,150 | Python |
| kubeflow/spark-operator | 3,124 | Python |
| kubeflow/trainer | 2,107 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,463 | Jsonnet |
| kubeflow/manifests | 1,019 | YAML |
| kubeflow/arena | 811 | Go |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 23 | HTML |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |
| bmorphism/say-mcp-server | 20 | JavaScript |
| plurigrid/vcg-auction | 7 | Rust |
| plurigrid/ontology | 8 | JavaScript |

### Notable Activity (plurigrid)

- `gorj` (this repo): 266 open issues -- most active
- `eirobri`: 28 open issues -- EiRoBri replay world
- `nanoclj-zig`: 20 open issues -- NaN-boxed Clojure in Zig
- `ducklings`: 15 open issues
- `ontology`: 16 open issues

### Notable Activity (kubeflow)

- `kubeflow/notebooks`: 195 open issues -- Kubeflow Notebooks
- `kubeflow/sdk`: 134 open issues -- Universal Python SDK
- `kubeflow/trainer`: 128 open issues -- Distributed AI training on K8s

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A-Z)

All 28 Hamming-swarm wallets probed via Aptos mainnet fullnode.
**Result:** All wallets returned 0 APT (CoinStore resource not found or zero balance).
Consistent with accounts not funded on mainnet or CoinStore resource absent.

| World | Balance (APT) |
|-------|--------------|
| alice | 0.0 |
| bob | 0.0 |
| A-Z (26 wallets) | 0.0 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** with 2-of-N signatures required.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | YES |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | YES |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | YES |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | YES |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | YES |

### MNX Testnet Markets

**Status:** Unavailable
`https://testnet.mnx.fi/api/markets` returns 404. The site is a Next.js SPA ("The AI Exchange")
with client-side rendering; market data is not accessible via static fetch.
No market records inserted (1 unavailability marker row).

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| `world_increments` | 391 |
| `repo_snapshots` | 391 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 1 (unavailable marker) |
