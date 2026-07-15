# World-Increment Sweep — 2026-07-15

## Sweep Metadata
- **Date:** 2026-07-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python SDK)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 307 |
| Total Repo Snapshots (cumulative) | 1,228 |
| This-run repo count | 284 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — This Run (284 new increments)

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=**MINUS**

| GF3 Name | Color | Count (cumulative) |
|----------|-------|--------------------|
| ERGODIC | `#d3869b` | 101 |
| PLUS | `#b8bb26` | 103 |
| MINUS | `#cc241d` | 103 |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 50 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| TeglonLabs | org | 5 |
| migalkin | social | 8 |
| wasita | social | 5 |
| AustinCStone | social | 6 |
| DJedamski | social | 4 |
| kristinezheng | social | 4 |
| M1shaaa | social | 4 |
| **TOTAL** | | **284** |

### Top Repos by Stars (this run)

| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| kubeflow/kubeflow | — | 15,777 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,166 | 2026-07-15 |
| kubeflow/spark-operator | Python | 3,136 | 2026-07-14 |
| kubeflow/trainer | Go | 2,148 | 2026-07-14 |
| kubeflow/katib | Python | 1,690 | 2026-07-15 |
| kubeflow/examples | Jsonnet | 1,460 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1,029 | 2026-07-13 |
| kubeflow/arena | Go | 815 | 2026-07-14 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| plurigrid/asi | HTML | 30 | 2026-07-10 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |
| bmorphism/say-mcp-server | JavaScript | 20 | 2025-01-07 |

### Plurigrid Highlights (pushed 2026)

| Repo | Language | Stars | Issues | Description |
|------|----------|-------|--------|-------------|
| gorj | Clojure | 1 | 1,179 | forj + Rama topology nREPL routing + GF(3) gay trit coloring |
| asi | HTML | 30 | 4 | everything is topological chemputer! |
| place | TeX | 1 | 13 | |
| eirobri | Clojure | 0 | 30 | EiRoBri replay world |
| nash-portal | Rust | 2 | 1 | NASH token TUI in the browser |
| zig-syrup | Zig | 2 | 0 | High-performance Zig OCapN Syrup |
| nanoclj-zig | Zig | 1 | 20 | NaN-boxed Clojure interpreter in Zig 0.15 |
| gatomic | Clojure | 0 | 0 | Deterministic color identity store with sonification |

### bmorphism Highlights (pushed 2026)

| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| Gay.jl | Julia | 2 | Wide-gamut color sampling (187 open issues) |
| ocaml-mcp-sdk | OCaml | 61 | OCaml SDK for MCP using Jane Street's oxc |
| gay-chat | Scheme | 0 | gay://chat over Spritely Brassica Chat |
| world | Python | 0 | Local worlds launcher for SA3, jank, world proofs |
| oxgame | OCaml | 0 | Stellar resolution and open-game composition |

### zubyul Highlights

| Repo | Language | Pushed | Description |
|------|----------|--------|-------------|
| nash-tui | Rust | 2026-04-13 | NASH token TUI: real-time candles, ticker |
| nash-web | Rust | 2026-04-13 | NASH token browser TUI via ratzilla WASM |
| gay-world | Python | 2026-03-26 | Goblin world builder, each goblin is a world |
| kinesis-kb360pro | Python | 2026-03-26 | Claude Code skill for Kinesis Advantage360 Pro |
| tilelang-kernels | Python | 2026-03-16 | TileLang GPU kernels for SplitMix64 + GF(3) |

### Social Graph (zubyul's network)

| User | Repos | Notable |
|------|-------|---------|
| migalkin | 8 sampled (19 total) | NodePiece 144★, StarE 89★ — knowledge graph ML researcher |
| wasita | 5 sampled (11 total) | Network science, personal site, Kobo tools |
| AustinCStone | 6 sampled (41 total) | TextGAN 92★, CV/ML researcher |
| DJedamski | 4 sampled (6 total) | Data science, Kaggle |
| kristinezheng | 4 sampled (5 total) | MIT neuroscience, HackMIT 2021 |
| M1shaaa | 4 sampled (8 total) | Yale CS, lab bookshelf tooling |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried via `https://fullnode.mainnet.aptoslabs.com/v1`.  
**Result:** All 28 addresses return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — accounts have no funded APT CoinStore.

| World | Address (prefix) | Balance |
|-------|-----------------|---------|
| alice | 0xc793acdec12b4a... | 0.0 APT |
| bob | 0x0a3c00c58fdf90... | 0.0 APT |
| A | 0x8699edc0960dd5... | 0.0 APT |
| B | 0x3f892ebe6e4516... | 0.0 APT |
| C | 0x38b99e63ada9b6... | 0.0 APT |
| D–Z (22 more) | ... | 0.0 APT each |

### Multisig Contract Probes (Mainnet)

POST to `0x1::multisig_account::num_signatures_required`.  
**All 5 healthy — 2-of-2 multisig.**

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428a0c007... | 2 | ✅ healthy |
| A-G | 0xf56c4a1c090621... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1812b2df4... | 2 | ✅ healthy |
| S-T | 0x3b1c3ae905d44c... | 2 | ✅ healthy |
| V-W | 0x40fad7b423a843... | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` is Vercel-protected (authentication required). Tried `/`, `/api/markets`, `/api/v1/markets` — all return authentication challenge. No market data available without Vercel bypass token or authentication credential.

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

## Star Growth Since 2026-04-12

| Repo | Apr 12 | Jul 15 | Delta |
|------|--------|--------|-------|
| kubeflow/kubeflow | 15,565 | 15,777 | +212 |
| kubeflow/pipelines | 4,119 | 4,166 | +47 |
| kubeflow/spark-operator | 3,111 | 3,136 | +25 |
| kubeflow/trainer | 2,080 | 2,148 | +68 |
| plurigrid/asi | 16 | 30 | +14 |
| bmorphism/Gay.jl | — | 2 | new |
| migalkin/NodePiece | 143 | 144 | +1 |
