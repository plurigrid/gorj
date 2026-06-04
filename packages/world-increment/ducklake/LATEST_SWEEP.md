# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-04  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.3 (Variegata)  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 30 |
| kubeflow | org | 20 |
| TeglonLabs | org | 4 |
| bmorphism | user | 14 |
| zubyul | user | 11 |
| migalkin | social graph | 5 |
| DJedamski | social graph | 6 |
| wasita | social graph | 5 |
| kristinezheng | social graph | 2 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 4 |
| **TOTAL** | | **109** |

### GF(3) Color Chain Distribution

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | #d3869b | 37 |
| PLUS | +1 | #b8bb26 | 37 |
| MINUS | -1 | #cc241d | 35 |

Chain sequence: `MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → ...` (109 steps)

### Top Repos by Stars

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15705 | — | 2026-05-24 |
| kubeflow/pipelines | 4152 | Python | 2026-06-04 |
| kubeflow/spark-operator | 3124 | Python | 2026-06-03 |
| kubeflow/trainer | 2111 | Go | 2026-06-04 |
| kubeflow/katib | 1685 | Python | 2026-06-04 |
| kubeflow/examples | 1462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1020 | YAML | 2026-06-04 |
| kubeflow/arena | 811 | Go | 2026-05-07 |
| kubeflow/kale | 690 | Python | 2026-06-04 |
| kubeflow/fairing | 337 | Jsonnet | 2022-04-11 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| plurigrid/asi | 25 | HTML | 2026-04-26 |
| migalkin/kgcourse2021 | 25 | HTML | 2026-02-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-02-05 |

### Most Active Repos (Recent Push)

| Repo | Pushed At |
|------|-----------|
| plurigrid/place | 2026-06-04 |
| plurigrid/gorj | 2026-06-04 |
| kubeflow/pipelines | 2026-06-04 |
| kubeflow/hub | 2026-06-04 |
| kubeflow/manifests | 2026-06-04 |
| kubeflow/trainer | 2026-06-04 |
| kubeflow/sdk | 2026-06-04 |
| kubeflow/katib | 2026-06-04 |
| kubeflow/dashboard | 2026-06-04 |
| wasita/wasita.github.io | 2026-06-01 |
| bmorphism/world | 2026-06-02 |

### Notable Observations

- **plurigrid** is deeply active in GF(3)/Gay.jl color theory (gay-rs, gay-go, gay-terminal, gatomic, lazygay), Zig implementation work (zig-syrup, nanoclj-zig, tree-sitter-nanoclj-zig), and Spritely/Goblins ecosystem mirrors. `gorj` (this repo) has 351 open issues.
- **bmorphism** spans OCaml MCP SDK (61★), Wide-gamut Gay.jl color, Zig geocoding (open-location-code-zig 3★), and compositional game theory (monero-rental-hash-war). 189 open issues on Gay.jl.
- **kubeflow** is massively active with pipelines (4152★), spark-operator (3124★), trainer (2111★) all pushed today. kubeflow/kubeflow itself has 15705★.
- **zubyul** social graph is tightly coupled to bmorphism — voice-observatory companion, Gay.jl fork, tilelang GPU kernels for GF(3) color generation.
- **migalkin** focuses on Knowledge Graph ML: NodePiece (144★), StarE (89★), NBFNet_mlx.
- **wasita** (network science researcher) active Svelte personal site + vocoder.
- **TeglonLabs** has 4 public repos: mathpix-gem (Ruby, 2★), coin-flip-mcp (JS), monad-mcp-server, topoi.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version 5568026253. These accounts have not initialized an APT coin store on mainnet. Balances recorded as NULL.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | NULL |
| bob | 0x0a3c...2d5d | NULL |
| A | 0x8699...9d7a | NULL |
| B | 0x3f89...b13 | NULL |
| C | 0x38b9...35e | NULL |
| D | 0xf776...dd1 | NULL |
| E | 0xdc1d...d36 | NULL |
| F | 0x18a1...f71 | NULL |
| G | 0x69a3...f32 | NULL |
| H | 0xce67...00f | NULL |
| I–Z | 0x070f...97c | NULL (all 18) |

### Multisig Contract Probes

All 5 multisig accounts probed via `POST /v1/view` with `0x1::multisig_account::num_signatures_required`. All healthy — all require 2-of-2 signatures.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**Swarm health: 5/5 multisigs live, all 2-of-2.**

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` is a Next.js SPA — no REST API endpoints accessible at `/api/markets` or `/api/v1/markets`. Market data is client-side rendered; no data extractable without a browser runtime. `mnx_snapshots` table is empty (unavailable).

---

## Database Summary

| Table | Rows | Notes |
|-------|------|-------|
| world_increments | 109 | one per repo, GF(3) colored |
| repo_snapshots | 109 | full metadata per repo |
| aptos_snapshots | 28 | all NULL (no APT coin store) |
| multisig_probes | 5 | all healthy, 2-of-2 |
| mnx_snapshots | 0 | SPA-only, unavailable |

## GF(3) Assignment Rule

- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**

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

**GF(3) sweep complete. 5/5 multisigs healthy (all 2-of-2). APT coin stores not initialized on mainnet. MNX SPA-only, no market data extractable.**
