# World-Increment Sweep — 2026-04-30

## Sweep Metadata
- **Date:** 2026-04-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.2.1 (Muddy Duck)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 26 (max id=14) |
| Total Repo Snapshots | 945 |
| Aptos Wallets Snapshotted | 28 |
| Multisig Contracts Probed | 5 |
| MNX Market Entries | 0 (SPA, no JSON API) |
| GitHub API Status | Rate limited (0/60 remaining) |

---

## GF(3) Color Chain — New Increments This Sweep

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (org) | sweep_start (gorj) | +1 | `#b8bb26` | **PLUS** |
| 13 | github-api (meta) | rate_limited | +1 | `#b8bb26` | **PLUS** |
| 14 | world-increment-sweep | sweep_complete | -1 | `#cc241d` | **MINUS** |

Cumulative GF(3) chain from id=1: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## GitHub Social Graph Sweep

**Status:** GitHub API rate limited (0/60 remaining) — unauthenticated quota exhausted.

**Branch inventory (plurigrid/gorj via MCP):** 21 sweep branches active
| Branch | SHA |
|--------|-----|
| master | ebf263f5 |
| world-increment/sweep-2026-04-30-0712 | 096d37f7 |
| world-increment/sweep-2026-04-30-0531 | f8d4c526 |
| world-increment/sweep-2026-04-29-1316 | 007a3543 |
| world-increment/sweep-2026-04-29-1238 | 4ca72834 |
| ... (16 more sweep branches) | |

**Latest commit on master:** `ebf263f5` — "world-increment ducklake: sync world.duckdb sweep state" (2026-04-14T18:07:20Z)

**Repo snapshot added (MCP-sourced):**
| Repo | Language | Pushed At | Description |
|------|----------|-----------|-------------|
| plurigrid/gorj | Clojure | 2026-04-14 | MCP server + hooks that give AI coding agents a Clojure REPL |

**Sources rate-limited this sweep (no new snapshots):**
- Orgs: plurigrid, kubeflow, TeglonLabs
- Users: bmorphism, zubyul
- Social graph: migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

---

## Hamming Swarm — Aptos Snapshot (2026-04-30)

All 28 wallets queried via `fullnode.mainnet.aptoslabs.com`.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A | 0x8699...d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Note:** All balances 0.0 APT — CoinStore resources not initialized or accounts unfunded on mainnet.

---

## Multisig Contract Probes (2026-04-30)

All 5 multisig contracts healthy — 2-of-N threshold confirmed via `/v1/view`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

**5/5 multisig contracts healthy with 2-of-N threshold.**

---

## MNX Markets (testnet.mnx.fi)

**Status:** SPA (Next.js) — no JSON API endpoints accessible. Root serves HTML bundle only. No market data inserted.

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

## Previous Sweep Highlights (retained)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP using oxcaml_effect
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer

## This Sweep Highlights
- **Hamming swarm (A-Z + alice + bob)**: 28 addresses snapshotted, all show 0 APT
- **Multisig quorum**: A-B, A-G, Y-Z, S-T, V-W all require 2 signatures — swarm intact
- **gorj branches**: 21 active sweep branches on plurigrid/gorj
- **Increment 14**: MINUS — sweep_complete, closing 5th partial GF(3) cycle
