# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 185 |
| Total Repo Snapshots (cumulative) | 1106 |
| New increments this run | 162 |
| Sources Covered this run | 3 orgs + 8 users |
| Aptos addresses probed | 28 |
| Multisig contracts probed | 5 |

---

## JOB 1: GitHub Social Graph

### Top Repos by Stars (2026-07-24)

| Repo | Stars | Language | Notes |
|------|-------|----------|-------|
| kubeflow/kubeflow | 15,791 | — | ML Toolkit for Kubernetes |
| kubeflow/pipelines | 4,169 | Python | ML Pipelines (pushed 2026-07-24) |
| kubeflow/spark-operator | 3,143 | Python | Kubernetes Spark operator |
| kubeflow/trainer | 2,153 | Go | Distributed AI training |
| kubeflow/katib | 1,692 | Python | AutoML on Kubernetes |
| migalkin/NodePiece | 144 | Python | ICLR'22 KG representations |
| AustinCStone/TextGAN | 92 | Python | TensorFlow text GAN |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | OCaml MCP SDK (Jane Street oxcaml_effect) |
| bmorphism/anti-bullshit-mcp-server | 22 | JavaScript | Epistemological claim analysis |
| bmorphism/say-mcp-server | 20 | JavaScript | macOS TTS MCP |
| plurigrid/asi | 31 | HTML | everything is topological chemputer |

### Repo Counts by Source

| Source | Type | Total Repos |
|--------|------|-------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 106 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user | 12 |
| AustinCStone | user | 41 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |

### GF(3) Color Chain Distribution (this run)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 61 |
| +1 | `#b8bb26` | PLUS | 62 |
| -1 | `#cc241d` | MINUS | 62 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm addresses returned `resource_not_found` from the Aptos fullnode at ledger version ~6,430,507,878. Balance recorded as **0.00000000 APT** for all worlds (alice, bob, A–Z).

These accounts have not received APT or hold only non-APT assets.

### Multisig Contract Probes (0x1::multisig_account)

All 5 multisig contracts are **healthy** — responsive and requiring **2 signatures**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

| Endpoint | Result |
|----------|--------|
| `https://testnet.mnx.fi/api/markets` | 404 (SPA) |
| `https://api.testnet.mnx.fi/markets` | no healthy upstream |
| `https://api.testnet.mnx.fi/v1/markets` | no healthy upstream |

CSP headers confirm the API lives at `https://api.testnet.mnx.fi` — backend temporarily unavailable. Recorded in `mnx_snapshots` as `UNAVAILABLE`.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,791 stars (+226 since last sweep 2026-04-12) — flagship ML platform
- **kubeflow/pipelines**: 4,169 stars (+50 since last sweep) — active as of 2026-07-24
- **bmorphism/Gay.jl**: 187 open issues — wide-gamut splittable-determinism color library
- **zubyul/tilelang-kernels**: TileLang GPU kernels targeting NVIDIA GB10 Blackwell (CUDA 13.0, compute 12.1)
- **plurigrid/asi**: 31 stars, last pushed 2026-07-10 — "everything is topological chemputer"
- **All Hamming swarm multisigs**: 2-of-N threshold confirmed healthy across all 5 pairs
- **MNX testnet**: API backend down but SPA confirms correct endpoint structure
