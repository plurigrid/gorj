# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-13T11:10:00Z  
**DuckDB:** `world-increments.duckdb` (v1.5.3 Variegata)  
**GF(3) Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Unique Repos | Max Stars |
|--------|------|-------------|-----------|
| plurigrid | org | 201 | 16 |
| bmorphism | user | 115 | 61 |
| TeglonLabs | org | 56 | 2 |
| kubeflow | org | 47 | 15,572 |
| AustinCStone | user (social) | 43 | 92 |
| wasita | user (social) | 32 | 2 |
| migalkin | user (social) | 30 | 144 |
| zubyul | user | 27 | 2 |
| kristinezheng | user (social) | 19 | 0 |
| M1shaaa | user (social) | 16 | 0 |
| DJedamski | user (social) | 11 | 2 |

**Total unique repos:** 597 across 11 sources  
**Events captured:** 60 (30 bmorphism, 30 zubyul)

### World Increments (GF3 Color Chain)
| GF3 Name | Color | Count |
|----------|-------|-------|
| ERGODIC | #d3869b (pink) | 157 |
| PLUS | #b8bb26 (yellow-green) | 158 |
| MINUS | #cc241d (red) | 158 |
| **Total** | | **473** |

### Recent Event Distribution (bmorphism + zubyul)
| Event Type | Count |
|------------|-------|
| WatchEvent | 17 |
| CreateEvent | 17 |
| PullRequestEvent | 15 |
| PushEvent | 8 |
| ForkEvent | 3 |

### Notable Repos by Source
- **kubeflow/kubeflow** — 15,572 ⭐ (MLOps platform for Kubernetes)
- **kubeflow/pipelines** — 4,119 ⭐ (Python, ML pipelines, pushed 2026-04-14)
- **kubeflow/spark-operator** — 3,114 ⭐ (Python, Spark on K8s, pushed 2026-04-13)
- **kubeflow/trainer** — 2,082 ⭐ (Go, distributed training, pushed 2026-04-13)
- **migalkin/NodePiece** — 144 ⭐ (KG embeddings, Python)
- **bmorphism** top: ocaml-mcp-sdk (61 ⭐), anti-bullshit-mcp-server (23 ⭐)
- **plurigrid/asi** — 16 ⭐ (topological chemputer, HTML)
- **AustinCStone/TextGAN** — 92 ⭐ (text generation with GANs)

### GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, name=ERGODIC, color=#d3869b
- `id mod 3 == 1` → trit=+1, name=PLUS, color=#b8bb26
- `id mod 3 == 2` → trit=-1, name=MINUS, color=#cc241d

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice, bob, A-Z)
All 28 Hamming swarm addresses probed against Aptos mainnet  
via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All 28 addresses returned 0 APT (CoinStore resource not found).  
These accounts have not been funded on Aptos mainnet.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...cb0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes
All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | healthy |
| A-G | 0xf56c...096 | 2 | healthy |
| Y-Z | 0xd3ff...883 | 2 | healthy |
| S-T | 0x3b1c...883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

**5/5 multisig contracts healthy — all require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)
**Unavailable.** The endpoint is a single-page application; REST API paths  
(`/api/markets`, `/api/v1/markets`) returned no structured data.  
`mnx_snapshots` table is empty for this run.

---

## DuckDB Table Counts

| Table | Rows |
|-------|------|
| world_increments | 473 |
| repo_snapshots | 1,334 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```
