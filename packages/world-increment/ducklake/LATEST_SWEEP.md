# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-09  
**Run:** world-increment-sweep + hamming-swarm-snapshot  

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 50 |
| bmorphism | user | 10 (top by activity) |
| TeglonLabs | org | 5 |
| zubyul | user | 10 (top by activity) |
| migalkin | user | 5 (top by stars) |
| wasita | user | 6 |
| AustinCStone | user | 3 (top) |
| **Total** | | **89 unique repos** |

> Note: `kubeflow` org (49 repos) captured via MCP search but excluded from final snapshot to keep scope on social graph. DJedamski/kristinezheng/M1shaaa had no public repos returned by search.  
> Note: Direct GitHub org/user API paths (`/orgs/{org}/repos`, `/users/{user}/repos`) are proxy-blocked in this remote environment; data collected via GitHub MCP search tools.

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 59 | HTML |
| migalkin/kgcourse2021 | 24 | HTML |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 29 |
| 1 | `#b8bb26` | PLUS | 30 |
| -1 | `#cc241d` | MINUS | 30 |

### Notable Activity (bmorphism)
- `Gay.jl` — Wide-gamut color sampling with splittable determinism (Julia, pushed 2026-07-21)
- `gay-chat` — gay://chat over Spritely Brassica (Scheme, pushed 2026-07-14)
- `anti-bullshit-mcp-server` — Epistemological claim analysis MCP (JS, pushed 2026-08-02)
- `ocaml-mcp-sdk` — OCaml MCP SDK via Jane Street oxcaml_effect (61 ⭐)

### Notable Activity (zubyul)
- `big-bad-plurigrid-quiz` — Emacs drill flashcards from plurigrid/bmorphism activity
- `ghostel-emacs-worlds` — Ghostty + alice/bob emacs stack (GLSL, pushed 2026-04-24)
- `voice-observatory` — Passive macOS TUI for voice-download pathways

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice–Z, 28 addresses)

All 28 Hamming swarm addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~6,677,072,000. This indicates all accounts have **0 APT** (CoinStore resource not initialized — accounts unfunded on mainnet).

| World | Balance (APT) | Status |
|-------|--------------|--------|
| alice–Z (all) | 0.0 | resource_not_found |

### Multisig Contract Probes (5 pairs)

All 5 multisig accounts are **healthy** with `num_signatures_required = 2`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428...` | 2 | ✓ |
| A-G | `0xf56c4a1c...` | 2 | ✓ |
| Y-Z | `0xd3ffe181...` | 2 | ✓ |
| S-T | `0x3b1c3ae9...` | 2 | ✓ |
| V-W | `0x40fad7b4...` | 2 | ✓ |

All multisig pairs use 2-of-N threshold. Contracts respond normally on mainnet.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA (HTTP 200 root). No JSON API endpoints found at common paths (`/api/markets`, `/api/v1/markets`, `/api/tickers` → 404). Market data **unavailable** via API — requires browser JS execution.

---

## DuckDB Schema (ducklake/world-increments.duckdb)

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 89 | GF(3) color-chained repo events |
| `repo_snapshots` | 89 | Full repo metadata snapshot |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances |
| `multisig_probes` | 5 | Multisig contract health probes |
| `mnx_snapshots` | 0 | MNX market data (API unavailable) |
