# World-Increment Sweep + Hamming Snapshot — 2026-05-31

## Sweep Metadata
- **Date:** 2026-05-31
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 372 |
| Total Repo Snapshots (cumulative) | 1,293 |
| New Repo Snapshots (this sweep) | 349 |
| Sources Covered (this sweep) | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — This Sweep (349 increments)

| Trit | Hex Color | Name | Count |
|------|-----------|------|-------|
| 0 | `#d3869b` | ERGODIC | 116 |
| +1 | `#b8bb26` | PLUS | 117 |
| -1 | `#cc241d` | MINUS | 116 |

GF(3) chain cycles: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...` (349 increments = 116 full cycles + 1 ERGODIC)

---

## Top Repos by Source (This Sweep)

### plurigrid (100 repos, latest push 2026-05-31)
Top repos from previous sweeps: `plurigrid/asi` (16★), `plurigrid/gorj`, `plurigrid/vivarium`, `plurigrid/ontology`

### kubeflow (48 repos, latest push 2026-05-30)
| Repo | Language | Stars |
|------|----------|-------|
| kubeflow | — | 15,565 |
| pipelines | Python | 4,119 |
| spark-operator | Python | 3,111 |
| trainer | Go | 2,080 |
| katib | Python | 1,676 |

### bmorphism (100 repos, latest push 2026-05-31)
Top repos: `ocaml-mcp-sdk` (60★), `anti-bullshit-mcp-server` (23★)

### TeglonLabs (4 repos this sweep)
| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| mathpix-gem | Ruby | 2 | Math images → LaTeX, chemistry → SMILES |
| coin-flip-mcp | JavaScript | 0 | MCP server for random.org coin flips |
| monad-mcp-server | — | 0 | Monad MCP Server |
| topoi | Python | 0 | — |

### Social Graph Highlights
| Repo | Owner | Stars | Description |
|------|-------|-------|-------------|
| NodePiece | migalkin | 144 | Compositional KG embeddings (ICLR'22) |
| StarE | migalkin | 89 | Hyper-Relational KG message passing (EMNLP'20) |
| TextGAN | AustinCStone | 92 | GAN for text generation (TensorFlow) |
| StereoVisionMRF | AustinCStone | 11 | Loopy belief propagation stereo depth |
| kgcourse2021 | migalkin | 25 | Knowledge Graphs course materials |
| wasita.github.io | wasita | 1 | Personal site (Svelte+SvelteKit) |
| magic-garden | wasita | 2 | Discord bot for magic garden game |

## Repo Counts by Source (This Sweep)

| Source | Type | Repos | Latest Push |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 2026-05-31 |
| bmorphism | user | 100 | 2026-05-31 |
| zubyul | user | 49 | 2026-04-24 |
| kubeflow | org | 48 | 2026-05-30 |
| AustinCStone | user (social) | 10 | 2026-04-01 |
| migalkin | user (social) | 9 | 2026-05-28 |
| wasita | user (social) | 9 | 2026-05-20 |
| M1shaaa | user (social) | 8 | 2026-02-04 |
| kristinezheng | user (social) | 6 | 2026-05-14 |
| DJedamski | user (social) | 6 | 2023-04-21 |
| TeglonLabs | org | 4 | 2026-01-01 |
| **TOTAL** | | **349** | |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, Mainnet)
All 28 swarm members (alice, bob, A–Z) queried via:
`GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result:** All 28 returned `resource_not_found` — accounts not funded on mainnet or CoinStore not initialized.  
**Total swarm APT:** 0.00000000

### Multisig Contract Probes (5/5 HEALTHY)
Probed via `POST /v1/view → 0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4…7003` | 2 | ✓ |
| A-G | `0xf56c…0096` | 2 | ✓ |
| Y-Z | `0xd3ff…b883` | 2 | ✓ |
| S-T | `0x3b1c…7883` | 2 | ✓ |
| V-W | `0x40fa…eb6d` | 2 | ✓ |

All 5 multisig accounts require 2-of-N signatures and are healthy.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Both `/api/markets` and `/api/v1/markets` return Next.js SPA HTML.  
No public REST/JSON market data endpoint detected. Recorded in `mnx_snapshots` as `unavailable`.

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights (2026-05-31 Sweep)
- **kubeflow/kubeflow**: 15,565★ flagship ML platform; kubeflow still highly active (push 2026-05-30)
- **kubeflow/pipelines**: 4,119★ most popular ML pipeline for Kubernetes
- **migalkin/NodePiece**: 144★ scalable KG embeddings (ICLR'22), actively maintained
- **migalkin/StarE**: 89★ hyper-relational KG message passing (EMNLP'20)
- **AustinCStone/TextGAN**: 92★ GAN text generation in TensorFlow
- **bmorphism/ocaml-mcp-sdk**: 60★ OCaml MCP SDK using Jane Street oxcaml_effect
- **plurigrid**: 100 repos, pushed 2026-05-31 — very active
- **bmorphism**: 100 repos, pushed 2026-05-31 — very active
- **5 Aptos multisig contracts**: All healthy at 2-of-N threshold
- **28 Hamming swarm wallets**: All show 0 APT on mainnet (unfunded)
- **Cumulative world_increments**: 372 across all sweeps
