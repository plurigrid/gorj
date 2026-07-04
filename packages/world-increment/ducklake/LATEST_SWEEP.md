# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-04

## Sweep Metadata
- **Date:** 2026-07-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 114 |
| Total Repo Snapshots | 114 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 38 |
| 1 | `#b8bb26` | PLUS | 38 |
| -1 | `#cc241d` | MINUS | 38 |

Chain balanced: 38/38/38 across 114 increments.

---

## GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Most Recent Push |
|--------|------|----------------|-----------------|
| plurigrid | org | 33 | 2026-07-04 (gorj) |
| kubeflow | org | 20 | 2026-07-04 (hub) |
| TeglonLabs | org | 5 | 2026-06-08 |
| bmorphism | user | 19 | 2026-07-04 (Gay.jl) |
| zubyul | user | 13 | 2026-04-24 |
| migalkin | user (social) | 6 | 2026-05-28 |
| DJedamski | user (social) | 4 | 2023-04-21 |
| wasita | user (social) | 5 | 2026-07-02 |
| kristinezheng | user (social) | 3 | 2026-07-01 |
| M1shaaa | user (social) | 2 | 2024-12-31 |
| AustinCStone | user (social) | 5 | 2026-04-01 |
| **TOTAL** | | **114** | |

### Notable Repos (by stars)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15761 | — | 2026-06-18 |
| kubeflow/pipelines | 4169 | Python | 2026-07-03 |
| kubeflow/spark-operator | 3132 | Python | 2026-07-02 |
| kubeflow/trainer | 2129 | Go | 2026-07-03 |
| kubeflow/katib | 1689 | Python | 2026-07-01 |
| kubeflow/examples | 1460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1028 | YAML | 2026-07-03 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| plurigrid/gorj | 0 | Clojure | **2026-07-04** (963 open issues) |

### Hot Today (2026-07-04)

- `plurigrid/gorj` — this repo, 963 open issues, forj+GF3 REPL orchestration
- `kubeflow/hub` — Go, Model Registry, pushed 05:35 UTC
- `bmorphism/Gay.jl` — Julia, 187 open issues, GF(3) wide-gamut color library

---

## Hamming Swarm Snapshot

### Aptos Wallet Balances (28 worlds: alice, bob, A–Z)

All 28 addresses queried against Aptos mainnet (ledger version 6098168841, 2026-07-04).

**Result: 0 APT for all 28 addresses** — APT `CoinStore<0x1::aptos_coin::AptosCoin>` resource not registered on any account.  
Error: `resource_not_found` — accounts exist on-chain but have never received APT.

| World | Address (truncated) | Balance |
|-------|---------------------|---------|
| alice | `0xc793ac...` | 0 APT |
| bob | `0x0a3c00...` | 0 APT |
| A–Z | (26 wallets) | 0 APT each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts returned `num_signatures_required = 2` — **all healthy**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f4...` | 2 | ✓ healthy |
| A-G | `0xf56c4a...` | 2 | ✓ healthy |
| Y-Z | `0xd3ffe1...` | 2 | ✓ healthy |
| S-T | `0x3b1c3a...` | 2 | ✓ healthy |
| V-W | `0x40fad7...` | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Vercel deployment protection active (HTTP 401).  
Cannot scrape without Vercel auth token or bypass. No market data this sweep.

---

## DuckDB Schema

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| `world_increments` | 114 |
| `repo_snapshots` | 114 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 |

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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

## Key Observations

1. **plurigrid/gorj** — pushed 2026-07-04 with 963 open issues; this is the active forj+GF3 REPL repo.
2. **kubeflow** ecosystem extremely active — hub, trainer, pipelines, spark-operator all pushed within 24h.
3. **bmorphism/Gay.jl** — 187 open issues, the GF(3) color library underlying this sweep's trit chain.
4. **All 28 Hamming swarm addresses have 0 APT** — CoinStore not registered; accounts are on-chain but unfunded.
5. **All 5 multisig contracts healthy** — 2-of-2 threshold, no anomalies.
6. **MNX testnet** — behind Vercel auth, unavailable without credentials.
