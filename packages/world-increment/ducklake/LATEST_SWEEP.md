# World-Increment Sweep — 2026-04-01

## Sweep Metadata
- **Date:** 2026-04-01T08:00:00Z (UTC)
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 254 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GitHub Sweep: Repos Per Source

| Source | Type | Repos | GF3 ID | GF3 Trit | GF3 Color | GF3 Name |
|--------|------|-------|--------|----------|-----------|----------|
| plurigrid | org | 93 | 1 | 1 | #b8bb26 | PLUS |
| kubeflow | org | 46 | 2 | -1 | #cc241d | MINUS |
| TeglonLabs | org | 3 | 3 | 0 | #d3869b | ERGODIC |
| bmorphism | user | 15 | 4 | 1 | #b8bb26 | PLUS |
| zubyul | user | 44 | 5 | -1 | #cc241d | MINUS |
| migalkin | user | 19 | 6 | 0 | #d3869b | ERGODIC |
| DJedamski | user | 6 | 7 | 1 | #b8bb26 | PLUS |
| wasita | user | 9 | 8 | -1 | #cc241d | MINUS |
| kristinezheng | user | 6 | 9 | 0 | #d3869b | ERGODIC |
| M1shaaa | user | 8 | 10 | 1 | #b8bb26 | PLUS |
| AustinCStone | user | 5 | 11 | -1 | #cc241d | MINUS |
| **TOTAL** | | **254** | | | | |

## Top Repos by Stars (All Sources)

| Org/User | Repo | Stars | Forks | Language |
|----------|------|-------|-------|----------|
| kubeflow | kubeflow | 15,548 | 2,626 | — |
| kubeflow | pipelines | 4,118 | 1,983 | Python |
| kubeflow | spark-operator | 3,110 | 1,480 | Python |
| kubeflow | trainer | 2,071 | 943 | Go |
| kubeflow | katib | 1,674 | 520 | Python |
| kubeflow | examples | 1,459 | 755 | Jsonnet |
| kubeflow | manifests | 1,006 | 1,068 | YAML |
| kubeflow | arena | 809 | 190 | Go |
| kubeflow | kale | 681 | 156 | Python |
| kubeflow | mpi-operator | 519 | 236 | Go |
| migalkin | NodePiece | 143 | 21 | Python |
| AustinCStone | TextGAN | 92 | 30 | Python |
| migalkin | StarE | 88 | 16 | Python |
| bmorphism | ocaml-mcp-sdk | 60 | 2 | OCaml |
| migalkin | kgcourse2021 | 25 | 9 | HTML |
| bmorphism | anti-bullshit-mcp-server | 23 | 7 | JavaScript |
| bmorphism | risc0-cosmwasm-example | 23 | 2 | Rust |
| bmorphism | say-mcp-server | 20 | 8 | JavaScript |
| bmorphism | babashka-mcp-server | 18 | 6 | JavaScript |
| plurigrid | asi | 14 | 4 | HTML |

---

## Aptos Hamming Swarm Snapshot

**Query Time:** 2026-04-01T08:00:00Z
**Note:** All 28 accounts returned 0 APT — addresses have no initialized CoinStore resource on Aptos mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...9a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

---

## Multisig Contract Probes

All 5 multisig contracts successfully probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

All multisig contracts require **2 signatures** and are healthy (responsive on Aptos mainnet).

---

## MNX Markets Status

**Status: UNAVAILABLE**

Both endpoints returned HTML (Next.js frontend) rather than JSON API responses:
- `https://testnet.mnx.fi/api/markets` → HTML 200
- `https://testnet.mnx.fi/api/v1/markets` → HTML 200

No public REST API is exposed at these paths. No market data recorded in `mnx_snapshots`.

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

## Notable Highlights
- **kubeflow/pipelines**: 4,118 stars — ML pipelines for Kubernetes (active as of 2026-04-01)
- **kubeflow/spark-operator**: 3,110 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 143 stars — ICLR'22 knowledge graph representations
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — TensorFlow text generation GAN
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **plurigrid/asi**: 14 stars — everything is topological chemputer (pushed 2026-03-30)
