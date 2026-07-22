# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-22

## Sweep Metadata
- **Date:** 2026-07-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 248 |
| Total Repo Snapshots (cumulative) | 1169 |
| Repos ingested this run | 225 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos wallets queried | 28 |
| Multisig contracts probed | 5/5 healthy |

---

## JOB 2: Hamming Swarm Snapshot (2026-07-22)

### Aptos Wallet Balances
All 28 Hamming addresses (alice, bob, A–Z) returned `resource_not_found` — these accounts are not initialized on Aptos mainnet (no CoinStore resource; accounts have not received APT).

### Multisig Contract Probes — All 5 Healthy ✓
| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...87003 | 2 | ✓ healthy |
| A-G | 0xf56c...c0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

All contracts enforce 2-of-2 multisig. No anomalies detected.

### MNX Markets (testnet.mnx.fi)
Next.js SPA — `/api/markets` and `/api/tickers` serve HTML shell only; no JSON API accessible without client-side JS execution. **Status: unavailable** (SPA data-loading only).

---

## GF(3) Color Chain — Distribution (cumulative)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| +1 | `#b8bb26` | PLUS | 83 |
| -1 | `#cc241d` | MINUS | 83 |
| 0 | `#d3869b` | ERGODIC | 82 |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...`

---

## Top Repos by Source

### Top Repos by Stars (2026-07-22 snapshot)
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | Go | 15,789 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,168 | 2026-07-21 |
| kubeflow/spark-operator | Python | 3,142 | 2026-07-17 |
| kubeflow/trainer | Go | 2,152 | 2026-07-21 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| AustinCStone/StereoVisionMRF | Python | 11 | 2026-04-01 |
| migalkin/NBFNet_mlx | Python | 10 | 2026-03-11 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 2026-01-01 |

### Most Recently Active (pushed after 2026-07-01)
- **wasita/wasita.github.io** — 2026-07-21 (Svelte personal website)
- **kubeflow/pipelines** — 2026-07-21
- **kubeflow/trainer** — 2026-07-21
- **kubeflow/kubeflow** — 2026-07-10
- **migalkin/kgcourse2021** — 2026-07-10
- **AustinCStone/byteruckus** — 2026-07-15 (new HTML repo)
- **kristinezheng/kristinezheng.github.io** — 2026-07-01

### TeglonLabs Highlights (GF3-adjacent)
- **jank-crane** (C++, 2026-06-08): crane-jank converged-IR hub with loopify pass spec and GF3 convergence maps — directly adjacent to this pipeline
- **mathpix-gem** (Ruby, ★2): LaTeX/SMILES math OCR; 11 open issues
- **coin-flip-mcp** (JS): MCP server for randomness, 2 forks

---

## Repo Counts by Source (2026-07-22)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 41 |
| migalkin | user | 19 |
| wasita | user | 12 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 5 |
| **TOTAL (this run)** | | **394** |

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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights (2026-07-22)
- **kubeflow/kubeflow**: 15,789 stars (up from 15,565 in April sweep) — flagship ML platform for Kubernetes; pushed 2026-07-10
- **kubeflow/pipelines**: 4,168 stars (up ~50) — pushed 2026-07-21
- **kubeflow/spark-operator**: 3,142 stars (up ~31) — pushed 2026-07-17
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **TeglonLabs/jank-crane**: new repo (C++) — GF3 convergence maps, directly tracking this pipeline's math
- **wasita/wasita.github.io**: active as of 2026-07-21 — personal site in Svelte
- **All 5 multisig pairs**: 2-of-2 sigs required, all healthy on Aptos mainnet
- **Hamming swarm**: all 28 wallet addresses inactive on mainnet (resource_not_found)
