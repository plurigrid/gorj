# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-04

## Sweep Metadata
- **Date:** 2026-08-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Job 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 61 |
| Total Repo Snapshots | 61 (representative sample per source) |
| Sources Covered | 3 orgs + 8 users |

### Sources

| Source | Type | Sample Repos |
|--------|------|------|
| plurigrid | org | 9 |
| kubeflow | org | 10 |
| TeglonLabs | org | 5 |
| bmorphism | user | 8 |
| zubyul | user | 7 |
| migalkin | user | 5 |
| DJedamski | user | 3 |
| wasita | user | 4 |
| kristinezheng | user | 3 |
| M1shaaa | user | 3 |
| AustinCStone | user | 4 |

### GF(3) Color Chain — Increment Distribution

| GF3 Name | Color Hex | Count |
|----------|-----------|-------|
| PLUS (trit=+1) | `#b8bb26` | 21 |
| ERGODIC (trit=0) | `#d3869b` | 20 |
| MINUS (trit=-1) | `#cc241d` | 20 |

Assignment rule: `id mod 3 == 0` → ERGODIC, `id mod 3 == 1` → PLUS, `id mod 3 == 2` → MINUS.

### Top Repos by Stars

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,805 | 2026-08-04 |
| kubeflow/pipelines | Python | 4,175 | 2026-08-04 |
| kubeflow/spark-operator | Python | 3,143 | 2026-08-04 |
| kubeflow/trainer | Go | 2,167 | 2026-08-04 |
| kubeflow/katib | Python | 1,694 | 2026-08-01 |
| kubeflow/kale | Python | 699 | 2026-08-04 |
| kubeflow/mcp-apache-spark-history-server | Python | 185 | 2026-08-01 |
| kubeflow/hub | Go | 180 | 2026-08-03 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| kubeflow/sdk | Python | 132 | 2026-08-04 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| plurigrid/asi | HTML | 58 | 2026-07-10 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| AustinCStone/StereoVisionMRF | Python | 11 | 2026-04-01 |
| migalkin/NBFNet_mlx | Python | 10 | 2026-03-11 |
| migalkin/RWL | Python | 8 | 2026-05-28 |
| bmorphism/Gay.jl | Julia | 2 | 2026-07-21 |
| plurigrid/gorj | Clojure | 1 | **2026-08-04** ← this repo |

### Notable Highlights (delta from last sweep 2026-04-12)
- **kubeflow/kubeflow**: 15,805 stars (+240 since April sweep at 15,565)
- **kubeflow/trainer**: 2,167 stars (+87 since April sweep at 2,080)
- **kubeflow/pipelines**: 4,175 stars (+56 since April sweep at 4,119)
- **kubeflow/mcp-server** (new): 31 stars — new MCP server repo for AI-Assisted Dev
- **bmorphism/anti-bullshit-mcp-server**: 23 stars, last pushed 2026-08-02
- **plurigrid/gorj**: 1 star, 1,626 open issues — active dev (pushed 2026-08-04 today)
- **plurigrid/eirobri**: EiRoBri replay world, 31 open issues, pushed 2026-08-04
- **wasita/joint-planning-lit**: new repo created 2026-08-04 (same day as sweep)
- **bmorphism/gay-chat**: gay://chat Scheme implementation over Spritely Brassica Chat

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Result:** All 28 addresses queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
**Outcome:** `resource_not_found` for all addresses.
**Diagnosis:** Accounts exist on mainnet (alice has `sequence_number: 72`) but do not hold APT via the legacy Coin standard. These addresses use the newer **Fungible Asset (FA) standard** (`0x1::fungible_asset`) rather than the deprecated CoinStore interface.

| World | Status |
|-------|--------|
| alice | account exists (seq=72), no legacy CoinStore |
| bob | account exists, no legacy CoinStore |
| A–Z (26 addresses) | accounts exist, no legacy CoinStore |

### Multisig Contract Probes

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | `0x0da4f4...87003` | **2** | ✅ healthy |
| A-G | `0xf56c4a...0096` | **2** | ✅ healthy |
| Y-Z | `0xd3ffe1...b883` | **2** | ✅ healthy |
| S-T | `0x3b1c3a...7883` | **2** | ✅ healthy |
| V-W | `0x40fad7...eb6d` | **2** | ✅ healthy |

All 5 multisig accounts are live on Aptos mainnet and uniformly require 2-of-N signatures. No anomalies detected.

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable as raw API.
`testnet.mnx.fi` is a Next.js SPA ("The AI Exchange") with no accessible REST API endpoint. The `/api/markets` path returns the SPA shell, not JSON data. Market data is loaded client-side via JavaScript after hydration; no server-side data endpoint is exposed.

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
- `id mod 3 == 0` → trit=0, color=#d3869b (pink), name=**ERGODIC**
- `id mod 3 == 1` → trit=+1, color=#b8bb26 (yellow-green), name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d (red), name=**MINUS**
