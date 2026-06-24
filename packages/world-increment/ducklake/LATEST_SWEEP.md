# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-24  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.4 (Variegata) — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 56 |
| bmorphism | user | 100 |
| zubyul | user | 27 |
| migalkin | user | 30 |
| DJedamski | user | 11 |
| wasita | user | 32 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| AustinCStone | user | 43 |
| **TOTAL** | | **481 repos + 20 events = 501 world_increments** |

### GF(3) Color Chain Distribution
| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 167 |
| PLUS | #b8bb26 | +1 | 167 |
| MINUS | #cc241d | -1 | 167 |

*Perfect triadic balance. Rule: id%3==0→ERGODIC, id%3==1→PLUS, id%3==2→MINUS*

### Top Languages (across social graph)
| Language | Repos |
|----------|-------|
| Python | 80 |
| HTML | 20 |
| Go | 18 |
| Rust | 16 |
| Jupyter Notebook | 15 |
| JavaScript | 15 |
| TypeScript | 13 |
| Clojure | 9 |
| R | 8 |
| Jsonnet | 7 |

### Notable Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15742 | — | 2026-06-18 |
| kubeflow/pipelines | 4157 | Python | 2026-06-24 |
| kubeflow/spark-operator | 3128 | Python | 2026-06-24 |
| kubeflow/trainer | 2120 | Go | 2026-06-24 |
| kubeflow/katib | 1685 | Python | 2026-06-23 |
| kubeflow/community-distribution | 1028 | YAML | 2026-06-24 |
| kubeflow/arena | 813 | Go | 2026-05-07 |
| kubeflow/mcp-apache-spark-history-server | 178 | Python | 2026-06-23 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| plurigrid/asi | 26 | HTML | 2026-06-10 |
| plurigrid/place | 1 | TeX | 2026-06-24 |

### Recent Events
| User | Event Type | Count |
|------|-----------|-------|
| bmorphism | PushEvent | 6 |
| bmorphism | WatchEvent | 4 |
| zubyul | CreateEvent | 9 |
| zubyul | PushEvent | 1 |

### plurigrid Org Highlights (100 repos)
- `asi` (26★, HTML, pushed 2026-06-10) — most starred
- `place` (TeX, pushed **2026-06-24 today** — most recent push)
- `nash-portal` (Rust), `zig-syrup` (Zig), `vivarium` (Clojure), `nanoclj-zig` (Zig)

### TeglonLabs Org Highlights (56 repos)
- MCP ecosystem: `mcp-terminal`, `agent-client-protocol`, `duck-ui`, `coin-flip-mcp`
- `jank` (pushed 2026-06-08), `Stahl` (Rust), `bison`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet ledger v5908925302)

All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
Accounts are on-chain but have not initialized an APT coin store.

**All 28 balances: 0.0 APT** (alice, bob, A-Z — coin store uninitialized across entire swarm)

### Multisig Contract Probes (5 pairs, mainnet)

Function: `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...4987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...fbc0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...75b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...ded7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...c80eb6d | 2 | HEALTHY |

**All 5 multisig contracts healthy — 2-of-N sigs required.**

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Vercel deployment protection active. Requires `x-vercel-trusted-oidc-idp-token`
or bypass token. No market data extractable from `/api/markets` or `/api/v1/markets`.

---

## DuckDB Tables

| Table | Rows | Notes |
|-------|------|-------|
| world_increments | 501 | GF(3) triadic color chain |
| repo_snapshots | 481 | Full metadata per repo |
| aptos_snapshots | 28 | All 0.0 APT (coin store uninitialized) |
| multisig_probes | 5 | All healthy, 2 sigs required |
| mnx_snapshots | 1 | Sentinel: Vercel auth unavailable |

---

*Generated 2026-06-24 by world-increment-sweep + hamming-swarm-snapshot agent*
