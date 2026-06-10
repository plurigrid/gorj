# World-Increment Sweep — 2026-06-10 + Hamming Swarm Snapshot

## Sweep Metadata
- **Date:** 2026-06-10T11:09 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 122 |
| Total Repo Snapshots | 122 |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 40 |
| +1 | `#b8bb26` | PLUS | 41 |
| -1 | `#cc241d` | MINUS | 41 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 42 |
| kubeflow | org | 16 |
| bmorphism | user | 14 |
| zubyul | user | 11 |
| wasita | user (social graph) | 7 |
| DJedamski | user (social graph) | 6 |
| M1shaaa | user (social graph) | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user (social graph) | 5 |
| AustinCStone | user (social graph) | 5 |
| migalkin | user (social graph) | 5 |
| **TOTAL** | | **122** |

### Top Repos by Stars

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,714 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,153 | 2026-06-09 |
| kubeflow/spark-operator | Python | 3,126 | 2026-06-09 |
| kubeflow/trainer | Go | 2,112 | 2026-06-10 |
| kubeflow/katib | Python | 1,685 | 2026-06-05 |
| kubeflow/examples | Jsonnet | 1,462 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,022 | 2026-06-09 |
| kubeflow/arena | Go | 812 | 2026-05-07 |
| kubeflow/kale | Python | 693 | 2026-06-05 |
| kubeflow/mpi-operator | Go | 528 | 2026-06-02 |
| AustinCStone/TextGAN | Python | 92 | 2016-10-04 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| migalkin/NodePiece | Python | 144 | 2022-02-02 |
| migalkin/StarE | Python | 89 | 2023-12-01 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |

### Notable Activity (2026-06-10)

- **plurigrid/gorj** — 476 open issues, pushed today (this repo)
- **bmorphism/Gay.jl** — 189 open issues, pushed today — wide-gamut GF(3) color sampling
- **kubeflow/trainer** — pushed today (distributed LLM fine-tuning)
- **M1shaaa/M1shaaa** — pushed today (profile config)
- **TeglonLabs/jank-crane** — C++ crane-jank IR hub with GF3 convergence maps (pushed 2026-06-08)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice, bob, A–Z) — 28 wallets

All 28 Hamming swarm wallets probed via Aptos fullnode mainnet API.
**Result: No `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource found on any address.**
Addresses exist on-chain but hold no direct APT (may use delegated staking, wrapped resources, or accounts not yet fully bootstrapped).

| World | Address (truncated) |
|-------|---------------------|
| alice | 0xc793...c7b |
| bob   | 0x0a3c...5d |
| A     | 0x8699...9d7a |
| B     | 0x3f89...b13 |
| C     | 0x38b9...35e |
| D–Z   | (25 more addresses, all null APT) |

### Multisig Contract Probes (5/5 healthy)

All 5 multisig contracts are live and responding with `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428...87003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — site returns HTTP 401 (Vercel Deployment Protection).
Requires visitor password or OIDC via Vercel Trusted Sources. No market data available.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
