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
| Total World Increments | 11 |
| Total Repo Snapshots | 335 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice–Z) |
| Multisig Contracts Probed | 5 (all healthy) |

---

## GF(3) Color Chain — 11 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | bmorphism (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | zubyul (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | TeglonLabs (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-24 |
| place | TeX | 1 | 2026-07-14 |
| nash-portal | Rust | 2 | 2026-05-19 |
| zig-syrup | Zig | 2 | 2026-04-30 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,792 | 2026-07-10 |
| pipelines | Python | 4,169 | 2026-07-24 |
| spark-operator | Python | 3,143 | 2026-07-17 |
| trainer | Go | 2,153 | 2026-07-24 |
| katib | Python | 1,692 | 2026-07-22 |

### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| shitcoin | Python | 5 | 2026-04-08 |
| Gay.jl | Julia | 2 | 2026-07-24 |
| aella | Rascal | 1 | 2026-02-01 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| jank-crane | C++ | 0 | 2026-06-08 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### migalkin (6 of 19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |
| NBFNet_mlx | Python | 10 |

### AustinCStone (5 of 41 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| plurigrid | org | 100 | 83 |
| kubeflow | org | 49 | 34,409 |
| bmorphism | user | 100 | 246 |
| zubyul | user | 49 | 14 |
| TeglonLabs | org | 5 | 2 |
| migalkin | user | 6 | 278 |
| DJedamski | user | 6 | 3 |
| wasita | user | 6 | 4 |
| kristinezheng | user | 5 | 0 |
| M1shaaa | user | 4 | 0 |
| AustinCStone | user | 5 | 106 |
| **TOTAL** | | **335** | **35,145** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (alice–Z, 28 addresses)

**Endpoint:** `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

All 28 Hamming-swarm addresses returned **0 APT** — the `CoinStore` resource is not initialized on these accounts (accounts have not received APT). Expected for freshly-derived addresses.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 pairs **healthy**, all require **2-of-N signatures**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status:** SPA only — `/api/markets`, `/api/v1/markets`, `/api/v1/prices` all return the Next.js HTML shell. No REST API is publicly exposed. Recorded as **unavailable** (0 rows in `mnx_snapshots`).

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
- **kubeflow/kubeflow**: 15,792 stars — flagship ML platform for Kubernetes (↑227 since Apr)
- **kubeflow/pipelines**: 4,169 stars — pushed today 2026-07-24
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs in TensorFlow
- **plurigrid/asi**: 31 stars — topological chemputer (↑15 since Apr)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) trit coloring
- **bmorphism/Gay.jl**: Julia — pushed today
- **Multisig swarm**: 5 of 5 pairs healthy with 2-sig threshold

*Generated by automated sweep on 2026-07-24*
