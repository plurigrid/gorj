# World-Increment Sweep + Hamming Snapshot — 2026-08-02

## Sweep Metadata
- **Date:** 2026-08-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 334 |
| Sources Covered | 3 orgs + 2 users + 6 social graph |

### Repo Counts by Source

| Source | Type | Repos | Total Stars | Max Stars |
|--------|------|-------|-------------|-----------|
| kubeflow | org | 49 | 34,453 | 15,803 |
| bmorphism | user | 100 | 240 | 61 |
| plurigrid | org | 100 | 109 | 58 |
| migalkin | social | 5* | 275 | 144 |
| AustinCStone | social | 5* | 103 | 92 |
| zubyul | user | 49 | 14 | 2 |
| wasita | social | 5* | 5 | 2 |
| DJedamski | social | 6* | 3 | 1 |
| TeglonLabs | org | 5 | 2 | 2 |
| kristinezheng | social | 5* | 0 | 0 |
| M1shaaa | social | 5* | 0 | 0 |
| **TOTAL** | | **334** | **35,204** | |

*Social graph: top-5 repos sampled per user

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 2  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 3  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 4  | bmorphism | user | 0 | `#d3869b` | **ERGODIC** |
| 5  | zubyul | user | +1 | `#b8bb26` | **PLUS** |
| 6  | migalkin | social | -1 | `#cc241d` | **MINUS** |
| 7  | DJedamski | social | 0 | `#d3869b` | **ERGODIC** |
| 8  | wasita | social | +1 | `#b8bb26` | **PLUS** |
| 9  | kristinezheng | social | -1 | `#cc241d` | **MINUS** |
| 10 | M1shaaa | social | 0 | `#d3869b` | **ERGODIC** |
| 11 | AustinCStone | social | +1 | `#b8bb26` | **PLUS** |

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## Top Repos by Source

### kubeflow (49 repos — actively maintained)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,803 | 2026-07-10 |
| pipelines | Python | 4,173 | 2026-08-01 |
| spark-operator | Python | 3,142 | 2026-07-31 |
| trainer | Go | 2,165 | 2026-07-31 |
| mpi-operator | Go | 530 | 2026-07-28 |

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Plurigraph | JavaScript | 3 | 2025-01-05 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |
| zig-syrup | Zig | 2 | 2026-07-28 |
| ontology | JavaScript | 8 | 2025-05-27 |
| duck-kanban | Rust | 1 | 2025-09-26 |

### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | **2026-08-02 (TODAY)** |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |
| manifold-mcp-server | JavaScript | 14 | 2025-01-11 |
| babashka-mcp-server | JavaScript | 19 | 2025-01-05 |
| open-location-code-zig | Zig | 3 | 2025-12-30 |

### migalkin (social — KG researcher)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |
| RWL | Python | 8 |
| NBFNet_mlx | Python | 10 |

### AustinCStone (social — ML engineer)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Alice–Z, 28 addresses)

All 28 Hamming swarm wallets returned **0 APT** — CoinStore resources not initialized on mainnet (wallets unfunded).

| Worlds | Total APT |
|--------|-----------|
| alice, bob, A–Z (28 total) | 0.0 |

### Multisig Contract Probes — ALL HEALTHY ✓

All 5 multisig contracts respond with **2-of-2 threshold**:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: unavailable** — The endpoint returns a Next.js SPA. No public REST API found at `/api/markets` or `/api/v1/markets`. Market data requires browser-side JS execution.

---

## DuckDB Schema

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 334 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA) |

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
- **bmorphism/Gay.jl** pushed TODAY (2026-08-02) — wide-gamut color sampling w/ splittable determinism
- **kubeflow/kubeflow**: 15,803 stars — flagship ML platform for Kubernetes
- **kubeflow/spark-operator**: 3,142 stars, pushed 2026-07-31 — actively maintained
- **migalkin/NodePiece**: 144 stars — ICLR'22 compositional KG representations
- **AustinCStone/TextGAN**: 92 stars — TF text generation GAN
- **plurigrid/zig-syrup**: OCapN Syrup+CapTP in Zig, pushed 2026-07-28
- **All 5 Hamming multisigs healthy** with 2-of-2 threshold on Aptos mainnet
- **Hamming swarm wallets (28)**: all unfunded (0 APT) on mainnet
