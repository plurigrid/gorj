# World-Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-07-12T12:15:01Z  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**World-increment records:** 67 (GF3 color chain: ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d)

---

## Sweep Metadata
- **Date:** 2026-07-12
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

**Status: BLOCKED — session proxy scope restriction**

The environment proxy enforces scope to `plurigrid/gorj` only. All cross-org and cross-user GitHub REST API calls return an auth error. Both `curl https://api.github.com/orgs/{org}/repos` and equivalent paths were blocked.

Attempted sources (all blocked):
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Users:** bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

All 11 sources recorded in `world_increments` with `event_type=repo_sweep_blocked`.

**Resolution:** Run sweep from a session not scoped to a single repo, or supply a GITHUB_TOKEN with `read:org` / `public_repo` scopes as an env var.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried via `POST /v1/view` with `0x1::coin::balance` (FA-compatible; legacy CoinStore not used).

| World | Address | APT Balance |
|-------|---------|-------------|
| bob   | 0x0a3c00c5… | **12.657007** |
| F     | 0x18a14b5b… | 1.960516 |
| L     | 0x7c2eaeaf… | 1.927269 |
| J     | 0x4d964db8… | 1.895093 |
| alice | 0xc793acde… | 0.436434 |
| O     | 0x73252b60… | 0.210136 |
| K     | 0xa732040a… | 0.161961 |
| P     | 0x62187920… | 0.140136 |
| M     | 0x6fed37a7… | 0.112285 |
| N     | 0xe7dde6da… | 0.106121 |
| Q     | 0xac40fa50… | 0.103240 |
| S     | 0xb8753014… | 0.091788 |
| R     | 0x7ce605cc… | 0.090217 |
| T     | 0x35781dc0… | 0.073713 |
| U     | 0x75860da4… | 0.055773 |
| A     | 0x8699edc0… | 0.051767 |
| V     | 0xb59dd817… | 0.048833 |
| Y     | 0xd8e32848… | 0.044449 |
| W     | 0x5f32aef7… | 0.040705 |
| X     | 0xa95cbbd1… | 0.042577 |
| B     | 0x3f892ebe… | 0.036256 |
| Z     | 0x7af0ef6e… | 0.024268 |
| D     | 0xf7765624… | 0.011629 |
| C     | 0x38b99e63… | 0.010185 |
| E     | 0xdc1d9d53… | 0.009372 |
| H     | 0xce67c327… | 0.001681 |
| G     | 0x69a394c0… | 0.000681 |
| I     | 0x070fe5d7… | 0.000681 |

**Total swarm APT:** 20.3448 APT  
**Richest:** bob (12.657 APT — 62.2% of swarm total)  
**Dustiest:** G, I (0.000681 APT each — minimum storage deposit)

### Multisig Contract Probes

| Pair | Address | sigs_required | Healthy |
|------|---------|---------------|---------|
| A-B  | 0x0da4f428… | 2 | ✓ |
| A-G  | 0xf56c4a1c… | 2 | ✓ |
| Y-Z  | 0xd3ffe181… | 2 | ✓ |
| S-T  | 0x3b1c3ae9… | 2 | ✓ |
| V-W  | 0x40fad7b4… | 2 | ✓ |

**All 5/5 multisig contracts healthy** — all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — site requires Vercel deployment authentication for all paths including `/api/markets` and `/api/v1/markets`. Recorded as `unavailable` in `mnx_snapshots`.

---

## DuckDB Schema

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

## Row Counts

| Table | Rows |
|-------|------|
| world_increments | 67 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable) |
| repo_snapshots | 0 (blocked) |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=**MINUS**

## Alerts
- **GitHub sweep blocked** (11 sources): Session proxy restricts to `plurigrid/gorj`. Re-run in broader-scope session.
- **MNX Markets inaccessible**: Vercel auth gate. No market data captured.
- **bob holds 62.2% of swarm APT**: Concentration risk if this is an operational hot wallet.
