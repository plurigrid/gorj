# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-08

## Sweep Metadata
- **Date:** 2026-06-08
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 88 |
| Total Repo Snapshots | 1,009 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 28 |
| +1 | PLUS | `#b8bb26` | 30 |
| -1 | MINUS | `#cc241d` | 30 |

GF(3) rule: `id mod 3 == 0` → ERGODIC · `id mod 3 == 1` → PLUS · `id mod 3 == 2` → MINUS

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 25 | 2026-04-26 |
| ontology | JavaScript | 8 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-26 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| nash-portal | Rust | 2 | 2026-05-19 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,707 | 2026-05-24 |
| pipelines | Python | 4,152 | 2026-06-06 |
| spark-operator | Python | 3,126 | 2026-06-04 |
| trainer | Go | 2,112 | 2026-06-05 |
| katib | Python | 1,685 | 2026-06-05 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 (TODAY) |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-03-16 |

### bmorphism (103 repos)
| Repo | Language | Stars |
|------|----------|-------|
| say-mcp-server | JavaScript | 20 |
| babashka-mcp-server | JavaScript | 19 |
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| risc0-cosmwasm-example | Rust | 23 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (40 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Most Active Repos (Pushed Today)
| Repo | Language | Description |
|------|----------|-------------|
| plurigrid/gorj | Clojure | forj + Rama nREPL routing + GF(3) |
| TeglonLabs/jank-crane | C++ | crane-jank converged-IR hub |
| kubeflow/dashboard | TypeScript | Kubeflow Central Dashboard |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 103 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 5 |
| DJedamski | user | 6 |
| **TOTAL** | | **394** (sample; 1,009 stored) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 28 addresses)

All 28 addresses in the Hamming alphabet (alice, bob, A–Z) returned **0.00000000 APT**. The CoinStore resource is either unregistered or unfunded on mainnet for these addresses.

| Range | Status |
|-------|--------|
| alice, bob | 0 APT |
| A through Z | 0 APT each |

### Multisig Contract Probes — ALL HEALTHY

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

All 5 multisig contracts require exactly **2 signatures** — 2-of-N threshold confirmed.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — all API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return Vercel deployment protection (authentication required). No market data accessible without a bypass token or Vercel CLI.

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

## Notable Highlights
- **plurigrid/gorj** pushed TODAY — the very repo hosting this sweep
- **TeglonLabs/jank-crane** created and first-pushed TODAY — new crane-jank converged-IR hub
- **kubeflow/kubeflow**: 15,707 stars — grown since April sweep
- **bmorphism/ocaml-mcp-sdk**: 61 stars — active OCaml MCP ecosystem
- **Hamming swarm**: All 5 multisig contracts healthy with 2-sig threshold
- **MNX testnet**: Behind Vercel auth — inaccessible this sweep
