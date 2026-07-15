# World-Increment Sweep — 2026-07-15

## Sweep Metadata
- **Date:** 2026-07-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (via pip)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| World Increments (this sweep) | 1 |
| Repo Snapshots (this sweep) | 0 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (Vercel auth required) |

---

## GF(3) Color Chain — This Sweep's 12 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 24  | world-increment-sweep (sweep) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `ERGODIC`

---

## Repo Counts by Source (This Sweep)

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| **TOTAL** | | **0** | | |

---

## Top Repos by Source (Stars)


---

## Most Recently Pushed Repos

| Full Name | Pushed At |
|-----------|-----------|

---

## Hamming Swarm — Aptos Snapshot

**API:** `fullnode.mainnet.aptoslabs.com/v1`
**Status:** All 28 addresses probed; `CoinStore<AptosCoin>` resource not found for any address
  (addresses are unregistered for legacy coin module — may use Fungible Asset standard instead)

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| Z | `0x7af0ef6e...4e197c` | NULL |
| Y | `0xd8e32848...2444c4` | NULL |
| X | `0xa95cbbd1...33047d` | NULL |
| W | `0x5f32aef7...ccc7b0` | NULL |
| V | `0xb59dd817...9af2c3` | NULL |
| U | `0x75860da4...ef9956` | NULL |
| T | `0x35781dc0...3f4588` | NULL |
| S | `0xb8753014...9d0386` | NULL |
| R | `0x7ce605cc...d76e10` | NULL |
| Q | `0xac40fa50...5c89a9` | NULL |
| P | `0x6218792d...1ec948` | NULL |
| O | `0x73252b60...25a89d` | NULL |
| N | `0xe7dde6da...551b2c` | NULL |
| M | `0x6fed37a7...b7f2e9` | NULL |
| L | `0x7c2eaeaf...37eba9` | NULL |
| K | `0xa732040a...425dc4` | NULL |
| J | `0x4d964db8...e87f54` | NULL |
| I | `0x070fe5d7...0c1fc9` | NULL |
| H | `0xce67c327...e5300f` | NULL |
| G | `0x69a394c0...cc7f32` | NULL |
| F | `0x18a14b5b...c3cf71` | NULL |
| E | `0xdc1d9d53...958d36` | NULL |
| D | `0xf7765624...fcfdd1` | NULL |
| C | `0x38b99e63...91535e` | NULL |
| B | `0x3f892ebe...77cb13` | NULL |
| A | `0x8699edc0...be9d7a` | NULL |
| bob | `0x0a3c00c5...512d5d` | NULL |
| alice | `0xc793acde...24cc7b` | NULL |

---

## Multisig Contract Probes

**Function:** `0x1::multisig_account::num_signatures_required`

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| V-W | `0x40fad7b4...80eb6d` | 2 | ✓ |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✓ |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✓ |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✓ |
| A-B | `0x0da4f428...987003` | 2 | ✓ |

---

## MNX Markets

**Status:** Unavailable — `testnet.mnx.fi` requires Vercel authentication (HTTP 401).
No market data could be extracted in this sweep.

---

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **M1shaaa/M1shaaa** profile repo: pushed 2026-07-15 (today!) — active
- **wasita/wasita.github.io**: pushed 2026-07-14 — very recent personal site update
- **kristinezheng/kristinezheng.github.io**: pushed 2026-07-01 — recent
- **TeglonLabs/jank-crane**: new C++ repo (crane-jank IR hub with GF3 convergence maps) — June 2026
- **All 5 multisig contracts**: healthy, require 2-of-N signatures
- **Hamming swarm (alice/bob/A–Z)**: APT CoinStore not registered on any address; may use FungibleAsset standard
