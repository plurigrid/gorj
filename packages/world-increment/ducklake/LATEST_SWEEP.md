# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-11

## Sweep Metadata
- **Date:** 2026-06-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 105 |
| Total Repo Snapshots | 105 |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 35 |
| +1 | `#b8bb26` | PLUS | 35 |
| −1 | `#cc241d` | MINUS | 35 |

GF(3) rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## Top Repos by Source (2026-06-11 snapshot)

### plurigrid (24 repos sampled)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 25 | 2026-06-10 |
| gorj | Clojure | 0 (501 issues) | 2026-06-11 |
| nash-portal | Rust | 2 | 2026-05-19 |
| ontology | JavaScript | 8 | 2025-05-27 |
| agent | Python | 5 | 2023-03-31 |

### kubeflow (16 repos sampled)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,714 | 2026-05-24 |
| pipelines | Python | 4,152 | 2026-06-11 |
| spark-operator | Python | 3,126 | 2026-06-09 |
| trainer | Go | 2,111 | 2026-06-10 |
| mcp-apache-spark-history-server | Python | 176 | 2026-06-10 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (15 repos sampled)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 1 (189 issues) | 2026-06-11 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |

### Social Graph
| User | Notable Repo | Stars | Pushed At |
|------|-------------|-------|-----------|
| migalkin | NodePiece | 144 | 2022-02-02 |
| migalkin | StarE | 89 | 2023-12-01 |
| AustinCStone | TextGAN | 92 | 2016-10-04 |
| wasita | wasita.github.io | 1 | 2026-06-01 |
| kristinezheng | kristinezheng.github.io | 0 | 2026-06-07 |
| M1shaaa | M1shaaa | 0 | 2026-06-11 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses, 2026-06-11)

All 28 addresses probed at `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 addresses returned 0.0 APT** — CoinStore resource absent on mainnet (accounts not initialized or unfunded).

Addresses: alice, bob, A–Z (full address list in aptos_snapshots table).

### Multisig Contract Probes (5 pairs, all healthy)

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | **2** | ✓ healthy |
| A-G | 0xf56c4a... | **2** | ✓ healthy |
| Y-Z | 0xd3ffe1... | **2** | ✓ healthy |
| S-T | 0x3b1c3a... | **2** | ✓ healthy |
| V-W | 0x40fad7... | **2** | ✓ healthy |

All 5 multisigs require 2-of-N signatures and are live on mainnet.

### MNX Markets (testnet.mnx.fi)

**Status: Authentication Required** — All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) returned an authentication gate. No market data available without credentials.

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

## Notable Highlights (2026-06-11)
- **kubeflow/kubeflow**: 15,714 stars (+149 since April sweep) — flagship ML platform
- **kubeflow/pipelines**: 4,152 stars (+33) — ML Pipelines for Kubernetes, pushed today
- **kubeflow/hub**: 173 stars — Model Registry for ML developers, pushed today
- **bmorphism/Gay.jl**: 189 open issues — wide-gamut color sampling, pushed today
- **plurigrid/gorj**: 501 open issues (this repo!) — forj + GF(3) nREPL orchestration
- **migalkin/NodePiece**: 144 stars — knowledge graph tokenization (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — generative adversarial text generation
- **TeglonLabs/jank-crane**: jank IR hub with GF3 convergence maps, pushed 2026-06-08
- **All 5 multisigs**: 2-of-N threshold, live on Aptos mainnet
- **Hamming swarm**: 28 addresses, all 0.0 APT (uninitiated on mainnet)
