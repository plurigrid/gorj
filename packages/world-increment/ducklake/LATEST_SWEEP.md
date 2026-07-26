# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-26

## Sweep Metadata
- **Date:** 2026-07-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.2.1
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 313 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | SPA-only, no JSON API |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-26)

**All 28 wallets returned 0.0000 APT** — addresses are either unfunded or have no registered `CoinStore<AptosCoin>`.

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...cc7b | 0.0000 APT |
| bob | 0x0a3c...2d5d | 0.0000 APT |
| A–Z (26 wallets) | various | 0.0000 APT each |

### Multisig Contract Probes (0x1::multisig_account)

All 5 pairs healthy, all require **2 signatures**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

SPA-only (Next.js). `/api/markets` returned HTML, not JSON. No market data extractable via HTTP. Recorded as unavailable in `mnx_snapshots`.

---

## GF(3) Color Chain — All 11 Increments (2026-07-26)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 1  | plurigrid (org) | -1 | `#cc241d` | **MINUS** |
| 2  | kubeflow (org) | 0 | `#d3869b` | **ERGODIC** |
| 3  | TeglonLabs (org) | 1 | `#b8bb26` | **PLUS** |
| 4  | bmorphism (user) | -1 | `#cc241d` | **MINUS** |
| 5  | zubyul (user) | 0 | `#d3869b` | **ERGODIC** |
| 6  | migalkin (user) | 1 | `#b8bb26` | **PLUS** |
| 7  | wasita (user) | -1 | `#cc241d` | **MINUS** |
| 8  | DJedamski (user) | 0 | `#d3869b` | **ERGODIC** |
| 9  | kristinezheng (user) | 1 | `#b8bb26` | **PLUS** |
| 10 | M1shaaa (user) | -1 | `#cc241d` | **MINUS** |
| 11 | AustinCStone (user) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source (2026-07-26 snapshot)

### plurigrid (100 repos, 90★ total)
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| asi | HTML | 38 | 2026-07-10 |
| place | TeX | 1 | 2026-07-14 |
| gorj | Clojure | 1 | 2026-07-26 |
| eirobri | Clojure | 0 | 2026-07-21 |
| nash-portal | Rust | 2 | 2026-05-19 |

### kubeflow (49 repos, 34,411★ total)
| Repo | Language | Stars |
|------|----------|-------|
| kubeflow | — | ~15,000+ |
| pipelines | Python | ~4,000+ |
| spark-operator | Python | ~3,000+ |

### TeglonLabs (5 repos this sweep)
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (100 repos, 246★ total)
Top repos visible in this sweep cycle.

### migalkin — social graph (3 sampled repos, 257★)
| Repo | Stars |
|------|-------|
| NodePiece | 144 |
| StarE | 89 |
| kgcourse2021 | 24 |

### AustinCStone — social graph (2 sampled, 92★)
| Repo | Stars |
|------|-------|
| TextGAN | 92 |

---

## Repo Counts by Source (2026-07-26)

| Source | Type | Repos Sampled | Stars |
|--------|------|---------------|-------|
| kubeflow | org | 49 | 34,411 |
| plurigrid | org | 100 | 90 |
| bmorphism | user | 100 | 246 |
| zubyul | user | 49 | 14 |
| migalkin | social | 3 | 257 |
| AustinCStone | social | 2 | 92 |
| TeglonLabs | org | 5 | 2 |
| wasita | social | 2 | 3 |
| DJedamski | social | 1 | 0 |
| kristinezheng | social | 1 | 0 |
| M1shaaa | social | 1 | 0 |
| **TOTAL** | | **313** | **35,115** |

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

## Notable Highlights (2026-07-26)
- **plurigrid/asi**: 38★ (up from 16★ in 2026-04-12 sweep) — topological chemputer, pushed 2026-07-10
- **plurigrid/gorj**: This repo, pushed TODAY 2026-07-26
- **migalkin/NodePiece**: 144★ — scalable KG embeddings (ICLR'22)
- **AustinCStone/TextGAN**: 92★ — GANs for text generation
- **TeglonLabs/jank-crane**: newest TeglonLabs repo, references GF3 convergence maps
- **Hamming swarm**: 28/28 wallets at 0.0000 APT — swarm currently unfunded on mainnet
- **Multisig health**: 5/5 contracts healthy, uniform 2-of-N threshold across all pairs
- **MNX testnet**: SPA-only, no extractable market data via HTTP
