# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-08-04 (automated run)
**DuckDB version:** v1.5.5 (Variegata)
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured (this run) |
|--------|------|--------------------------|
| plurigrid | org | 42 |
| kubeflow | org | 15 |
| TeglonLabs | org | 5 |
| bmorphism | user | 18 |
| zubyul | user | 14 |
| migalkin | user (social graph) | 5 |
| AustinCStone | user (social graph) | 2 |
| kristinezheng | user (social graph) | 1 |
| wasita | user (social graph) | 3 |
| M1shaaa | user (social graph) | 2 |
| DJedamski | user (social graph) | 1 |
| **Total this run** | | **108** |

### DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 130 |
| repo_snapshots | 1,051 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

### GF(3) Distribution (cumulative)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | ~43 |
| +1 | #b8bb26 | PLUS | ~44 |
| -1 | #cc241d | MINUS | ~43 |

GF(3) chain rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

### Notable Recent Activity (2026-08-04)

**plurigrid** (most active):
- `gorj` — pushed 2026-08-04, 1,623 open issues (Clojure + GF(3) REPL orchestration)
- `eirobri` — pushed 2026-08-04, EiRoBri replay world (Clojure)
- `place` — pushed 2026-08-02, 15 open issues (TeX/forester)
- `zig-syrup` — pushed 2026-07-28, OCapN Syrup in Zig (2 ⭐)
- `asi` — 58 ⭐, topological chemputer

**bmorphism**:
- `Gay.jl` — pushed 2026-08-04, 188 issues, wide-gamut color sampling (Julia)
- `ocaml-mcp-sdk` — 61 ⭐, OCaml SDK for MCP using Jane Street oxcaml_effect
- `anti-bullshit-mcp-server` — 23 ⭐, epistemological claim analysis

**kubeflow** (infrastructure — very active):
- `kubeflow` core — 15,805 ⭐, pushed 2026-08-04
- `pipelines` — 4,175 ⭐, pushed 2026-08-04
- `spark-operator` — 3,143 ⭐, pushed 2026-08-04
- `mcp-apache-spark-history-server` — 185 ⭐, new Spark MCP server
- `mcp-server` — 31 ⭐, new Kubeflow MCP server (2026-04-08)

**wasita** (social graph — new today):
- `joint-planning-lit` — created 2026-08-04

**migalkin** (social graph, KG research):
- `NodePiece` — 144 ⭐, ICLR'22 knowledge graph embeddings
- `StarE` — 89 ⭐, EMNLP 2020 hyper-relational KG message passing

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z = 28 addresses)

All addresses queried against `fullnode.mainnet.aptoslabs.com/v1`.

**Result:** All 28 wallets returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

This indicates these addresses either have 0 APT balance, do not exist on-chain,
or have migrated to the Aptos fungible asset standard (FA migration removes
the legacy CoinStore resource). All 28 rows stored with `balance_apt = 0.0`.

| World | Count | Balance (APT) |
|-------|-------|--------------|
| alice, bob | 2 | 0.0 each |
| A through Z | 26 | 0.0 each |

### Multisig Contract Probes (5 contracts)

All probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428... | **2** | ✅ |
| A-G | 0xf56c4a1c... | **2** | ✅ |
| Y-Z | 0xd3ffe181... | **2** | ✅ |
| S-T | 0x3b1c3ae9... | **2** | ✅ |
| V-W | 0x40fad7b4... | **2** | ✅ |

**Summary:** All 5 multisig contracts alive and require 2-of-N signatures. No anomalies.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` returns a Next.js SPA (HTML only, no REST API exposed).
Endpoints tried: `/api/markets`, `/api/v1/markets`, `/api/tickers`.
All returned HTML (SPA shell). Market data unavailable via direct REST.
`mnx_snapshots` table: 0 rows.

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
