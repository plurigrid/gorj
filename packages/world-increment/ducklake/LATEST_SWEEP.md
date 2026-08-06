# World-Increment Sweep — 2026-08-06

## Sweep Metadata
- **Date:** 2026-08-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GitHub scope:** plurigrid org (MCP-scoped; other orgs/users from prior sweep retained)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 14 |
| Total Repo Snapshots (cumulative) | 994 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| New GF(3) Increments This Run | 2 |

---

## GF(3) Color Chain — This Run (Increments 13–14)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | hamming_swarm | aptos_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain continues: `…ERGODIC → PLUS → MINUS`

---

## GitHub Sweep — plurigrid (50 repos)

### Top by Stars
| Repo | Language | Stars | Forks | Pushed At |
|------|----------|-------|-------|-----------|
| asi | HTML | 59 | 13 | 2026-07-10 |
| ontology | JavaScript | 8 | 9 | 2025-05-27 |
| asi-skills | Julia | 3 | 0 | 2026-04-26 |
| Plurigraph | JavaScript | 3 | 5 | 2025-01-05 |
| act | Python | 3 | 1 | 2024-07-26 |

### Most Recently Pushed
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 1 | 2026-08-06 |
| eirobri | Clojure | 0 | 2026-08-04 |
| place | TeX | 1 | 2026-08-02 |
| zig-syrup | Zig | 2 | 2026-07-28 |
| asi | HTML | 59 | 2026-07-10 |

**Notable:** plurigrid/gorj has 1,660 open issues and was pushed 2026-08-06. plurigrid/asi jumped to 59 stars (was 16 in April).

---

## Hamming Swarm — Aptos Wallet Snapshot

**Total APT across 28 wallets:** 20.344773 APT

| Rank | World | APT Balance | Address (short) |
|------|-------|-------------|-----------------|
| 1 | bob | 12.65700700 | `0x0a3c00c5...512d5d` |
| 2 | F | 1.96051600 | `0x18a14b5b...c3cf71` |
| 3 | L | 1.92726900 | `0x7c2eaeaf...37eba9` |
| 4 | J | 1.89509300 | `0x4d964db8...e87f54` |
| 5 | alice | 0.43643352 | `0xc793acde...24cc7b` |
| 6 | O | 0.21013600 | `0x73252b60...25a89d` |
| 7 | K | 0.16196100 | `0xa732040a...425dc4` |
| 8 | P | 0.14013600 | `0x6218792d...1ec948` |
| 9 | M | 0.11228500 | `0x6fed37a7...b7f2e9` |
| 10 | N | 0.10612100 | `0xe7dde6da...551b2c` |
| 11 | Q | 0.10324000 | `0xac40fa50...5c89a9` |
| 12 | S | 0.09178800 | `0xb8753014...9d0386` |
| 13 | R | 0.09021700 | `0x7ce605cc...d76e10` |
| 14 | T | 0.07371300 | `0x35781dc0...3f4588` |
| 15 | U | 0.05577300 | `0x75860da4...ef9956` |
| 16 | A | 0.05176700 | `0x8699edc0...be9d7a` |
| 17 | V | 0.04883299 | `0xb59dd817...9af2c3` |
| 18 | Y | 0.04444900 | `0xd8e32848...2444c4` |
| 19 | X | 0.04257700 | `0xa95cbbd1...33047d` |
| 20 | W | 0.04070500 | `0x5f32aef7...ccc7b0` |
| 21 | B | 0.03625600 | `0x3f892ebe...77cb13` |
| 22 | Z | 0.02426800 | `0x7af0ef6e...4e197c` |
| 23 | D | 0.01162900 | `0xf7765624...fcfdd1` |
| 24 | C | 0.01018500 | `0x38b99e63...91535e` |
| 25 | E | 0.00937200 | `0xdc1d9d53...958d36` |
| 26 | H | 0.00168100 | `0xce67c327...e5300f` |
| 27 | G | 0.00068100 | `0x69a394c0...cc7f32` |
| 28 | I | 0.00068100 | `0x070fe5d7...0c1fc9` |

**Observations:**
- `bob` dominates with **12.6570 APT** — 10× larger than next
- `F`, `L`, `J` each hold ~1.9 APT — likely active operational wallets
- `G`, `I` near-empty (0.00068 APT) — dust/inactive
- `alice` holds 0.436 APT — contract/module account with multiverse::MultiverseState

---

## Multisig Probes

All 5 multisig contracts are **healthy** — each requires exactly 2 signatures.

| Pair | Address (short) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | `0x0da4f428...7003` | 2 | ✅ HEALTHY |
| A-G | `0xf56c4a1c...0096` | 2 | ✅ HEALTHY |
| Y-Z | `0xd3ffe181...b883` | 2 | ✅ HEALTHY |
| S-T | `0x3b1c3ae9...7883` | 2 | ✅ HEALTHY |
| V-W | `0x40fad7b4...eb6d` | 2 | ✅ HEALTHY |

---

## MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — site is a Next.js SPA; no public REST API endpoints found. All paths (/api/markets, /api/tickers, /markets, etc.) return the client-side HTML shell. Market data requires browser-side JS execution.

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
