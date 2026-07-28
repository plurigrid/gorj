# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-28

## Sweep Metadata
- **Date:** 2026-07-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (this sweep)

| Metric | Value |
|--------|-------|
| World Increments added | 48 |
| Repo Snapshots added | 48 (plurigrid, in-scope only) |
| Aptos wallets probed | 28 |
| Multisig contracts probed | 5 |
| MNX market tickers | 0 (SPA, no REST API) |
| DuckDB cumulative world_increments | 71 |
| DuckDB cumulative repo_snapshots | 992 |

**GitHub scope note:** Cross-org/user queries (kubeflow, TeglonLabs, bmorphism, zubyul social graph) are outside this session's GitHub API scope (`plurigrid/gorj` only). Data from those sources preserved from the 2026-04-12 sweep below.

---

## JOB 2 — Hamming Swarm Snapshot (NEW — 2026-07-28)

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm addresses returned **0 APT** on mainnet. The `CoinStore<AptosCoin>` resource is not initialized for any of these accounts — they exist as public key derivations but have not received funds on mainnet.

| world | balance APT |
|-------|------------|
| alice | 0.00 |
| bob | 0.00 |
| A–Z (26 wallets) | 0.00 each |
| **Total swarm** | **0.00 APT** |

### Multisig Contract Probes

All 5 multisig contracts healthy — 2-of-N threshold confirmed for each pair.

| pair | address (prefix) | sigs_required | healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

All API paths return the Next.js SPA HTML — no public REST API endpoints found. Recorded as **unavailable**.

---

## JOB 1 — GitHub Social Graph Sweep

### plurigrid org (2026-07-28 snapshot — 48 repos)

| Repo | Language | Stars | Open Issues | Last Pushed |
|------|----------|-------|-------------|-------------|
| zig-syrup | Zig | 2 | 0 | 2026-07-28 |
| asi | HTML | 52 | 4 | 2026-07-10 |
| gorj | Clojure | 1 | 1466 | 2026-07-28 |
| eirobri | Clojure | 0 | 31 | 2026-07-21 |
| place | TeX | 1 | 14 | 2026-07-14 |
| nash-portal | Rust | 2 | 1 | 2026-05-19 |
| asi-skills | Julia | 3 | 0 | 2026-04-26 |
| nanoclj-zig | Zig | 1 | 20 | 2026-04-25 |
| ontology | JavaScript | 8 | 16 | 2025-05-27 |
| Plurigraph | JavaScript | 3 | 4 | 2025-01-05 |
| act | Python | 3 | 4 | 2024-07-26 |
| *(37 more at 0 stars)* | | | | |

**Hot today:** `zig-syrup` (pushed 13:02 UTC), `gorj` (pushed 15:17 UTC)  
**Most starred:** `asi` (52 ↑ from 16 on 2026-04-12)

### GF(3) Color Chain — this sweep (48 increments)
| trit | color | name | count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 23 |
| +1 | #b8bb26 | PLUS | 24 |
| -1 | #cc241d | MINUS | 24 |

### Cross-org data (from 2026-04-12 prior sweep — preserved)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL (prior)** | | **471** |

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
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-10)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark (pushed 2026-04-10)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
