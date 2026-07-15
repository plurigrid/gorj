# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-15

## Sweep Metadata
- **Date:** 2026-07-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) chain:** ERGODIC #d3869b | PLUS #b8bb26 | MINUS #cc241d

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 55 |
| Total Repo Snapshots | 1,075 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts | 5 (all healthy) |
| Sources Covered | 3 orgs + 5 users (this run) |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried (This Run)

| Source | Type | Repos Found | Notes |
|--------|------|-------------|-------|
| plurigrid | org | 100 | fully inserted |
| bmorphism | user | 106 | 10 key repos inserted |
| zubyul | user | 49 | 10 inserted |
| TeglonLabs | org | 5 | all inserted |
| migalkin | user (social) | 19 | 6 inserted |
| DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone | user (social) | — | in prior sweep |

### Most Active Repos (pushed July 2026)

| Repo | Last Push |
|------|-----------|
| plurigrid/gorj | 2026-07-15 |
| bmorphism/gay-chat | 2026-07-14 |
| plurigrid/place | 2026-07-14 |
| bmorphism/Gay.jl | 2026-07-14 |
| plurigrid/eirobri | 2026-07-14 |
| bmorphism/anti-bullshit-mcp-server | 2026-07-12 |
| migalkin/kgcourse2021 | 2026-07-10 |
| plurigrid/asi | 2026-07-10 |

### Top Repos by Stars

| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| kubeflow/kubeflow | — | 15,572 | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | Python | 4,119 | ML Pipelines for Kubeflow |
| kubeflow/spark-operator | Python | 3,114 | Kubernetes operator for Apache Spark |
| kubeflow/trainer | Go | 2,082 | Distributed AI Model Training / LLM Fine-Tuning |
| migalkin/NodePiece | Python | 144 | Compositional KG Representations (ICLR'22) |
| migalkin/StarE | Python | 89 | Hyper-Relational KG (EMNLP 2020) |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | OCaml SDK for Model Context Protocol |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 22 | MCP claims validation server |
| plurigrid/asi | HTML | 30 | everything is topological chemputer! |

### Language Distribution (all 1,075 snapshots)

| Language | Repos |
|----------|-------|
| Python | 173 |
| Rust | 45 |
| HTML | 43 |
| Go | 38 |
| TypeScript | 34 |
| JavaScript | 33 |
| Jupyter Notebook | 28 |
| Clojure | 25 |

### GF(3) Trit Distribution

| Name | Color | Count |
|------|-------|-------|
| PLUS | #b8bb26 | 19 |
| MINUS | #cc241d | 18 |
| ERGODIC | #d3869b | 18 |

Balance: 19/18/18 — near-uniform ✓

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Ledger version at query time:** 6,284,638,707
**Aptos epoch:** 16,541 | **Block height:** 900,016,349
**Query timestamp:** 2026-07-15T04:08:25Z

### Wallet Balances (A–Z + alice/bob)

All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All 28 addresses returned HTTP 404 `resource_not_found` — no native APT CoinStore registered at these addresses on mainnet at ledger v6,284,638,707. Wallets may hold other tokens or exist only on testnet.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | null (no CoinStore) |
| bob | 0x0a3c…12d5 | null |
| A–Z | (26 addresses) | null (all) |

### Multisig Probes — 5/5 Healthy ✓

All contracts responded to `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…7003 | **2** | ✓ |
| A-G | 0xf56c…0096 | **2** | ✓ |
| Y-Z | 0xd3ff…b883 | **2** | ✓ |
| S-T | 0x3b1c…7883 | **2** | ✓ |
| V-W | 0x40fa…eb6d | **2** | ✓ |

All 5 multisig contracts live, all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` returned no response — SPA with no accessible REST API or testnet offline. No market data captured.

---

## DuckDB Schema

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

---

## Notable Highlights (2026-07-15)

- **plurigrid/gorj** pushed today (1,176 open issues) — active forj + Rama topology work
- **bmorphism/gay-chat** created 2026-07-14 — gay://chat over Spritely Brassica Chat
- **bmorphism/Gay.jl** 187 open issues, pushed 2026-07-14 — wide-gamut splittable determinism
- **plurigrid/place** and **plurigrid/eirobri** both pushed 2026-07-14 — active
- **migalkin/kgcourse2021** pushed 2026-07-10 — KG course materials still maintained
- **Multisig health**: 5/5 contracts at 2-of-N — Hamming swarm coordination layer intact
- **APT CoinStore**: all 28 addresses empty on mainnet — swarm may be testnet-only or using non-APT tokens

*Generated by world-increment-sweep + hamming-swarm-snapshot · plurigrid/gorj · 2026-07-15*
