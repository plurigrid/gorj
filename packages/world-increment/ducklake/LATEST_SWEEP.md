# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-04

## Sweep Metadata
- **Date:** 2026-08-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 (total: 103) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 (total: 106) |
| zubyul | user | 49 |
| migalkin | social_graph | 5 (top by activity) |
| wasita | social_graph | 5 |
| kristinezheng | social_graph | 2 |
| M1shaaa | social_graph | 2 |
| AustinCStone | social_graph | 4 |
| DJedamski | social_graph | 1 |
| **TOTAL** | | **322 repos** |

### Top Repos by Stars (this sweep)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/pipelines | 4173 | Python | 2026-08-04 |
| kubeflow/spark-operator | 3142 | Python | 2026-08-03 |
| kubeflow/trainer | 2165 | Go | 2026-08-03 |
| kubeflow/katib | 1694 | Python | 2026-08-04 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| migalkin/kgcourse2021 | 24 | HTML | 2026-07-10 |
| plurigrid/asi | 58 | HTML | 2026-07-10 |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |

### Most Recently Pushed Repos (last 7 days from sweep)

- **plurigrid/gorj** (Clojure) — 2026-08-04 ← current repo
- **kubeflow/pipelines** (Python) — 2026-08-04
- **kubeflow/katib** (Python) — 2026-08-04
- **kubeflow/blog** (Jupyter Notebook) — 2026-08-03
- **kubeflow/hub** (Go) — 2026-08-03
- **kubeflow/spark-operator** (Python) — 2026-08-03
- **bmorphism/Gay.jl** (Julia) — 2026-08-03

### TeglonLabs Highlights

- **jank-crane** (C++) — crane-jank converged-IR hub with GF3 convergence maps — pushed 2026-06-08
- **mathpix-gem** (Ruby) — Math OCR gem, 2 stars, 11 open issues
- **coin-flip-mcp** (JavaScript) — MCP coin-flip server with random.org, 2 forks
- **monad-mcp-server** — Monad MCP Server (Apache-2.0)
- **topoi** (Python) — pushed 2025-01-24

### Social Graph Highlights

- **migalkin/NodePiece** — 144★ — Compositional KG embeddings (ICLR'22)
- **migalkin/StarE** — 89★ — Hyper-relational KG embeddings (EMNLP 2020)
- **AustinCStone/TextGAN** — 92★ — Text GAN in TensorFlow
- **wasita/magic-garden** — 2★ — Discord auto-bot for Magic Garden game
- **wasita/send2kobo** — 1★ — Kobo e-reader document sender

### GF(3) Color Chain Distribution

| Color | Name | Trit | Count |
|-------|------|------|-------|
| #d3869b | ERGODIC | 0 | 114 |
| #b8bb26 | PLUS | +1 | 116 |
| #cc241d | MINUS | -1 | 115 |

Assignment rule: `id%3==0` → ERGODIC · `id%3==1` → PLUS · `id%3==2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Endpoint:** `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result:** All 28 addresses returned `resource_not_found` — APT CoinStore resource not initialized. These wallets have zero APT balance or have not yet been activated on Aptos mainnet.

| World | Address | Status |
|-------|---------|--------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9... | not initialized |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782... | not initialized |
| A–Z | (26 Hamming addresses) | not initialized |

### Multisig Contract Health Check

**Endpoint:** `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Multisig Address | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee208... | 2 | ✅ healthy |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6... | 2 | ✅ healthy |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae... | 2 | ✅ healthy |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0c... | 2 | ✅ healthy |

**All 5 multisig contracts healthy — 2-of-2 threshold maintained.**

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` is a Next.js SPA — API paths (`/api/markets`, `/api/v1/markets`) return the HTML shell with no machine-readable data. **MNX market data unavailable** via static HTTP; requires browser-side JS execution or a WebSocket/authenticated API connection.

---

## DuckDB Ducklake Schema

Database: `packages/world-increment/ducklake/world-increments.duckdb`

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

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 345 |
| repo_snapshots | 1266 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent · 2026-08-04*
