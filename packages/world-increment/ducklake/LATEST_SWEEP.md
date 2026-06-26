# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-26

## Sweep Metadata
- **Date:** 2026-06-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 114 |
| Total Repo Snapshots | 114 |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### Repos by Source

| Source | Type | Repos Captured | Stars Total |
|--------|------|---------------|-------------|
| kubeflow | org | 15 | 31,944 |
| plurigrid | org | 31 | 74 |
| bmorphism | user | 12 | 142 |
| migalkin | user (zubyul social graph) | 10 | 294 |
| AustinCStone | user (zubyul social graph) | 6 | 106 |
| zubyul | user | 12 | 7 |
| wasita | user (zubyul social graph) | 7 | 5 |
| TeglonLabs | org | 5 | 2 |
| DJedamski | user (zubyul social graph) | 6 | 3 |
| kristinezheng | user (zubyul social graph) | 5 | 0 |
| M1shaaa | user (zubyul social graph) | 5 | 0 |
| **TOTAL** | | **114** | **32,577** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 38 |
| +1 | `#b8bb26` | PLUS | 38 |
| -1 | `#cc241d` | MINUS | 38 |

GF(3) assignment rule:
- `id % 3 == 0` → trit=0, ERGODIC `#d3869b`
- `id % 3 == 1` → trit=1, PLUS `#b8bb26`
- `id % 3 == 2` → trit=-1, MINUS `#cc241d`

Perfectly balanced: 38 × 3 = 114 ✓

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,745 | — | 2026-06-18 |
| kubeflow/pipelines | 4,156 | Python | 2026-06-26 |
| kubeflow/spark-operator | 3,128 | Python | 2026-06-26 |
| kubeflow/trainer | 2,122 | Go | 2026-06-25 |
| kubeflow/katib | 1,685 | Python | 2026-06-23 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,028 | YAML | 2026-06-25 |
| AustinCStone/TextGAN | 92 | Python | 2016-09-19 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2025-06-01 |
| migalkin/NodePiece | 144 | Python | 2021-06-14 |
| migalkin/StarE | 89 | Python | 2020-09-17 |
| plurigrid/asi | 26 | HTML | 2026-06-26 |

### Notable Activity (today, 2026-06-26)

- **plurigrid/gorj** — 837 open issues, pushed today; GF3 REPL orchestration active
- **plurigrid/asi** — 26 stars, pushed today; topological chemputer
- **plurigrid/place** — pushed today
- **bmorphism/Gay.jl** — pushed today; core GF(3) color system
- **kubeflow/pipelines** — pushed today; 457 open issues
- **kubeflow/spark-operator** — pushed today; 3,128 stars
- **kubeflow/arena** — pushed today
- **kubeflow/sdk** — pushed today

### Gay.jl Ecosystem (GF3 Color Fabric)

The Gay.jl color system appears across 8+ repos in the swarm, serving as the connective tissue:

| Repo | Role |
|------|------|
| bmorphism/Gay.jl | Primary Julia implementation |
| zubyul/Gay.jl | Fork/companion |
| plurigrid/gay-rs | Rust crate |
| plurigrid/gay-go | Go port |
| plurigrid/gay-terminal | ANSI terminal coloring |
| plurigrid/lazybjj | jj TUI with Gay.jl GF(3) |
| zubyul/gay-world | Goblin world builder using Gay.jl |
| zubyul/gay-terminal-colors | SplitMix64 per-terminal color identity |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-26)

All 28 Hamming-swarm addresses probed via `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All 28 addresses returned `Resource not found` — no `CoinStore<AptosCoin>` resource is registered at any of these addresses. The wallets are unfunded / uninitialized on Aptos mainnet.

| World | Balance (APT) | Status |
|-------|--------------|--------|
| alice | 0.0 | Uninitialized |
| bob | 0.0 | Uninitialized |
| A through Z (26 wallets) | 0.0 each | Uninitialized |

**Total APT across swarm: 0.0 APT**

### Multisig Contract Probes

All 5 multisig contracts probed via `POST /v1/view` with function `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | `0x0da4f428...987003` | 2 | Healthy |
| A-G | `0xf56c4a1c...c0096` | 2 | Healthy |
| Y-Z | `0xd3ffe181...b883` | 2 | Healthy |
| S-T | `0x3b1c3ae9...7883` | 2 | Healthy |
| V-W | `0x40fad7b4...eb6d` | 2 | Healthy |

All multisigs are **2-of-2** and responding correctly on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` requires Vercel deployment protection authentication. All paths (`/`, `/api/markets`, `/api/v1/markets`) return authentication-required. No market data could be extracted without a bypass token or Vercel CLI.

---

## DuckDB Schema

```sql
world_increments  -- 114 rows: GF3 trit-tagged repo-snapshot events
  (id, ts, gf3_trit, gf3_color, gf3_name,
   source_type, source_name, event_type, repo_name, actor, snapshot_hash)

repo_snapshots    -- 114 rows: repo metadata by org/user
  (id, ts, increment_id, org_or_user, repo_name, full_name,
   language, stars, forks, open_issues, pushed_at, description)

aptos_snapshots   -- 28 rows: hamming swarm wallet states
  (ts, world, address, balance_apt)

multisig_probes   -- 5 rows: A-B, A-G, Y-Z, S-T, V-W
  (ts, pair, address, sigs_required, healthy)

mnx_snapshots     -- 0 rows: unavailable (Vercel auth)
  (ts, ticker, name, category, price, change_pct)
```

---

## Key Observations

1. **Hamming swarm wallets are uninitialized** — all 28 addresses have 0 APT on mainnet. The swarm exists as addresses/keypairs but none have received funding yet.

2. **Multisig fabric is fully healthy** — all 5 monitored 2-of-2 multisig pairs are live and responding correctly on Aptos mainnet.

3. **plurigrid/gorj has 837 open issues** — the highest open-issue count in the entire social graph, indicating gorj is the primary active workspace.

4. **Gay.jl is today's hottest update** — bmorphism/Gay.jl pushed 2026-06-26 (today), and the GF(3) color system propagates through 8+ repos across the swarm.

5. **kubeflow dominates by star-count** (31,944 stars across 15 sampled repos) but plurigrid is the most dynamically active cluster with gorj + asi + place all pushing today.

6. **GF(3) balance achieved** — the 114 repo-increment events divide perfectly into 38 ERGODIC / 38 PLUS / 38 MINUS, demonstrating the color chain property for this sweep cycle.
