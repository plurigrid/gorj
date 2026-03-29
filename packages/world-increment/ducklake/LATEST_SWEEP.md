# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-03-29T14:00:00Z
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Sweep Summary

### Repos per org/user

| Source | Type | Repos Collected |
|--------|------|-----------------|
| plurigrid | org | 12 |
| kubeflow | org | 12 |
| TeglonLabs | org | 5 |
| bmorphism | user | 4 |
| migalkin | user | 3 |
| DJedamski | user | 2 |
| wasita | user | 2 |
| kristinezheng | user | 2 |
| AustinCStone | user | 2 |
| zubyul | user | 0 (rate-limited) |
| M1shaaa | user | 0 (rate-limited) |

**Total repos:** 44

### Top Repos by Stars

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15540 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4112 | Python | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | 3109 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2069 | Go | Distributed AI Model Training and LLM Fine-Tuning |
| kubeflow/katib | 1673 | Python | Automated Machine Learning on Kubernetes |
| kubeflow/examples | 1459 | Jsonnet | Extended examples and tutorials |
| kubeflow/arena | 810 | Go | A CLI for Kubeflow |
| kubeflow/kale | 681 | Python | Kubeflow's superfood for Data Scientists |
| migalkin/NodePiece | 143 | Python | Compositional Representations for Large Knowledge Graphs |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | OCaml SDK for Model Context Protocol |
| migalkin/StarE | 88 | Python | Message Passing for Hyper-Relational Knowledge Graphs |
| plurigrid/asi | 13 | HTML | everything is topological chemputer! |

### Recent Public Events (bmorphism)

| Actor | Event Type | Repo |
|-------|------------|------|
| bmorphism | IssueCommentEvent | Textualize/textual |
| bmorphism | PullRequestEvent | plurigrid/zig-syrup |
| bmorphism | CreateEvent | bmorphism/zig-syrup-1 |
| bmorphism | ForkEvent | plurigrid/zig-syrup |
| bmorphism | ForkEvent | JuliaWeb/RemoteREPL.jl |

### Recent Public Events (zubyul)

| Actor | Event Type | Repo |
|-------|------------|------|
| zubyul | PushEvent | plurigrid/gorj |
| zubyul | CreateEvent | plurigrid/gorj |
| zubyul | PullRequestEvent | plurigrid/gorj |
| zubyul | PushEvent | plurigrid/gorj |
| zubyul | PullRequestEvent | plurigrid/gorj |

---

## Aptos Hamming Swarm Snapshot

All 28 addresses queried via `https://fullnode.mainnet.aptoslabs.com/v1`.
Balances reflect the APT CoinStore resource at sweep time.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...3cf71 | 0.0 |
| G | 0x69a3...cf32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

> All accounts returned 0 APT (accounts empty or not initialized on mainnet).

---

## Multisig Probes

All 5 multisig contracts responded successfully with `sigs_required=2`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

---

## MNX Markets

**Status: Unavailable**

All three attempted endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) returned HTML (Next.js SPA), not JSON market data. No ticker data could be extracted.

---

## DuckDB Table Row Counts

| Table | Rows |
|-------|------|
| world_increments | 44 |
| repo_snapshots | 44 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## GF(3) Color Chain Applied

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 15 |
| 1 | #b8bb26 | PLUS | 15 |
| -1 | #cc241d | MINUS | 14 |

Color chain applied sequentially to all 44 world_increment rows (`id % 3` determines trit assignment).
