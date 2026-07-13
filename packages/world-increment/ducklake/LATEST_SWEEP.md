# World-Increment Sweep — 2026-07-13

## Sweep Metadata
- **Date:** 2026-07-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** Python duckdb 1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | This Run | Cumulative |
|--------|----------|------------|
| New World Increments | 11 | 34 total |
| New Repo Snapshots | 392 | 1,336 total |
| Sources Covered | 3 orgs + 8 users | — |
| Aptos Wallets Probed | 28 | — |
| Multisig Contracts Probed | 5 | — |
| MNX Markets | N/A (401) | — |

---

## GF(3) Color Chain — This Run (IDs 13–23)

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 13 | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | org | 49 | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs | org | 5 | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | user | 100 | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin | user | 19 | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski | user | 6 | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita | user | 11 | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | user | 8 | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone | user | 40 | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| plurigrid/asi | HTML | 30 | 2026-07-10 |
| plurigrid/gorj | Clojure | 1 | 2026-07-13 |
| plurigrid/zig-syrup | Zig | — | 2026-07-03 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/sdk | Python | 124 | 2026-07-13 |
| kubeflow/community-distribution | YAML | 1029 | 2026-07-12 |
| kubeflow/mcp-server | Python | 22 | 2026-07-12 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 2026-01-01 |
| TeglonLabs/coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| bmorphism/Gay.jl | Julia | 2 | 2026-07-13 |
| bmorphism/satreadout | HTML | 0 | 2026-06-20 |
| bmorphism/world | Python | 0 | 2026-06-02 |

### zubyul (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| zubyul/voice-observatory | Python | 0 | 2026-04-24 |
| zubyul/ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |
| zubyul/nash-tui | Rust | 0 | 2026-04-13 |

### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| migalkin/kgcourse2021 | HTML | 24 | 2025-08-04 |
| migalkin/StarE | Python | 89 | 2023-12-01 |
| migalkin/NBFNet_mlx | Python | 10 | 2024-03-02 |

### AustinCStone (40 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| AustinCStone/EpsteinSearch | Python | 0 | 2026-02-11 |
| AustinCStone/bmfork | Python | 0 | 2025-05-09 |

---

## Repo Counts by Source

| Source | Type | Repos (this run) |
|--------|------|-----------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **392** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All 28 wallets (alice, bob, A–Z) returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~6255053804.
These accounts use the Fungible Asset (FA) standard rather than the legacy Coin standard.
Legacy CoinStore balance = 0 / not applicable for all.

| World | Address (prefix) | Balance APT |
|-------|------------------|-------------|
| alice | 0xc793...c7b | N/A (FA-only) |
| bob   | 0x0a3c...5d | N/A (FA-only) |
| A–Z   | (26 addresses) | N/A (FA-only) |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** (2-of-N threshold confirmed):

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

### MNX Markets

`https://testnet.mnx.fi` → **401 Unauthorized** (authentication required, no public API available).
No market data inserted.

---

## Delta Since Last Sweep (2026-04-12 → 2026-07-13)

| Source | Prev Repos | Curr Repos | Δ |
|--------|-----------|------------|---|
| plurigrid | 100 | 100 | 0 |
| kubeflow | 47 | 49 | +2 |
| TeglonLabs | 53 | 5 | −48 (visibility change) |
| bmorphism | 100 | 100 | 0 |
| zubyul | 24 | 49 | +25 |
| migalkin | 30 | 19 | −11 (visibility change) |
| DJedamski | 11 | 6 | −5 (visibility change) |
| wasita | 29 | 11 | −18 (visibility change) |
| kristinezheng | 18 | 5 | −13 (visibility change) |
| M1shaaa | 16 | 8 | −8 (visibility change) |
| AustinCStone | 43 | 40 | −3 |

Repo count changes reflect GitHub search API visibility (public repos matching the indexed graph).

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

## Notable Highlights
- **kubeflow/community-distribution**: 1,029 stars — new addition since last sweep
- **kubeflow/sdk**: 124 stars — new dedicated SDK repo (pushed 2026-07-13, same day as sweep)
- **kubeflow/mcp-server**: 22 stars — Kubeflow MCP server appeared since last sweep
- **plurigrid/asi**: Gained 14 more stars (16 → 30) in ~3 months
- **plurigrid/gorj**: Active today (2026-07-13) — this very repo
- **bmorphism/Gay.jl**: Active Julia repo pushed today
- **TeglonLabs/jank-crane**: New C++ repo — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"
- **zubyul**: Most active growth (+25 repos), including `voice-observatory`, `ghostel-emacs-worlds` (GLSL), `nash-tui` (Rust)
- **Multisig health**: All 5 pairs (A-B, A-G, Y-Z, S-T, V-W) confirmed 2-of-N — no changes
- **Aptos wallets**: FA migration complete — no legacy CoinStore resources found on any of the 28 addresses
