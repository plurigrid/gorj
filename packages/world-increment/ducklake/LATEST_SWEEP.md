# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-24

## Sweep Metadata
- **Date:** 2026-06-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 101 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Market Data | unavailable (Vercel auth) |

---

## GF(3) Color Chain — 11 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source

### plurigrid (21 repos snapshotted)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 0 | 2026-06-24 |
| place | TeX | 1 | 2026-06-24 |
| eirobri | Clojure | 0 | 2026-06-23 |
| asi | HTML | 26 | 2026-06-10 |
| nash-portal | Rust | 2 | 2026-05-19 |

### kubeflow (20 repos snapshotted)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,742 | 2026-06-18 |
| pipelines | Python | 4,157 | 2026-06-24 |
| spark-operator | Python | 3,128 | 2026-06-24 |
| trainer | Go | 2,119 | 2026-06-24 |
| katib | Python | 1,685 | 2026-06-23 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (15 repos snapshotted)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| Gay.jl | Julia | 2 |
| shitcoin | Python | 5 |

### migalkin (6 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (7 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 21 |
| kubeflow | org | 20 |
| bmorphism | user | 15 |
| zubyul | user | 10 |
| AustinCStone | user | 7 |
| migalkin | user | 6 |
| wasita | user | 6 |
| TeglonLabs | org | 5 |
| DJedamski | user | 4 |
| kristinezheng | user | 4 |
| M1shaaa | user | 3 |
| **TOTAL** | | **101** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A–Z)

All 28 wallets queried via Aptos mainnet fullnode API (`fullnode.mainnet.aptoslabs.com`).  
**Result: All balances = 0 APT**

The `CoinStore<0x1::aptos_coin::AptosCoin>` resource was absent on all queried addresses — these appear to be unfunded accounts or accounts where APT CoinStore was never initialized.

### Multisig Contract Probes (5 pairs)

All 5 probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| pair | address (prefix)   | sigs_required | healthy |
|------|--------------------|---------------|---------|
| A-B  | 0x0da4f428a0c0...  | 2             | ✓       |
| A-G  | 0xf56c4a1c0906...  | 2             | ✓       |
| Y-Z  | 0xd3ffe1812b2d...  | 2             | ✓       |
| S-T  | 0x3b1c3ae905d4...  | 2             | ✓       |
| V-W  | 0x40fad7b423a8...  | 2             | ✓       |

**All 5 multisig contracts healthy** — each requires 2-of-N signatures. The contracts are live on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` and `testnet.mnx.fi/api/markets` both return Vercel deployment protection authentication gate. No market data extractable without a bypass token. No rows in `mnx_snapshots`.

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
- **kubeflow/kubeflow**: 15,742 stars — flagship ML platform for Kubernetes (up from 15,565 in April)
- **kubeflow/spark-operator**: 3,128 stars, pushed today 2026-06-24 — most active kubeflow project
- **kubeflow/mcp-server**: NEW since last sweep (17★) — MCP server for AI-assisted Kubeflow dev
- **bmorphism/Gay.jl**: 187 open issues — extremely active, wide-gamut color/SPI work
- **plurigrid/gorj**: 791 open issues today — this repo actively evolving
- **TeglonLabs/jank-crane**: NEW since last sweep (2026-06-08) — C++ jank-crane converged-IR hub
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings (ICLR'22)
- **All 5 Aptos multisigs healthy**: A-B, A-G, Y-Z, S-T, V-W — all 2-of-N, live on mainnet
- **28 Hamming swarm wallets**: alice+bob+A-Z all show 0 APT (unfunded/uninitialized CoinStores)
