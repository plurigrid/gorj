# World-Increment Sweep — 2026-06-27

## GitHub Social Graph

| Source | Type | Repos | Top Star Count |
|--------|------|-------|---------------|
| plurigrid | org | 100 | asi (26★) |
| kubeflow | org | 48 | kubeflow (15,748★) |
| TeglonLabs | org | 5 | mathpix-gem (2★) |
| bmorphism | user | 100 | ocaml-mcp-sdk (61★) |
| zubyul | user | 49 | personal/experimental |
| migalkin | social | 19 | NodePiece (144★) |
| DJedamski | social | 6 | academic projects |
| wasita | social | 11 | magic-garden (2★) |
| kristinezheng | social | 5 | cognitive science |
| M1shaaa | social | 8 | Lookit research |
| AustinCStone | social | 30 | TextGAN (92★) |

**Total repos indexed:** ~381 across 11 sources

### Notable Recent Activity (last 30 days)
- `plurigrid/gorj` — pushed today (2026-06-27), 858 open issues
- `plurigrid/asi` — 26★, active AI systems work
- `bmorphism/ocaml-mcp-sdk` — 61★, MCP tooling
- `bmorphism/anti-bullshit-mcp-server` — 23★
- `kubeflow/kubeflow` — 15,748★, `kubeflow/pipelines` — 4,157★
- `migalkin/NodePiece` — 144★, `migalkin/StarE` — 89★
- `AustinCStone/TextGAN` — 92★

---

## Hamming Swarm Snapshot

### Aptos Mainnet Balances

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793... | 0.0 |
| bob | 0x0a3c... | 0.0 |
| A–Z | 0x8699...–0x7af0... | 0.0 each |

**All 28 addresses: 0 APT** — wallets unfunded on mainnet (expected for swarm nodes).

### Multisig Contract Probes

Probed via `0x1::multisig_account::num_signatures_required` view function.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4... | 2 | ✅ healthy |
| A-G | 0xf56c... | 2 | ✅ healthy |
| Y-Z | 0xd3ff... | 2 | ✅ healthy |
| S-T | 0x3b1c... | 2 | ✅ healthy |
| V-W | 0x40fa... | 2 | ✅ healthy |

**All 5 multisig contracts healthy** — 2-of-N threshold confirmed.

### MNX Markets

`https://testnet.mnx.fi/api/markets` → **401 Unauthorized** (unavailable, no data captured)

---

## GF(3) Trit Legend

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1,036 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

Database: `packages/world-increment/ducklake/world-increments.duckdb`
