# World-Increment Sweep + Hamming Snapshot — 2026-06-04

## Sweep Metadata
- **Date:** 2026-06-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 390 |
| Total Repo Snapshots | 390 (unique) |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 130 |
| +1 | PLUS | `#b8bb26` | 130 |
| -1 | MINUS | `#cc241d` | 130 |

Chain pattern: `PLUS → MINUS → ERGODIC` repeating 130× across all 390 repo increments.

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **390** |

### Top Languages

| Language | Repos |
|----------|-------|
| Python | 82 |
| Rust | 26 |
| JavaScript | 25 |
| TypeScript | 23 |
| Go | 15 |
| HTML | 15 |
| Jupyter Notebook | 14 |
| Clojure | 14 |
| Julia | 9 |
| Jsonnet | 7 |

### Top Starred Repos

| Repo | Stars | Forks | Language | Last Push |
|------|-------|-------|----------|-----------|
| kubeflow/kubeflow | 15,706 | 2,670 | — | 2026-05-24 |
| kubeflow/pipelines | 4,152 | 2,005 | Python | 2026-06-04 |
| kubeflow/spark-operator | 3,124 | 1,488 | Python | 2026-06-04 |
| kubeflow/trainer | 2,111 | 964 | Go | 2026-06-04 |
| kubeflow/katib | 1,684 | 525 | Python | 2026-06-04 |
| kubeflow/examples | 1,462 | 756 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,020 | 1,065 | YAML | 2026-06-04 |
| AustinCStone/TextGAN | 92 | 30 | Python | 2016-10-04 |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | OCaml | 2026-03-16 |
| migalkin/NodePiece | 144 | 21 | Python | 2022-02-02 |
| migalkin/StarE | 89 | 16 | Python | 2023-12-01 |
| bmorphism/anti-bullshit-mcp-server | 23 | 7 | JavaScript | 2026-01-16 |
| migalkin/kgcourse2021 | 25 | 9 | HTML | 2025-08-04 |
| plurigrid/asi | 25 | 6 | HTML | 2026-04-26 |

### Most Recent Activity (sweep timestamp 2026-06-04)

| Repo | Pushed At |
|------|-----------|
| kubeflow/pipelines | 2026-06-04T20:47 |
| plurigrid/gorj | 2026-06-04T20:20 |
| kubeflow/spark-operator | 2026-06-04T17:55 |
| kubeflow/mcp-apache-spark-history-server | 2026-06-04T17:24 |
| M1shaaa/M1shaaa | 2026-06-04T14:51 |
| plurigrid/eirobri | 2026-06-03T20:43 |
| kubeflow/community | 2026-06-02T15:52 |
| wasita/wasita.github.io | 2026-06-01T04:15 |

### Notable Repos by Source

**plurigrid (100)** — Active GF(3)/Gay.jl coloring, `nanoclj-zig` (NaN-boxed Clojure in Zig), `nash-portal` (Rust WASM TUI + GeckoTerminal), `zig-syrup` (OCapN), `gorj` (this repo, 356 open issues). Most recent: `eirobri` replay world.

**bmorphism (100)** — `ocaml-mcp-sdk` (61★, Jane Street oxcaml_effect), `anti-bullshit-mcp-server` (23★), `Gay.jl` (Julia wide-gamut colors, 189 open issues), `nanoclj-zig`, `vibespace-mcp-go-ternary`, `oxgame` (OCaml open-game composition).

**zubyul (49)** — `nash-tui`/`nash-web` (Rust NASH TUI), `tilelang-kernels` (GPU GF(3) trit kernels), `chromatic-vrf` (Kotlin), `openbci-visualizer` (Zig), `Gay.jl` fork, `gay-terminal-colors` (Clojure).

**kubeflow (48)** — Flagship ML-on-Kubernetes: `pipelines` (4,152★), `spark-operator` (3,124★), `trainer` (2,111★), `katib` (1,684★). New: `mcp-apache-spark-history-server` (173★ Python MCP), `mcp-server` (10★), `sdk` (120★ universal Python).

**TeglonLabs (4)** — `mathpix-gem` (Ruby, 2★), `coin-flip-mcp` (JS, random.org), `monad-mcp-server`, `topoi` (Python).

**migalkin (19)** — KG research: `NodePiece` (144★), `StarE` (89★ hyper-relational KGs), `NBFNet_mlx` (10★ Apple Silicon), `kgcourse2021` (25★).

**wasita (11)** — Personal site (Svelte, pushed 2026-06-01), `magic-garden` bot (2★), `send2kobo`, `wins-search`, `wm-cv`.

**AustinCStone (40)** — `TextGAN` (92★ TF GAN text gen), `StereoVisionMRF` (11★), `StructureFromMotion`, `TFBirds`, recent ML/crypto activity.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

- **Endpoint:** `fullnode.mainnet.aptoslabs.com/v1`
- **Ledger Version at probe:** ~5,571,426,552
- **Result:** All 28 Hamming swarm addresses (alice, bob, A–Z) returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. Wallets exist at the protocol level (addresses are valid) but have unregistered coin stores — no APT coin transactions have ever occurred on these addresses.

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0 APT (unregistered) |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0 APT (unregistered) |
| A | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a | 0 APT (unregistered) |
| B–Z | (see DB) | 0 APT each (unregistered) |

### Multisig Contract Probes

All 5 contracts respond correctly with `num_signatures_required = 2`. All healthy.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✅ healthy |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✅ healthy |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✅ healthy |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✅ healthy |

### MNX Markets

`testnet.mnx.fi` is reachable (TLS cert CN=*.mnx.fi, issued 2026-06-04). The site runs a Next.js SPA — no REST `/api/markets` endpoint is exposed. Market data unavailable via API probe. `mnx_snapshots` table is empty.

---

## DuckDB Schema

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

### Row Counts (2026-06-04 sweep)

```
world_increments    390
repo_snapshots      390
aptos_snapshots      28
multisig_probes       5
mnx_snapshots         0
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights (2026-06-04)
- **kubeflow/kubeflow**: 15,706★ — up 141 since 2026-04-12 sweep
- **kubeflow/pipelines**: 4,152★ — active daily pushes
- **plurigrid/gorj**: 356 open issues — active GF(3) + Rama routing development
- **bmorphism/Gay.jl**: 189 open issues — wide-gamut color + SPI active
- **All 5 Hamming multisigs**: 2-of-N, healthy
- **28 Hamming wallets**: All unregistered on Aptos mainnet (0 APT)
- **MNX testnet**: SPA live, no REST API

*Generated by world-increment-sweep + hamming-swarm-snapshot agent, 2026-06-04*
