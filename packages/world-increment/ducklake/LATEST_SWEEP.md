# World Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-06-15 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (v1.5.3 Variegata)  
**GF(3) Color Chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Source | Type | Repos Captured | Top Star Repo |
|--------|------|----------------|---------------|
| plurigrid | org | 100 | asi (26★) |
| bmorphism | user | 100 | ocaml-mcp-sdk (61★) |
| zubyul | user | 49 | (all 0★, actively maintained) |
| kubeflow | org | 48 | kubeflow/kubeflow (15725★) |
| TeglonLabs | org | 5 | mathpix-gem (2★) |
| migalkin | user | 5 (top) | NodePiece (144★) |
| wasita | user | 3 (top) | magic-garden (2★) |
| kristinezheng | user | 2 (top) | kristinezheng.github.io |
| M1shaaa | user | 2 (top) | lab-bookshelf- |
| AustinCStone | user | 3 (top) | TextGAN (92★) |
| DJedamski | user | 2 (top) | School (1★) |
| **TOTAL** | | **319 rows** | |

### GF(3) World Increments Distribution
- Total increments: 319
- ERGODIC #d3869b (trit=0): ~107 entries (id%3==0)
- PLUS #b8bb26 (trit=1): ~106 entries (id%3==1)
- MINUS #cc241d (trit=-1): ~106 entries (id%3==2)

### Notable Activity (June 2026)
- **plurigrid/gorj** (this repo): 595 open issues, pushed 2026-06-15 — most active
- **bmorphism/Gay.jl**: Julia, 189 open issues, pushed 2026-06-15 — wide-gamut color sampling
- **kubeflow/website**: pushed 2026-06-15 13:49 UTC — kubeflow docs most recently active
- **TeglonLabs/jank-crane**: C++ converged-IR hub with GF3 convergence maps, pushed Jun 2026
- **zubyul/voice-observatory**: Python TUI for voice-download pathways (companion to bmorphism/say-mcp-server)
- **zubyul/nash-tui**: Rust NASH token TUI via GeckoTerminal OHLCV
- **plurigrid/asi**: HTML, 26★ — "everything is topological chemputer!" pushed Jun 2026

### Top 10 Repos by Stars

| Source | Repo | Stars | Language |
|--------|------|-------|----------|
| kubeflow | kubeflow | 15725 | — |
| kubeflow | pipelines | 4154 | Python |
| kubeflow | spark-operator | 3127 | Python |
| kubeflow | trainer | 2115 | Go |
| kubeflow | katib | 1683 | Python |
| kubeflow | examples | 1461 | Jsonnet |
| kubeflow | community-distribution | 1023 | YAML |
| kubeflow | arena | 812 | Go |
| kubeflow | kale | 694 | Python |
| migalkin | NodePiece | 144 | Python |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Result: ALL 28 wallets returned `resource_not_found`** for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~5,749,231,772.

The accounts may use the newer Fungible Asset (FA) standard rather than legacy CoinStore, or are unfunded on mainnet.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...c7b | NULL (resource_not_found) |
| bob | 0x0a3c...2d5 | NULL (resource_not_found) |
| A–Z (26 addrs) | 0x8699... – 0x7af0... | NULL (resource_not_found) |

### Multisig Contract Probes (5 contracts)

All 5 probed via `0x1::multisig_account::num_signatures_required` — all returned `"2"`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...987003 | 2 | ✓ |
| A-G | 0xf56c4a1c...c0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✓ |
| V-W | 0x40fad7b4...80eb6d | 2 | ✓ |

**5/5 multisig contracts healthy** — all are 2-of-N at Aptos mainnet ledger ~5.749B.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection blocks unauthenticated access. The SPA returns an auth gate requiring a Vercel bypass token or OIDC. No market data extracted.

---

## DuckDB Schema

```sql
-- 319 rows: GF(3) colored world increments (one per repo snapshotted)
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

-- 319 rows: repo metadata
repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

-- 28 rows: Hamming swarm addresses (all NULL - resource_not_found)
aptos_snapshots(timestamp, world, address, balance_apt)

-- 5 rows: multisig probes (all healthy, sigs_required=2)
multisig_probes(timestamp, pair, address, sigs_required, healthy)

-- 0 rows: MNX unavailable (Vercel auth gate)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## Quick Queries

```sql
-- Top repos by stars
SELECT org_or_user, repo_name, stars, language
FROM repo_snapshots ORDER BY stars DESC LIMIT 20;

-- GF3 distribution
SELECT gf3_name, gf3_color, COUNT(*)
FROM world_increments GROUP BY gf3_name, gf3_color;

-- Most recently pushed
SELECT org_or_user, repo_name, pushed_at
FROM repo_snapshots ORDER BY pushed_at DESC LIMIT 10;

-- Multisig health summary
SELECT pair, sigs_required, healthy FROM multisig_probes;

-- Aptos wallets with balances
SELECT world, address, balance_apt FROM aptos_snapshots;
```

## Changes vs Previous Sweep (2026-04-12)
- plurigrid/gorj: 595 open issues (new high), star count stable
- plurigrid/asi: 26★ (was 16★ — gained 10 stars)
- bmorphism/ocaml-mcp-sdk: 61★ (was 60★)
- kubeflow/kubeflow: 15725★ (was 15565★, +160 stars)
- kubeflow/pipelines: 4154★ (was 4119★, +35 stars)
- TeglonLabs: jank-crane added (C++, Jun 2026)
- **NEW**: Hamming swarm Aptos snapshot added — all 28 addrs resource_not_found
- **NEW**: 5 multisig contracts probed — all healthy (2-of-N)
- **NEW**: MNX Markets probe — blocked by Vercel auth
