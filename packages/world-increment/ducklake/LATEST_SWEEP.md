# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-27

## Sweep Metadata
- **Date:** 2026-06-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — Today's 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|----------|-------|------|
| 1 | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2 | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3 | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4 | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5 | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6 | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7 | wasita | user | +1 | `#b8bb26` | **PLUS** |
| 8 | kristinezheng | user | -1 | `#cc241d` | **MINUS** |
| 9 | M1shaaa | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS→MINUS→ERGODIC→PLUS→MINUS→ERGODIC→PLUS→MINUS→ERGODIC→PLUS→MINUS`

### Top Repos by Source (new entries this sweep)

#### plurigrid (org) — 12 repos indexed
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| gorj | Clojure | 0 | 2026-06-27 |
| place | TeX | 1 | 2026-06-27 |
| asi | HTML | 26 | 2026-06-26 |
| eirobri | Clojure | 0 | 2026-06-23 |
| nash-portal | Rust | 2 | 2026-05-19 |
| asi-skills | Julia | 3 | 2026-04-26 |
| ontology | JavaScript | 8 | 2025-05-27 |

#### kubeflow (org) — 12 repos indexed
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| kubeflow | — | 15748 | 2026-06-27 |
| pipelines | Python | 4157 | 2026-06-27 |
| trainer | Go | 2124 | 2026-06-27 |
| spark-operator | Python | 3129 | 2026-06-27 |
| kale | Python | 694 | 2026-06-27 |
| katib | Python | 1687 | 2026-06-26 |
| arena | Go | 813 | 2026-06-26 |
| mcp-apache-spark-history-server | Python | 178 | 2026-06-23 |

#### TeglonLabs (org) — 5 repos indexed
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-03-16 |

#### bmorphism (user) — 10 repos indexed
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| Gay.jl | Julia | 2 | 2026-06-20 |
| penrose-mcp | JavaScript | 9 | 2026-06-24 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| world | Python | 0 | 2026-06-02 |
| risc0-cosmwasm-example | Rust | 23 | 2025-05-21 |

#### zubyul (user) — 6 repos indexed
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| gay-world | Python | 1 | 2026-04-05 |
| ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |
| tilelang-kernels | Python | 0 | 2026-03-16 |
| kinesis-kb360pro | Python | 0 | 2026-03-26 |

#### Social Graph Users
| User | Top Repo | Stars | Pushed |
|------|----------|-------|--------|
| migalkin | NodePiece (ICLR'22 KG embeddings) | 144 | 2026-05-07 |
| migalkin | StarE (EMNLP 2020 hyper-relational KGs) | 89 | 2026-04-16 |
| wasita | wasita.github.io (personal site) | 1 | 2026-06-25 |
| AustinCStone | TextGAN (GAN for text gen) | 92 | 2025-03-03 |
| kristinezheng | kristinezheng.github.io | 0 | 2026-06-07 |
| M1shaaa | lab-bookshelf- | 0 | 2024-12-31 |
| DJedamski | Getting-and-Cleaning-Data | 1 | 2023-04-21 |

### DuckDB Ducklake Cumulative Status
- **Total increments (all-time):** 34
- **Total repo snapshots (all-time):** 1,007
- **Today's new increments:** 11
- **Today's new repo entries:** 63
- **Historical sweep range:** 2026-04-10 → 2026-06-27

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

Queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

All 28 hamming-swarm wallets (alice, bob, A–Z) returned **no CoinStore resource** — APT balance **0.0** across the entire swarm. Addresses exist on-chain but hold no APT coin store (unfunded or holding non-APT assets only).

| Range | Count | APT Balance |
|-------|-------|-------------|
| alice, bob | 2 | 0.0 each |
| A–Z (26 worlds) | 26 | 0.0 each |
| **Total swarm** | **28** | **0.0 APT** |

### Multisig Contract Probes (5 pairs) — ALL HEALTHY

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...7003 | **2** | ✓ healthy |
| A-G | 0xf56c4a1c...0096 | **2** | ✓ healthy |
| Y-Z | 0xd3ffe181...b883 | **2** | ✓ healthy |
| S-T | 0x3b1c3ae9...7883 | **2** | ✓ healthy |
| V-W | 0x40fad7b4...eb6d | **2** | ✓ healthy |

All 5 multisig contracts are live on Aptos mainnet and require **2-of-N signatures**. No degraded or missing contracts.

### MNX Testnet Markets

`https://testnet.mnx.fi` requires **Vercel authentication** (HTTP 200 with auth gate, no JSON API exposed). All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return the same auth wall. Market data unavailable — recorded as empty in `mnx_snapshots`.

---

## Schema Reference
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
- **kubeflow/kubeflow**: 15,748★ — up 183★ since April sweep
- **kubeflow/pipelines**: 4,157★ — most active KF repo (pushed 2026-06-27)
- **kubeflow/mcp-apache-spark-history-server**: 178★ new MCP entrant (born 2025-06-26)
- **bmorphism/ocaml-mcp-sdk**: 61★ OCaml MCP SDK growing
- **TeglonLabs/jank-crane**: new C++ repo for crane-jank GF3 convergence
- **plurigrid/gorj**: 860 open issues — very active GF(3) REPL routing repo
- **All 5 multisig contracts**: healthy 2-sig threshold on Aptos mainnet
- **Hamming swarm wallets**: all 28 addresses at 0.0 APT — swarm unfunded on mainnet
