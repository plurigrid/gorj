# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-27

## Sweep Metadata
- **Date:** 2026-04-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 43 |
| Total Repo Snapshots | 43 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 14 |
| 1 | `#b8bb26` | PLUS | 15 |
| 2 (-1) | `#cc241d` | MINUS | 14 |

GF(3) rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

### Top Repos by Source (2026-04-27)

#### plurigrid (10 captured, most recently pushed)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 0 | 2026-04-27 |
| asi | HTML | 17 | 2026-04-26 |
| zig-syrup | Zig | 2 | 2026-04-26 |
| horse | TeX | 1 | 2026-04-26 |
| asi-skills | Julia | 3 | 2026-04-26 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |
| ontology | JavaScript | 7 | 2025-05-27 |
| vivarium | Clojure | 1 | 2026-04-08 |

#### kubeflow (7 captured, most starred)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,607 | 2026-01-05 |
| pipelines | Python | 4,126 | 2026-04-26 |
| spark-operator | Python | 3,120 | 2026-04-24 |
| trainer | Go | 2,094 | 2026-04-25 |
| katib | Python | 1,681 | 2026-04-14 |
| hub | Go | 174 | 2026-04-27 |
| mcp-apache-spark | Python | 152 | 2026-04-25 |

#### TeglonLabs (4, all)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |
| topoi | Python | 0 |
| monad-mcp-server | — | 0 |

#### bmorphism (6, most recently pushed)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 1 | 2026-04-27 |
| nanoclj-zig | Zig | 0 | 2026-04-25 |
| postweb | Go | 0 | 2026-04-09 |
| shitcoin | Python | 5 | 2026-04-08 |
| ocaml-mcp-sdk | OCaml | 60 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |

#### zubyul (6, most recently pushed)
| Repo | Language | Stars |
|------|----------|-------|
| voice-observatory | Python | 0 |
| ghostel-emacs-worlds | GLSL | 0 |
| nash-web | Rust | 0 |
| nash-tui | Rust | 0 |
| Gay.jl | Julia | 0 |
| gay-world | Python | 1 |

#### Social Graph Highlights
| User | Repo | Stars | Note |
|------|------|-------|------|
| migalkin | NodePiece | 143 | ICLR'22 KG embeddings |
| migalkin | StarE | 89 | Hyper-relational KG (EMNLP'20) |
| AustinCStone | TextGAN | 92 | GAN for text (TensorFlow) |
| wasita | wasita.github.io | 1 | Svelte personal site, pushed 2026-04-27 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-04-27)

Queried 28 addresses via `0x1::coin::CoinStore<AptosCoin>` with 1s sleep between calls.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | `0xc793...4cc7b` | no coin store |
| bob | `0x0a3c...512d5d` | no coin store |
| A | `0x8699...e9d7a` | no coin store |
| B | `0x3f89...cb13` | 0.0 |
| C | `0x38b9...535e` | no coin store |
| D | `0xf776...cfdd1` | no coin store |
| E–Z | all remaining | 0.0 each |

> Addresses with `no coin store` have no `0x1::coin::CoinStore<AptosCoin>` resource — accounts may be uninitialized or use a different token structure. Addresses with `0.0` have an initialized store but zero balance.

### Multisig Contract Probes (5 pairs, all healthy)

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f4...87003` | 2 | ✓ |
| A-G | `0xf56c4a...0096` | 2 | ✓ |
| Y-Z | `0xd3ffe1...b883` | 2 | ✓ |
| S-T | `0x3b1c3a...7883` | 2 | ✓ |
| V-W | `0x40fad7...eb6d` | 2 | ✓ |

All 5 multisig accounts require **2-of-N signatures** and respond successfully on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA — no JSON API endpoints available (`/api/markets`, `/api/v1/markets`, `/api/tickers` all serve HTML). Market data recorded as **unavailable** in `mnx_snapshots`.

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
- `id mod 3 == 2` → trit=2 (-1), color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,607 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,126 stars — most active KF repo (pushed 2026-04-26)
- **migalkin/NodePiece**: 143 stars — compositional KG embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK using Jane Street oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/gorj**: 0 stars, 4 open issues — this very repo, pushed 2026-04-27
- **All 5 multisig pairs**: 2-of-N, healthy on Aptos mainnet
- **Hamming swarm**: 28 wallets (A–Z + alice + bob), all either 0 APT or uninitialized
