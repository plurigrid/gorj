# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-02T01:10:00Z  
**DuckDB:** `world-increments.duckdb`  
**GF(3) color chain:** ERGODIC=#d3869b (trit=0) · PLUS=#b8bb26 (trit=1) · MINUS=#cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried

| Source | Type | Repos captured |
|---|---|---|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 7 |
| AustinCStone | user (social) | 5 |
| wasita | user (social) | 5 |
| kristinezheng | user (social) | 4 |
| M1shaaa | user (social) | 4 |
| DJedamski | user (social) | 0 (no public repos) |
| **Total** | | **326** |

### Top repos by stars

| Repo | Stars | Language |
|---|---|---|
| kubeflow/kubeflow | 15,700 | — |
| kubeflow/pipelines | 4,151 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,109 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,019 | YAML |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |

### GF(3) increment distribution

| Name | Color | Count |
|---|---|---|
| ERGODIC (trit=0) | #d3869b | 108 |
| PLUS (trit=1) | #b8bb26 | 109 |
| MINUS (trit=-1) | #cc241d | 109 |

### Notable signals

- **plurigrid** (100 repos): category-theory / cybernetics themes; Scheme, Dart, Julia heavy; active forj/MCP ecosystem
- **kubeflow** (48 repos): dominant ML-infra org; spark-operator and trainer are heavily starred; issues in hundreds
- **TeglonLabs** (4 repos): topoi (Python), mathpix-gem (Ruby/2 stars), monad-mcp-server, coin-flip-mcp
- **bmorphism** (100 repos): MCP servers, prediction markets, esoteric math; manifold-mcp-server top at 14 stars
- **zubyul** (49 repos): quantum telephone, Toad ACP terminal extension, REPL tools; very low star counts
- **migalkin**: knowledge-graph researcher; NodePiece (144 stars, ICLR'22), StarE (89 stars, EMNLP'20)
- **wasita**: Svelte/TypeScript personal site, network science tools, magic-garden Discord bot
- **AustinCStone**: bitmind/bmorphism forks, Python ML tools
- **kristinezheng/M1shaaa**: MIT/Yale cognitive-science student projects (Lookit studies, auditory illusions)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets (alice, bob, A-Z) queried against `fullnode.mainnet.aptoslabs.com`.  
**All returned 0 APT** — accounts have no funded CoinStore on mainnet at time of sweep.

| World | Address (prefix) | Balance (APT) |
|---|---|---|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A | 0x8699ed... | 0.0 |
| B | 0x3f892e... | 0.0 |
| C | 0x38b99e... | 0.0 |
| D | 0xf77656... | 0.0 |
| E | 0xdc1d9d... | 0.0 |
| F | 0x18a14b... | 0.0 |
| G | 0x69a394... | 0.0 |
| H | 0xce67c3... | 0.0 |
| I | 0x070fe5... | 0.0 |
| J | 0x4d964d... | 0.0 |
| K | 0xa73204... | 0.0 |
| L | 0x7c2eae... | 0.0 |
| M | 0x6fed37... | 0.0 |
| N | 0xe7dde6... | 0.0 |
| O | 0x73252b... | 0.0 |
| P | 0x621879... | 0.0 |
| Q | 0xac40fa... | 0.0 |
| R | 0x7ce605... | 0.0 |
| S | 0xb87530... | 0.0 |
| T | 0x357810... | 0.0 |
| U | 0x758600... | 0.0 |
| V | 0xb59dd8... | 0.0 |
| W | 0x5f32ae... | 0.0 |
| X | 0xa95cbb... | 0.0 |
| Y | 0xd8e328... | 0.0 |
| Z | 0x7af0ef... | 0.0 |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4f4... | 2 | healthy |
| A-G | 0xf56c4a... | 2 | healthy |
| Y-Z | 0xd3ffe1... | 2 | healthy |
| S-T | 0x3b1c3a... | 2 | healthy |
| V-W | 0x40fad7... | 2 | healthy |

All multisig pairs require **2-of-N** signatures and responded successfully.

### MNX Markets (testnet.mnx.fi)

**Status: Market data unavailable via REST.**  
`testnet.mnx.fi` is a Next.js SPA. All REST paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return 404.  
The backend at `api.testnet.mnx.fi` serves data exclusively over WebSocket (`wss://api.testnet.mnx.fi`).  
No market rows inserted; sentinel recorded in `mnx_snapshots`.

---

## DuckDB Schema Summary

```sql
world_increments  -- 326 rows (one per repo, GF3-colored)
repo_snapshots    -- 326 rows (full repo metadata)
aptos_snapshots   -- 28 rows  (alice, bob, A-Z balances)
multisig_probes   -- 5 rows   (A-B, A-G, Y-Z, S-T, V-W)
mnx_snapshots     -- 1 row    (unavailable sentinel)
```
