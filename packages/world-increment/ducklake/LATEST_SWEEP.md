# World-Increment Sweep + Hamming Snapshot — 2026-06-14

## Sweep Metadata
- **Date:** 2026-06-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GF(3) Color Chain

| id%3 | trit | color | name |
|------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | −1 | `#cc241d` | MINUS |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Snapshot Totals

| Source | Type | Repos Indexed | Notable |
|--------|------|---------------|---------|
| plurigrid | org | 50 | gorj (575★ issues), asi (26★), ontology (8★) |
| kubeflow | org | 21 | kubeflow/kubeflow (15721★), pipelines (4154★), spark-operator (3127★) |
| TeglonLabs | org | 5 | jank-crane (C++, GF3 convergence maps) |
| bmorphism | user | 30 | ocaml-mcp-sdk (61★), Gay.jl (189 open), anti-bullshit-mcp (23★) |
| zubyul | user | 15 | gay-world, nash-tui, plurigrid-site (11 open) |
| migalkin | social | 7 | NodePiece (144★), StarE (89★) — KG researchers |
| DJedamski | social | 4 | kaggle_ncaa18, EDA, School |
| wasita | social | 6 | wasita.github.io, magic-garden (2★) |
| kristinezheng | social | 4 | kristinezheng.github.io (MIT) |
| M1shaaa | social | 4 | lab-bookshelf- (TypeScript) |
| AustinCStone | social | 8 | TextGAN (92★), StereoVisionMRF (11★) |
| **TOTAL** | | **153** | |

### Most Recently Pushed (as of sweep)

| Full Name | Pushed | Stars | Language |
|-----------|--------|-------|----------|
| kubeflow/spark-operator | 2026-06-14 | 3127 | Python |
| kubeflow/pipelines | 2026-06-14 | 4154 | Python |
| plurigrid/gorj | 2026-06-14 | 0 | Clojure |
| bmorphism/Gay.jl | 2026-06-14 | 1 | Julia |
| kubeflow/website | 2026-06-13 | 184 | HTML |
| kubeflow/trainer | 2026-06-13 | 2115 | Go |

### Top Starred

| Full Name | Stars | Forks |
|-----------|-------|-------|
| kubeflow/kubeflow | 15721 | 2673 |
| kubeflow/pipelines | 4154 | 2007 |
| kubeflow/spark-operator | 3127 | 1490 |
| kubeflow/trainer | 2115 | 969 |
| kubeflow/katib | 1683 | 527 |
| migalkin/NodePiece | 144 | 21 |
| AustinCStone/TextGAN | 92 | 30 |
| bmorphism/ocaml-mcp-sdk | 61 | 2 |
| plurigrid/vcg-auction | 7 | 2 |

### Highest Open Issue Count

| Full Name | Open Issues |
|-----------|-------------|
| plurigrid/gorj | 575 |
| bmorphism/Gay.jl | 189 |
| kubeflow/notebooks | 171 |
| kubeflow/docs-agent | 151 |
| kubeflow/sdk | 132 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 probed addresses (alice, bob, A–Z) returned `null` for
`CoinStore<aptos_coin::AptosCoin>`. These accounts either carry a zero APT
balance or have not yet registered the CoinStore resource on mainnet.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793acde… | 0.0 |
| bob | 0x0a3c00c5… | 0.0 |
| A | 0x8699edc0… | 0.0 |
| B | 0x3f892ebe… | 0.0 |
| C | 0x38b99e63… | 0.0 |
| D | 0xf7765624… | 0.0 |
| E | 0xdc1d9d53… | 0.0 |
| F | 0x18a14b5b… | 0.0 |
| G | 0x69a394c0… | 0.0 |
| H | 0xce67c327… | 0.0 |
| I | 0x070fe5d7… | 0.0 |
| J | 0x4d964db8… | 0.0 |
| K | 0xa732040a… | 0.0 |
| L | 0x7c2eaeaf… | 0.0 |
| M | 0x6fed37a7… | 0.0 |
| N | 0xe7dde6da… | 0.0 |
| O | 0x73252b60… | 0.0 |
| P | 0x62187929… | 0.0 |
| Q | 0xac40fa50… | 0.0 |
| R | 0x7ce605cc… | 0.0 |
| S | 0xb8753014… | 0.0 |
| T | 0x35781dc0… | 0.0 |
| U | 0x75860da4… | 0.0 |
| V | 0xb59dd817… | 0.0 |
| W | 0x5f32aef7… | 0.0 |
| X | 0xa95cbbd1… | 0.0 |
| Y | 0xd8e32848… | 0.0 |
| Z | 0x7af0ef6e… | 0.0 |

### Multisig Contract Probes

All 5 contracts responded successfully: **`num_signatures_required = 2`**  
All pairs are **HEALTHY** (2-of-N active).

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428… | 2 | ✓ |
| A-G | 0xf56c4a1c… | 2 | ✓ |
| Y-Z | 0xd3ffe181… | 2 | ✓ |
| S-T | 0x3b1c3ae9… | 2 | ✓ |
| V-W | 0x40fad7b4… | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `/api/markets` and `/api/v1/markets` returned no data.
The SPA does not expose a crawlable REST endpoint from this environment.

---

## DuckDB Table Summary

```
world_increments  — 153 rows  (GF3-colored increment chain, one per repo)
repo_snapshots    — 153 rows  (org/user repo metadata)
aptos_snapshots   — 28 rows   (alice, bob, A–Z balances; all 0.0 APT)
multisig_probes   — 5 rows    (A-B, A-G, Y-Z, S-T, V-W; all healthy)
mnx_snapshots     — 1 row     (unavailable marker)
```

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

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot, 2026-06-14*
