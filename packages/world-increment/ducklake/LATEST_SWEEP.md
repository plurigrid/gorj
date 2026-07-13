# World-Increment Sweep — 2026-07-13

## Sweep Metadata
- **Date:** 2026-07-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (via Python module)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 392 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 (alice, bob, A–Z) |
| Multisig Pairs Probed | 5 |
| MNX Markets | Vercel auth required — unavailable |

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Type | Event Type | GF3 Trit | Color | Name |
|----|--------|------|------------|-----------|-------|------|
| 1  | plurigrid | org | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| plurigrid/asi | HTML | 30 | 2026-07-10 |
| plurigrid/gorj | Clojure | 1 | 2026-07-13 |
| plurigrid/place | TeX | 1 | 2026-07-07 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/pipelines | Python | 4165 | 2026-07-13 |
| kubeflow/trainer | Go | 2138 | 2026-07-13 |
| kubeflow/kale | Python | 695 | 2026-07-13 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 2026-01-01 |
| TeglonLabs/coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| bmorphism/Gay.jl | Julia | 2 | 2026-07-13 |

### zubyul (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| zubyul/voice-observatory | Python | 0 | 2026-04-24 |
| zubyul/ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |
| zubyul/nash-tui | Rust | 0 | 2026-04-13 |

### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| migalkin/kgcourse2021 | HTML | 24 | 2025-08-04 |
| migalkin/NBFNet_mlx | Python | 10 | 2024-03-02 |

### DJedamski (6 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| DJedamski/Kaggle | — | 1 | 2014-11-03 |
| DJedamski/Getting-and-Cleaning-Data | R | 1 | 2014-10-26 |
| DJedamski/School | R | 1 | 2014-10-09 |

### wasita (11 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| wasita/wasita.github.io | Svelte | 1 | 2026-07-06 |

### kristinezheng (5 repos)
All 0 stars. Latest push: kristinezheng.github.io (HTML, 2026-07-01).

### M1shaaa (8 repos)
All 0 stars. Profile repo pushed 2026-07-13 (today!).

### AustinCStone (40 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| AustinCStone/EpsteinSearch | Python | 0 | 2026-02-11 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| TeglonLabs | org | 5 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| **TOTAL** | | **392** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Result:** All 28 addresses returned `Resource not found` — accounts are not initialized on Aptos mainnet (no APT CoinStore resource). Balance recorded as `0.0 APT` for all.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793acd… | 0.0 |
| bob | 0x0a3c00c… | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (5 pairs)

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428… | 2 | ✓ |
| A-G | 0xf56c4a1c… | 2 | ✓ |
| Y-Z | 0xd3ffe181… | 2 | ✓ |
| S-T | 0x3b1c3ae9… | 2 | ✓ |
| V-W | 0x40fad7b4… | 2 | ✓ |

All 5 multisig contracts are healthy with threshold `2/N`.

### MNX Markets (testnet.mnx.fi)

**Status:** Vercel deployment protection active — authentication required. No market data extractable without bypass token or Vercel CLI auth.

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

## Notable Highlights
- **kubeflow/pipelines**: 4,165 stars — still most active ML pipeline for Kubernetes
- **kubeflow/trainer**: 2,138 stars — pushed today (2026-07-13)
- **plurigrid/asi**: 30 stars (+14 since Apr) — rapid growth on topological chemputer
- **bmorphism/Gay.jl**: Julia, pushed today (2026-07-13)
- **M1shaaa profile**: pushed today (2026-07-13)
- **wasita/wasita.github.io**: Svelte personal site, last pushed 2026-07-06
- **TeglonLabs/jank-crane**: New since last sweep — C++ crane-jank converged-IR hub with GF3 convergence maps
- **All Aptos wallets**: Uninitialized (no CoinStore) — swarm wallets not yet funded
- **All multisigs**: Healthy, 2-of-N threshold across 5 pairs (A-B, A-G, Y-Z, S-T, V-W)
