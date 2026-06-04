# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-04

## Sweep Metadata
- **Date:** 2026-06-04  
- **Agent:** world-increment-sweep + hamming-swarm-snapshot  
- **DuckDB version:** v1.5.3 (Variegata)  
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Snapshotted | Total Stars |
|--------|------|-------------------|-------------|
| kubeflow | org | 19 | 32,743 |
| migalkin | user (social) | 6 | 279 |
| bmorphism | user | 18 | 188 |
| AustinCStone | user (social) | 6 | 104 |
| plurigrid | org | 30 | 74 |
| zubyul | user | 13 | 8 |
| wasita | user (social) | 5 | 5 |
| TeglonLabs | org | 4 | 2 |
| DJedamski | user (social) | 4 | 2 |
| kristinezheng | user (social) | 3 | 0 |
| M1shaaa | user (social) | 4 | 0 |
| **TOTAL** | | **112** | **33,405** |

### Notable Repos
- `kubeflow/kubeflow` — 15,705★ Machine Learning Toolkit for Kubernetes
- `kubeflow/pipelines` — 4,152★ ML Pipelines (pushed 2026-06-04)
- `kubeflow/spark-operator` — 3,124★ Kubernetes Spark operator
- `kubeflow/trainer` — 2,111★ Distributed AI Model Training
- `migalkin/NodePiece` — 144★ Knowledge Graph representations (ICLR'22)
- `AustinCStone/TextGAN` — 92★ TensorFlow GAN for text generation
- `bmorphism/ocaml-mcp-sdk` — 61★ OCaml MCP SDK (Jane Street oxcaml_effect)
- `plurigrid/gorj` — 347 open issues (this repo!)

### GF(3) Color Chain Distribution
| Trit | Color | Name | Increment Count |
|------|-------|------|-----------------|
| 0 | `#d3869b` | ERGODIC | 37 |
| +1 | `#b8bb26` | PLUS | 38 |
| -1 | `#cc241d` | MINUS | 37 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 addresses (alice, bob, A–Z) queried via `https://fullnode.mainnet.aptoslabs.com`.  
API returned valid responses; coinstore balance = **0.00000000 APT** for all wallets.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 |
| A | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a | 0.0 |
| B | 0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13 | 0.0 |
| C | 0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e | 0.0 |
| D–Z | (see aptos_snapshots table) | 0.0 each |

### Multisig Contract Probes (Aptos Mainnet)
All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✅ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✅ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✅ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✅ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✅ |

**All 5 multisigs healthy — uniform 2-of-N threshold.**

### MNX Markets (testnet.mnx.fi)
- Site `https://testnet.mnx.fi` reachable — Next.js SPA, self-described as "The AI Exchange"
- Real API backend at `https://api.testnet.mnx.fi` — no public REST routes accessible
- MegaETH testnet + Arbitrum Sepolia integration visible in CSP headers
- **Status: SPA available, market data API not publicly accessible without auth**
- `mnx_snapshots` table: empty (0 rows)

---

## DuckDB Table Summary

| Table | Rows | Notes |
|-------|------|-------|
| `world_increments` | 112 | GF(3) colored repo snapshot events |
| `repo_snapshots` | 112 | GitHub repos from 11 sources |
| `aptos_snapshots` | 28 | alice, bob, A–Z wallets |
| `multisig_probes` | 5 | A-B, A-G, Y-Z, S-T, V-W |
| `mnx_snapshots` | 0 | API unavailable |

---

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
