# World-Increment Sweep + Hamming Snapshot — 2026-07-17

## Sweep Metadata
- **Date:** 2026-07-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 9 (top by activity) |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 7 (public) |
| migalkin | user (social) | 4 (top) |
| AustinCStone | user (social) | 2 (recent) |
| DJedamski | user (social) | 1 |
| wasita | user (social) | 2 |
| kristinezheng | user (social) | 1 |
| M1shaaa | user (social) | 1 |
| **Total** | | **232 this sweep** |

### GF(3) Color Chain Distribution (this sweep)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 84 |
| 1 | #b8bb26 | PLUS | 86 |
| -1 | #cc241d | MINUS | 85 |

### Top Repos by Stars (this sweep)

| Repo | Language | Stars |
|------|----------|-------|
| kubeflow/kubeflow | — | 15,779 |
| kubeflow/pipelines | Python | 4,167 |
| kubeflow/spark-operator | Python | 3,137 |
| kubeflow/trainer | Go | 2,151 |
| kubeflow/katib | Python | 1,690 |
| kubeflow/community-distribution | YAML | 1,029 |
| migalkin/NodePiece | Python | 144 |
| AustinCStone/TextGAN | Python | 92 |
| migalkin/StarE | Python | 89 |
| plurigrid/asi | HTML | 30 |

### Top Languages (cumulative DB)

| Language | Repos |
|----------|-------|
| Python | 190 |
| Rust | 53 |
| HTML | 47 |
| JavaScript | 43 |
| Go | 41 |
| TypeScript | 39 |
| Clojure | 29 |
| Jupyter Notebook | 29 |
| Julia | 19 |
| Jsonnet | 16 |

### Notable Activity (pushed today / this week)

- **plurigrid/gorj** (Clojure) — pushed 2026-07-17, active forj MCP server
- **kubeflow/trainer** — pushed 2026-07-17 02:22 UTC; Distributed AI / LLM fine-tuning on Kubernetes
- **kubeflow/mcp-apache-spark-history-server** — pushed 2026-07-16; MCP Server for Spark debugging
- **wasita/wasita.github.io** (Svelte) — pushed 2026-07-16
- **wasita/pnas-typst-template** — pushed 2026-07-16
- **AustinCStone/byteruckus** (HTML) — pushed 2026-07-15
- **TeglonLabs/jank-crane** (C++) — crane-jank converged-IR hub with GF3 convergence maps

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-17)

> Method: `0x1::coin::balance` view function  
> Note: `CoinStore` REST resource returns 404 (accounts migrated to FungibleAsset framework);
> view function still works for APT legacy coin balances.

| World | Balance (APT) | Address (truncated) |
|-------|--------------|---------------------|
| bob | 12.657007 | 0x0a3c00c58f... |
| F | 1.960516 | 0x18a14b5b4b... |
| L | 1.927269 | 0x7c2eaeafad... |
| J | 1.895093 | 0x4d964db8f5... |
| alice | 0.436434 | 0xc793acdec1... |
| O | 0.210136 | 0x73252b6011... |
| K | 0.161961 | 0xa732040a6b... |
| P | 0.140136 | 0x62187921de... |
| M | 0.112285 | 0x6fed37a755... |
| N | 0.106121 | 0xe7dde6da0a... |
| Q | 0.103240 | 0xac40fa50b8... |
| S | 0.091788 | 0xb8753014e4... |
| R | 0.090217 | 0x7ce605cc8f... |
| T | 0.073713 | 0x35781dc0e4... |
| U | 0.055773 | 0x75860da475... |
| A | 0.051767 | 0x8699edc096... |
| X | 0.042577 | 0xa95cbbd116... |
| W | 0.040705 | 0x5f32aef70f... |
| Y | 0.044449 | 0xd8e32848f1... |
| B | 0.036256 | 0x3f892ebe6e... |
| Z | 0.024268 | 0x7af0ef6e1b... |
| D | 0.011629 | 0xf77656248f... |
| C | 0.010185 | 0x38b99e63ad... |
| E | 0.009372 | 0xdc1d9d533b... |
| H | 0.001681 | 0xce67c327a7... |
| G | 0.000681 | 0x69a394c0b0... |
| I | 0.000681 | 0x070fe5d74e... |
| V | 0.048833 | 0xb59dd81703... |

**Total APT across swarm: 20.344773 APT**

Key observations:
- `bob` holds **62.2%** of total swarm APT (12.657 / 20.345)
- Cluster F/J/L all hold ~1.9 APT — likely a funded trio
- Worlds G, H, I are near-dust (< 0.002 APT each)
- alice has sequence_number=72 — most active account

### Multisig Contract Probes

All 5 multisig pairs are **healthy** — all require 2-of-N signatures.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df406... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a... | 2 | ✓ |
| V-W | 0x40fad7b423a84365... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — `testnet.mnx.fi` is behind Vercel deployment protection. Authentication required (no bypass token). API endpoints `/api/markets` and `/api/v1/markets` both return auth-gated HTML. Marked as unavailable in `mnx_snapshots` table.

---

## DuckDB Tables (cumulative)

| Table | Rows |
|-------|------|
| world_increments | 255 |
| repo_snapshots | 1,176 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable marker) |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
