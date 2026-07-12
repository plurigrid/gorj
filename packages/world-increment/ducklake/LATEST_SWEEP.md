# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-12

## Sweep Metadata
- **Date:** 2026-07-12
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| World Increments (this sweep) | 125 |
| World Increments (cumulative) | 148 |
| Repo Snapshots (cumulative) | 1069 |
| Sources Covered | 3 orgs + 5 users + 6-node social graph |
| Aptos swarm addresses probed | 28 (alice, bob, A–Z) |
| Multisig contracts probed | 5 |
| MNX markets | unavailable (Vercel auth gate) |

---

## JOB 1 — GitHub Social Graph

### Orgs

#### plurigrid (50 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 30 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-12 |
| place | TeX | 1 | 2026-07-07 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| nash-portal | Rust | 2 | 2026-05-19 |

`plurigrid/gorj` has **1133 open issues** — highest activity in the org. `plurigrid/asi` ("everything is topological chemputer!") most recently active.

#### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,771 | 2026-07-10 |
| pipelines | Python | 4,169 | 2026-07-12 |
| spark-operator | Python | 3,137 | 2026-07-12 |
| trainer | Go | 2,136 | 2026-07-10 |
| katib | Python | 1,690 | 2026-07-10 |
| mcp-server | Python | 20 | 2026-07-12 |

`kubeflow/mcp-server` (20★) launched since last sweep — AI-assisted development with Kubeflow tools.

#### TeglonLabs (5 repos)
| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| jank-crane | C++ | 0 | crane-jank converged-IR hub: GF3 convergence maps |
| mathpix-gem | Ruby | 2 | Math image → LaTeX OCR gem |
| coin-flip-mcp | JS | 0 | random.org coin flip MCP server (2 forks) |

### Users

#### bmorphism (top repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JS | 23 |
| hypernym-mcp-server | JS | 6 |
| shitcoin | Python | 5 |
| Gay.jl | Julia | 2 (187 open issues!) |
| satreadout | HTML | 0 (new: Lean 4.28 saturating perceptual readout) |

#### zubyul (top repos)
| Repo | Language | Stars |
|------|----------|-------|
| voice-observatory | Python | 0 |
| gay-world | Python | 1 |
| big-bad-plurigrid-quiz | Emacs Lisp | 0 |
| tilelang-kernels | Python | 0 |

### Social Graph (zubyul connections)

| User | Repo | Stars |
|------|------|-------|
| migalkin | NodePiece | 144 (ICLR'22 KG reps) |
| migalkin | StarE | 89 (EMNLP 2020) |
| migalkin | kgcourse2021 | 24 |
| wasita | wasita.github.io | 1 (Svelte, 8 open issues) |
| wasita | magic-garden | 2 (discord bot) |
| AustinCStone | TextGAN | 92 (text GAN, TensorFlow) |
| kristinezheng | kristinezheng.github.io | 0 |
| M1shaaa | lab-bookshelf- | 0 (TypeScript) |

### GF(3) Color Chain (this sweep, first 9 increments as sample)

| ID | Repo | Source | GF3 Trit | Color | Name |
|----|------|--------|----------|-------|------|
| 1 | asi | plurigrid | +1 | `#b8bb26` | PLUS |
| 2 | gorj | plurigrid | −1 | `#cc241d` | MINUS |
| 3 | shrimp | plurigrid | 0 | `#d3869b` | ERGODIC |
| 4 | place | plurigrid | +1 | `#b8bb26` | PLUS |
| 5 | eirobri | plurigrid | −1 | `#cc241d` | MINUS |
| 6 | nash-portal | plurigrid | 0 | `#d3869b` | ERGODIC |
| … | … | … | … | … | … |
| 125 | lastfm_analysis | zubyul-graph | ? | GF3(125%3) | ERGODIC |

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z = 28 addresses)

**All 28 addresses: `resource_not_found` on Aptos mainnet**

The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource does not exist for any Hamming swarm address. These wallets have not been activated with APT coins. All recorded as 0.0 APT in `aptos_snapshots`.

Sample addresses checked:
- alice `0xc793acd…`: 0.0 APT (not funded)
- bob `0x0a3c00c…`: 0.0 APT (not funded)
- A `0x8699edc…` through Z `0x7af0ef6…`: 0.0 APT each (not funded)

### Multisig Contract Probes — ALL HEALTHY

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4f428a0c007da… | **2** | ✓ healthy |
| A-G | 0xf56c4a1c09062143… | **2** | ✓ healthy |
| Y-Z | 0xd3ffe1812b2df406… | **2** | ✓ healthy |
| S-T | 0x3b1c3ae905d44c3a… | **2** | ✓ healthy |
| V-W | 0x40fad7b423a84365… | **2** | ✓ healthy |

All 5 multisig accounts exist on-chain and require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Vercel authentication gate (HTTP 403). No market data accessible. `mnx_snapshots` table remains empty.

---

## DuckDB State (cumulative)

```
db: packages/world-increment/ducklake/world-increments.duckdb
  world_increments:  148 rows  (+125 this sweep)
  repo_snapshots:   1069 rows  (+125 this sweep)
  aptos_snapshots:    28 rows  (+28 this sweep)
  multisig_probes:     5 rows  (+5 this sweep)
  mnx_snapshots:       0 rows  (unavailable)
```

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
