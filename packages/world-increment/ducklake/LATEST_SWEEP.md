# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-13

## Sweep Metadata
- **Date:** 2026-07-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 319 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy) |
| MNX Markets | unavailable (401) |

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 1  | plurigrid | org | 100 | 0 | `#d3869b` | **ERGODIC** |
| 2  | kubeflow | org | 49 | 1 | `#b8bb26` | **PLUS** |
| 3  | bmorphism | user | 100 | -1 | `#cc241d` | **MINUS** |
| 4  | zubyul | user | 49 | 0 | `#d3869b` | **ERGODIC** |
| 5  | TeglonLabs | org | 5 | 1 | `#b8bb26` | **PLUS** |
| 6  | migalkin | user | 4 | -1 | `#cc241d` | **MINUS** |
| 7  | wasita | user | 3 | 0 | `#d3869b` | **ERGODIC** |
| 8  | AustinCStone | user | 3 | 1 | `#b8bb26` | **PLUS** |
| 9  | M1shaaa | user | 2 | -1 | `#cc241d` | **MINUS** |
| 10 | DJedamski | user | 2 | 0 | `#d3869b` | **ERGODIC** |
| 11 | kristinezheng | user | 2 | 1 | `#b8bb26` | **PLUS** |

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## Hamming Swarm — Aptos Snapshot

### Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A–Z) returned **HTTP 404** from Aptos mainnet fullnode.  
No `CoinStore<AptosCoin>` resource found — accounts are uninitialized on mainnet.  
Recorded balance_apt = NULL for all.

### Multisig Contract Probes (5 pairs — all healthy ✅)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da… | 2-of-2 | ✅ healthy |
| A-G | 0xf56c4a1c0906214f… | 2-of-2 | ✅ healthy |
| Y-Z | 0xd3ffe1812b2df406… | 2-of-2 | ✅ healthy |
| S-T | 0x3b1c3ae905d44c3a… | 2-of-2 | ✅ healthy |
| V-W | 0x40fad7b423a84365… | 2-of-2 | ✅ healthy |

All 5 multisig accounts are live on mainnet and require 2-of-2 signatures.

### MNX Markets (testnet.mnx.fi)

All API paths (`/api/markets`, `/api/tickers`, `/api/v1/markets`, `/api/v1/tickers`) returned **401 Unauthorized**.  
Market data unavailable without an auth token. `mnx_snapshots` table is empty.

---

## Top Repos by Source

### plurigrid (100 repos sampled, 103 total)
See full data in `repo_snapshots` — plurigrid covers Clojure/infra/AI research repos.

### kubeflow (49 repos)
Key repos: `kubeflow` (★15k+), `pipelines` (★4k+), `spark-operator` (★3k+), `trainer` (★2k+)

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (100 repos sampled, 105 total)
Notable: `ocaml-mcp-sdk` (★60), `anti-bullshit-mcp-server` (★23)

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |
| NBFNet_mlx | Python | 10 |

### AustinCStone (40 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

### wasita (11 repos)
Active: `wasita.github.io` (Svelte, pushed 2026-07-06), `magic-garden` (Python bot, ★2)

### Social Graph (M1shaaa, DJedamski, kristinezheng)
Smaller academic/personal repos; mostly Python/R/Jupyter.

---

## Repo Counts by Source (this run)

| Source | Type | Repos in DB |
|--------|------|-------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| TeglonLabs | org | 5 |
| migalkin | user | 4 |
| wasita | user | 3 |
| AustinCStone | user | 3 |
| M1shaaa | user | 2 |
| DJedamski | user | 2 |
| kristinezheng | user | 2 |
| **TOTAL** | | **319** |

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
- **kubeflow/kubeflow**: flagship ML platform — largest repo in sweep
- **migalkin/NodePiece**: 144 stars — ICLR'22 scalable KG embeddings
- **AustinCStone/TextGAN**: 92 stars — text GAN in TensorFlow
- **migalkin/StarE**: 89 stars — EMNLP 2020 hyper-relational KGs
- **TeglonLabs/jank-crane**: pushed 2026-06-08 — crane-jank converged-IR hub with GF3 maps
- **wasita/wasita.github.io**: pushed 2026-07-06 — most recently active social-graph repo
- **Multisig**: all 5 Hamming-swarm pairs (A-B, A-G, Y-Z, S-T, V-W) healthy on mainnet
- **Aptos wallets**: 28 addresses all uninitialized (404) — no APT CoinStore registered
- **MNX testnet**: API requires auth token — market data not available in automated runs
