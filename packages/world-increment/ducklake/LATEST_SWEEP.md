# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-12T00:00:00Z
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| AustinCStone | user (social graph) | 30 |
| migalkin | user (social graph) | 19 |
| wasita | user (social graph) | 11 |
| M1shaaa | user (social graph) | 8 |
| DJedamski | user (social graph) | 6 |
| kristinezheng | user (social graph) | 5 |
| **TOTAL** | | **381** |

### Top 10 repositories by stars

| Rank | Repo | Stars | Language |
|------|------|-------|----------|
| 1 | kubeflow/kubeflow | 15,714 | — |
| 2 | kubeflow/pipelines | 4,152 | Python |
| 3 | kubeflow/spark-operator | 3,127 | Python |
| 4 | kubeflow/trainer | 2,111 | Go |
| 5 | kubeflow/katib | 1,683 | Python |
| 6 | kubeflow/examples | 1,461 | Jsonnet |
| 7 | kubeflow/manifests | 1,022 | YAML |
| 8 | kubeflow/arena | 812 | Go |
| 9 | kubeflow/kale | 693 | Python |
| 10 | kubeflow/mpi-operator | 528 | Go |

### Stars by source

| Source | Repos | Total Stars |
|--------|-------|-------------|
| kubeflow | 48 | 34,192 |
| migalkin | 19 | 280 |
| bmorphism | 100 | 247 |
| AustinCStone | 30 | 108 |
| plurigrid | 100 | 76 |
| zubyul | 49 | 14 |
| wasita | 11 | 5 |
| DJedamski | 6 | 3 |
| TeglonLabs | 5 | 2 |
| M1shaaa | 8 | 0 |
| kristinezheng | 5 | 0 |

### Notable repos (non-kubeflow)

- **migalkin/NodePiece** — 144★ Python — Compositional Representations for Large Knowledge Graphs (ICLR'22)
- **AustinCStone/TextGAN** — 92★ Python — GAN for text generation in TensorFlow
- **migalkin/StarE** — 89★ Python — Message Passing for Hyper-Relational Knowledge Graphs (EMNLP 2020)
- **bmorphism/ocaml-mcp-sdk** — 61★ OCaml — OCaml SDK for Model Context Protocol
- **bmorphism/anti-bullshit-mcp-server** — 23★ JS — MCP server for analyzing claims
- **bmorphism/risc0-cosmwasm-example** — 23★ Rust — CosmWasm + zkVM RISC-V EFI template
- **bmorphism/say-mcp-server** — 20★ JS — MCP server for macOS text-to-speech
- **bmorphism/babashka-mcp-server** — 19★ JS — MCP server for Babashka
- **plurigrid/gorj** — 0★ Clojure — 515 open issues! forj + Rama + GF(3) trit coloring
- **bmorphism/Gay.jl** — 1★ Julia — 189 open issues! Wide-gamut color sampling

### GF(3) color chain distribution

| Trit | Name | Color | Increments |
|------|------|-------|------------|
| 0 | ERGODIC | `#d3869b` | 127 |
| 1 | PLUS | `#b8bb26` | 127 |
| -1 | MINUS | `#cc241d` | 127 |

Total world increments recorded: **381** (perfectly balanced GF(3) chain)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A-Z)

All 28 Hamming swarm addresses queried against Aptos mainnet
(`fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`).

**Result:** All 28 wallets returned 0 APT. Accounts are either uninitialized or
have no `AptosCoin` CoinStore resource on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B–Z | (see DB) | 0.0 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts responded successfully via
`0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — `testnet.mnx.fi` is behind Vercel deployment
authentication. All API paths (`/api/markets`, `/api/v1/markets`, `/`) return
an auth-required page. No market data accessible without a Vercel bypass token.

---

## Database Tables

| Table | Rows |
|-------|------|
| `world_increments` | 381 |
| `repo_snapshots` | 381 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 (unavailable) |

**Total GitHub stars across sweep:** 34,927
**GF(3) balance:** perfectly uniform — 127 ERGODIC / 127 PLUS / 127 MINUS
