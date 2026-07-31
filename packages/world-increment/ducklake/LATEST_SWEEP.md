# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-31

## Sweep Metadata
- **Date:** 2026-07-31 12:12 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 336 |
| Total Repo Snapshots (cumulative) | 1,257 |
| Sources Covered (this run) | 3 orgs + 8 users = 394 repos |
| Aptos addresses probed | 28 (alice, bob, A–Z) |
| Multisig contracts probed | 5 |

---

## GF(3) Color Chain Distribution (cumulative)

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 111 |
| PLUS | #b8bb26 | +1 | 113 |
| MINUS | #cc241d | -1 | 112 |

Chain rule: `id%3==0 → ERGODIC`, `id%3==1 → PLUS`, `id%3==2 → MINUS`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source (this run)

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 188 |
| kubeflow | org | 49 | 102,167 |
| bmorphism | user | 100 | 508 |
| zubyul | user | 49 | 40 |
| TeglonLabs | org | 5 | 14 |
| AustinCStone | user | 41 | 308 |
| migalkin | user | 19 | 811 |
| wasita | user | 12 | 9 |
| M1shaaa | user | 8 | 0 |
| kristinezheng | user | 5 | 0 |
| DJedamski | user | 6 | 14 |
| **TOTAL** | | **394** | **104,059** |

### Notable Recent Activity (2026-07)
- **plurigrid/gorj** (Clojure) — pushed 2026-07-31 (this repo)
- **plurigrid/zig-syrup** (Zig) — pushed 2026-07-28
- **plurigrid/asi** (HTML) — 56 stars, pushed 2026-07-10
- **kubeflow/hub**, **trainer**, **spark-operator** — all pushed 2026-07-31
- **kubeflow/spark-operator**: 3,142 stars | **kubeflow/pipelines**: 4,171 stars
- **bmorphism/Gay.jl** (Julia) — pushed 2026-07-31
- **bmorphism/ocaml-mcp-sdk** (OCaml) — 61 stars, OCaml MCP SDK
- **wasita/wasita.github.io** (Svelte) — pushed 2026-07-21
- **AustinCStone/byteruckus** (HTML) — pushed 2026-07-15
- **TeglonLabs/jank-crane** (C++) — crane-jank converged-IR hub, pushed 2026-06-08
- **migalkin/NodePiece** (Python) — 144 stars, ICLR'22 KG embeddings

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-31)

All 28 addresses queried via Aptos fullnode mainnet API.

**Result: All 28 addresses hold 0.0 APT** (alice, bob, A–Z)

Addresses are on-chain but unfunded — the swarm is in a latent/initialized state.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

**All 5 multisig contracts healthy** — each requires 2-of-2 signatures.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` returns a Next.js SPA for all paths including `/api/markets`.  
Status: **UNAVAILABLE** — no public JSON API endpoints accessible.

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

## Notable Highlights (2026-07-31)
- **kubeflow/pipelines**: 4,171 stars — most active ML pipeline platform for Kubernetes
- **kubeflow/spark-operator**: 3,142 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 144 stars — ICLR'22 compositional KG embeddings
- **AustinCStone/TextGAN**: 92 stars — generative adversarial text generation
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK (active 2026-03)
- **plurigrid/asi**: 56 stars — topological chemputer (pushed 2026-07-10)
- **plurigrid/gorj**: This very repo — forj + Clojure REPL + GF(3) trit coloring (pushed 2026-07-31)
- **Multisig swarm**: 5/5 pairs healthy at 2-of-2 threshold
- **Hamming swarm**: 28 addresses at 0.0 APT — latent state, unfunded
