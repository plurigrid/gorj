# World Increment Sweep + Hamming Snapshot — 2026-07-17

## Sweep Metadata
- **Date:** 2026-07-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** 1.5.4 (via pip)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments inserted (this run) | 60 |
| Total Repo Snapshots inserted (this run) | 60 |
| Aptos wallets probed | 28 |
| Multisig contracts probed | 5 |
| MNX market data | UNAVAILABLE (Vercel auth) |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### Orgs / Users Queried

| Source | Type | Repos Found | Notes |
|--------|------|-------------|-------|
| plurigrid | org | 103 total | gorj (1215 open issues!), asi (30★), ontology (8★) |
| kubeflow | org | 49 total | kubeflow (15779★), pipelines (4167★), spark-op (3137★) |
| TeglonLabs | org | 5 total | jank-crane (C++, GF3 maps), mathpix-gem (Ruby, 2★) |
| bmorphism | user | 106 total | Gay.jl (Julia, 187 issues), ocaml-mcp-sdk (61★) |
| zubyul | user | 49 total | Gay.jl fork, nash-tui, voice-observatory |
| migalkin | social | 19 total | NodePiece (144★), StarE (89★), kgcourse2021 (24★) |
| DJedamski | social | 6 total | kaggle_ncaa18, School |
| AustinCStone | social | 41 total | byteruckus (fresh 2026-07-15) |
| wasita | social | 12 total | wasita.github.io (active 2026-07-16) |
| kristinezheng | social | 5 total | lookit-jenga, auditory-illusion |
| M1shaaa | social | 8 total | lab-bookshelf- (TypeScript) |

### Most Active Repos (past 7 days)

| Repo | Stars | Pushed | Language |
|------|-------|--------|----------|
| plurigrid/gorj | 1 | 2026-07-17 | Clojure — forj REPL MCP (this repo!) |
| kubeflow/sdk | 125 | 2026-07-17 | Python — Universal AI on K8s SDK |
| kubeflow/pipelines | 4167 | 2026-07-16 | Python |
| kubeflow/spark-operator | 3137 | 2026-07-16 | Python |
| kubeflow/trainer | 2151 | 2026-07-16 | Go |
| kubeflow/mcp-apache-spark | 183 | 2026-07-16 | Python |
| wasita/wasita.github.io | 1 | 2026-07-16 | Svelte |
| bmorphism/Gay.jl | 2 | 2026-07-14 | Julia |
| bmorphism/gay-chat | 0 | 2026-07-14 | Scheme |
| plurigrid/place | 1 | 2026-07-14 | TeX |

### GF(3) Color Chain — Sample Increments

| ID | Repo | GF3 Trit | Color | Name |
|----|------|-----------|-------|------|
| 1 | plurigrid/gorj | +1 | `#b8bb26` | PLUS |
| 2 | plurigrid/asi | -1 | `#cc241d` | MINUS |
| 3 | plurigrid/place | 0 | `#d3869b` | ERGODIC |
| 4 | plurigrid/eirobri | +1 | `#b8bb26` | PLUS |
| 5 | plurigrid/shrimp | -1 | `#cc241d` | MINUS |
| … | … | … | … | … |
| 60 | M1shaaa/Lookit-Demo | 0 | `#d3869b` | ERGODIC |

GF(3) rule: `id%3==0 → ERGODIC #d3869b`, `id%3==1 → PLUS #b8bb26`, `id%3==2 → MINUS #cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm addresses queried via `fullnode.mainnet.aptoslabs.com`.

**Result: All wallets show 0.0 APT** — accounts have no CoinStore resource on mainnet (unfunded or testnet-only addresses).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B | 0x3f89…b13 | 0.0 |
| C–Z | (24 addresses) | 0.0 each |

### Multisig Contract Probes — 5/5 HEALTHY

All 5 multisig contracts responded successfully with `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4…003 | 2 | ✓ healthy |
| A-G | 0xf56c…096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff…883 | 2 | ✓ healthy |
| S-T | 0x3b1c…883 | 2 | ✓ healthy |
| V-W | 0x40fa…b6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE**  
Site is behind Vercel deployment protection. All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return authentication walls. No market data extractable without a bypass token or Vercel authentication.

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

---

## Key Findings

1. **plurigrid/gorj** has 1215 open issues as of 2026-07-17 — extremely active development
2. **All 5 Aptos multisig contracts** (A-B, A-G, Y-Z, S-T, V-W) are healthy with 2-of-N threshold
3. **Hamming swarm wallets** show zero balance on mainnet — may be testnet/development addresses
4. **kubeflow** is most active org: 6+ repos pushed within last 24h, flagship at 15779★
5. **MNX testnet** requires Vercel auth — inaccessible without credentials; logged as unavailable
6. **bmorphism/Gay.jl** still active (pushed 2026-07-14), 187 open issues, core GF(3) color library
7. **wasita** (social graph) has active recent pushes (2026-07-16), Svelte/TypeScript stack
8. **AustinCStone/byteruckus** is a brand-new repo created 2026-07-15 (1 day ago)
