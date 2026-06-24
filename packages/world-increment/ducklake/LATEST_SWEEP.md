# World-Increment Sweep + Hamming Snapshot — 2026-06-24

## Sweep Metadata
- **Date:** 2026-06-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 13 |
| Total Repo Snapshots | 115 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — All 13 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | snapshot | 0 | `#d3869b` | **ERGODIC** |
| 2  | kubeflow (org) | snapshot | +1 | `#b8bb26` | **PLUS** |
| 3  | TeglonLabs (org) | snapshot | -1 | `#cc241d` | **MINUS** |
| 4  | bmorphism (user) | snapshot | 0 | `#d3869b` | **ERGODIC** |
| 5  | zubyul (user) | snapshot | +1 | `#b8bb26` | **PLUS** |
| 6  | migalkin (user) | snapshot | -1 | `#cc241d` | **MINUS** |
| 7  | DJedamski (user) | snapshot | 0 | `#d3869b` | **ERGODIC** |
| 8  | wasita (user) | snapshot | +1 | `#b8bb26` | **PLUS** |
| 9  | kristinezheng (user) | snapshot | -1 | `#cc241d` | **MINUS** |
| 10 | M1shaaa (user) | snapshot | 0 | `#d3869b` | **ERGODIC** |
| 11 | AustinCStone (user) | snapshot | +1 | `#b8bb26` | **PLUS** |
| 12 | bmorphism (user) | aptos_snapshot | -1 | `#cc241d` | **MINUS** |
| 13 | zubyul (user) | aptos_snapshot | 0 | `#d3869b` | **ERGODIC** |

GF(3) rule: `id%3==0 → ERGODIC #d3869b`, `id%3==1 → PLUS #b8bb26`, `id%3==2 → MINUS #cc241d`

---

## Repo Counts by Source

| Source | Type | Repos Sampled | Total Stars | Latest Push |
|--------|------|--------------|-------------|-------------|
| plurigrid | org | 27 | 69 | 2026-06-24 (gorj, place) |
| kubeflow | org | 19 | 32,647 | 2026-06-24 (spark-operator, sdk) |
| TeglonLabs | org | 5 | 2 | 2026-06-08 (jank-crane) |
| bmorphism | user | 23 | 209 | 2026-06-24 (Gay.jl) |
| zubyul | user | 17 | 7 | 2026-04-24 (voice-observatory) |
| migalkin | user | 5 | 276 | 2026-05-28 (RWL) |
| DJedamski | user | 2 | 1 | 2023-04-21 |
| wasita | user | 5 | 4 | 2026-06-19 (proj-template) |
| kristinezheng | user | 3 | 0 | 2026-06-07 |
| M1shaaa | user | 3 | 0 | 2026-02-04 |
| AustinCStone | user | 6 | 107 | 2026-04-01 (StereoVisionMRF) |
| **TOTAL** | | **115** | **~33,322** | |

---

## Hot Repos (pushed 2026-06-24)

- **kubeflow/spark-operator** — 3,128★ — Kubernetes operator for Apache Spark
- **kubeflow/sdk** — 121★ — Universal Python SDK for Kubeflow on Kubernetes
- **kubeflow/mcp-server** — 17★ — MCP Server for AI-Assisted Development with Kubeflow
- **plurigrid/gorj** — 0★ — forj + Rama topology nREPL routing + GF(3) gay trit coloring (784 open issues!)
- **bmorphism/Gay.jl** — 2★ — Wide-gamut color sampling with splittable determinism (187 open issues)
- **plurigrid/place** — 1★ — pushed 2026-06-24T00:41

## Notable Clusters

**GF(3) / Gay.jl ecosystem:** bmorphism/Gay.jl, zubyul/Gay.jl, plurigrid/gay-rs, plurigrid/gay-go, plurigrid/gay-terminal, plurigrid/lazygay, zubyul/gay-world, zubyul/gay-terminal-colors — deterministic wide-gamut color infrastructure shared across the plurigrid social graph.

**MCP server ecosystem:** bmorphism hosts 10+ MCP servers (babashka, say, manifold, nats, anti-bullshit, marginalia, penrose, hypernym, graphistry, slowtime); kubeflow recently launched kubeflow/mcp-server and kubeflow/mcp-apache-spark-history-server.

**NASH token:** plurigrid/nash-portal (Rust/ratzilla WASM) + zubyul/nash-tui — browser and TUI frontends for the same GeckoTerminal OHLCV feed.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) returned **0 APT** from the mainnet CoinStore resource endpoint. Accounts exist on-chain but hold no APT in `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — either zero balance or resource not initialized.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.00 |
| bob | 0x0a3c...2d5d | 0.00 |
| A–Z (26) | various | 0.00 each |

### Multisig Contract Probes (5 pairs) — ALL HEALTHY ✓

All 5 multisig contracts responded with `num_signatures_required = 2`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` is behind Vercel deployment protection. All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) returned authentication-required pages. No market data extractable without bypass token.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,742 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,157 stars — most popular ML pipeline for Kubernetes (pushed 2026-06-23)
- **kubeflow/spark-operator**: 3,128 stars — Kubernetes operator for Apache Spark (pushed 2026-06-24)
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs (TensorFlow)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring (784 open issues)
- **Increment 13**: ERGODIC #d3869b — zubyul aptos_snapshot closes the sweep

*Generated by world-increment-sweep + hamming-swarm-snapshot agent, 2026-06-24*
