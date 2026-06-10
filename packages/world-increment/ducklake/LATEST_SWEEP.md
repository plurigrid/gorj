# World Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-06-10  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Summary

| ID | GF3 | Color | Source | Type | Repos | ★ Stars |
|----|-----|-------|--------|------|------:|-------:|
| 1 | PLUS (+1) | #b8bb26 | plurigrid | org | 100 | 76 |
| 2 | MINUS (-1) | #cc241d | kubeflow | org | 48 | 34,194 |
| 3 | ERGODIC (0) | #d3869b | TeglonLabs | org | 5 | 2 |
| 4 | PLUS (+1) | #b8bb26 | bmorphism | user | 100 | 247 |
| 5 | MINUS (-1) | #cc241d | zubyul | user | 49 | 14 |
| 6 | ERGODIC (0) | #d3869b | migalkin | user (social) | 19 | 280 |
| 7 | PLUS (+1) | #b8bb26 | DJedamski | user (social) | 6 | 3 |
| 8 | MINUS (-1) | #cc241d | wasita | user (social) | 11 | 5 |
| 9 | ERGODIC (0) | #d3869b | kristinezheng | user (social) | 5 | 0 |
| 10 | PLUS (+1) | #b8bb26 | M1shaaa | user (social) | 8 | 0 |
| 11 | MINUS (-1) | #cc241d | AustinCStone | user (social) | 40 | 108 |

**Total:** 391 repos across 11 world increments  
**GF(3) chain:** PLUS → MINUS → ERGODIC → PLUS → ...

### Notable Repos

**By Stars:**
- `kubeflow/kubeflow` — 15,714 ★ (ML Toolkit for Kubernetes)
- `kubeflow/pipelines` — 4,153 ★ (Machine Learning Pipelines)
- `kubeflow/spark-operator` — 3,126 ★ (Kubernetes Spark Operator)
- `migalkin/NodePiece` — 144 ★ (Large Knowledge Graph Representations)
- `migalkin/StarE` — 89 ★ (EMNLP 2020 Hyper-Relational KGs)
- `AustinCStone/TextGAN` — 92 ★ (GAN for text generation, TensorFlow)
- `bmorphism/ocaml-mcp-sdk` — 61 ★ (OCaml SDK for MCP)
- `plurigrid/asi` — 25 ★ (everything is topological chemputer!)

**Most Active (open issues):**
- `kubeflow/pipelines` — 494 open issues
- `plurigrid/gorj` — 473 open issues
- `bmorphism/Gay.jl` — 189 open issues

**Recently Pushed (2026-06-10):**
- `plurigrid/place` (TeX)
- `kubeflow/trainer` (Go — distributed AI training)
- `M1shaaa/M1shaaa` (profile config)

### Schema
```sql
world_increments (id, timestamp, gf3_trit, gf3_color, gf3_name, source_type, source_name, event_type, repo_name, actor, snapshot_hash)
repo_snapshots   (id, timestamp, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
```

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances

**28 wallets probed (alice, bob, A-Z)** via Aptos Mainnet fullnode

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...2d5d | 0.00000000 |
| A-Z | (26 wallets each) | 0.00000000 |

**All 28 wallets returned 0.0 APT** — CoinStore resources not initialized on mainnet.

### Multisig Contract Probes

`POST /v1/view` via `0x1::multisig_account::num_signatures_required`

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|:-------------:|:-------:|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

**All 5 multisig contracts healthy** — 2-of-N threshold across all pairs.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — gated behind Vercel deployment protection (auth-gate HTML, not JSON). No ticker data extractable.

### Schema
```sql
aptos_snapshots  (timestamp, world, address, balance_apt)
multisig_probes  (timestamp, pair, address, sigs_required, healthy)
mnx_snapshots    (timestamp, ticker, name, category, price, change_pct)
```

---

## GF(3) Color Chain Key

| Trit | Name | Hex | Meaning |
|------|------|-----|---------|
| +1 | PLUS | #b8bb26 | Active / additive |
| -1 | MINUS | #cc241d | Contractive / subtractive |
| 0 | ERGODIC | #d3869b | Stationary / mixing |
