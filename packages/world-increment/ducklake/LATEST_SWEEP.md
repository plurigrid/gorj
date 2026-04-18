# World-Increment Sweep + Hamming Snapshot — 2026-04-18

## Sweep Metadata
- **Date:** 2026-04-18
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| World Increments (this sweep) | 531 |
| Repo Snapshots (this sweep) | 473 |
| Event Snapshots (this sweep) | 58 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain Distribution
- ERGODIC (trit=0, `#d3869b`): 177 increments
- PLUS (trit=1, `#b8bb26`): 177 increments
- MINUS (trit=-1, `#cc241d`): 177 increments

GF(3) rule: `id mod 3 == 0` → ERGODIC · `id mod 3 == 1` → PLUS · `id mod 3 == 2` → MINUS

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user (zubyul social) | 43 |
| wasita | user (zubyul social) | 31 |
| migalkin | user (zubyul social) | 30 |
| zubyul | user | 24 |
| kristinezheng | user (zubyul social) | 18 |
| M1shaaa | user (zubyul social) | 16 |
| DJedamski | user (zubyul social) | 11 |
| **TOTAL** | | **473** |

### Events Captured
- bmorphism: 28 recent public events
- zubyul: 30 recent public events
- **Total:** 58 events

### Top Repos by Source

**plurigrid** — gorj (Clojure, 220 issues, pushed 2026-04-18), horse (TeX), reafference (HTML), nash-portal (Rust), asi (HTML, 17★)

**kubeflow** — kubeflow (15565★), pipelines (Python, 4119★), spark-operator (Python, 3111★), trainer (Go, 2080★), katib (Python, 1676★)

**TeglonLabs** — topological-inventory, polaris, vibespace (HTML, 2★), mcp-terminal

**bmorphism** — ocaml-mcp-sdk (OCaml, 60★), anti-bullshit-mcp-server (JS, 23★), shitcoin (Python, 5★)

**migalkin** — NodePiece (Python, 143★), StarE (Python, 88★), kgcourse2021 (HTML, 25★)

**AustinCStone** — TextGAN (Python, 92★), StereoVisionMRF (11★), SpectralClustering (3★)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

| World | Address | Balance (APT) |
|-------|---------|---------------|
| bob | 0x0a3c...512d | **12.6570** |
| F | 0x18a1...cf71 | 1.9605 |
| L | 0x7c2e...eba9 | 1.9273 |
| J | 0x4d96...7f54 | 1.8951 |
| alice | 0xc793...cc7b | 0.4364 |
| O | 0x7325...a89d | 0.2101 |
| K | 0xa732...5dc4 | 0.1620 |
| P | 0x6218...c948 | 0.1401 |
| M | 0x6fed...f2e9 | 0.1123 |
| N | 0xe7dd...1b2c | 0.1061 |
| Q | 0xac40...89a9 | 0.1032 |
| S | 0xb875...0386 | 0.0918 |
| R | 0x7ce6...6e10 | 0.0902 |
| T | 0x3578...4588 | 0.0737 |
| U | 0x7586...f956 | 0.0558 |
| A | 0x8699...9d7a | 0.0518 |
| Y | 0xd8e3...44c4 | 0.0444 |
| B | 0x3f89...cb13 | 0.0363 |
| X | 0xa95c...047d | 0.0426 |
| V | 0xb59d...f2c3 | 0.0488 |
| W | 0x5f32...c7b0 | 0.0407 |
| Z | 0x7af0...197c | 0.0243 |
| D | 0xf776...fdd1 | 0.0116 |
| C | 0x38b9...535e | 0.0102 |
| E | 0xdc1d...8d36 | 0.0094 |
| H | 0xce67...300f | 0.0017 |
| G | 0x69a3...f32 | 0.0007 |
| I | 0x070f...1fc9 | 0.0007 |

**Total Swarm Balance: 20.3448 APT**
**Average per wallet: 0.7266 APT**
**Method:** `0x1::coin::balance` view function (new fungible asset API)

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig contracts **healthy** — all require **2-of-N** signatures.

### MNX Markets (testnet.mnx.fi)

Site is a Next.js SPA. No public REST API endpoints returned JSON (`/api/markets`, `/api/v1/markets`, `/markets`, `/api/pools` all returned HTML shell). Market data **unavailable** without browser JS execution. Recorded as unavailable in `mnx_snapshots`.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **plurigrid/gorj**: 220 open issues — active GF(3) forj development
- **Hamming swarm leader**: bob (12.657 APT), followed by F, L, J
- **All 5 multisigs healthy**: A-B, A-G, Y-Z, S-T, V-W all require 2 sigs
