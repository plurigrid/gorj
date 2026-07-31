# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-31

## Sweep Metadata
- **Date:** 2026-07-31
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Ledger version (Aptos mainnet):** 6553498943

---

## Summary Counts (This Sweep — 2026-07-31)

| Metric | Value |
|--------|-------|
| New World Increments | 172 (IDs 1-172) |
| New Repo Snapshots | 172 |
| Cumulative Increments (DB) | 195 |
| Cumulative Repo Snapshots (DB) | 1116 |
| Sources Covered | 3 orgs + 2 primary users + 6 social-graph users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain (This Sweep)

**Rule:** `id mod 3 == 0` → ERGODIC #d3869b | `id mod 3 == 1` → PLUS #b8bb26 | `id mod 3 == 2` → MINUS #cc241d

| GF3 Name | Color | Count (this sweep) |
|----------|-------|-------------------|
| ERGODIC | #d3869b | 57 |
| PLUS | #b8bb26 | 58 |
| MINUS | #cc241d | 57 |

Sample chain: `(1) PLUS → (2) MINUS → (3) ERGODIC → (4) PLUS → (5) MINUS → (6) ERGODIC → ...`

---

## GitHub Social Graph — Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 56 | 2026-07-10 |
| zig-syrup | Zig | 2 | 2026-07-28 |
| nash-portal | Rust | 2 | 2026-05-19 |
| gorj | Clojure | 1 | 2026-07-31 |
| place | TeX | 1 | 2026-07-14 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15801 | 2026-07-10 |
| pipelines | Python | 4172 | 2026-07-31 |
| spark-operator | Python | 3141 | 2026-07-31 |
| trainer | Go | 2165 | 2026-07-31 |
| katib | Python | 1695 | 2026-07-26 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| jank-crane | C++ | 0 | 2026-06-08 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (106 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| Gay.jl | Julia | 2 | 2026-07-21 |
| satreadout | HTML | 0 | 2026-06-20 |

### zubyul (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gay-world | Python | 1 | 2026-04-05 |
| voice-observatory | Python | 0 | 2026-04-24 |
| ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |

### Social Graph Users
| User | Top Repo | Stars |
|------|----------|-------|
| migalkin | NodePiece (Python) | 144 |
| AustinCStone | TextGAN (Python) | 92 |
| wasita | magic-garden (Python) | 2 |
| kristinezheng | lookit-jenga | 0 |
| M1shaaa | lab-bookshelf- (TypeScript) | 0 |
| DJedamski | kaggle_ncaa18 (Jupyter) | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

**Result:** All 28 Hamming-swarm wallets returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version 6553498943.  
All wallets are **uninitialized** on Aptos mainnet (no APT coin store registered).

| World | Address (first 10 chars) | Balance (APT) |
|-------|--------------------------|--------------|
| alice | 0xc793acdec1... | 0.0 |
| bob | 0x0a3c00c58f... | 0.0 |
| A | 0x8699edc096... | 0.0 |
| B–Z | (24 addresses) | 0.0 each |

### Multisig Contract Probes (0x1::multisig_account::num_signatures_required)

| Pair | Address (first 10 chars) | Sigs Required | Healthy |
|------|--------------------------|--------------|---------|
| A-B | 0x0da4f428a0... | 2 | ✅ |
| A-G | 0xf56c4a1c09... | 2 | ✅ |
| Y-Z | 0xd3ffe1812b... | 2 | ✅ |
| S-T | 0x3b1c3ae905... | 2 | ✅ |
| V-W | 0x40fad7b423... | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed for all pairs.**

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable via server-side probe.** testnet.mnx.fi is a Next.js SPA.  
No REST API endpoints (`/api/markets`, `/api/v1/markets`) return JSON without  
browser-side JavaScript execution. `mnx_snapshots` table has 0 rows.

---

## DuckDB State

| Table | Rows (cumulative) | Added This Sweep |
|-------|-------------------|-----------------|
| world_increments | 195 | 172 |
| repo_snapshots | 1116 | 172 |
| aptos_snapshots | 28 | 28 |
| multisig_probes | 5 | 5 |
| mnx_snapshots | 0 | 0 |

---

## Notable Highlights (2026-07-31)

- **kubeflow/pipelines** (4172★), **spark-operator** (3141★), **trainer** (2165★) all pushed today
- **plurigrid/gorj** (this repo) pushed today — most recently active plurigrid repo
- **plurigrid/asi** grew from 16★ (Apr sweep) to **56★** — significant traction
- **bmorphism/Gay.jl** updated with 188 open issues — high activity
- **bmorphism/ocaml-mcp-sdk** now at 61★ (was 60 in Apr sweep)
- **migalkin/NodePiece** now at 144★ (was 143 in Apr sweep)
- **TeglonLabs/jank-crane** (C++) — new repo since Apr sweep, GF3 + loopify pass spec
- **All 5 Hamming-swarm multisig contracts**: 2-of-N threshold intact, healthy
- **Hamming swarm wallets (A–Z + alice/bob)**: uninitialized on Aptos mainnet

*Generated by world-increment-sweep + hamming-swarm-snapshot agent, 2026-07-31*
