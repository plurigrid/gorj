# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-16

## Sweep Metadata
- **Date:** 2026-07-16T21:09 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (This Run)

| Metric | Value |
|--------|-------|
| World Increments Added | 150 |
| Repo Snapshots Added | 150 |
| Aptos Wallets Snapped | 28 |
| Multisig Probes | 5/5 healthy |
| MNX Markets | Unavailable (Vercel auth) |
| Sources Covered | 3 orgs + 9 users |

---

## GF(3) Color Chain Distribution (150 increments this run)

- PLUS #b8bb26 (trit=+1): 58 increments
- MINUS #cc241d (trit=-1): 58 increments  
- ERGODIC #d3869b (trit=0): 57 increments (≈balanced across GF3, 173 total since last reset)

---

## Hamming Swarm Snapshot (NEW)

### Aptos Mainnet Wallet Balances (28 addresses)
All 28 Hamming swarm addresses (alice, bob, A–Z) queried via Aptos fullnode mainnet.  
**Result:** All wallets show 0.0000 APT. CoinStore resources present but zero balance.  
This indicates pre-funded test infrastructure awaiting deployment or fully-spent wallets.

### Multisig Probes (5/5 healthy — 2-of-N threshold confirmed)
| Pair | Contract | Sigs Required |
|------|----------|---------------|
| A-B | 0x0da4f428… | 2 ✓ |
| A-G | 0xf56c4a1c… | 2 ✓ |
| Y-Z | 0xd3ffe181… | 2 ✓ |
| S-T | 0x3b1c3ae9… | 2 ✓ |
| V-W | 0x40fad7b4… | 2 ✓ |

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — Vercel authentication required; no market data accessible.

---

## Top Repos by Source (2026-07-16 snapshot)

### plurigrid (103 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 30 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-16 |
| place | TeX | 1 | 2026-07-14 |
| eirobri | Clojure | 0 | 2026-07-14 |
| shrimp | — | 0 | 2026-07-03 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| pipelines | Python | 4167 | 2026-07-16 |
| spark-operator | Python | 3137 | 2026-07-16 |
| trainer | Go | 2150 | 2026-07-16 |
| mcp-apache-spark-history-server | Python | 183 | 2026-07-16 |
| mlflow-integration | Python | 6 | 2026-07-16 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

### bmorphism (106 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| Gay.jl | Julia | 2 | 2026-07-14 |
| gay-chat | Scheme | 0 | 2026-07-14 |

### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 24 | 2026-07-10 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |

### wasita (12 repos) — active today
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| wasita.github.io | Svelte | 1 | 2026-07-16 |
| pnas-typst-template | — | 0 | 2026-07-16 |
| wm-cv | Svelte | 0 | 2026-07-14 |

---

## Repo Counts by Source (2026-07-16)

| Source | Type | Total | Snapped |
|--------|------|-------|---------|
| plurigrid | org | 103 | 100 |
| bmorphism | user | 106 | 30 |
| TeglonLabs | org | 5 | 5 |
| kubeflow | org | 49 | 30 |
| AustinCStone | user | 41 | 10 |
| migalkin | user | 19 | 10 |
| wasita | user | 12 | 10 |
| zubyul | user | 49 | 30 |
| kristinezheng | user | 5 | 5 |
| M1shaaa | user | 8 | 8 |
| DJedamski | user | 6 | 6 |
| Social graph combined | | | 7 (top per user) |
| **TOTAL SNAPPED** | | | **150** |

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

## Notable Highlights (2026-07-16 delta)
- **plurigrid/asi**: 30 stars (was 16 in Apr 2026) — growing
- **kubeflow/pipelines**: 4,167 stars (was 4,119) — +48 since April
- **bmorphism/ocaml-mcp-sdk**: 61 stars (was 60) — steady
- **bmorphism/gay-chat**: NEW repo (Scheme, Spritely Brassica Chat)
- **wasita** pushed 2 repos today (2026-07-16) — active right now
- **AustinCStone/byteruckus**: NEW repo created 2026-07-15
- **migalkin/kgcourse2021**: pushed 2026-07-10 — course materials actively maintained
- **Hamming swarm A-Z**: all 28 wallets at 0 APT; all 5 multisigs healthy at 2-of-N
- **MNX testnet**: inaccessible (Vercel auth gate)
