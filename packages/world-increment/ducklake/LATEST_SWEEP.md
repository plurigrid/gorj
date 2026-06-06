# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-06  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Notes |
|--------|------|-------|-------|
| plurigrid | org | 100 | Most recent: gorj (pushed 2026-06-06), eirobri, place |
| kubeflow | org | 48 | Highly active ML ops org |
| TeglonLabs | org | 4 | mathpix-gem, coin-flip-mcp, monad-mcp-server, topoi |
| bmorphism | user | 100 | MCP servers, OCaml, Zig, Julia, Clojure tools |
| zubyul | user | 49 | Gay.jl, vibespace, plurigrid social repos |
| migalkin | user | 19 | Knowledge graph ML research (NodePiece ★144, StarE ★89) |
| DJedamski | user | 6 | Data science, R, Kaggle |
| wasita | user | 11 | Svelte, personal site, vocoder, ch3-lib |
| kristinezheng | user | 5 | Cognitive science, HackMIT, Lookit studies |
| M1shaaa | user | 8 | Lookit experiments, Yale work |
| AustinCStone | user | 30 | ML/CV, TextGAN ★92, StereoVisionMRF ★11 |

**Total repos snapshotted:** 380

### Top Starred Repos

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,706 | — | 2026-05-24 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-06 |
| kubeflow/spark-operator | 3,125 | Python | 2026-06-04 |
| kubeflow/trainer | 2,111 | Go | 2026-06-05 |
| kubeflow/katib | 1,685 | Python | 2026-06-05 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |

### Most Active (recently pushed)

- `plurigrid/gorj` — 2026-06-06, 398 open issues, Clojure (this repo)
- `kubeflow/pipelines` — 2026-06-06, 491 open issues, Python
- `kubeflow/notebooks` — 2026-06-06
- `M1shaaa/M1shaaa` — 2026-06-06 (profile config)
- `bmorphism/Gay.jl` — 2026-06-06, wide-gamut color sampling

### GF(3) Color Chain Distribution

| GF(3) Trit | Color | Name | Count |
|-----------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 127 |
| 1 | `#b8bb26` | PLUS | 127 |
| -1 | `#cc241d` | MINUS | 126 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried at ledger version ~5,603,301,431.

**Note:** All addresses return `resource_not_found` for `0x1::coin::CoinStore<AptosCoin>`.
At least one address (alice/0xc793...) has sequence_number=72, confirming on-chain activity.
These accounts use the **Fungible Asset (FA)** standard for APT rather than the legacy
coin module, so balances are not queryable via the CoinStore resource path.

| World | Address | Balance (APT) | Status |
|-------|---------|---------------|--------|
| alice | 0xc793...cc7b | 0 (FA std) | account active, seq=72 |
| bob | 0x0a3c...512d | 0 (FA std) | resource_not_found |
| A–Z (26) | see DB | 0 (FA std) | resource_not_found |

### Multisig Contract Probes (5 pairs)

All probes used `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

All 5 multisig contracts are live and require **2-of-N** signatures. All healthy.

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — Vercel deployment protection active. The testnet site
requires authentication (Vercel OIDC or bypass token). No market data extractable
without auth credentials. mnx_snapshots table has 0 rows.

---

## Database Schema

```
world-increments.duckdb
  world_increments   380 rows  GF(3) color-chained increment log
  repo_snapshots     380 rows  GitHub repo metadata
  aptos_snapshots     28 rows  Hamming swarm wallet balances
  multisig_probes      5 rows  Multisig contract health
  mnx_snapshots        0 rows  MNX markets (unavailable - Vercel auth)
```

## Query Examples

```sql
-- Most starred repos by source
SELECT org_or_user, max(stars) as top_stars, count(*) as repos
FROM repo_snapshots GROUP BY org_or_user ORDER BY top_stars DESC;

-- GF3 color distribution
SELECT gf3_name, gf3_color, count(*) FROM world_increments GROUP BY 1,2;

-- All healthy multisigs
SELECT pair, address, sigs_required FROM multisig_probes WHERE healthy=true;

-- Recent plurigrid activity
SELECT full_name, stars, pushed_at FROM repo_snapshots
WHERE org_or_user='plurigrid' ORDER BY pushed_at DESC LIMIT 10;
```
