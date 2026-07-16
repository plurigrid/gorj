# World-Increment Sweep — 2026-07-16

## Sweep Metadata
- **Date:** 2026-07-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (via pip)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots (sampled) | 67 |
| GitHub Sources | 3 orgs + 8 users |
| Repos Discovered | ~413 across 11 sources |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (Vercel auth) |

---

## GF(3) Color Chain — All 12 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|----------|-------|------|
| 1 | plurigrid (org) | repo_snapshot | 0 | `#b8bb26` | **PLUS** |
| 2 | kubeflow (org) | repo_snapshot | 1 | `#cc241d` | **MINUS** |
| 3 | TeglonLabs (org) | repo_snapshot | -1 | `#d3869b` | **ERGODIC** |
| 4 | bmorphism (user) | repo_snapshot | 0 | `#b8bb26` | **PLUS** |
| 5 | zubyul (user) | repo_snapshot | 1 | `#cc241d` | **MINUS** |
| 6 | migalkin (user) | repo_snapshot | -1 | `#d3869b` | **ERGODIC** |
| 7 | DJedamski (user) | repo_snapshot | 0 | `#b8bb26` | **PLUS** |
| 8 | wasita (user) | repo_snapshot | 1 | `#cc241d` | **MINUS** |
| 9 | kristinezheng (user) | repo_snapshot | -1 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | 0 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | 1 | `#cc241d` | **MINUS** |
| 12 | gorj (sweep) | sweep_complete | -1 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## GitHub Social Graph Sweep

### plurigrid (103 repos)
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| asi | HTML | 30 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-07 |
| ontology | JavaScript | 8 | 2026-05-09 |
| vcg-auction | Rust | 7 | 2025-12-16 |
| nash-portal | Rust | 2 | 2026-05-19 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| asi-skills | Julia | 3 | 2026-04-26 |

### kubeflow (49 repos)
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow | — | 15,779 | 2026-07-16 |
| pipelines | Python | 4,167 | 2026-07-16 |
| spark-operator | Python | 3,137 | 2026-07-16 |
| trainer | Go | 2,150 | 2026-07-15 |
| katib | Python | 1,690 | 2026-07-16 |
| arena | Go | 815 | 2026-07-16 |
| mcp-server | Python | 26 | 2026-07-16 |
| sdk | Python | 125 | 2026-07-16 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-03-16 |

### bmorphism (106 repos)
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| gay-chat | Scheme | 0 | 2026-07-14 |
| Gay.jl | Julia | 2 | 2026-07-14 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| penrose-mcp | JavaScript | 9 | 2026-06-24 |
| babashka-mcp-server | JavaScript | 19 | 2026-06-05 |
| say-mcp-server | JavaScript | 20 | 2026-03-19 |
| risc0-cosmwasm-example | Rust | 23 | 2025-05-21 |

### zubyul (49 repos)
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| voice-observatory | Python | 0 | 2026-04-24 |
| ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |
| gay-world | Python | 1 | 2026-04-05 |
| Gay.jl | Julia | 0 | 2026-03-28 |

### Social Graph (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)
| User | Total Repos | Top Repo | Stars |
|------|-------------|----------|-------|
| migalkin | 19 | NodePiece (ICLR'22) | 144 |
| DJedamski | 6 | Kaggle | 1 |
| wasita | 11 | magic-garden | 2 |
| kristinezheng | 5 | kristinezheng.github.io | 0 |
| M1shaaa | 8 | M1shaaa | 0 |
| AustinCStone | 41 | TextGAN | 92 |

---

## Hamming Swarm Snapshot — Aptos Mainnet

### Wallet Balances (28 addresses: alice, bob, A–Z)

**Status: All 28 addresses → HTTP 404 (no APT CoinStore on mainnet)**

Accounts not yet activated on-chain. Aptos requires an initial on-chain transaction to register a CoinStore; none of these addresses have been funded.

| World | Balance (APT) | Status |
|-------|---------------|--------|
| alice | — | 404 Not Found |
| bob | — | 404 Not Found |
| A through Z (26) | — | 404 Not Found × 26 |

### Multisig Contract Probes (5/5 healthy ✓)

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4…003 | 2-of-2 | ✓ healthy |
| A-G | 0xf56c…096 | 2-of-2 | ✓ healthy |
| Y-Z | 0xd3ff…883 | 2-of-2 | ✓ healthy |
| S-T | 0x3b1c…883 | 2-of-2 | ✓ healthy |
| V-W | 0x40fa…b6d | 2-of-2 | ✓ healthy |

All 5 multisig contracts live on mainnet and responding. All uniformly require 2 signatures.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable — Vercel deployment protection (Vercel auth required)**

The testnet.mnx.fi deployment is behind Vercel authentication. The root and `/api/markets`, `/api/v1/markets` paths all return an auth wall. No market data accessible in this sweep.

---

## Delta vs Previous Sweep (2026-04-12)

| Metric | Apr 12 | Jul 16 | Delta |
|--------|--------|--------|-------|
| plurigrid repos | 100 | 103 | +3 |
| kubeflow repos | 47 | 49 | +2 |
| TeglonLabs repos | 3 | 5 | +2 |
| bmorphism repos | 90 | 106 | +16 |
| zubyul repos | 40 | 49 | +9 |
| Multisigs probed | 0 | 5/5 ✓ | new |
| Aptos wallets probed | 0 | 28 | new |

**Notable new repos since Apr 12:**
- `plurigrid/shrimp` — Jank worked example (2026-07-03)
- `bmorphism/gay-chat` — gay://chat over Spritely Brassica Chat (2026-07-14)
- `AustinCStone/byteruckus` — (2026-07-15)
- `kubeflow/mcp-server` — Kubeflow AI agent tooling
- `kubeflow/docs-agent` — Documentation AI agent
