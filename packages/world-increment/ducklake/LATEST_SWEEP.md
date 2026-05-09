# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-09

## Sweep Metadata
- **Date:** 2026-05-09T21:18 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 59 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Market Snapshots | 0 (SPA — no public API) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — All 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Top Repos by Stars

| Repo | Language | Stars | Forks | Pushed |
|------|----------|-------|-------|--------|
| kubeflow/kubeflow | — | 15,628 | 2,647 | 2026-05-09 |
| kubeflow/pipelines | Python | 4,137 | 1,989 | 2026-05-09 |
| kubeflow/spark-operator | Python | 3,125 | 1,480 | 2026-05-09 |
| kubeflow/trainer | Go | 2,096 | 948 | 2026-05-09 |
| kubeflow/katib | Python | 1,683 | 522 | 2026-05-05 |
| kubeflow/examples | Jsonnet | 1,462 | 756 | 2026-05-08 |
| migalkin/NodePiece | Python | 144 | 21 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 16 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-05-08 |
| plurigrid/gorj | Clojure | 0 | 0 | 2026-05-08 (131 issues) |

### Plurigrid Activity Highlights (2026)
- **gorj** (Clojure): 131 open issues — active GF(3) compositional REPL work
- **zig-syrup**: OCapN Syrup in Zig, pushed 2026-04-30
- **nanoclj-zig**: NaN-boxed Clojure in Zig 0.15, interaction nets + GF(3) conservation
- **nash-portal**: NASH token TUI with ratzilla WASM + GeckoTerminal OHLCV
- **asi**: 21 stars — topological chemputer, pushed 2026-05-07

### bmorphism Highlights
- **ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP via Jane Street oxcaml_effect
- **Gay.jl**: 187 open issues — wide-gamut SPI color sampling with LispSyntax
- **anti-bullshit-mcp-server**: 23 stars — claim analysis with epistemological frameworks
- **whale**: MATLAB — omniglot + sperm whale codas = metawhaling

### Note on GitHub API
Unauthenticated GitHub REST API (60 req/hr) was rate-exhausted. All data obtained via authenticated MCP GitHub search tools. Events endpoints for bmorphism/zubyul unavailable without auth token.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-05-09)

All 28 addresses (alice, bob, A–Z) probed via `https://fullnode.mainnet.aptoslabs.com/v1`.

**Result:** `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource absent on all addresses — no APT native coin balance registered.

| World | Address (truncated) | APT |
|-------|---------------------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

**Total swarm APT: 0.00000000**

### Multisig Contract Probes (Aptos Mainnet)

Function: `0x1::multisig_account::num_signatures_required`

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**5/5 multisigs healthy. All enforce 2-of-N threshold.**

### MNX Markets (testnet.mnx.fi)

Site returns HTTP 200 with a Next.js SPA (293KB HTML). CSP reveals live API at `https://api.testnet.mnx.fi` but no public unauthenticated REST endpoints responded with structured JSON at `/api/markets`, `/api/v1/markets`, or `/markets`.

**Status: MNX market data unavailable — wallet-connected SPA only.**

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
- `id mod 3 == 0` → trit=0,  color=#d3869b, name=ERGODIC
