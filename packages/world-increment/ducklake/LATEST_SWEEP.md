# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-10
**Agent:** world-increment-sweep + hamming-swarm-snapshot
**DuckDB version:** v1.5.3 (Variegata)
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 307 |
| Total Repo Snapshots (rows) | 1,228 |
| Unique Repos | 562 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | UNAVAILABLE (Vercel auth) |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Queried |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 (of 103 total) |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| AustinCStone | user (social) | 30 |
| wasita | user (social) | 11 |
| DJedamski | user (social) | 6 |
| M1shaaa | user (social) | 8 |
| kristinezheng | user (social) | 5 |

### GF(3) Color Chain

| Color | Hex | Trit | Assignment | Count |
|-------|-----|------|-----------|-------|
| ERGODIC | #d3869b | 0 | id%3==0 | 101 |
| PLUS | #b8bb26 | +1 | id%3==1 | 103 |
| MINUS | #cc241d | -1 | id%3==2 | 103 |

### Top Repos by Stars

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,715 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,153 | 2026-06-10 |
| kubeflow/spark-operator | Python | 3,126 | 2026-06-09 |
| kubeflow/trainer | Go | 2,112 | 2026-06-10 |
| kubeflow/katib | Python | 1,685 | 2026-06-05 |
| kubeflow/examples | Jsonnet | 1,462 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,022 | 2026-06-09 |
| kubeflow/arena | Go | 812 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-02-05 |
| plurigrid/asi | HTML | 25 | 2026-06-10 |
| plurigrid/ontology | JavaScript | 8 | 2025-05-27 |
| plurigrid/vcg-auction | Rust | 7 | 2023-03-16 |

### Most Active (by open issues, 2026-06-10)

| Repo | Open Issues |
|------|-------------|
| kubeflow/pipelines | 495 |
| plurigrid/gorj | 485 |
| kubeflow/notebooks | 169 |
| bmorphism/Gay.jl | 189 |
| kubeflow/docs-agent | 151 |
| kubeflow/sdk | 132 |
| kubeflow/fairing | 134 |

### Plurigrid Social Graph Notable Activity (2026)

**plurigrid org** — Active Clojure/Zig/Rust/Julia/Scheme projects:
- `gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring (485 issues, pushed 2026-06-10)
- `asi` — topological chemputer (25 stars, pushed 2026-06-10)
- `zig-syrup` — OCapN Syrup in Zig
- `nanoclj-zig` — NaN-boxed Clojure interpreter in Zig 0.15

**bmorphism** — OCaml/Julia/Zig/Clojure focus:
- `ocaml-mcp-sdk` — 61 stars, OCaml SDK for MCP using Jane Street's oxcaml_effect
- `Gay.jl` — wide-gamut color sampling with splittable determinism (189 open issues)
- `anti-bullshit-mcp-server` — 23 stars, claim validation MCP

**zubyul** — recently active:
- `voice-observatory` — passive macOS TUI for voice-download pathways
- `nash-tui` + `nash-web` — NASH token TUI (GeckoTerminal OHLCV)
- `tilelang-kernels` — GPU kernels for SplitMix64/GF(3) on Blackwell

**TeglonLabs** — 5 repos:
- `jank-crane` — crane-jank converged-IR hub with GF3 convergence maps (C++, pushed 2026-06-08)
- `mathpix-gem` — mathematical image → LaTeX Ruby gem (2 stars)

**migalkin** — KG research:
- `NodePiece` — 144 stars, compositional KG representations (ICLR'22)
- `StarE` — 89 stars, hyper-relational KG message passing (EMNLP 2020)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (ledger version 5,671,719,472)

All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
CoinStore is not initialized — accounts may use FA (Fungible Asset) standard or are unfunded.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (Aptos Mainnet)

All 5 contracts are live and returning valid responses via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | **2** | ✅ HEALTHY |
| A-G | 0xf56c...096 | **2** | ✅ HEALTHY |
| Y-Z | 0xd3ff...883 | **2** | ✅ HEALTHY |
| S-T | 0x3b1c...883 | **2** | ✅ HEALTHY |
| V-W | 0x40fa...b6d | **2** | ✅ HEALTHY |

All pairs require **2-of-N** signatures. No unhealthy contracts detected.

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — `testnet.mnx.fi` is behind Vercel deployment protection.
Requires bypass token or Vercel CLI authentication. No market data recorded.

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
