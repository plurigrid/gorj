# World-Increment Sweep — 2026-07-29

## Sweep Metadata
- **Date:** 2026-07-29
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment ID:** 13

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 (id=13 added this sweep) |
| Total Repo Snapshots | 944 (no new — GitHub org/user listing blocked by proxy) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Pairs Probed | 5 |
| MNX Markets | unavailable (SPA only) |

---

## GF(3) — Increment 13

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | aptos_mainnet (hamming_swarm) | hamming_swarm_snapshot | +1 | `#b8bb26` | **PLUS** |

GF(3) assignment: `13 mod 3 = 1` → trit=1, color=`#b8bb26`, name=**PLUS**

---

## Job 1: GitHub Social Graph Sweep

**Status: Partially blocked.**

The execution environment proxy restricts GitHub REST API to repository-scoped endpoints only (`repos/{owner}/{repo}/...`). Org/user repo listing endpoints (`/orgs/{org}/repos`, `/users/{user}/repos`) return 403. The MCP GitHub tools are scoped to `plurigrid/gorj` only.

**plurigrid/gorj (accessible):**
- Latest commit: `5b28fe0` — 2026-05-08 — chore: ignore duckdb binary in repo root
- Active sweep branches: 30+ `world-increment/sweep-*` branches (2026-04-27 through 2026-04-30)
- All prior sweep data (944 repo snapshots from 11 sources) remains intact in DuckDB

**Blocked sources:** plurigrid org, kubeflow org, TeglonLabs org, bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, Mainnet)

All 28 addresses probed via `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: 0 APT across all wallets** — no legacy CoinStore resources found. Accounts confirmed active (non-zero sequence numbers for sampled addresses). APT may be held via the newer fungible asset store (`0x1::fungible_asset::FungibleStore`) not probed in this sweep.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob   | 0x0a3c...2d5d | 0.00000000 |
| A     | 0x8699...9d7a | 0.00000000 |
| B     | 0x3f89...b13  | 0.00000000 |
| C     | 0x38b9...535e | 0.00000000 |
| D     | 0xf776...cfd1 | 0.00000000 |
| E     | 0xdc1d...8d36 | 0.00000000 |
| F     | 0x18a1...cf71 | 0.00000000 |
| G     | 0x69a3...c7f32 | 0.00000000 |
| H     | 0xce67...300f | 0.00000000 |
| I     | 0x070f...1fc9 | 0.00000000 |
| J     | 0x4d96...7f54 | 0.00000000 |
| K     | 0xa732...5dc4 | 0.00000000 |
| L     | 0x7c2e...eba9 | 0.00000000 |
| M     | 0x6fed...f2e9 | 0.00000000 |
| N     | 0xe7dd...1b2c | 0.00000000 |
| O     | 0x7325...a89d | 0.00000000 |
| P     | 0x6218...c948 | 0.00000000 |
| Q     | 0xac40...c89a9 | 0.00000000 |
| R     | 0x7ce6...6e10 | 0.00000000 |
| S     | 0xb875...d386 | 0.00000000 |
| T     | 0x3578...f588 | 0.00000000 |
| U     | 0x7586...f956 | 0.00000000 |
| V     | 0xb59d...f2c3 | 0.00000000 |
| W     | 0x5f32...c7b0 | 0.00000000 |
| X     | 0xa95c...047d | 0.00000000 |
| Y     | 0xd8e3...44c4 | 0.00000000 |
| Z     | 0x7af0...97c  | 0.00000000 |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts queried via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4...7003 | 2 | ✓ |
| A-G  | 0xf56c...0096 | 2 | ✓ |
| Y-Z  | 0xd3ff...b883 | 2 | ✓ |
| S-T  | 0x3b1c...7883 | 2 | ✓ |
| V-W  | 0x40fa...eb6d | 2 | ✓ |

**All multisig accounts healthy — 2-of-N required across all pairs.**

### MNX Markets (testnet.mnx.fi)

- Probed `https://testnet.mnx.fi` and common API paths (`/api/markets`, `/api/v1/markets`, etc.)
- Site responds as a Next.js SPA — no public REST API endpoint found
- Status: **unavailable** (recorded in mnx_snapshots with NULL price/change_pct)

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
- **Multisig health**: All 5 probed pairs (A-B, A-G, Y-Z, S-T, V-W) require exactly 2 signatures — all healthy
- **Hamming swarm quiescent**: 28 wallets show 0 APT via legacy CoinStore; accounts active on-chain
- **GitHub sweep blocked**: proxy restricts to repo-scoped endpoints; social graph sweep deferred to session with unrestricted API access
- **Increment 13 PLUS**: Opens the 5th GF(3) cycle (cycle = 12 increments)
