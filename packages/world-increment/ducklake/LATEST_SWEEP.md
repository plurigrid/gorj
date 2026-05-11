# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-11

## Sweep Metadata
- **Date:** 2026-05-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.1.3 (Ossivibrans)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 34 |
| Total Repo Snapshots | 1004 (501 unique repos) |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Healthy | 5/5 |

---

## GF(3) Color Chain — Sources

| Source | Type | GF3 Trit | Color | Name |
|--------|------|-----------|-------|------|
| plurigrid | org | 0 | `#d3869b` | **ERGODIC** |
| kubeflow | org | +1 | `#b8bb26` | **PLUS** |
| TeglonLabs | org | -1 | `#cc241d` | **MINUS** |
| bmorphism | user | 0 | `#d3869b` | **ERGODIC** |
| zubyul | user | +1 | `#b8bb26` | **PLUS** |
| migalkin | user | -1 | `#cc241d` | **MINUS** |
| DJedamski | user | 0 | `#d3869b` | **ERGODIC** |
| wasita | user | +1 | `#b8bb26` | **PLUS** |
| kristinezheng | user | -1 | `#cc241d` | **MINUS** |
| M1shaaa | user | 0 | `#d3869b` | **ERGODIC** |
| AustinCStone | user | +1 | `#b8bb26` | **PLUS** |

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## Top Repos by Source

### plurigrid (116 unique repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ontology | JavaScript | 8 | 2025-05-27 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| graded-optic | Haskell | 0 | 2026-02-08 |
| nblm-flashcards | Hy | 0 | 2026-03-26 |

### kubeflow (47 unique repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,572 | 2026-01-05 |
| pipelines | Python | 4,138 | 2026-04-10 |
| spark-operator | Python | 3,125 | 2026-04-10 |
| trainer | Go | 2,097 | 2026-04-10 |
| katib | Python | 1,678 | 2026-04-02 |

### TeglonLabs (53 unique repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| topoi | Python | 0 | 2025-01-24 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |

### bmorphism (108 unique repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| risc0-cosmwasm-example | Rust | 23 | 2025-05-21 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-02-05 |
| say-mcp-server | JavaScript | 20 | 2026-03-19 |
| babashka-mcp-server | JavaScript | 18 | 2026-03-26 |
| Gay.jl | Julia | 1 | 2026-04-17 (188 open issues) |

### migalkin (30 unique repos, zubyul social graph)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 25 | 2026-02-16 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |

### zubyul (26 unique repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gay-world | Python | 1 | 2026-04-05 |
| voice-observatory | Python | 0 | 2026-04-24 |
| ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |
| big-bad-plurigrid-quiz | Emacs Lisp | 0 | 2026-04-09 |

### AustinCStone (43 unique repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Unique Repos |
|--------|------|-------------|
| plurigrid | org | 116 |
| bmorphism | user | 108 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| wasita | user | 33 |
| migalkin | user | 30 |
| zubyul | user | 26 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **501** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, Mainnet)

All 28 Hamming-swarm wallets (alice, bob, A–Z) were queried via
`fullnode.mainnet.aptoslabs.com`. Every address returned **0 APT**.
The wallets are indexed on-chain but have not received any APT funding.

| World | Address (truncated) | Balance APT |
|-------|---------------------|------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…512d | 0.0 |
| A–Z | 0x8699…–0x7af0… | 0.0 (all) |

**Rows in `aptos_snapshots`: 28**

### Multisig Contract Probes — 5/5 Healthy

All 5 pair contracts responded to `num_signatures_required` with `2`:

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | `0x0da4f428…4987003` | 2 | ✓ healthy |
| A-G | `0xf56c4a1c…bc0096` | 2 | ✓ healthy |
| Y-Z | `0xd3ffe181…e75b883` | 2 | ✓ healthy |
| S-T | `0x3b1c3ae9…ed7883` | 2 | ✓ healthy |
| V-W | `0x40fad7b4…c80eb6d` | 2 | ✓ healthy |

**All multisig accounts are 2-of-N. 5/5 healthy. Rows in `multisig_probes`: 5**

### MNX Markets (testnet.mnx.fi)

Probed `/api/markets`, `/api/v1/markets`, and `/api/tickers`. All paths
returned the Next.js SPA HTML — no structured REST API is exposed at these
endpoints on the testnet. **Market data unavailable this sweep.**

**Rows in `mnx_snapshots`: 0**

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,572 stars — flagship ML platform for Kubernetes
- **migalkin/NodePiece**: 144 ★ — scalable KG embeddings (ICLR'22), freshly pushed 2026-05-07
- **bmorphism/ocaml-mcp-sdk**: 61 ★ — OCaml MCP SDK via Jane Street oxcaml_effect, pushed 2026-05-08
- **AustinCStone/TextGAN**: 92 ★ — GAN text generation in TensorFlow
- **plurigrid/nanoclj-zig**: NaN-boxed Clojure interpreter in Zig, 20 open issues, pushed 2026-04-25
- **plurigrid/zig-syrup**: High-performance OCapN Syrup in Zig, pushed 2026-04-30
- **zubyul/voice-observatory**: Passive macOS TUI for voice-download paths, pushed 2026-04-24
- **Hamming swarm**: 5/5 multisig contracts 2-of-N healthy; all 28 wallets unfunded (0 APT)
