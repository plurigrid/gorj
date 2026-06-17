# World-Increment Sweep + Hamming Snapshot — 2026-06-17

## Sweep Metadata
- **Date:** 2026-06-17T20:30 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts (cumulative DB state after this run)

| Metric | Value |
|--------|-------|
| Total World Increments | 34 |
| Total Repo Snapshots | 1088 |
| Aptos Snapshots | 28 |
| Multisig Probes | 5 |
| Sources Covered | 3 orgs + 8 users |

### Sources Swept This Run

| Source | Type | Repos Found | Total Stars | GF(3) Trit | Color | Name |
|--------|------|-------------|-------------|------------|-------|------|
| plurigrid | org | 101 | 152 | +1 | `#b8bb26` | **PLUS** |
| kubeflow | org | 48 | 101,519 | -1 | `#cc241d` | **MINUS** |
| TeglonLabs | org | 5 | 2 | 0 | `#d3869b` | **ERGODIC** |
| bmorphism | user | 104 | 470 | +1 | `#b8bb26` | **PLUS** |
| zubyul | user | 49 | 36 | -1 | `#cc241d` | **MINUS** |
| migalkin | user | social-graph | — | 0 | `#d3869b` | **ERGODIC** |
| DJedamski | user | social-graph | — | +1 | `#b8bb26` | **PLUS** |
| wasita | user | social-graph | — | -1 | `#cc241d` | **MINUS** |
| kristinezheng | user | social-graph | — | 0 | `#d3869b` | **ERGODIC** |
| M1shaaa | user | social-graph | — | +1 | `#b8bb26` | **PLUS** |
| AustinCStone | user | social-graph | — | -1 | `#cc241d` | **MINUS** |

### Most Active Repos (by push date, 2026)

**plurigrid (101 total):**
| Repo | Language | Stars | Open Issues | Pushed |
|------|----------|-------|-------------|--------|
| gorj | Clojure | 0 | **641** | 2026-06-17 |
| place | TeX | 1 | 8 | 2026-06-15 |
| asi | HTML | **26** | 4 | 2026-06-10 |
| eirobri | Clojure | 0 | 29 | 2026-06-03 |
| nash-portal | Rust | 2 | 1 | 2026-05-19 |
| nanoclj-zig | Zig | 1 | 20 | 2026-04-25 |
| asi-skills | Julia | 3 | 0 | 2026-04-26 |
| zig-syrup | Zig | 2 | 0 | 2026-04-30 |
| ontology | JavaScript | 8 | 16 | 2025-05-27 |

**kubeflow (48 total, most pushed 2026-06-17):**
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| kubeflow | — | **15,729** | 2026-06-17 |
| pipelines | Python | 4,154 | 2026-06-17 |
| spark-operator | Python | 3,127 | 2026-06-17 |
| trainer | Go | 2,115 | 2026-06-17 |
| community-distribution | YAML | 1,025 | 2026-06-17 |
| katib | Python | 1,683 | 2026-06-15 |
| hub | Go | 173 | 2026-06-17 |

**TeglonLabs (5 total):**
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

**bmorphism (104 total):**
| Repo | Language | Stars | Open Issues | Pushed |
|------|----------|-------|-------------|--------|
| Gay.jl | Julia | 1 | **187** | 2026-06-17 |
| satreadout | Lean | 0 | 0 | 2026-06-15 |
| ocaml-mcp-sdk | OCaml | **61** | 0 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 1 | 2026-01-16 |
| risc0-cosmwasm-example | Rust | 23 | 1 | 2022-10-20 |
| world | Python | 0 | 0 | 2026-06-02 |
| oxgame | OCaml | 0 | 0 | 2026-05-15 |

**zubyul (49 total):**
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |
| voice-observatory | Python | 0 | 2026-04-24 |
| nash-tui | Rust | 0 | 2026-04-13 |
| nash-web | Rust | 0 | 2026-04-13 |
| gay-world | Python | 1 | 2026-03-26 |
| kinesis-kb360pro | Python | 0 | 2026-03-26 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (2026-06-17)
Queried `fullnode.mainnet.aptoslabs.com/v1` with 1s delay between calls.

**All 28 wallets (alice, bob, A–Z) returned 0.00000000 APT.**  
CoinStore resource `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` not found  
for any address — wallets exist but are unfunded / APT resource not initialized.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793acdec12b4a63… | 0.00000000 |
| bob   | 0x0a3c00c58fdf9020… | 0.00000000 |
| A–Z   | 26 addresses | 0.00000000 each |

### Multisig Contract Probes

All 5 multisig accounts **healthy** — require exactly **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428a0c007da… | 2 | ✓ |
| A-G | 0xf56c4a1c09062143… | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df406… | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a… | 2 | ✓ |
| V-W | 0x40fad7b423a84365… | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Vercel deployment protection active on all API paths  
(`/api/markets`, `/api/v1/markets`, `/api/tickers`). No bypass token available.  
`mnx_snapshots` table: 0 rows.

---

## GF(3) Color Chain Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

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

## Notable Highlights (2026-06-17 sweep)
- **kubeflow/kubeflow**: 15,729 stars (+164 since April) — most active kubeflow org repo
- **plurigrid/gorj**: 641 open issues — most active issue tracker in sweep, pushed today
- **bmorphism/Gay.jl**: 187 open issues, pushed today — wide-gamut GF(3) color system
- **plurigrid/asi**: 26 stars — topological chemputer, pushed 2026-06-10
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK with Jane Street oxcaml_effect
- **TeglonLabs/jank-crane**: pushed 2026-06-08 — crane-jank IR hub with GF(3) convergence maps
- **Multisig**: All 5 Hamming-swarm pairs require exactly 2/N sigs — swarm is balanced
- **Aptos wallets**: All 28 unfunded — swarm accounts not yet initialized on mainnet
