# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-20
**Agent:** world-increment-sweep + hamming-swarm-snapshot
**DuckDB version:** v1.5.2 (Variegata)
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Surveyed |
|---|---|---|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 101 |
| zubyul | user | 47 |
| migalkin | user (zubyul social) | 19 |
| wasita | user (zubyul social) | 10 |
| kristinezheng | user (zubyul social) | 6 |
| DJedamski | user (zubyul social) | 6 |
| M1shaaa | user (zubyul social) | 8 |
| AustinCStone | user (zubyul social) | 40 |
| **TOTAL** | | **388** |

### GF(3) Trit Distribution (this run: 73 increments inserted)

| Trit | Color | Name | Count |
|---|---|---|---|
| 0 | `#d3869b` | ERGODIC | 31 |
| 1 | `#b8bb26` | PLUS | 33 |
| -1 | `#cc241d` | MINUS | 32 |

GF(3) chain: `PLUS → MINUS → ERGODIC → …` (repeating, balanced)

### Notable Repos (Most Stars)

| Repo | Stars | Language | Description |
|---|---|---|---|
| kubeflow/kubeflow | 15,587 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,125 | Python | ML Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,116 | Python | K8s operator for Apache Spark |
| kubeflow/trainer | 2,085 | Go | Distributed AI Model Training |
| kubeflow/katib | 1,680 | Python | AutoML on Kubernetes |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation in TensorFlow |
| migalkin/NodePiece | 143 | Python | KG representations ICLR22 |
| migalkin/StarE | 89 | Python | Hyper-Relational KG EMNLP2020 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | OCaml SDK for Model Context Protocol |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | CosmWasm + zkVM RISC-V |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | MCP server for claim analysis |
| plurigrid/asi | 17 | HTML | everything is topological chemputer |

### Active Frontiers (pushed 2026-04)

- `plurigrid/nanoclj-zig` — NaN-boxed Clojure in Zig 0.15, GF(3) trit conservation, 21 issues
- `plurigrid/nash-portal` — NASH token TUI via ratzilla WASM + GeckoTerminal OHLCV
- `plurigrid/gorj` — this repo, forj + Rama topology + GF(3) coloring, 241 open issues
- `bmorphism/whale` — omniglot + sperm whale codas metawhaling
- `bmorphism/Gay.jl` — wide-gamut SPI color sampling, 187 open issues
- `zubyul/nash-web` / `zubyul/nash-tui` — NASH TUI in Rust (private)
- `zubyul/big-bad-plurigrid-quiz` — 27 flashcards from bmorphism/plurigrid/zubyul activity
- `wasita/wasita.github.io` — personal Svelte site, pushed 2026-04-20
- `migalkin/StarE` — still receiving stars as of 2026-04-16

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A–Z)

**API:** `https://fullnode.mainnet.aptoslabs.com/v1` — ledger height ~4,947,763,524

All 28 wallets: `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
APT CoinStore not initialized → **balance = 0.0 APT** for all.

| World | Address (truncated) | Balance APT |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Total swarm APT: 0.0**

### Multisig Contract Probes (5 pairs)

All probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Contract Address (truncated) | Sigs Required | Status |
|---|---|---|---|
| A-B | `0x0da4f428...4987003` | 2 | ✅ HEALTHY (2-of-2) |
| A-G | `0xf56c4a1c...fbc0096` | 2 | ✅ HEALTHY (2-of-2) |
| Y-Z | `0xd3ffe181...e75b883` | 2 | ✅ HEALTHY (2-of-2) |
| S-T | `0x3b1c3ae9...ded7883` | 2 | ✅ HEALTHY (2-of-2) |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✅ HEALTHY (2-of-2) |

**All 5 multisig contracts: 2-of-2, deployed and responsive.**

### MNX Markets (testnet.mnx.fi)

- Frontend: Next.js SPA, HTTP 200 ✅ online
- API (`api.testnet.mnx.fi`): **WebSocket-only** — no REST GET endpoints respond
- CSP reveals backend: `https://api.testnet.mnx.fi`, `https://carrot.megaeth.com` (MegaETH)
- Status: **SPA online; REST market data unavailable** (WS-only protocol)
- `mnx_snapshots` table: 0 rows (no extractable REST data)

---

## DuckDB Tables Summary

| Table | Rows (cumulative) |
|---|---|
| world_increments | 96 |
| repo_snapshots | 1,017 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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

- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
