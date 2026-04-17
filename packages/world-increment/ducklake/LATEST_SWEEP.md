# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-17

## Sweep Metadata
- **Date:** 2026-04-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 11 |
| zubyul | user | 6 |
| migalkin | user | 5 |
| wasita | user | 3 |
| AustinCStone | user | 3 |
| DJedamski | user | 2 |
| kristinezheng | user | 2 |
| M1shaaa | user | 2 |
| **Total** | | **185** |

### Top Repos by Stars

| repo | ★ | forks | language |
|------|---|-------|----------|
| kubeflow/kubeflow | 15,579 | 2,640 | — |
| kubeflow/pipelines | 4,121 | 1,985 | Python |
| kubeflow/spark-operator | 3,117 | 1,481 | Python |
| kubeflow/trainer | 2,085 | 945 | Go |
| kubeflow/katib | 1,679 | 521 | Python |
| kubeflow/examples | 1,460 | 756 | Jsonnet |
| kubeflow/manifests | 1,010 | 1,067 | YAML |
| AustinCStone/TextGAN | 92 | 30 | Python |
| bmorphism/ocaml-mcp-sdk | 60 | 2 | OCaml |
| migalkin/NodePiece | 143 | 21 | Python |

### Recent Activity Highlights (plurigrid, pushed last 7 days)

- `plurigrid/gorj` — pushed 2026-04-17 (Clojure, forj+Rama+GF3, 212 open issues)
- `plurigrid/reafference` — pushed 2026-04-16 (HTML, reafference adaptation)
- `plurigrid/horse` — pushed 2026-04-16 (TeX, ★1)
- `plurigrid/nash-portal` — pushed 2026-04-15 (Rust, NASH token TUI WASM)
- `plurigrid/asi` — pushed 2026-04-13 (HTML, topological chemputer, ★17)
- `plurigrid/nanoclj-zig` — pushed 2026-04-09 (Zig, NaN-boxed Clojure + interaction nets)
- `plurigrid/zig-syrup` — pushed 2026-04-09 (Zig, OCapN Syrup+CapTP, ★2)

### Zubyul Social Graph Highlights

- `zubyul/big-bad-plurigrid-quiz` — pushed 2026-04-09 (Emacs Lisp, 27 flashcards)
- `zubyul/gay-world` — pushed 2026-04-05 (Python, goblin world builder, ★1)
- `zubyul/Gay.jl` — pushed 2026-03-28 (Julia, GF3 wide-gamut color SPI)
- `migalkin/StarE` — pushed 2026-04-16 (Python, EMNLP2020, ★89)
- `wasita/wasita.github.io` — pushed 2026-04-13 (Svelte)
- `kristinezheng/kristinezheng.github.io` — pushed 2026-04-09 (HTML)

### GF(3) Color Chain Distribution (185 world_increments)

| trit | color | name | count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 61 |
| 1 | `#b8bb26` | PLUS | 62 |
| 2 | `#cc241d` | MINUS | 62 |

Assignment rule: `id%3==0` → ERGODIC · `id%3==1` → PLUS · `id%3==2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

Queried via `https://fullnode.mainnet.aptoslabs.com`. All 28 wallets returned 0.00 APT — accounts either uninitialized or CoinStore empty on mainnet at snapshot time (2026-04-17).

| world | address (prefix) | APT |
|-------|-----------------|-----|
| alice | 0xc793acdec12b4a... | 0.00 |
| bob | 0x0a3c00c58fdf90... | 0.00 |
| A | 0x8699edc0960dd5... | 0.00 |
| B–Z (24 more) | ... | 0.00 each |

### Multisig Contract Probes (Aptos mainnet `0x1::multisig_account`)

All 5 probed multisig accounts are **healthy** — each requires 2 signatures.

| pair | address (prefix) | sigs_required | healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428a0c007... | 2 | ✓ |
| A-G | 0xf56c4a1c090621... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c... | 2 | ✓ |
| V-W | 0x40fad7b423a843... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Unavailable.** `testnet.mnx.fi` is a Next.js SPA — `/api/markets` and `/api/v1/markets` both return HTML. No structured market data accessible without browser JS execution. Logged as `unavailable` in `mnx_snapshots`.

---

## DuckDB Tables

| table | rows | description |
|-------|------|-------------|
| world_increments | 185 | GF3-colored increment per repo snapshot |
| repo_snapshots | 185 | Full repo metadata (name, lang, stars, forks, issues, pushed_at) |
| aptos_snapshots | 28 | Hamming swarm wallet balances (A–Z + alice/bob) |
| multisig_probes | 5 | Multisig contract sigs_required + healthy flag |
| mnx_snapshots | 1 | MNX markets (unavailable) |

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
