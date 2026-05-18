# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-18

## Sweep Metadata
- **Date:** 2026-05-18
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 381 |
| Total Repo Snapshots | 381 (deduplicated) |
| Sources Covered | 3 orgs + 8 users |

### Source Breakdown

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user (zubyul social) | 30 |
| migalkin | user (zubyul social) | 19 |
| wasita | user (zubyul social) | 11 |
| M1shaaa | user (zubyul social) | 8 |
| kristinezheng | user (zubyul social) | 6 |
| DJedamski | user (zubyul social) | 6 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **381 unique repos** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 127 |
| +1 | `#b8bb26` | PLUS | 127 |
| -1 | `#cc241d` | MINUS | 127 |

GF(3) rule: `id mod 3 == 0` → ERGODIC `#d3869b` | `id mod 3 == 1` → PLUS `#b8bb26` | `id mod 3 == 2` → MINUS `#cc241d`

### Top Repos by Stars

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,647 | — | 2026-01-05 |
| kubeflow/pipelines | 4,140 | Python | 2026-04-10 |
| kubeflow/spark-operator | 3,126 | Python | 2026-04-10 |
| kubeflow/trainer | 2,100 | Go | 2026-04-10 |
| kubeflow/katib | 1,682 | Python | 2026-04-02 |
| kubeflow/examples | 1,463 | Jsonnet | 2025-04-04 |
| kubeflow/manifests | 1,017 | YAML | 2026-04-11 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |

### Notable Highlights

- **plurigrid/gorj** (this repo): 241 open issues, last pushed 2026-05-18
- **TeglonLabs/mathpix-gem**: Ruby gem for math OCR (LaTeX/SMILES/Markdown), 11 open issues
- **migalkin/NodePiece** (ICLR'22): 144★ parameter-efficient KG representations, pushed 2026-05-07
- **wasita/wasita.github.io**: pushed today (2026-05-18), active Svelte personal site
- **AustinCStone/bmfork / bmforkupdate**: bitmind forks — active connection to bmorphism network
- **plurigrid/gorj**: 241 open issues — highly active development

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice, bob, A–Z = 28 total)

All 28 addresses queried against `fullnode.mainnet.aptoslabs.com`. **All returned `resource_not_found`** for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

This means all swarm addresses have **unactivated APT coin stores** — addresses exist on Aptos but have never received an APT transfer to initialize the CoinStore resource. Balance recorded as NULL in `aptos_snapshots`.

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...cc7b | NULL (unactivated) |
| bob | 0x0a3c...512d | NULL (unactivated) |
| A–Z | (26 addresses) | NULL (all unactivated) |

### Multisig Contract Probes

Queried via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...987003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c...c0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ HEALTHY |

**All 5 multisig contracts are live 2-of-2 multisigs on Aptos mainnet.** All healthy.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a **Next.js SPA** — all server API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return the HTML shell. Market data requires browser JS execution to hydrate. **Recorded as unavailable** in `mnx_snapshots`.

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
