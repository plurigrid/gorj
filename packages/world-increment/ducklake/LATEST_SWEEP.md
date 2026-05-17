# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-17

## Sweep Metadata
- **Date:** 2026-05-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb` (4 cumulative sweeps)

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts (this sweep)

| Metric | Value |
|--------|-------|
| World Increments added | 11 |
| Repo Snapshots added | 327 |
| Sources Covered | 3 orgs + 8 users |
| Cumulative DB Rows (repo_snapshots) | 1,271 |

### GF(3) Color Chain — This Sweep's 11 Increments

| # | GF3 Trit | Color | Name | Source | Type |
|---|----------|-------|------|--------|------|
| 1 | +1 | `#b8bb26` | **PLUS** | AustinCStone | user |
| 2 | -1 | `#cc241d` | **MINUS** | DJedamski | user (zubyul graph) |
| 3 | 0 | `#d3869b` | **ERGODIC** | M1shaaa | user (zubyul graph) |
| 4 | +1 | `#b8bb26` | **PLUS** | TeglonLabs | org |
| 5 | -1 | `#cc241d` | **MINUS** | bmorphism | user |
| 6 | 0 | `#d3869b` | **ERGODIC** | kristinezheng | user (zubyul graph) |
| 7 | +1 | `#b8bb26` | **PLUS** | kubeflow | org |
| 8 | -1 | `#cc241d` | **MINUS** | migalkin | user (zubyul graph) |
| 9 | 0 | `#d3869b` | **ERGODIC** | plurigrid | org |
| 10 | +1 | `#b8bb26` | **PLUS** | wasita | user (zubyul graph) |
| 11 | -1 | `#cc241d` | **MINUS** | zubyul | user |

GF(3) rule: `id%3==0` → ERGODIC #d3869b · `id%3==1` → PLUS #b8bb26 · `id%3==2` → MINUS #cc241d

---

### Top Repos by Stars (this sweep)

| Repo | Language | Stars |
|------|----------|-------|
| kubeflow/kubeflow | — | 15,643 |
| kubeflow/pipelines | Python | 4,140 |
| kubeflow/spark-operator | Python | 3,125 |
| kubeflow/trainer | Go | 2,099 |
| kubeflow/katib | Python | 1,682 |
| kubeflow/examples | Jsonnet | 1,463 |
| kubeflow/manifests | YAML | 1,017 |
| kubeflow/arena | Go | 810 |
| kubeflow/kale | Python | 687 |
| kubeflow/mpi-operator | Go | 527 |
| migalkin/NodePiece | Python | 144 |
| AustinCStone/TextGAN | Python | 92 |
| migalkin/StarE | Python | 89 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 |
| migalkin/kgcourse2021 | HTML | 25 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 |
| plurigrid/asi | HTML | 23 |

### Repo Counts by Source

| Source | Type | Repos (this sweep) | Top Stars |
|--------|------|--------------------|-----------|
| plurigrid | org | 100 | 23 (asi) |
| kubeflow | org | 48 | 15,643 |
| TeglonLabs | org | 4 | 2 (mathpix-gem) |
| bmorphism | user | 100 | 61 (ocaml-mcp-sdk) |
| zubyul | user | 49 | 2 |
| migalkin | user | 19 | 144 (NodePiece) |
| DJedamski | user | 6 | 1 |
| wasita | user | 11 | 2 (magic-garden) |
| kristinezheng | user | 6 | 0 |
| M1shaaa | user | 8 | 0 |
| AustinCStone | user | 40 | 92 (TextGAN) |
| **TOTAL** | | **391** | |

### Notable Activity (since April sweep)

- **kubeflow/kubeflow**: +78 stars (15,565 → 15,643) since April 10
- **kubeflow/pipelines**: +21 stars (4,119 → 4,140)
- **bmorphism/ocaml-mcp-sdk**: +1 star (60 → 61)
- **migalkin/NodePiece**: +1 star (143 → 144)
- **wasita** — Actively pushing in 2026: `vocoder` (May 6), `wm-cv` (May 13), `wasita.github.io` (May 17)
- **TeglonLabs/mathpix-gem**: 11 open issues, last pushed Jan 2026

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 hamming-swarm wallets (alice, bob, A–Z) returned **0.00 APT**.
The `0x1::coin::CoinStore<AptosCoin>` resource was not found on any address — accounts are either uninitialized for APT or hold zero balance on mainnet.

| Range | Balance (APT) |
|-------|---------------|
| alice | 0.00 |
| bob | 0.00 |
| A–Z (26 addresses) | 0.00 each |

### Multisig Contract Probes (5 pairs) — ALL HEALTHY

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | `0x0da4f428...987003` | 2 | ✓ healthy |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✓ healthy |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✓ healthy |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✓ healthy |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✓ healthy |

All 5 multisig contracts use a **2-of-N** signature scheme and respond correctly on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no public JSON API available.**
All probed endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) returned the Next.js SPA shell HTML. No structured market data is accessible via REST. Recorded as `category='SPA_unavailable'` in `mnx_snapshots`.

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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Cumulative DB State (all sweeps)

| Table | Total Rows |
|-------|-----------|
| world_increments | 34 |
| repo_snapshots | 1,271 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |
