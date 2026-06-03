# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-03

## Sweep Metadata
- **Date:** 2026-06-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned

| Source | Type | Repos Indexed | Total Stars |
|--------|------|---------------|-------------|
| kubeflow | org | 109 | 99,590 |
| migalkin | user (social graph) | 65 | 830 |
| bmorphism | user | 213 | 436 |
| AustinCStone | user (social graph) | 89 | 322 |
| plurigrid | org | 232 | 145 |
| zubyul | user | 59 | 27 |
| DJedamski | user (social graph) | 25 | 17 |
| TeglonLabs | org | 110 | 14 |
| wasita | user (social graph) | 64 | 10 |
| kristinezheng | user (social graph) | 38 | 0 |
| M1shaaa | user (social graph) | 34 | 0 |

### GF(3) Color Distribution (this sweep: 94 new increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 38 |
| 1 | #b8bb26 | PLUS | 40 |
| -1 | #cc241d | MINUS | 39 |

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...`

### Top Repos by Stars

| Repo | Language | Stars | Forks | Last Pushed |
|------|----------|-------|-------|-------------|
| kubeflow/kubeflow | — | 15,705 | 2,668 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,151 | 2,004 | 2026-06-03 |
| kubeflow/spark-operator | Python | 3,125 | 1,488 | 2026-06-01 |
| kubeflow/trainer | Go | 2,110 | 963 | 2026-06-03 |
| kubeflow/katib | Python | 1,685 | 525 | 2026-05-29 |
| kubeflow/examples | Jsonnet | 1,462 | 755 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,020 | 1,065 | 2026-06-02 |
| kubeflow/arena | Go | 811 | 191 | 2026-05-07 |
| kubeflow/mpi-operator | Go | 528 | 235 | 2026-06-02 |
| migalkin/NodePiece | Python | 144 | 21 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 16 | 2026-04-16 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 | 2026-01-16 |
| bmorphism/risc0-cosmwasm-example | Rust | 23 | 2 | 2022-10-20 |
| plurigrid/asi | HTML | 24 | 6 | 2026-04-26 |
| plurigrid/ontology | JavaScript | 8 | 9 | 2025-05-27 |
| plurigrid/vcg-auction | Rust | 7 | 2 | 2023-03-16 |
| migalkin/kgcourse2021 | HTML | 25 | 9 | 2026-02-16 |

### Most Recently Active (pushed 2026-06-03)

| Repo | Description |
|------|-------------|
| kubeflow/hub | Model Registry — ML model developers index and manage models |
| kubeflow/sdk | Universal Python SDK to run AI workloads on Kubernetes |
| kubeflow/pipelines | Machine Learning Pipelines for Kubeflow |
| bmorphism/Gay.jl | Wide-gamut color sampling with splittable determinism |
| plurigrid/gorj | forj + Rama topology nREPL routing + GF(3) gay trit coloring |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-03)

All 28 addresses (alice, bob, A–Z) queried via `fullnode.mainnet.aptoslabs.com/v1`. All returned **0 APT** — these swarm addresses have zero native coin balance on mainnet (may hold other on-chain resources or tokens not captured by APT CoinStore query).

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.00 |
| bob | 0x0a3c...512d | 0.00 |
| A | 0x8699...e9d7 | 0.00 |
| B | 0x3f89...b13 | 0.00 |
| C | 0x38b9...535e | 0.00 |
| D | 0xf776...fdd1 | 0.00 |
| E | 0xdc1d...8d36 | 0.00 |
| F | 0x18a1...cf71 | 0.00 |
| G | 0x69a3...7f32 | 0.00 |
| H | 0xce67...300f | 0.00 |
| I | 0x070f...1fc9 | 0.00 |
| J | 0x4d96...f54 | 0.00 |
| K | 0xa732...dc4 | 0.00 |
| L | 0x7c2e...ba9 | 0.00 |
| M | 0x6fed...2e9 | 0.00 |
| N | 0xe7dd...b2c | 0.00 |
| O | 0x7325...89d | 0.00 |
| P | 0x6218...948 | 0.00 |
| Q | 0xac40...89a9 | 0.00 |
| R | 0x7ce6...e10 | 0.00 |
| S | 0xb875...386 | 0.00 |
| T | 0x3578...588 | 0.00 |
| U | 0x7586...956 | 0.00 |
| V | 0xb59d...2c3 | 0.00 |
| W | 0x5f32...7b0 | 0.00 |
| X | 0xa95c...47d | 0.00 |
| Y | 0xd8e3...44c4 | 0.00 |
| Z | 0x7af0...97c | 0.00 |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`. All return **2/2** — healthy 2-of-2 threshold.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` serves a Next.js SPA — no REST endpoints exposed at `/api/markets` or `/api/v1/markets`. All market data is rendered client-side. **Status: UNAVAILABLE via API probe.** Recorded as a null row in `mnx_snapshots`.

---

## Database Summary

```
packages/world-increment/ducklake/world-increments.duckdb
├── world_increments   117 rows  (GF3-colored sweep events, 94 new this sweep)
├── repo_snapshots     cumulative (94 new rows this sweep)
├── aptos_snapshots     28 rows  (Hamming swarm: alice/bob + A–Z)
├── multisig_probes      5 rows  (all pairs 2/2 signatures, all HEALTHY)
└── mnx_snapshots        1 row   (unavailable marker — SPA, no REST API)
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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
