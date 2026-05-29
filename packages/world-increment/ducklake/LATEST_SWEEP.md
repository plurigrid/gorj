# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-29

## Sweep Metadata
- **Date:** 2026-05-29
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 359 |
| Total Repo Snapshots | 359 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (SPA, no public REST) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain Summary

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 119 |
| +1 | `#b8bb26` | PLUS | 120 |
| -1 | `#cc241d` | MINUS | 120 |

Assignment rule: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`

### Sources and Repo Counts

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 48 | 34,147 |
| migalkin | user (social graph) | 19 | 280 |
| bmorphism | user | 100 | 247 |
| AustinCStone | user (social graph) | 8 | 107 |
| plurigrid | org | 100 | 74 |
| zubyul | user | 49 | 14 |
| wasita | user (social graph) | 11 | 5 |
| DJedamski | user (social graph) | 6 | 3 |
| TeglonLabs | org | 4 | 2 |
| kristinezheng | user (social graph) | 6 | 0 |
| M1shaaa | user (social graph) | 8 | 0 |
| **TOTAL** | | **359** | **34,879** |

### Notable Repos by Stars

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,686 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,150 | Python | ML Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,124 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,107 | Go | Distributed AI Model Training on Kubernetes |
| kubeflow/katib | 1,685 | Python | Automated Machine Learning on Kubernetes |
| migalkin/NodePiece | 144 | Python | Parameter-Efficient Representations for KGs (ICLR'22) |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation in TensorFlow |
| migalkin/StarE | 89 | Python | EMNLP 2020: Hyper-Relational KGs |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | OCaml SDK for Model Context Protocol |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | MCP server for claim validation |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | CosmWasm + zkVM RISC-V template |
| plurigrid/asi | 23 | HTML | everything is topological chemputer! |
| bmorphism/say-mcp-server | 20 | JavaScript | macOS text-to-speech MCP server |
| bmorphism/manifold-mcp-server | 14 | JavaScript | Manifold Markets prediction MCP server |
| bmorphism/babashka-mcp-server | 18 | JavaScript | Babashka MCP server |
| plurigrid/gorj | 0 (253 issues) | Clojure | forj + Rama topology nREPL (this repo) |

### Most Active (by pushed_at)

- `kubeflow/pipelines` — pushed 2026-05-29 (today)
- `bmorphism/Gay.jl` — pushed 2026-05-29 (189 open issues)
- `plurigrid/gorj` — pushed 2026-05-29 (this repo, 253 open issues)
- `plurigrid/eirobri` — pushed 2026-05-26
- `kubeflow/manifests` — pushed 2026-05-29

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm addresses queried via Aptos mainnet fullnode
(`fullnode.mainnet.aptoslabs.com`). The legacy
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource returned null for
all 28 addresses. Account sequence numbers are live (e.g. `alice` at seq=72),
indicating these accounts exist but have migrated to the Aptos Fungible Asset
(FA) standard (`0x1::fungible_asset::FungibleStore`) rather than the legacy
coin module. Balances recorded as NULL in `aptos_snapshots`.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793acde...24cc7b | null (FA standard) |
| bob | 0x0a3c00c5...512d5d | null (FA standard) |
| A | 0x8699edc0...e9d7a | null (FA standard) |
| B | 0x3f892ebe...b13 | null (FA standard) |
| C | 0x38b99e63...535e | null (FA standard) |
| D | 0xf7765624...cfdd1 | null (FA standard) |
| E | 0xdc1d9d53...8d36 | null (FA standard) |
| F | 0x18a14b5b...cf71 | null (FA standard) |
| G | 0x69a394c0...7f32 | null (FA standard) |
| H | 0xce67c327...300f | null (FA standard) |
| I | 0x070fe5d7...1fc9 | null (FA standard) |
| J | 0x4d964db8...7f54 | null (FA standard) |
| K | 0xa732040a...5dc4 | null (FA standard) |
| L | 0x7c2eaeaf...eba9 | null (FA standard) |
| M | 0x6fed37a7...7f2e9 | null (FA standard) |
| N | 0xe7dde6da...51b2c | null (FA standard) |
| O | 0x73252b60...5a89d | null (FA standard) |
| P | 0x62187920...ec948 | null (FA standard) |
| Q | 0xac40fa50...c89a9 | null (FA standard) |
| R | 0x7ce605cc...76e10 | null (FA standard) |
| S | 0xb8753014...d0386 | null (FA standard) |
| T | 0x35781dc0...3f4588 | null (FA standard) |
| U | 0x75860da4...ef9956 | null (FA standard) |
| V | 0xb59dd817...af2c3 | null (FA standard) |
| W | 0x5f32aef7...cc7b0 | null (FA standard) |
| X | 0xa95cbbd1...3047d | null (FA standard) |
| Y | 0xd8e32848...2444c4 | null (FA standard) |
| Z | 0x7af0ef6e...e197c | null (FA standard) |

### Multisig Contract Probes (5 contracts)

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.
All contracts are live on Aptos mainnet with **2-of-N** signature threshold.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...87003 | 2 | ✓ |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ |

**Result:** All 5 multisig contracts healthy, all requiring 2 signatures.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a React SPA. Direct REST probes to
`api.testnet.mnx.fi/{markets,v1/markets,api,health}` all returned HTTP 404.
The CSP header indicates the backend at `api.testnet.mnx.fi` and `api.dev.mnx.fi`
requires authenticated WebSocket connections (wss://). No public market data
discoverable via unauthenticated REST. `mnx_snapshots` table left empty.

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)
-- 359 rows, GF(3) chain per repo snapshot

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
-- 359 rows across 11 sources

aptos_snapshots(timestamp, world, address, balance_apt)
-- 28 rows, all balance_apt=null (FA standard migration)

multisig_probes(timestamp, pair, address, sigs_required, healthy)
-- 5 rows, all healthy (sigs_required=2)

mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
-- 0 rows (SPA, no public REST API found)
```
