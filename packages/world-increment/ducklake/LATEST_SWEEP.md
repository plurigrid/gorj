# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-18

## Sweep Metadata
- **Date:** 2026-07-18 (this run) / prior run: 2026-04-12
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** 1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep (2026-07-18)

### Sources Queried

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 106 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 12 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 41 |
| **Total** | | **400** |

### Hot Repos (Pushed ≤ 48h as of 2026-07-18)

- **plurigrid/gorj** — Clojure, 1228 open issues, pushed 2026-07-18. *forj + Rama topology nREPL routing + GF(3) gay trit coloring*
- **kubeflow/trainer** — Go ★2151, pushed 2026-07-18. *Distributed AI Model Training and LLM Fine-Tuning on Kubernetes*
- **kubeflow/hub** — Go ★177, pushed 2026-07-17.
- **kubeflow/sdk** — Python ★125, pushed 2026-07-17.
- **kubeflow/pipelines** — Python ★4168, pushed 2026-07-17.
- **plurigrid/asi** — HTML ★31, pushed 2026-07-10.
- **bmorphism/gay-chat** — Scheme, pushed 2026-07-14. *gay://chat over Spritely Brassica Chat*
- **bmorphism/Gay.jl** — Julia ★2, 187 open issues, pushed 2026-07-14. *Wide-gamut color sampling + splittable determinism*
- **bmorphism/anti-bullshit-mcp-server** — JS ★22, pushed 2026-07-12.
- **wasita/wasita.github.io** — Svelte ★1, pushed 2026-07-16.
- **AustinCStone/byteruckus** — HTML, pushed 2026-07-15 (new repo).

### Top Repos by Stars

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| kubeflow/kubeflow | 15,779 | — | ML Toolkit for Kubernetes |
| kubeflow/pipelines | 4,168 | Python | ML Pipelines |
| kubeflow/spark-operator | 3,138 | Python | Kubernetes Spark operator |
| kubeflow/trainer | 2,151 | Go | Distributed AI Training |
| kubeflow/community-distribution | 1,029 | YAML | KF Community Distribution |
| kubeflow/katib | 1,690 | Python | AutoML on Kubernetes |
| AustinCStone/TextGAN | 92 | Python | Text generation GANs |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | OCaml MCP SDK |
| migalkin/NodePiece | 144 | Python | KG embeddings (ICLR'22) |
| migalkin/StarE | 89 | Python | Hyper-relational KGs (EMNLP'20) |
| bmorphism/anti-bullshit-mcp-server | 22 | JS | Claim analysis MCP |
| bmorphism/say-mcp-server | 20 | JS | macOS TTS MCP |
| bmorphism/babashka-mcp-server | 19 | JS | Babashka MCP |
| bmorphism/manifold-mcp-server | 14 | JS | Manifold Markets MCP |
| plurigrid/asi | 31 | HTML | topological chemputer |

### GF(3) Color Chain (this run, 63 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 21 |
| 1 | #b8bb26 | PLUS | 21 |
| -1 | #cc241d | MINUS | 21 |

### Cumulative DB State (world-increments.duckdb)

| Table | Rows |
|-------|------|
| world_increments | 82 |
| repo_snapshots | 1003 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## JOB 2: Hamming Swarm Snapshot (2026-07-18)

### Aptos Mainnet Wallet Balances

Queried `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on mainnet for all 28 addresses.

| World | Address (prefix…suffix) | APT Balance |
|-------|------------------------|-------------|
| alice | 0xc793…cc7b | 0.00000000 |
| bob | 0x0a3c…12d5 | 0.00000000 |
| A | 0x8699…e9d7 | 0.00000000 |
| B | 0x3f89…b13 | 0.00000000 |
| C | 0x38b9…535e | 0.00000000 |
| D | 0xf776…fdd1 | 0.00000000 |
| E | 0xdc1d…8d36 | 0.00000000 |
| F | 0x18a1…cf71 | 0.00000000 |
| G | 0x69a3…7f32 | 0.00000000 |
| H | 0xce67…300f | 0.00000000 |
| I | 0x070f…1fc9 | 0.00000000 |
| J | 0x4d96…7f54 | 0.00000000 |
| K | 0xa732…5dc4 | 0.00000000 |
| L | 0x7c2e…eba9 | 0.00000000 |
| M | 0x6fed…f2e9 | 0.00000000 |
| N | 0xe7dd…1b2c | 0.00000000 |
| O | 0x7325…a89d | 0.00000000 |
| P | 0x6218…c948 | 0.00000000 |
| Q | 0xac40…89a9 | 0.00000000 |
| R | 0x7ce6…6e10 | 0.00000000 |
| S | 0xb875…0386 | 0.00000000 |
| T | 0x3578…4588 | 0.00000000 |
| U | 0x7586…9956 | 0.00000000 |
| V | 0xb59d…f2c3 | 0.00000000 |
| W | 0x5f32…c7b0 | 0.00000000 |
| X | 0xa95c…047d | 0.00000000 |
| Y | 0xd8e3…44c4 | 0.00000000 |
| Z | 0x7af0…197c | 0.00000000 |

**Result: All 28 Hamming swarm wallets hold 0.00 APT** (accounts exist on-chain, CoinStore resource present, but no APT balance — possibly using Fungible Assets or unfunded).

### Multisig Contract Probes (5/5 ✅ HEALTHY)

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | ✅ |
| A-G | 0xf56c…0096 | 2 | ✅ |
| Y-Z | 0xd3ff…b883 | 2 | ✅ |
| S-T | 0x3b1c…7883 | 2 | ✅ |
| V-W | 0x40fa…eb6d | 2 | ✅ |

All 5 multisig accounts require **2-of-N signatures** and responded healthy on Aptos mainnet.

### MNX Markets

- **URL:** `https://testnet.mnx.fi`
- **Status:** `SPA_ONLY` — renders a JavaScript single-page app; no REST API endpoints (`/api/markets`, `/api/v1/markets`) return data without browser execution.
- **Action:** No rows inserted to `mnx_snapshots`; requires Playwright/browser automation for future sweeps.

---

## GF(3) Schema Reference

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

### GF(3) Assignment Rule
- `id % 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id % 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id % 3 == 2` → trit=-1, color=#cc241d, name=MINUS
