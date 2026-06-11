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
| Total World Increments | 394 |
| Total Repo Snapshots | 371 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain

Color chain cycles per-row over all 394 increments:
- `id%3==0` → trit=0, **ERGODIC** `#d3869b` (~131 rows)
- `id%3==1` → trit=1, **PLUS** `#b8bb26` (~132 rows)
- `id%3==2` → trit=-1, **MINUS** `#cc241d` (~131 rows)

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| AustinCStone | user (social) | 30 |
| migalkin | user (social) | 19 |
| M1shaaa | user (social) | 8 |
| TeglonLabs | org | 5 |
| kristinezheng | user (social) | 5 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 1 |
| **TOTAL** | | **371** |

### Top Repos by Stars

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,714 | 2026-01-05 |
| kubeflow/pipelines | Python | 4,153 | 2026-04-10 |
| kubeflow/spark-operator | Python | 3,126 | 2026-04-10 |
| kubeflow/trainer | Go | 2,112 | 2026-04-10 |
| kubeflow/manifests | YAML | 1,022 | 2026-04-10 |
| migalkin/NodePiece | Python | 144 | 2022-02-02 |
| migalkin/StarE | Python | 89 | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2025-05-xx |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | — |
| TeglonLabs/mathpix-gem | Ruby | 2 | 2026-01-01 |

### Org/User Highlights

**plurigrid (100 repos):** Active Clojure/Rust/Python ecosystem. `gorj` (Clojure, 489 open issues, pushed 2026-06-11) is the most active. Mix includes `ontology` (JS, 8★), `microworlds` (Rust, 3★), `agent` (Python, 5★), `vcg-auction` (Rust, 7★).

**kubeflow (48 repos):** Production ML infrastructure. Total ecosystem ~27K+ stars. Most active repos: `kubeflow/kubeflow` (15,714★), `pipelines` (4,153★), `spark-operator` (3,126★), `trainer` (2,112★, Distributed AI training on K8s).

**TeglonLabs (5 repos):** `jank-crane` (C++, pushed 2026-06-08, "GF3 convergence maps, loopify pass spec"), `mathpix-gem` (Ruby, 2★), `coin-flip-mcp` (JS), `monad-mcp-server`, `topoi` (Python).

**bmorphism (100 repos):** MCP servers + experimental. `ocaml-mcp-sdk` (61★), `anti-bullshit-mcp-server` (23★), `say-mcp-server` (20★), `babashka-mcp-server` (19★), `Gay.jl` (Julia, 189 open issues).

**zubyul (49 repos):** World-building + tooling. `gay-world` (Python), `plurigrid-site` (Svelte, 11 open issues), `cascade-world`, `defcon`, `ghostty-modifications`.

### Social Graph (zubyul connections)

| User | Focus | Notable |
|------|-------|---------|
| migalkin | Knowledge Graphs, GNNs | NodePiece (144★), StarE (89★), kgcourse2021 |
| DJedamski | Data Science / R | Kaggle, grad school stats |
| wasita | Personal site | wasita.github.io (Svelte, active 2026-06) |
| kristinezheng | Cognitive Science | kristinezheng.github.io active 2026-06-07 |
| M1shaaa | Behavioral Research | profile repo active 2026-06-10, Lookit studies |
| AustinCStone | Python / ML | EpsteinSearch (2026), bmfork (Bitmind fork) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 addresses (alice, bob, A–Z) via Aptos fullnode mainnet API with 1s sleep between calls.

| Result | Count |
|--------|-------|
| 0.0 APT (no CoinStore resource) | 28 |

All 28 addresses return 0 APT. The `0x1::coin::CoinStore<AptosCoin>` resource is not initialized for these accounts under the legacy coin standard. These are likely smart contract accounts or unactivated wallets on the Hamming lattice.

### Multisig Contract Probes

Probed 5 multisig pairs via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4f428... | **2** | ✓ HEALTHY |
| A-G | 0xf56c4a1c... | **2** | ✓ HEALTHY |
| Y-Z | 0xd3ffe181... | **2** | ✓ HEALTHY |
| S-T | 0x3b1c3ae9... | **2** | ✓ HEALTHY |
| V-W | 0x40fad7b4... | **2** | ✓ HEALTHY |

All 5 multisig contracts are live and require 2-of-N signatures. Network latency nominal.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is a Vercel-deployed SPA protected by Vercel deployment authentication. Both root and `/api/markets` endpoints return auth challenge HTML (no market data accessible without bypass token or Vercel CLI auth). No `mnx_snapshots` rows inserted.

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
