# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-15

## Sweep Metadata
- **Date:** 2026-07-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all sweeps) | 160 |
| Total Repo Snapshots (all sweeps) | 1081 |
| Sources Queried This Run | 6 |

### Sources Queried This Run

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 106 |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |

**Note:** GitHub search API rejects multi-user OR queries; DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone not searchable in one call — migalkin searched individually.

### GF(3) Color Distribution (all increments)

| Name | Trit | Color | Count |
|------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 52 |
| PLUS | +1 | `#b8bb26` | 54 |
| MINUS | -1 | `#cc241d` | 54 |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → …`

### Top Repos by Stars (latest snapshot)

| Repo | Language | ★ Stars | 🍴 Forks | Pushed |
|------|----------|---------|---------|--------|
| kubeflow/kubeflow | — | 15,776 | 2,685 | 2026-07-15 |
| kubeflow/pipelines | Python | 4,166 | 2,034 | 2026-07-15 |
| kubeflow/spark-operator | Python | 3,136 | 1,500 | 2026-07-14 |
| kubeflow/trainer | Go | 2,146 | 987 | 2026-07-15 |
| kubeflow/katib | Python | 1,690 | 533 | 2026-07-15 |
| migalkin/NodePiece | Python | 144 | 21 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 16 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-05-08 |
| bmorphism/risc0-cosmwasm-example | Rust | 23 | 2 | 2025-05-21 |
| bmorphism/say-mcp-server | JavaScript | 20 | 9 | 2026-03-19 |

### Notable Activity (July 2026)

- **plurigrid/gorj** (Clojure) — pushed 2026-07-15, 1177 open issues, GF(3) REPL orchestration
- **plurigrid/asi** (HTML) — pushed 2026-07-10, topological chemputer (30★)
- **bmorphism/gay-chat** (Scheme) — pushed 2026-07-14, gay://chat via Spritely Brassica
- **bmorphism/Gay.jl** (Julia) — pushed 2026-07-14, 187 open issues, GF(3) wide-gamut color SPI
- **kubeflow/trainer** (Go) — pushed 2026-07-15, distributed LLM fine-tuning on K8s

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**Ledger version probed:** 6285940709 (mainnet)  
**Result:** All 28 wallets returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — CoinStore not initialized.

**Total APT across all 28 wallets: 0.00000000 APT**

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793ac…cc7b | 0.0 |
| bob | 0x0a3c00…2d5d | 0.0 |
| A | 0x8699ed…9d7a | 0.0 |
| B | 0x3f892e…b13 | 0.0 |
| C | 0x38b99e…535e | 0.0 |
| D | 0xf77656…fdd1 | 0.0 |
| E | 0xdc1d9d…8d36 | 0.0 |
| F | 0x18a14b…3cf71 | 0.0 |
| G | 0x69a394…7f32 | 0.0 |
| H | 0xce67c3…300f | 0.0 |
| I | 0x070fe5…1fc9 | 0.0 |
| J | 0x4d964d…7f54 | 0.0 |
| K | 0xa73204…5dc4 | 0.0 |
| L | 0x7c2eae…ba9 | 0.0 |
| M | 0x6fed37…f2e9 | 0.0 |
| N | 0xe7dde6…1b2c | 0.0 |
| O | 0x73252b…a89d | 0.0 |
| P | 0x621879…c948 | 0.0 |
| Q | 0xac40fa…c89a9 | 0.0 |
| R | 0x7ce605…6e10 | 0.0 |
| S | 0xb87530…0386 | 0.0 |
| T | 0x35781d…4588 | 0.0 |
| U | 0x75860d…f9956 | 0.0 |
| V | 0xb59dd8…af2c3 | 0.0 |
| W | 0x5f32ae…c7b0 | 0.0 |
| X | 0xa95cbb…047d | 0.0 |
| Y | 0xd8e328…444c4 | 0.0 |
| Z | 0x7af0ef…197c | 0.0 |

### Multisig Account Probes

All 5 multisig accounts **healthy** — 2-of-N threshold active:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f4…7003 | 2 | ✅ healthy |
| A-G | 0xf56c4a…0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1…b883 | 2 | ✅ healthy |
| S-T | 0x3b1c3a…7883 | 2 | ✅ healthy |
| V-W | 0x40fad7…eb6d | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` is behind **Vercel deployment authentication** —
requires visitor password or OIDC token. No market data extractable. `mnx_snapshots` table: 0 rows.

---

## DuckDB Schema

```sql
-- packages/world-increment/ducklake/world-increments.duckdb
world_increments   (160 rows) — GF(3)-colored increment log
repo_snapshots    (1081 rows) — GitHub repo metadata across all sweeps
aptos_snapshots     (28 rows) — Hamming swarm wallet balances (this run)
multisig_probes      (5 rows) — On-chain multisig health checks
mnx_snapshots        (0 rows) — MNX markets (auth-gated, unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
