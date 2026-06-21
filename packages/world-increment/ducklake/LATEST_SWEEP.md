# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-21

## Sweep Metadata
- **Date:** 2026-06-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos (total) | Snapshotted | Top Stars |
|--------|------|---------------|-------------|-----------|
| plurigrid | org | 101 | 18 | asi (26★) |
| kubeflow | org | 48 | 15 | kubeflow/kubeflow (15,738★) |
| TeglonLabs | org | 5 | 5 | mathpix-gem (2★) |
| bmorphism | user | 105 | 10 | ocaml-mcp-sdk (61★) |
| zubyul | user | 49 | 7 | gay-world (1★) |
| migalkin | social | 19 | 5 | NodePiece (144★) |
| DJedamski | social | 6 | 3 | Kaggle (1★) |
| wasita | social | 11 | 5 | magic-garden (2★) |
| kristinezheng | social | 5 | 3 | (all 0★) |
| M1shaaa | social | 8 | 2 | (all 0★) |
| AustinCStone | social | 40 | 5 | TextGAN (92★) |

**This sweep added 101 new world_increment rows (cumulative DB: 1,022 repo_snapshots)**

### GF(3) Color Chain — This Sweep (first 12 of 101 increments shown)

GF(3) rule: `id%3==0 → trit=0 ERGODIC #d3869b` | `id%3==1 → trit=1 PLUS #b8bb26` | `id%3==2 → trit=-1 MINUS #cc241d`

| ID | Repo | Source | GF3 Trit | Color | Name |
|----|------|--------|-----------|-------|------|
| 1 | plurigrid/asi | plurigrid | +1 | `#b8bb26` | **PLUS** |
| 2 | plurigrid/place | plurigrid | -1 | `#cc241d` | **MINUS** |
| 3 | plurigrid/eirobri | plurigrid | 0 | `#d3869b` | **ERGODIC** |
| 4 | plurigrid/nash-portal | plurigrid | +1 | `#b8bb26` | **PLUS** |
| 5 | plurigrid/gorj | plurigrid | -1 | `#cc241d` | **MINUS** |
| 6 | plurigrid/zig-syrup | plurigrid | 0 | `#d3869b` | **ERGODIC** |
| 7 | plurigrid/asi-skills | plurigrid | +1 | `#b8bb26` | **PLUS** |
| 8 | plurigrid/nanoclj-zig | plurigrid | -1 | `#cc241d` | **MINUS** |
| 9 | plurigrid/bci-blue-share | plurigrid | 0 | `#d3869b` | **ERGODIC** |
| 10 | plurigrid/spi-race | plurigrid | +1 | `#b8bb26` | **PLUS** |
| 11 | plurigrid/reafference | plurigrid | -1 | `#cc241d` | **MINUS** |
| 12 | plurigrid/web-browser | plurigrid | 0 | `#d3869b` | **ERGODIC** |
| … | (89 more rows) | … | … | … | … |

### Notable Activity (pushed within 7 days of sweep)

| Repo | Org/User | Pushed | Issues | Notes |
|------|----------|--------|--------|-------|
| gorj | plurigrid | 2026-06-21 | **722** | forj + Rama + GF(3) — most active |
| place | plurigrid | 2026-06-20 | 9 | bci.place forester preview |
| katib | kubeflow | 2026-06-20 | 116 | AutoML on Kubernetes |
| pipelines | kubeflow | 2026-06-20 | 449 | ML Pipelines — 4,156★ |
| dashboard | kubeflow | 2026-06-21 | 80 | Central Dashboard |
| satreadout | bmorphism | 2026-06-20 | 0 | Lean 4.28 saturating readout |
| Gay.jl | bmorphism | 2026-06-20 | **187** | GF(3) SPI color library |
| jank-crane | TeglonLabs | 2026-06-08 | 0 | GF3 convergence maps, C++ |
| proj-template | wasita | 2026-06-19 | 0 | fresh template |
| wasita.github.io | wasita | 2026-06-15 | 8 | personal site |

### Top Repos by Stars (this sweep)

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,738 | — | ML Toolkit for Kubernetes |
| kubeflow/pipelines | 4,156 | Python | ML Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,127 | Python | Kubernetes operator for Spark |
| kubeflow/trainer | 2,118 | Go | Distributed AI Training on K8s |
| kubeflow/katib | 1,684 | Python | Automated ML on Kubernetes |
| AustinCStone/TextGAN | 92 | Python | Text GAN in TensorFlow |
| migalkin/NodePiece | 144 | Python | Compositional KG representations |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | OCaml SDK for MCP (Jane Street) |
| plurigrid/asi | 26 | HTML | Topological chemputer |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | Claim analysis MCP server |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Result: ALL 28 addresses → `resource_not_found` on `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`**

Ledger version at query time: ~5,850,728,714. The 28 Hamming swarm addresses have no APT CoinStore registered on Aptos mainnet. Accounts may exist at the address level but have not had an APT CoinStore initialized (requires receiving APT via a standard transfer).

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | not found |
| bob   | 0x0a3c…2d5d | not found |
| A     | 0x8699…9d7a | not found |
| B     | 0x3f89…b13  | not found |
| C–Z   | (24 addresses) | not found (all) |

### Multisig Contract Probes

All 5 multisig contracts are **ON-CHAIN and RESPONSIVE**:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4…7003 | **2** | ✓ HEALTHY |
| A-G | 0xf56c…0096 | **2** | ✓ HEALTHY |
| Y-Z | 0xd3ff…b883 | **2** | ✓ HEALTHY |
| S-T | 0x3b1c…7883 | **2** | ✓ HEALTHY |
| V-W | 0x40fa…eb6d | **2** | ✓ HEALTHY |

All 5 return `["2"]` from `0x1::multisig_account::num_signatures_required`. 2-of-n threshold confirmed.

### MNX Markets

**Status: UNAVAILABLE** — `testnet.mnx.fi` is password-protected via Vercel deployment protection. No market data extracted. Provide visitor password to enable future sweeps.

---

## DuckDB Cumulative State

```
world_increments: 101 rows (this sweep)
repo_snapshots:   1,022 rows (cumulative across all sweeps)
aptos_snapshots:  28 rows (this sweep, all null balance)
multisig_probes:  5 rows (this sweep, all healthy)
mnx_snapshots:    0 rows (unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

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

## Flags for Attention

1. **plurigrid/gorj** — 722 open issues as of 2026-06-21. Highest issue velocity in the graph.
2. **bmorphism/Gay.jl** — 187 open issues. Core GF(3)/SPI library likely needs triage.
3. **Aptos swarm** — 28/28 addresses have no APT CoinStore on mainnet. If funding is expected via standard transfer, it has not arrived.
4. **MNX testnet** — Vercel-gated; requires visitor password for market data access.
5. **Multisig health** — All 5 pairs confirmed healthy, 2-of-n threshold on-chain.
6. **kubeflow/pipelines** — 449 open issues and active (pushed 2026-06-20); worth monitoring.
7. **TeglonLabs/jank-crane** — New repo (created 2026-06-08), C++ GF3 convergence maps — active gorj-adjacent work.
