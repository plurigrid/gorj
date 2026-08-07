# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-07T04:30:00Z  
**Run type:** Automated sweep (world-increment-sweep + hamming-swarm-snapshot)

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos | Total Stars | GF(3) |
|--------|------|-------|-------------|-------|
| kubeflow | org | 49 | 98,944 | ERGODIC #d3869b |
| plurigrid | org | 100 | 151 | PLUS #b8bb26 |
| TeglonLabs | org | 5 | 14 | MINUS #cc241d |
| bmorphism | user | 50+ | 358 | ERGODIC #d3869b |
| zubyul | user | 49 | 27 | PLUS #b8bb26 |
| migalkin | user | 19 | 829 | MINUS #cc241d |
| AustinCStone | user | 41 | 322 | ERGODIC #d3869b |
| wasita | user | 14 | 10 | PLUS #b8bb26 |
| DJedamski | user | 6 | 16 | MINUS #cc241d |
| kristinezheng | user | 5 | 0 | ERGODIC #d3869b |
| M1shaaa | user | 8 | 0 | PLUS #b8bb26 |

### Notable Repos

**plurigrid (100 repos):**
- `plurigrid/gorj` — Clojure, 1,688 open issues, last pushed 2026-08-07 (active)
- `plurigrid/asi` — HTML, 59 stars, "everything is topological chemputer"
- `plurigrid/zig-syrup` — Zig, OCapN Syrup implementation

**kubeflow (49 repos, most starred org):**
- `kubeflow/kubeflow` — 15,805 stars, foundational ML toolkit
- `kubeflow/pipelines` — 4,180 stars, active Aug 7 2026
- `kubeflow/spark-operator` — 3,144 stars
- `kubeflow/trainer` — 2,172 stars, LLM fine-tuning

**TeglonLabs (5 repos):**
- `TeglonLabs/jank-crane` — C++, GF(3) convergence maps (active Jun 2026)
- `TeglonLabs/mathpix-gem` — Ruby, LaTeX OCR gem

**bmorphism social graph (50+ repos):**
- `bmorphism/ocaml-mcp-sdk` — 61 stars, OCaml MCP SDK
- `bmorphism/anti-bullshit-mcp-server` — 23 stars, multi-framework claim analysis
- `bmorphism/Gay.jl` — Julia, 188 open issues, wide-gamut deterministic color

**migalkin (zubyul social graph, knowledge graph researcher):**
- `migalkin/NodePiece` — 144 stars, ICLR'22 knowledge graph representations
- `migalkin/StarE` — 89 stars, EMNLP'20 hyper-relational KGs

### DuckDB Schema

```
world_increments:  34 rows  (11 sources × ~3 runs)
repo_snapshots:   1014 rows  (across all orgs/users)
aptos_snapshots:   28 rows
multisig_probes:    5 rows
mnx_snapshots:      0 rows  (SPA, no public API)
```

GF(3) color chain applied: trit 0 → ERGODIC #d3869b, trit 1 → PLUS #b8bb26, trit 2 (−1) → MINUS #cc241d

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-08-07)

**API:** `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{ADDR}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address (first 10) | Balance (APT) |
|-------|--------------------|---------------|
| alice | 0xc793acde… | 0.00 |
| bob | 0x0a3c00c5… | 0.00 |
| A–Z | (26 wallets) | 0.00 each |

All 28 wallets queried. All returned 0 APT — these are unfunded accounts on mainnet (no `CoinStore` resource registered). This is expected for fresh/unused addresses.

### Multisig Contract Probes (Aptos mainnet)

All 5 multisig pairs are **healthy** — `num_signatures_required = 2`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428… | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c… | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181… | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9… | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4… | 2 | ✓ HEALTHY |

**Interpretation:** All multisig contracts require 2-of-N signatures and are reachable on mainnet. No anomalies detected.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` is a **Next.js SPA** — no public REST API endpoints discovered (`/api/markets`, `/api/v1/markets`, `/api/tickers` all returned HTML). Market data unavailable from automated probe. No rows inserted into `mnx_snapshots`.

---

## DuckDB Location

```
packages/world-increment/ducklake/world-increments.duckdb
```

Query examples:
```sql
-- Top repos by stars
SELECT full_name, language, stars, pushed_at 
FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF(3) color distribution
SELECT gf3_name, gf3_color, count(*) 
FROM world_increments GROUP BY gf3_name, gf3_color;

-- Hamming swarm state
SELECT world, balance_apt FROM aptos_snapshots ORDER BY world;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;
```
