# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-09

## Sweep Metadata
- **Date:** 2026-05-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 81 |
| Total Repo Snapshots | 81 |
| Sources Covered | 3 orgs + 8 users |

### Sources Scanned

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 16 (top) of 100 |
| kubeflow | org | 10 (top) of 48 |
| TeglonLabs | org | 4 (all) |
| bmorphism | user | 16 (top) of ~80 |
| zubyul | user | 10 (top) of 49 |
| migalkin | social graph | 5 of 19 |
| DJedamski | social graph | 4 of 6 |
| wasita | social graph | 5 of 11 |
| kristinezheng | social graph | 3 of 6 |
| M1shaaa | social graph | 3 of 8 |
| AustinCStone | social graph | 5 of 40 |
| **TOTAL** | | **81 repo snapshots** |

### GF(3) Color Chain

Chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...` (27 full cycles)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` (pink) | ERGODIC | 27 |
| +1 | `#b8bb26` (green) | PLUS | 27 |
| -1 | `#cc241d` (red) | MINUS | 27 |

### Top Repos by Stars

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,628 | — | 2026-05-07 |
| kubeflow/pipelines | 4,137 | Python | 2026-05-08 |
| kubeflow/spark-operator | 3,125 | Python | 2026-05-08 |
| kubeflow/trainer | 2,096 | Go | 2026-05-08 |
| kubeflow/manifests | 1,015 | YAML | 2026-05-08 |
| kubeflow/katib | 1,683 | Python | 2026-05-08 |
| kubeflow/arena | 810 | Go | 2026-05-07 |
| kubeflow/kale | 684 | Python | 2026-05-09 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |

### Notable Recent Activity (plurigrid/gorj cluster)

- **plurigrid/gorj** — pushed 2026-05-09: forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **bmorphism/Gay.jl** — pushed 2026-05-09: 187 open issues, active wide-gamut color sampling
- **bmorphism/nanoclj-zig** — pushed 2026-05-07: NaN-boxed Clojure interpreter in Zig
- **bmorphism/zig-syrup** — pushed 2026-05-07: OCapN Syrup encoder/decoder in Zig
- **plurigrid/horse** — pushed 2026-05-07
- **kubeflow/kale** — pushed 2026-05-09: 684 stars, ML superfood for data scientists
- **kubeflow/mcp-apache-spark-history-server** — pushed 2026-05-09: 167 stars, new MCP entry

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) returned **0 APT**.
API response: `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — wallets exist on-chain but no CoinStore resource is initialized (no APT deposits recorded at ledger version 5,195,641,207).

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...512d | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B | 0x3f89...b13 | 0.00000000 |
| C | 0x38b9...35e | 0.00000000 |
| D | 0xf776...dd1 | 0.00000000 |
| E | 0xdc1d...d36 | 0.00000000 |
| F | 0x18a1...f71 | 0.00000000 |
| G | 0x69a3...f32 | 0.00000000 |
| H | 0xce67...00f | 0.00000000 |
| I | 0x070f...fc9 | 0.00000000 |
| J | 0x4d96...f54 | 0.00000000 |
| K | 0xa732...dc4 | 0.00000000 |
| L | 0x7c2e...ba9 | 0.00000000 |
| M | 0x6fed...2e9 | 0.00000000 |
| N | 0xe7dd...b2c | 0.00000000 |
| O | 0x7325...89d | 0.00000000 |
| P | 0x6218...948 | 0.00000000 |
| Q | 0xac40...9a9 | 0.00000000 |
| R | 0x7ce6...e10 | 0.00000000 |
| S | 0xb875...386 | 0.00000000 |
| T | 0x3578...588 | 0.00000000 |
| U | 0x7586...956 | 0.00000000 |
| V | 0xb59d...2c3 | 0.00000000 |
| W | 0x5f32...7b0 | 0.00000000 |
| X | 0xa95c...47d | 0.00000000 |
| Y | 0xd8e3...4c4 | 0.00000000 |
| Z | 0x7af0...97c | 0.00000000 |

### Multisig Contract Probes — 5/5 HEALTHY

All contracts respond to `0x1::multisig_account::num_signatures_required` and require 2 signers.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2-of-N | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2-of-N | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2-of-N | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2-of-N | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2-of-N | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is a Next.js SPA with client-side routing. Paths `/api/markets` and `/api/v1/markets` return HTML, not JSON. No market data extractable. Recorded as N/A in `mnx_snapshots`.

---

## DuckDB Schema

```sql
world_increments   -- 81 rows: GF(3) color-chained repo push events
repo_snapshots     -- 81 rows: org/user, name, lang, stars, forks, pushed_at
aptos_snapshots    -- 28 rows: alice/bob/A-Z wallet balances (all 0 APT)
multisig_probes    --  5 rows: A-B/A-G/Y-Z/S-T/V-W (all 2-of-N, healthy)
mnx_snapshots      --  1 row:  N/A (SPA, no API)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
