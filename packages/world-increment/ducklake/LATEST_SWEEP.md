# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-28

## Sweep Metadata
- **Date:** 2026-06-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (cumulative DB state)

| Metric | Value |
|--------|-------|
| Total World Increments | 105 |
| Total Repo Snapshots | 1,026 |
| Aptos Snapshots (this run) | 28 |
| Multisig Probes (this run) | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain (this run: increments 83–105)

Rule: `id%3==0` → trit=0 ERGODIC #d3869b · `id%3==1` → trit=1 PLUS #b8bb26 · `id%3==2` → trit=-1 MINUS #cc241d

This sweep added 82 new world_increment rows (one per sampled repo) continuing the chain.

---

## GitHub Social Graph Snapshot

### Repo Counts by Source (2026-06-28)

| Source | Type | Unique Repos | Latest Push |
|--------|------|-------------|-------------|
| plurigrid | org | 109 | 2026-06-28T19:11:25Z (gorj) |
| bmorphism | user | 109 | 2026-06-24T15:36:16Z |
| TeglonLabs | org | 54 | 2026-06-08T19:03:37Z |
| kubeflow | org | 49 | 2026-06-28T19:01:54Z |
| AustinCStone | user | 43 | 2026-04-01T07:39:41Z |
| wasita | user | 31 | 2026-06-25T16:23:02Z |
| migalkin | user | 30 | 2026-05-28T20:19:20Z |
| zubyul | user | 26 | 2026-04-24T05:56:20Z |
| kristinezheng | user | 18 | 2026-06-07T22:53:10Z |
| M1shaaa | user | 16 | 2026-04-13T13:19:39Z |
| DJedamski | user | 11 | 2023-04-21T01:42:35Z |

### Top Repos by Stars (2026-06-28)

| Repo | Stars | Forks | Language | Last Push |
|------|-------|-------|----------|-----------|
| kubeflow/kubeflow | 15,751 | 2,680 | — | 2026-06-28 |
| kubeflow/pipelines | 4,159 | 2,013 | Python | 2026-06-28 |
| kubeflow/spark-operator | 3,129 | 1,491 | Python | 2026-06-27 |
| kubeflow/trainer | 2,126 | 972 | Go | 2026-06-28 |
| kubeflow/katib | 1,687 | 527 | Python | 2026-06-26 |
| kubeflow/examples | 1,460 | 756 | Jsonnet | 2026-06-16 |
| kubeflow/community-distribution | 1,028 | 1,065 | YAML | 2026-06-28 |
| migalkin/NodePiece | 144 | 21 | Python | 2026-05-07 |
| migalkin/StarE | 89 | 16 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | OCaml | 2026-05-08 |

### Notable Activity Since Last Sweep (2026-04-12 → 2026-06-28)
- **plurigrid/gorj**: 889 open issues — forj + Rama nREPL, GF(3) trit coloring active
- **plurigrid/asi**: stars 16→26 (+10), pushed 2026-06-28 — topological chemputer
- **plurigrid/place**: pushed 2026-06-27 — bci.place forester preview
- **plurigrid/eirobri**: 30 open issues — EiRoBri replay world
- **bmorphism/Gay.jl**: 187 open issues — wide-gamut SPI color sampling
- **bmorphism/penrose-mcp**: stars 9 — Infinity-Topos Penrose server
- **bmorphism/babashka-mcp-server**: stars 19 — Babashka MCP server (pushed 2026-06-05)
- **kubeflow/kubeflow**: 15565→15751 (+186 stars) since April
- **kubeflow/trainer**: 2080→2126 (+46 stars) since April
- **zubyul/voice-observatory**: new — macOS TUI for voice-download pathways
- **TeglonLabs/jank-crane**: new — C++ jank-crane GF3 convergence hub
- **wasita/wasita.github.io**: active (pushed 2026-06-25)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Ledger version probed:** ~5,985,317,952

### Wallet Balances — All 28 Addresses

| World | Balance (APT) | Status |
|-------|---------------|--------|
| alice | 0.0 | CoinStore not initialized |
| bob | 0.0 | CoinStore not initialized |
| A–Z (26 addrs) | 0.0 each | CoinStore not initialized |

**Interpretation:** `resource_not_found` on `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` indicates these addresses have never received or held native APT. Addresses are valid (exist in Aptos address space) but no CoinStore resource has been registered. Total swarm balance: **0.0 APT**.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | **2** | ✓ healthy |
| A-G | 0xf56c...0096 | **2** | ✓ healthy |
| Y-Z | 0xd3ff...b883 | **2** | ✓ healthy |
| S-T | 0x3b1c...7883 | **2** | ✓ healthy |
| V-W | 0x40fa...eb6d | **2** | ✓ healthy |

All 5 multisig contracts respond and require exactly **2-of-N** signatures. Contracts are live on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Vercel authentication required for both SPA root and API paths (`/api/markets`, `/api/v1/markets`). No market data extractable without a bypass token. Recorded as unavailable in `mnx_snapshots`.

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
