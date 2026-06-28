# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-28

## Sweep Metadata
- **Date:** 2026-06-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Prior sweep:** 2026-04-12 (471 snapshots) → **now 968 cumulative**

---

## Job 1: GitHub Social Graph Sweep

### Repo Counts by Source (cumulative)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 200 |
| bmorphism | user | 200 |
| TeglonLabs | org | 111 |
| kubeflow | org | 94 |
| AustinCStone | user | 86 |
| wasita | user | 60 |
| migalkin | user | 60 |
| zubyul | user | 48 |
| kristinezheng | user | 41 |
| M1shaaa | user | 40 |
| DJedamski | user | 28 |
| **TOTAL** | | **968** |

### Top Repos by Stars (all sweeps)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,572 | — | 2026-01-05 |
| kubeflow/pipelines | 4,119 | Python | 2026-04-14 |
| kubeflow/spark-operator | 3,114 | Python | 2026-04-13 |
| kubeflow/trainer | 2,082 | Go | 2026-04-13 |
| kubeflow/katib | 1,678 | Python | 2026-04-14 |
| kubeflow/examples | 1,459 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,010 | YAML | 2026-04-11 |
| migalkin/NodePiece | 143 | Python | — |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | — |
| AustinCStone/TextGAN | 92 | Python | — |

### Language Distribution (top 15)

| Language | Repos |
|----------|-------|
| Python | 158 |
| HTML | 38 |
| Go | 36 |
| Rust | 31 |
| JavaScript | 29 |
| Jupyter Notebook | 28 |
| TypeScript | 25 |
| R | 19 |
| Clojure | 16 |
| Jsonnet | 16 |
| C | 12 |
| Java | 12 |
| TeX | 10 |
| Julia | 10 |

### Most Recently Pushed (this sweep)

| Repo | Stars | Pushed At |
|------|-------|-----------|
| M1shaaa/M1shaaa | 0 | 2026-06-28T13:38:52Z ← today |
| TeglonLabs/jank-crane | 0 | 2026-06-08T19:03:03Z |
| kristinezheng/kristinezheng.github.io | 0 | 2026-06-07T22:52:50Z |
| plurigrid/gorj | 0 | 2026-04-14T01:07:28Z |
| kubeflow/katib | 1,678 | 2026-04-14T01:21:37Z |

### Notable: TeglonLabs/jank-crane
C++ IR hub with "loopify pass spec, **GF3 convergence maps**, simonw workflow" — GF(3) motif appears in the social graph's own repos.

### GF(3) Color Chain — 37 World Increments

| Name | Trit | Color | Count |
|------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 11 |
| PLUS | +1 | `#b8bb26` | 13 |
| MINUS | −1 | `#cc241d` | 13 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## Job 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

28 addresses queried (alice, bob, A–Z) against `fullnode.mainnet.aptoslabs.com`.

**All 28 wallets: 0.0 APT** — unfunded or freshly generated addresses.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addrs) | 0.0 each |

### Multisig Contract Probes

All 5 contracts healthy — **2 signatures required** each (m-of-n = 2).

| Pair | Address | Sigs | Healthy |
|------|---------|------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Testnet Markets

**Status: Unavailable** — `testnet.mnx.fi` is Vercel-auth-protected. Both root and `/api/markets` return authentication walls. No market data extractable without credentials.

---

## DuckDB Ducklake State

**Path:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 37 |
| repo_snapshots | 968 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth-walled) |

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

## GF(3) Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=−1, color=#cc241d, name=MINUS
