# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-16  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.2 (Variegata) — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos | Total ★ | Top Repo |
|--------|------|------:|--------:|----------|
| kubeflow | org | 48 | 34,058 | kubeflow/kubeflow (15,634★) |
| migalkin | user | 19 | 279 | migalkin/NodePiece (144★) |
| bmorphism | user | 100 | 247 | bmorphism/risc0-cosmwasm-example (23★) |
| AustinCStone | user | 20 | 107 | AustinCStone/TextGAN (92★) |
| plurigrid | org | 100 | 74 | plurigrid/asi (23★) |
| zubyul | user | 49 | 14 | zubyul/jonikas_lab_data_analysis_misc (2★) |
| wasita | user | 11 | 4 | wasita/magic-garden (2★) |
| DJedamski | user | 6 | 3 | DJedamski/Kaggle (1★) |
| TeglonLabs | org | 4 | 2 | TeglonLabs/mathpix-gem (2★) |
| kristinezheng | user | 6 | 0 | — |
| M1shaaa | user | 8 | 0 | — |
| **TOTAL** | | **371** | **34,789** | |

### GF(3) Color Chain Distribution

| GF3 Name | Trit | Color | Count |
|----------|:----:|-------|------:|
| ERGODIC | 0 | `#d3869b` | 123 |
| PLUS | +1 | `#b8bb26` | 124 |
| MINUS | -1 | `#cc241d` | 124 |

Chain rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

### Most Recently Active Repos

| Repo | Source | Pushed | Stars |
|------|--------|--------|------:|
| plurigrid/gorj | plurigrid | 2026-05-16 | 0 |
| kubeflow/dashboard | kubeflow | 2026-05-16 | 17 |
| kubeflow/pipelines | kubeflow | 2026-05-15 | 4,139 |
| kubeflow/notebooks | kubeflow | 2026-05-15 | 72 |
| bmorphism/Gay.jl | bmorphism | 2026-05-16 | 1 |
| bmorphism/oxgame | bmorphism | 2026-05-15 | 0 |
| wasita/wasita.github.io | wasita | 2026-05-14 | 1 |
| kristinezheng/kristinezheng.github.io | kristinezheng | 2026-05-14 | 0 |

### Notable Repos by Source

**plurigrid** (100 repos): gorj (2026-05-16, this repo), asi (23★ topological chemputer), nash-portal (Rust WASM TUI), nanoclj-zig (Zig Clojure interpreter with GF(3) trits), vcg-auction (7★ CosmWasm)

**kubeflow** (48 repos): kubeflow/kubeflow (15,634★), pipelines (4,139★), spark-operator (3,125★), trainer (2,098★), katib (1,682★). Mature ML infra, active Python/Go development.

**bmorphism** (100 repos): ocaml-mcp-sdk (61★ Jane Street oxcaml_effect), anti-bullshit-mcp-server (23★), say-mcp-server (20★), manifold-mcp-server (14★). Heavy MCP server and categorical/functional programming focus. Gay.jl (188 open issues — heavy active dev).

**TeglonLabs** (4 repos): mathpix-gem (Ruby, LaTeX OCR), monad-mcp-server, topoi, coin-flip-mcp

**migalkin** (19 repos): NodePiece (144★, ICLR'22 KG embeddings), StarE (89★, EMNLP'20), kgcourse2021 (25★). Knowledge graph research.

**zubyul** (49 repos): voice-observatory, nash-web/nash-tui (Rust WASM candlestick TUI), Gay.jl fork, gay-world (goblin world builder), plurigrid-site

**AustinCStone** (20 shown / 40 total): TextGAN (92★, TF text generation), StereoVisionMRF (11★), bmfork/bmforkupdate (bmorphism tooling)

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet — fullnode.mainnet.aptoslabs.com)

All 28 addresses (alice, bob, A–Z) queried for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: 0.00 APT across all 28 addresses.**  
Accounts hold no registered APT CoinStore on mainnet (unregistered addresses or zero-balance reserves).

| Range | Count | Total APT |
|-------|------:|----------:|
| alice, bob | 2 | 0.00 |
| A–Z (26 addrs) | 26 | 0.00 |
| **Total** | **28** | **0.00** |

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | 0x0da4f428… | 2 | ✓ |
| A-G | 0xf56c4a1c… | 2 | ✓ |
| Y-Z | 0xd3ffe181… | 2 | ✓ |
| S-T | 0x3b1c3ae9… | 2 | ✓ |
| V-W | 0x40fad7b4… | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed on Aptos mainnet.**

### MNX Markets (testnet.mnx.fi)

Fetched `https://testnet.mnx.fi` — returns a Next.js SPA shell (~320 KB HTML). All market data is client-side JavaScript rendered. No REST API endpoint (`/api/markets`, `/api/v1/markets`) returned structured JSON. **MNX market data: UNAVAILABLE — SPA with no accessible REST API.**

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)               -- 371 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)               -- 371 rows

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct) -- 0 rows
```

## GF(3) Assignment Rule

- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**
