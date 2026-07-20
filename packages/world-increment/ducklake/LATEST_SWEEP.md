# World-Increment Sweep + Hamming Snapshot
**Timestamp:** 2026-07-20 18:11 UTC

---

## JOB 1: GitHub Social Graph Sweep

**Scope note:** GitHub MCP in this session is scoped to `plurigrid/gorj`. Queried `org:plurigrid` (parent org). External orgs (kubeflow, TeglonLabs) and user graphs (bmorphism, zubyul social) are outside MCP scope and were not queried.

### plurigrid org — 100 repos snapshotted

| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| plurigrid/asi | HTML | 31 | 10 | 2026-07-10 |
| plurigrid/ontology | JavaScript | 8 | 9 | 2025-05-27 |
| plurigrid/vcg-auction | Rust | 7 | 3 | 2023-03-16 |
| plurigrid/agent | Python | 5 | 1 | 2023-03-31 |
| plurigrid/StochFlow | Python | 4 | 1 | 2024-03-20 |
| plurigrid/asi-skills | Julia | 3 | 0 | 2026-04-26 |
| plurigrid/Plurigraph | JavaScript | 3 | 5 | 2025-01-05 |
| plurigrid/act | Python | 3 | 1 | 2024-07-26 |
| plurigrid/microworlds | Rust | 3 | 5 | 2023-05-13 |
| plurigrid/nash-portal | Rust | 2 | 2 | 2026-05-19 |

**Total stars across org:** 83

**Language distribution (top 5):**
- Unknown: 28 repos
- Rust: 12 repos
- TypeScript: 10 repos
- Clojure: 9 repos
- Python: 8 repos

### GF(3) Color Chain Assignment
- id%3==0 → trit=0 ERGODIC `#d3869b` (33 repos)
- id%3==1 → trit=1 PLUS `#b8bb26` (34 repos)
- id%3==2 → trit=-1 MINUS `#cc241d` (33 repos)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet — 28 Addresses (A–Z + alice/bob)

**Total APT across swarm:** 0.0000 APT

All 28 addresses returned 0.0000 APT. This indicates the accounts either:
- Have no `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource initialized, or
- Hold no native APT (may hold other tokens or be empty wallets)

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | `0xc793acde...24cc7b` | 0.0000 |
| bob | `0x0a3c00c5...512d5d` | 0.0000 |
| A | `0x8699edc0...be9d7a` | 0.0000 |
| B | `0x3f892ebe...77cb13` | 0.0000 |
| C | `0x38b99e63...91535e` | 0.0000 |
| D | `0xf7765624...fcfdd1` | 0.0000 |
| E | `0xdc1d9d53...958d36` | 0.0000 |
| F | `0x18a14b5b...c3cf71` | 0.0000 |
| G | `0x69a394c0...cc7f32` | 0.0000 |
| H | `0xce67c327...e5300f` | 0.0000 |
| I | `0x070fe5d7...0c1fc9` | 0.0000 |
| J | `0x4d964db8...e87f54` | 0.0000 |
| K | `0xa732040a...425dc4` | 0.0000 |
| L | `0x7c2eaeaf...37eba9` | 0.0000 |
| M | `0x6fed37a7...b7f2e9` | 0.0000 |
| N | `0xe7dde6da...551b2c` | 0.0000 |
| O | `0x73252b60...25a89d` | 0.0000 |
| P | `0x6218792d...1ec948` | 0.0000 |
| Q | `0xac40fa50...5c89a9` | 0.0000 |
| R | `0x7ce605cc...d76e10` | 0.0000 |
| S | `0xb8753014...9d0386` | 0.0000 |
| T | `0x35781dc0...3f4588` | 0.0000 |
| U | `0x75860da4...ef9956` | 0.0000 |
| V | `0xb59dd817...9af2c3` | 0.0000 |
| W | `0x5f32aef7...ccc7b0` | 0.0000 |
| X | `0xa95cbbd1...33047d` | 0.0000 |
| Y | `0xd8e32848...2444c4` | 0.0000 |
| Z | `0x7af0ef6e...4e197c` | 0.0000 |

### Multisig Contract Probes — 5/5 Healthy

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | ✓ |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✓ |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✓ |

**All 5 multisigs are healthy — 2-of-2 signature requirement confirmed on all pairs.**

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — Vercel deployment protection active (401 Password Protected). No market data extractable from SPA.

---

## DuckDB Ducklake Summary

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 123 |
| repo_snapshots | 1044 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

*(Row counts are cumulative across all sweep runs.)*
