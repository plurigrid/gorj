# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-15

## Sweep Metadata
- **Date:** 2026-05-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 325 |
| Total Repo Snapshots | 325 |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets Captured | 13 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Total Stars | Total Forks | Latest Push |
|--------|------|-------|-------------|-------------|-------------|
| kubeflow | org | 48 | 34,056 | 13,419 | 2026-05-15 |
| bmorphism | user | 100 | 251 | 74 | 2026-05-15 |
| migalkin | user (social) | 6 | 278 | 48 | 2026-05-07 |
| AustinCStone | user (social) | 3 | 106 | 36 | 2026-04-01 |
| plurigrid | org | 100 | 74 | 44 | 2026-05-15 |
| zubyul | user | 49 | 14 | 2 | 2026-04-24 |
| wasita | user (social) | 5 | 4 | 1 | 2026-05-14 |
| DJedamski | user (social) | 3 | 3 | 1 | 2023-04-21 |
| TeglonLabs | org | 4 | 2 | 2 | 2026-01-01 |
| kristinezheng | user (social) | 4 | 0 | 0 | 2026-05-14 |
| M1shaaa | user (social) | 3 | 0 | 0 | 2024-12-31 |
| **TOTAL** | | **325** | **34,788** | **13,627** | |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,632 | — | 2026-05-07 |
| kubeflow/pipelines | 4,140 | Python | 2026-05-15 |
| kubeflow/spark-operator | 3,125 | Python | 2026-05-12 |
| kubeflow/trainer | 2,098 | Go | 2026-05-15 |
| kubeflow/katib | 1,682 | Python | 2026-05-09 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,017 | YAML | 2026-05-13 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |

### Notable Active Repos (plurigrid, pushed 2026-05-15)

- **plurigrid/gorj** — forj + Rama topology nREPL routing + GF(3) gay trit coloring (201 open issues)
- **plurigrid/asi** — everything is topological chemputer! (23 stars)
- **plurigrid/zig-syrup** — High-performance Zig OCapN Syrup implementation (2 stars)
- **plurigrid/nanoclj-zig** — NaN-boxed Clojure interpreter in Zig 0.15

### GF(3) Trit Distribution (325 world_increments)

| Name | Color Hex | Trit | Count |
|------|-----------|------|-------|
| ERGODIC | #d3869b | 0 | 108 |
| PLUS | #b8bb26 | +1 | 109 |
| MINUS | #cc241d | −1 | 108 |

GF(3) chain balanced at 108/109/108 across 325 events (108 full cycles + 1 PLUS remainder).

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming addresses (alice, bob, A–Z) queried via `fullnode.mainnet.aptoslabs.com`.

**Result:** All 28 addresses returned **0 APT** balance — accounts exist on-chain but hold no APT coin resources at sweep time.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...512d | 0.00000000 |
| A–Z (26 addrs) | 0x8699...→ 0x7af0... | 0.00000000 each |

### Multisig Contract Probes

`POST 0x1::multisig_account::num_signatures_required` for each pair:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | **2** | ✓ |
| A-G | 0xf56c...0096 | **2** | ✓ |
| Y-Z | 0xd3ff...b883 | **2** | ✓ |
| S-T | 0x3b1c...7883 | **2** | ✓ |
| V-W | 0x40fa...eb6d | **2** | ✓ |

All 5 multisig contracts require **2 signatures** — healthy 2-of-N configuration.

### MNX Markets Snapshot (testnet.mnx.fi)

`/api/markets` → 404; data extracted from SPA at root:

| Ticker | Name | Category | Price | Chg % |
|--------|------|----------|-------|-------|
| OAI26 | OpenAI Final 2026 Valuation | prediction_market | $530B | −0.38% |
| ANT26 | Anthropic Final 2026 Valuation | prediction_market | $419B | +0.24% |
| CPI26 | U.S. CPI Annual Inflation Dec 2026 | prediction_market | 3% | +9.54% |
| NVDA | NVIDIA Corp | stock | $226.99 | −3.88% |
| MSFT | Microsoft Corp | stock | $422.01 | +3.36% |
| AAPL | Apple Inc | stock | $300.20 | +0.67% |
| TSLA | Tesla Inc | stock | $427.33 | −4.05% |
| AMZN | Amazon.com Inc | stock | $262.46 | −1.82% |
| GOLD | Gold Spot | commodity | $4,600 | −2.66% |
| SILVER | Silver Spot | commodity | $76.64 | −9.58% |
| USO | US Oil Fund | commodity | $147.02 | +3.65% |
| DPREZ | Democrat Elected President 2028 | prediction_market | 50% | −2.73% |
| INVADE27 | China invades Taiwan before 2027 | prediction_market | 17% | +5.77% |

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
- **kubeflow/kubeflow**: 15,632 stars — ML platform for Kubernetes (Δ+67 from April sweep)
- **kubeflow/pipelines**: 4,140 stars — active push 2026-05-15
- **kubeflow/notebooks**: new addition — Kubeflow Notebooks for Kubernetes
- **kubeflow/mcp-apache-spark-history-server**: new — MCP server for Spark debugging
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: OCaml SDK for MCP — most starred in bmorphism graph
- **AustinCStone/TextGAN**: 92 stars — TensorFlow text GAN
- **plurigrid/gorj**: 201 open issues — active development, pushed today
- **Aptos Hamming swarm**: all 28 addresses at 0 APT (accounts initialized, unfunded)
- **All 5 multisigs**: healthy at 2-of-N threshold
