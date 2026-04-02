# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-02T00:00:00Z  
**GF(3) color chain:**  id%3==0 → trit=0 ERGODIC `#d3869b` | id%3==1 → trit=1 PLUS `#b8bb26` | id%3==2 → trit=-1 MINUS `#cc241d`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Fetched | Status |
|--------|------|--------------|--------|
| plurigrid | org | 100 | OK |
| kubeflow | org | — | Not found / private |
| TeglonLabs | org | — | Not found / private |
| bmorphism | user | 100 | OK |
| zubyul | user | 23 | OK |
| migalkin | user | 30 | OK |
| DJedamski | user | 11 | OK |
| wasita | user | 29 | OK |
| kristinezheng | user | 18 | OK |
| M1shaaa | user | — | Not found |
| AustinCStone | user | — | Not found |

**Total new repo_snapshots this sweep:** 311  
**Total world_increments (all-time):** 322  
**Total repo_snapshots (all-time):** 780

### Top Repos by Stars (this sweep)

| Repo | Owner | Stars | Language | Last Pushed |
|------|-------|-------|----------|-------------|
| NodePiece | migalkin | 143 | Python | 2022-02-02 |
| StarE | migalkin | 88 | Python | 2023-12-01 |
| ocaml-mcp-sdk | bmorphism | 60 | OCaml | 2026-03-16 |
| kgcourse2021 | migalkin | 25 | HTML | 2025-08-04 |
| anti-bullshit-mcp-server | bmorphism | 23 | JavaScript | 2026-01-16 |
| asi | plurigrid | 14 | HTML | 2026-03-30 |
| NBFNet_mlx | migalkin | 10 | Python | 2024-03-02 |
| ontology | plurigrid | 7 | JavaScript | 2025-05-27 |
| RWL | migalkin | 7 | Python | 2022-12-01 |
| shitcoin | bmorphism | 5 | HTML | 2026-03-09 |

### Language Breakdown (new repos)

| Language | Count |
|----------|-------|
| Python | 34 |
| HTML | 12 |
| Rust | 11 |
| Jupyter Notebook | 10 |
| JavaScript | 9 |
| R | 8 |
| Clojure | 7 |
| TypeScript | 6 |
| Julia | 5 |
| Scheme | 4 |
| Go | 4 |
| Svelte | 4 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) probed at `fullnode.mainnet.aptoslabs.com`.

> **Result:** All addresses returned no `0x1::coin::CoinStore` resource — accounts are either uninitialized (never received APT) or do not exist on mainnet. Balance recorded as NULL.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793acdec12b4a63... | NULL (no resource) |
| bob | 0x0a3c00c58fdf9020... | NULL (no resource) |
| A | 0x8699edc0960dd5b9... | NULL (no resource) |
| B | 0x3f892ebe6e45164e... | NULL (no resource) |
| C | 0x38b99e63ada9b6fe... | NULL (no resource) |
| D | 0xf77656248f64d5dd... | NULL (no resource) |
| E | 0xdc1d9d533bac3507... | NULL (no resource) |
| F | 0x18a14b5b4bec118c... | NULL (no resource) |
| G | 0x69a394c0b0ac8421... | NULL (no resource) |
| H | 0xce67c327a7844e54... | NULL (no resource) |
| I | 0x070fe5d74e4eda30... | NULL (no resource) |
| J | 0x4d964db8f5383740... | NULL (no resource) |
| K | 0xa732040a6b0d5590... | NULL (no resource) |
| L | 0x7c2eaeafad972549... | NULL (no resource) |
| M | 0x6fed37a7553ef16b... | NULL (no resource) |
| N | 0xe7dde6da0a65f510... | NULL (no resource) |
| O | 0x73252b6011a75115... | NULL (no resource) |
| P | 0x6218792de4a9bc38... | NULL (no resource) |
| Q | 0xac40fa50b81b4ca6... | NULL (no resource) |
| R | 0x7ce605cc8fda4f8e... | NULL (no resource) |
| S | 0xb8753014e4888ea4... | NULL (no resource) |
| T | 0x35781dc0e42fef3f... | NULL (no resource) |
| U | 0x75860da47565f650... | NULL (no resource) |
| V | 0xb59dd8170321dfab... | NULL (no resource) |
| W | 0x5f32aef70f5ba530... | NULL (no resource) |
| X | 0xa95cbbd116548ac9... | NULL (no resource) |
| Y | 0xd8e32848f1dffa81... | NULL (no resource) |
| Z | 0x7af0ef6e1bd706f4... | NULL (no resource) |

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | YES |
| A-G | 0xf56c4a1c0906214f... | 2 | YES |
| Y-Z | 0xd3ffe1812b2df406... | 2 | YES |
| S-T | 0x3b1c3ae905d44c3a... | 2 | YES |
| V-W | 0x40fad7b423a84365... | 2 | YES |

All 5/5 multisig contracts healthy, each requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA. Root HTML loads but no public JSON API endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) returned data. Market data unavailable without browser JS execution. Recorded as `MNX_UNAVAILABLE`.

---

## DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 322 |
| repo_snapshots | 780 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

Database: `packages/world-increment/ducklake/world-increments.duckdb`
