# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-23

## Sweep Metadata
- **Date:** 2026-04-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 531 |
| Total Repo Snapshots | 475 |
| Event Increments | 56 (bmorphism: 28, zubyul: 28) |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| -1 | MINUS | `#cc241d` | 177 |
| 0 | ERGODIC | `#d3869b` | 177 |
| +1 | PLUS | `#b8bb26` | 177 |

GF(3) rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| wasita | user | 31 |
| migalkin | user | 30 |
| zubyul | user | 26 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **475** |

### Top Repos by Stars

| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow | — | 15597 | 2640 | 2026-01-05 |
| kubeflow/pipelines | Python | 4124 | 1985 | 2026-04-23 |
| kubeflow/spark-operator | Python | 3117 | 1483 | 2026-04-21 |
| kubeflow/trainer | Go | 2088 | 947 | 2026-04-23 |
| kubeflow/katib | Python | 1680 | 520 | 2026-04-14 |
| kubeflow/examples | Jsonnet | 1460 | 756 | 2025-04-14 |
| kubeflow/manifests | YAML | 1012 | 1065 | 2026-04-11 |
| kubeflow/arena | Go | 810 | 190 | 2026-04-16 |
| kubeflow/kale | Python | 686 | 156 | 2026-04-22 |
| kubeflow/mpi-operator | Go | 524 | 234 | 2026-04-14 |

### Notable bmorphism Repos
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |

### Notable migalkin Repos
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |

### Notable AustinCStone Repos
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

> Network: `fullnode.mainnet.aptoslabs.com` resolved to `34.36.29.190`. Wallets D, G, I returned transient DNS errors on retry. All others returned 0.000000 APT.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793ac…4cc7b | 0.000000 |
| bob | 0x0a3c00…512d5d | 0.000000 |
| A | 0x8699ed…e9d7a | 0.000000 |
| B | 0x3f892e…7cb13 | 0.000000 |
| C | 0x38b99e…535e | 0.000000 |
| D | 0xf77656…cfdd1 | N/A (DNS error) |
| E | 0xdc1d9d…8d36 | 0.000000 |
| F | 0x18a14b…cf71 | 0.000000 |
| G | 0x69a394…f32 | N/A (DNS error) |
| H | 0xce67c3…300f | 0.000000 |
| I | 0x070fe5…1fc9 | N/A (DNS error) |
| J | 0x4d964d…7f54 | 0.000000 |
| K | 0xa73204…5dc4 | 0.000000 |
| L | 0x7c2eae…eba9 | 0.000000 |
| M | 0x6fed37…f2e9 | 0.000000 |
| N | 0xe7dde6…1b2c | 0.000000 |
| O | 0x73252b…a89d | 0.000000 |
| P | 0x621879…c948 | 0.000000 |
| Q | 0xac40fa…c89a9 | 0.000000 |
| R | 0x7ce605…6e10 | 0.000000 |
| S | 0xb87530…0386 | 0.000000 |
| T | 0x35781d…f4588 | 0.000000 |
| U | 0x75860d…f9956 | 0.000000 |
| V | 0xb59dd8…af2c3 | 0.000000 |
| W | 0x5f32ae…c7b0 | 0.000000 |
| X | 0xa95cbb…3047d | 0.000000 |
| Y | 0xd8e328…444c4 | 0.000000 |
| Z | 0x7af0ef…e197c | 0.000000 |

**Total queryable APT: 0.000000** (25 addresses: 0 balance; 3 DNS-unavailable)

### Multisig Contract Probes

> `0x1::multisig_account::num_signatures_required` — Aptos mainnet HTTPS blocked by environment network policy for all 5 probes.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f4…87003 | N/A | ✗ |
| A-G | 0xf56c4a…0096 | N/A | ✗ |
| Y-Z | 0xd3ffe1…b883 | N/A | ✗ |
| S-T | 0x3b1c3a…d7883 | N/A | ✗ |
| V-W | 0x40fad7…eb6d | N/A | ✗ |

### MNX Markets

`https://testnet.mnx.fi` → HTTP 503 (service unavailable). No market data extracted.

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
