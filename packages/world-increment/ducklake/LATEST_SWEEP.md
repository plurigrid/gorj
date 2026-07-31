# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-31

## Sweep Metadata
- **Date:** 2026-07-31
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 318 |
| Total Repo Snapshots | 318 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution

GF(3) is perfectly balanced across 318 increments:

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 106 |
| +1 | PLUS | `#b8bb26` | 106 |
| -1 | MINUS | `#cc241d` | 106 |

---

## Repo Counts by Source (2026-07-31 snapshot)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| zubyul | user | 100 |
| kubeflow | org | 49 |
| bmorphism | user | 49 |
| migalkin | user | 5 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 2 |
| M1shaaa | user | 2 |
| AustinCStone | user | 2 |
| DJedamski | user | 2 |
| wasita | user | 2 |
| **TOTAL** | | **318** |

---

## Top Repos by Stars (2026-07-31)

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,801 | — | 2026-07-10 |
| kubeflow/pipelines | 4,172 | Python | 2026-07-31 |
| kubeflow/spark-operator | 3,141 | Python | 2026-07-31 |
| kubeflow/trainer | 2,165 | Go | 2026-07-31 |
| kubeflow/katib | 1,695 | Python | 2026-07-26 |
| kubeflow/examples | 1,461 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-29 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |

---

## Notable Recent Activity

### plurigrid (pushed today, 2026-07-31)
- `plurigrid/gorj` — Clojure, 1★ — forj + Rama topology nREPL routing + GF(3) gay trit coloring  
- `plurigrid/zig-syrup` — Zig, 2★ — High-performance OCapN Syrup with CapTP optimizations (pushed 2026-07-28)
- `plurigrid/place` — TeX — BCI documentation (pushed 2026-07-14)
- `plurigrid/eirobri` — Clojure — EiRoBri replay world (pushed 2026-07-21)

### bmorphism (recent)
- `bmorphism/Gay.jl` — Julia, 2★, 188 open issues — Wide-gamut GF(3) color sampling (pushed 2026-07-31)
- `bmorphism/ocaml-mcp-sdk` — OCaml, 61★ — MCP SDK using Jane Street oxcaml_effect

### kubeflow (active)
- `kubeflow/mcp-server` — Python, 31★ — MCP Server for AI-Assisted Kubeflow dev (pushed 2026-07-31)
- `kubeflow/sdk` — Python, 131★ — Universal Python SDK for AI on Kubernetes (pushed 2026-07-29)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) returned **0.00000000 APT** on mainnet.  
CoinStore resources are absent — these accounts exist on-chain but have not been
initialized with APT coin on mainnet.

### Multisig Contract Probes

All 5 multisig accounts are **healthy** — each requires 2-of-N signatures.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | `0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003` | 2 | ✅ |
| A-G | `0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096` | 2 | ✅ |
| Y-Z | `0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883` | 2 | ✅ |
| S-T | `0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883` | 2 | ✅ |
| V-W | `0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d` | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` is a Next.js SPA. The root and `/api/markets` endpoints
return the client-side rendered shell only — **no REST API data accessible** via
direct HTTP probe. Market data requires browser-side JS execution. Recorded as
unavailable; 0 rows in `mnx_snapshots`.

---

## DuckDB Tables

```
world-increments.duckdb
├── world_increments   — 318 rows (GF3-colored increment log per repo)
├── repo_snapshots     — 318 rows (full repo metadata: lang, stars, forks, issues)
├── aptos_snapshots    —  28 rows (A-Z + alice + bob, all 0.00 APT)
├── multisig_probes    —   5 rows (A-B, A-G, Y-Z, S-T, V-W — all healthy)
└── mnx_snapshots      —   0 rows (SPA unavailable)
```

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
