# World-Increment Sweep — 2026-07-28

## Sweep Metadata
- **Date:** 2026-07-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all time) | 35 |
| This Sweep Increments | 12 (IDs 13–24) |
| Total Repo Snapshots (all time) | 1338 |
| New Repos This Sweep | 394 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (SPA stub) |

---

## GF(3) Color Chain — This Sweep (IDs 13–24)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (org) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow (org) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs (org) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin (user) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng (user) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 24 | world-increment-sweep (meta) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source (New Highlights Since Apr 2026)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | **52** ★ | 2026-07-10 |
| vcg-auction | Rust | 7 | — |
| ontology | JavaScript | 8 | — |
| StochFlow | Python | 4 | — |
| agent | Python | 5 | — |
> **Notable:** `plurigrid/asi` grew from 16→52 stars since Apr sweep (+36 stars)

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | **15,793** ★ | 2026-07-10 |
| pipelines | Python | 4,171 | — |
| spark-operator | Python | 3,142 | — |
| trainer | Go | 2,156 | — |
| katib | Python | 1,692 | — |
> **Notable:** flagship kubeflow repo up 228 stars since Apr (15565→15793)

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| **jank-crane** | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |
> **Notable:** NEW repo `TeglonLabs/jank-crane` — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow" (C++, pushed 2026-06-08)

### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | — |
| risc0-cosmwasm-example | Rust | 23 | — |
| anti-bullshit-mcp-server | JavaScript | 22 | — |
| say-mcp-server | JavaScript | 20 | — |
| babashka-mcp-server | JavaScript | 19 | — |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | **144** ★ |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |
| NBFNet_mlx | Python | 10 |

### AustinCStone (41 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

### wasita (12 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| wasita.github.io | Svelte | 1 | 2026-07-21 |
| magic-garden | Python | 2 | — |

### M1shaaa (8 repos)
| Repo | Language | Pushed At |
|------|----------|-----------|
| M1shaaa (profile) | — | **2026-07-28** (TODAY) |
| lab-bookshelf- | TypeScript | 2024-12-31 |

---

## Repo Counts by Source (This Sweep)

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
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **394** |

---

## Hamming Swarm Snapshot — Aptos Mainnet

### Wallet Balances (A–Z + alice/bob)
All 28 Hamming swarm addresses returned **null CoinStore** (0 APT) — addresses have no legacy APT CoinStore resource on mainnet. This is expected for accounts that use the newer Aptos fungible asset framework or have never received APT to the legacy module.

| World | Address (truncated) | Balance |
|-------|-------------------|---------|
| alice | 0xc793...cc7b | 0 APT |
| bob | 0x0a3c...2d5d | 0 APT |
| A–Z | 0x8699...–0x7af0... | 0 APT each |

### Multisig Contract Probes (5/5 Healthy)

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | **2** | ✓ HEALTHY |
| A-G | 0xf56c...0096 | **2** | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | **2** | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | **2** | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | **2** | ✓ HEALTHY |

All 5 multisig accounts require 2-of-N signatures. All contracts are live and responding.

### MNX Markets (testnet.mnx.fi)
- Status: **Unavailable** — SPA returns only "MNX" with no market data at `/api/markets` (404) or root page.

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
- **TeglonLabs/jank-crane**: NEW C++ repo — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow" (created 2026-06-08)
- **plurigrid/asi**: +36 stars since Apr sweep (16→52), HTML topological chemputer project accelerating
- **kubeflow/kubeflow**: 15,793 stars (+228 since Apr), ML platform for Kubernetes still growing
- **M1shaaa** profile repo pushed **today** (2026-07-28) — active during this sweep
- **wasita/wasita.github.io**: pushed 2026-07-21 — recently active Svelte personal site
- **Multisig health**: All 5 Hamming swarm multisig contracts (A-B, A-G, Y-Z, S-T, V-W) are healthy with sigs_required=2
- **Aptos CoinStore**: 28/28 addresses have no legacy CoinStore (new fungible asset framework or unfunded)
- **Increment 24**: ERGODIC — closes the 8th GF(3) cycle (IDs 1–24 = 8 complete triads)
