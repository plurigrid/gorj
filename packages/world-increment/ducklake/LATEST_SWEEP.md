# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-31

## Sweep Metadata
- **Date:** 2026-05-31
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 361 |
| Total Repo Snapshots | 361 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 120 |
| +1 | PLUS | `#b8bb26` | 121 |
| -1 | MINUS | `#cc241d` | 120 |

361 increments with near-perfect GF(3) balance (120/121/120).  
Rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS.

---

## Top Repos by Stars

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,695 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,149 | 2026-05-31 |
| kubeflow/spark-operator | Python | 3,124 | 2026-05-29 |
| kubeflow/trainer | Go | 2,109 | 2026-05-30 |
| kubeflow/katib | Python | 1,685 | 2026-05-29 |
| kubeflow/examples | Jsonnet | 1,463 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,019 | 2026-05-29 |
| kubeflow/arena | Go | 811 | 2026-05-07 |
| kubeflow/kale | Python | 691 | 2026-05-29 |
| kubeflow/mpi-operator | Go | 528 | 2026-05-29 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| plurigrid/asi | HTML | 23 | 2026-04-26 |
| bmorphism/risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| bmorphism/say-mcp-server | JavaScript | 20 | 2025-01-07 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |

---

## Repo Counts by Source

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 74 |
| bmorphism | user | 100 | 247 |
| zubyul | user | 49 | 14 |
| kubeflow | org | 48 | 34,159 |
| migalkin | user (social) | 19 | 280 |
| wasita | user (social) | 11 | 5 |
| AustinCStone | user (social) | 10 | 108 |
| M1shaaa | user (social) | 8 | 0 |
| kristinezheng | user (social) | 6 | 0 |
| DJedamski | user (social) | 6 | 3 |
| TeglonLabs | org | 4 | 2 |
| **TOTAL** | | **361** | **34,892** |

---

## Most Active Repos (Open Issues)

| Repo | Open Issues | Source |
|------|------------|--------|
| plurigrid/gorj | 278 | This very repo |
| bmorphism/Gay.jl | 189 | Wide-gamut deterministic color sampling |
| kubeflow/notebooks | 195 | ML notebooks for Kubernetes |
| kubeflow/docs-agent | 154 | Documentation AI Agent |
| kubeflow/sdk | 135 | Universal Python SDK for Kubernetes |
| plurigrid/eirobri | 28 | EiRoBri replay world |

---

## Language Distribution (Top 10)

| Language | Repos |
|----------|-------|
| Python | 67 |
| Rust | 26 |
| JavaScript | 23 |
| TypeScript | 23 |
| Go | 15 |
| Clojure | 14 |
| Jupyter Notebook | 14 |
| HTML | 14 |
| Julia | 9 |
| Zig | 7 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 Hamming swarm wallets queried via `fullnode.mainnet.aptoslabs.com` with 1s sleep between calls.

| World | Address (truncated) | APT Balance |
|-------|---------------------|------------|
| alice | 0xc793...cc7b | 0.0000 |
| bob | 0x0a3c...2d5d | 0.0000 |
| A | 0x8699...9d7a | 0.0000 |
| B | 0x3f89...b13 | 0.0000 |
| C | 0x38b9...535e | 0.0000 |
| D | 0xf776...fdd1 | 0.0000 |
| E | 0xdc1d...8d36 | 0.0000 |
| F | 0x18a1...cf71 | 0.0000 |
| G | 0x69a3...f32 | 0.0000 |
| H | 0xce67...300f | 0.0000 |
| I | 0x070f...1fc9 | 0.0000 |
| J | 0x4d96...f54 | 0.0000 |
| K | 0xa732...dc4 | 0.0000 |
| L | 0x7c2e...ba9 | 0.0000 |
| M | 0x6fed...2e9 | 0.0000 |
| N | 0xe7dd...b2c | 0.0000 |
| O | 0x7325...a89d | 0.0000 |
| P | 0x6218...c948 | 0.0000 |
| Q | 0xac40...c89a9 | 0.0000 |
| R | 0x7ce6...e10 | 0.0000 |
| S | 0xb875...0386 | 0.0000 |
| T | 0x3578...f588 | 0.0000 |
| U | 0x7586...9956 | 0.0000 |
| V | 0xb59d...f2c3 | 0.0000 |
| W | 0x5f32...c7b0 | 0.0000 |
| X | 0xa95c...047d | 0.0000 |
| Y | 0xd8e3...44c4 | 0.0000 |
| Z | 0x7af0...97c | 0.0000 |

**Total swarm APT: 0.0000**  
Note: All wallets appear uninitialized or empty on mainnet (CoinStore resource not found or balance=0).

### Multisig Probes (5/5 Healthy ✓)

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4f428...987003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c...bc0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4...80eb6d | 2 | ✓ HEALTHY |

All pairs require **2-of-N signatures**. All contracts responsive on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

**Status: DATA UNAVAILABLE**  
`testnet.mnx.fi` is a Next.js SPA (HTTP 200 confirmed). REST API paths (`/api/markets`, `/api/v1/markets`) return 404. Market data not extractable without browser execution. Recorded as `MNX_UNAVAILABLE` in `mnx_snapshots` table.

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)
-- 361 rows: per-repo increments with GF(3) trit coloring

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
-- 361 rows: full GitHub repo metadata

aptos_snapshots(timestamp, world, address, balance_apt)
-- 28 rows: alice, bob, A-Z wallet balances (all 0.0 APT)

multisig_probes(timestamp, pair, address, sigs_required, healthy)
-- 5 rows: A-B, A-G, Y-Z, S-T, V-W (all 2 sigs, all healthy)

mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
-- 1 row: MNX_UNAVAILABLE marker
```

---

## Notable Highlights

- **kubeflow/kubeflow**: 15,695★ — ML Toolkit for Kubernetes (↑130 since Apr sweep)
- **kubeflow/pipelines**: 4,149★ — pushed today 2026-05-31 (actively maintained)
- **plurigrid/gorj**: 278 open issues — this very repo, most active in the plurigrid org
- **bmorphism/Gay.jl**: 189 open issues — wide-gamut deterministic color sampling
- **bmorphism/ocaml-mcp-sdk**: 61★ — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **migalkin/NodePiece**: 144★ — ICLR'22 paper, active KG embedding research
- **zubyul/tilelang-kernels**: GF(3) GPU kernels targeting NVIDIA GB10 Blackwell
- **All 5 multisig contracts**: Healthy with 2-sigs-required
- **GF(3) balance**: 120 ERGODIC / 121 PLUS / 120 MINUS across 361 increments

*Generated by world-increment-sweep + hamming-swarm-snapshot agent — 2026-05-31*
