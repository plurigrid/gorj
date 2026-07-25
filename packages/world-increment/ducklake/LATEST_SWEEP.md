# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-25

## Sweep Metadata
- **Date:** 2026-07-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **Sweep IDs:** 13–16
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 27 |
| Total Repo Snapshots | 986 |
| New Increments (this run) | 4 (IDs 13–16) |
| New Repos (this run) | 42 |
| Sources Covered (this run) | 2 orgs + 2 users + 1 hamming swarm |

---

## GF(3) Color Chain — New Increments (IDs 13–16)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (org) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 14 | TeglonLabs (org) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 15 | bmorphism+zubyul (users) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 16 | aptos_mainnet (hamming) | aptos_snapshot | +1 | `#b8bb26` | **PLUS** |

GF(3) extension: `…ERGODIC(12) → PLUS(13) → MINUS(14) → ERGODIC(15) → PLUS(16)`

---

## Top Repos by Source (this sweep)

### plurigrid (103 total public, 20 snapshotted)
| Repo | Language | Stars | Issues | Pushed At |
|------|----------|-------|--------|-----------|
| gorj | Clojure | 1 | 1382 | 2026-07-25 |
| eirobri | Clojure | 0 | 31 | 2026-07-21 |
| place | TeX | 1 | 14 | 2026-07-14 |
| shrimp | — | 0 | 0 | 2026-07-03 |
| asi | HTML | 31 | 4 | 2026-07-10 |
| nash-portal | Rust | 2 | 1 | 2026-05-19 |
| nanoclj-zig | Zig | 1 | 20 | 2026-04-25 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (106 total, 9 snapshotted)
| Repo | Language | Stars | Issues | Pushed At |
|------|----------|-------|--------|-----------|
| Gay.jl | Julia | 2 | 188 | 2026-07-21 |
| gay-chat | Scheme | 0 | 0 | 2026-07-14 |
| satreadout | HTML | 0 | 0 | 2026-06-20 |
| bci-preview | HTML | 0 | 0 | 2026-06-20 |
| world | Python | 0 | 0 | 2026-06-02 |

### zubyul (49 total, 8 snapshotted)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| voice-observatory | Python | 0 | 2026-04-24 |
| ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |
| gay-world | Python | 1 | 2026-04-05 |
| big-bad-plurigrid-quiz | Emacs Lisp | 0 | 2026-04-09 |

---

## Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 20 |
| bmorphism | user | 9 |
| zubyul | user | 8 |
| TeglonLabs | org | 5 |
| **TOTAL (this sweep)** | | **42** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses, increment 16)

Queried via `https://fullnode.mainnet.aptoslabs.com/v1/` at ledger version **6,443,287,121**  
(epoch 16661, block height 923,593,615).

All 28 Hamming swarm addresses (alice, bob, A–Z) returned `resource_not_found` for  
`CoinStore<0x1::aptos_coin::AptosCoin>` — **0.0 APT across all 28 addresses**.  
None of the swarm addresses hold an initialized APT CoinStore on Aptos mainnet.

### Multisig Contract Probes (5 pairs, all healthy)

| pair | address (truncated) | sigs_required | status |
|------|---------------------|--------------|--------|
| A-B | `0x0da4f428…` | 2 | ✅ healthy |
| A-G | `0xf56c4a1c…` | 2 | ✅ healthy |
| Y-Z | `0xd3ffe181…` | 2 | ✅ healthy |
| S-T | `0x3b1c3ae9…` | 2 | ✅ healthy |
| V-W | `0x40fad7b4…` | 2 | ✅ healthy |

All 5 multisig contracts respond on-chain with 2-of-2 signature requirement.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA with no public REST API at `/api/markets` or `/api/v1/markets`.  
**Status: unavailable** — no structured market data extractable via HTTP without JS runtime.

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
- **plurigrid/gorj**: 1,382 open issues, last push 2026-07-25 — heaviest active repo
- **plurigrid/asi**: 31 ★, 10 forks — "everything is topological chemputer!"
- **bmorphism/Gay.jl**: 2 ★, 188 issues — wide-gamut GF(3) color sampling, branch `gay`
- **bmorphism/gay-chat**: `gay://chat` over Spritely Brassica Chat (Scheme)
- **TeglonLabs/jank-crane**: GF3 convergence maps + simonw workflow (C++, pushed 2026-06-08)
- **All 5 multisig contracts**: healthy, 2-of-2 threshold confirmed on Aptos mainnet
- **Hamming swarm (A–Z + alice + bob)**: all 28 addresses at 0.0 APT — no CoinStore initialized
- **Increment 16**: PLUS — closes this 5th partial GF(3) cycle (13→16)
