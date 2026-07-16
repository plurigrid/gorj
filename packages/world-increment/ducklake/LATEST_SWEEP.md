# World-Increment Sweep — 2026-07-16

## Sweep Metadata
- **Date:** 2026-07-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 (id 1–13 distinct; max_id=13) |
| Total Repo Snapshots | 945 |
| Sources Covered | plurigrid/gorj (proxy-scoped; social graph blocked) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (A-B, A-G, Y-Z, S-T, V-W) |
| MNX Markets | Unavailable (Vercel auth) |

---

## GF(3) Color Chain — Current Increment

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | gorj (self) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |
| **13** | **plurigrid/gorj** | **sweep_complete** | **+1** | **`#b8bb26`** | **PLUS** ← current |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## GitHub Social Graph Sweep

### Access Constraints
The GitHub API in this environment is proxy-scoped to repository endpoints only (`repos/{owner}/{repo}/...`).
Org-level and user-level listing endpoints (`/orgs/{org}/repos`, `/users/{user}/repos`, `/users/{user}/events/public`) returned 403 errors.
Only **plurigrid/gorj** was accessible via the GitHub MCP server.

### plurigrid/gorj (accessible via MCP)
- **Latest commit:** `5b28fe0` — `chore: ignore duckdb binary in repo root` (2026-05-08, by Claude)
- **Total branches:** 50+ active `world-increment/sweep-*` branches (last: `sweep-2026-05-02-1318`)
- **Last sweep branch date:** 2026-05-02 (gap of ~75 days to today's sweep)
- **All commits by:** `claude` (automated sweeps since 2026-03-30)
- **Language:** Clojure

### Social Graph Targets (blocked by proxy)
The following were attempted but returned 403 from the GitHub proxy:
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Users:** bmorphism, zubyul
- **Social graph:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

Previous sweep data (2026-04-12) for these sources remains in `repo_snapshots` (944 rows from prior runs).

---

## Hamming Swarm — Aptos Wallet Snapshot

All 28 wallets probed against `fullnode.mainnet.aptoslabs.com` (ledger ~6,305,656,941).
**Result:** All wallets return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
Wallets exist on-chain but hold no APT in the standard CoinStore at this ledger version.

| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|---------------|--------|
| alice | 0xc793ac...cc7b | 0.0 | resource_not_found |
| bob   | 0x0a3c00...512d | 0.0 | resource_not_found |
| A     | 0x8699ed...e9d7a | 0.0 | resource_not_found |
| B     | 0x3f892e...cb13 | 0.0 | resource_not_found |
| C     | 0x38b99e...535e | 0.0 | resource_not_found |
| D     | 0xf77656...fdd1 | 0.0 | resource_not_found |
| E     | 0xdc1d9d...8d36 | 0.0 | resource_not_found |
| F     | 0x18a14b...f71 | 0.0 | resource_not_found |
| G     | 0x69a394...f32 | 0.0 | resource_not_found |
| H     | 0xce67c3...300f | 0.0 | resource_not_found |
| I     | 0x070fe5...fc9 | 0.0 | resource_not_found |
| J     | 0x4d964d...f54 | 0.0 | resource_not_found |
| K     | 0xa73204...dc4 | 0.0 | resource_not_found |
| L     | 0x7c2eae...ba9 | 0.0 | resource_not_found |
| M     | 0x6fed37...f2e9 | 0.0 | resource_not_found |
| N     | 0xe7dde6...1b2c | 0.0 | resource_not_found |
| O     | 0x73252b...a89d | 0.0 | resource_not_found |
| P     | 0x621879...c948 | 0.0 | resource_not_found |
| Q     | 0xac40fa...c89a9 | 0.0 | resource_not_found |
| R     | 0x7ce605...6e10 | 0.0 | resource_not_found |
| S     | 0xb87530...d386 | 0.0 | resource_not_found |
| T     | 0x35781d...f588 | 0.0 | resource_not_found |
| U     | 0x75860d...f956 | 0.0 | resource_not_found |
| V     | 0xb59dd8...f2c3 | 0.0 | resource_not_found |
| W     | 0x5f32ae...c7b0 | 0.0 | resource_not_found |
| X     | 0xa95cbb...047d | 0.0 | resource_not_found |
| Y     | 0xd8e328...44c4 | 0.0 | resource_not_found |
| Z     | 0x7af0ef...97c | 0.0 | resource_not_found |

---

## Multisig Contract Probes

All 5 probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f4...7003 | 2 | ✓ |
| A-G | 0xf56c4a...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1...b883 | 2 | ✓ |
| S-T | 0x3b1c3a...7883 | 2 | ✓ |
| V-W | 0x40fad7...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy. All require 2-of-N signatures.**

---

## MNX Markets

`https://testnet.mnx.fi` requires Vercel deployment authentication (visitor password or SSO).
No market data available. `mnx_snapshots` table has 0 rows.

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
- **Increment 13:** PLUS — 5th GF(3) cycle entry, sweep of plurigrid/gorj
- **plurigrid/gorj:** 75-day gap since last world-increment sweep (last: 2026-05-02); master updated 2026-05-08
- **Multisig health:** All 5 Hamming-swarm multisig pairs respond with 2-of-N — no degradation
- **Aptos balances:** All 28 Hamming-swarm wallets show 0 APT (CoinStore resource absent)
- **Proxy constraint:** Social graph (kubeflow, TeglonLabs, bmorphism et al.) inaccessible; prior sweep data still in DB
- **MNX Markets:** Vercel-auth-gated; monitoring not possible without credentials
