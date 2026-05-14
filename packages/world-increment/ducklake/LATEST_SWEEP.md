# World-Increment Sweep — 2026-05-14

## Sweep Metadata
- **Date:** 2026-05-14 ~12:20 UTC
- **Agent:** world-increment-sweep (autonomous)
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 0 (GitHub API rate-limited, unauthenticated) |
| Sources Attempted | 3 orgs + 8 users |
| Aptos Wallets Snapshotted | 28 (alice, bob, A-Z) |
| Multisig Probes | 5 (all healthy) |

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

Color distribution: PLUS=4 (ids 1,4,7,10), MINUS=4 (ids 2,5,8,11), ERGODIC=3 (ids 3,6,9)

---

## GitHub Sources (Rate-Limited)

The unauthenticated GitHub API rate limit (60 req/hour) was exhausted before data could be fetched.
No `GH_TOKEN` or `gh` CLI auth was available in this environment.
The previous sweep (2026-04-12) data from world-increments.duckdb is preserved.

**Previous sweep top repos (from 2026-04-12 data):**

### plurigrid (100 repos previously)
| Repo | Language | Stars |
|------|----------|-------|
| asi | HTML | 16 |
| ontology | JavaScript | 7 |
| asi-skills | Julia | 3 |
| zig-syrup | Zig | 2 |
| vivarium | Clojure | 1 |

### kubeflow (47 repos previously)
| Repo | Language | Stars |
|------|----------|-------|
| kubeflow | — | 15565 |
| pipelines | Python | 4119 |
| spark-operator | Python | 3111 |
| trainer | Go | 2080 |
| katib | Python | 1676 |

### TeglonLabs (53 repos previously)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos previously)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos previously)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-05-14)

Fetched via `0x1::coin::balance` view function. 1s sleep between calls.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.43643352 |
| bob   | 0x0a3c...2d5d | 12.657007 |
| A | 0x8699...9d7a | 0.051767 |
| B | 0x3f89...b13 | 0.036256 |
| C | 0x38b9...35e | 0.010185 |
| D | 0xf776...dd1 | 0.011629 |
| E | 0xdc1d...d36 | 0.009372 |
| F | 0x18a1...f71 | 1.960516 |
| G | 0x69a3...f32 | 0.000681 |
| H | 0xce67...00f | 0.001681 |
| I | 0x070f...fc9 | 0.000681 |
| J | 0x4d96...f54 | 1.895093 |
| K | 0xa732...dc4 | 0.161961 |
| L | 0x7c2e...ba9 | 1.927269 |
| M | 0x6fed...2e9 | 0.112285 |
| N | 0xe7dd...b2c | 0.106121 |
| O | 0x7325...89d | 0.210136 |
| P | 0x6218...948 | 0.140136 |
| Q | 0xac40...a9 | 0.10324 |
| R | 0x7ce6...e10 | 0.090217 |
| S | 0xb875...386 | 0.091788 |
| T | 0x3578...588 | 0.073713 |
| U | 0x7586...956 | 0.055773 |
| V | 0xb59d...2c3 | 0.04883299 |
| W | 0x5f32...7b0 | 0.040705 |
| X | 0xa95c...47d | 0.042577 |
| Y | 0xd8e3...4c4 | 0.044449 |
| Z | 0x7af0...97c | 0.024268 |

Notable: `bob` leads at 12.657 APT. `F` (1.961), `L` (1.927), `J` (1.895) are next. Most addresses hold dust amounts.

### Multisig Probe Results

All probed via `0x1::multisig_account::num_signatures_required` view function.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | true |
| A-G | 0xf56c...096 | 2 | true |
| Y-Z | 0xd3ff...883 | 2 | true |
| S-T | 0x3b1c...883 | 2 | true |
| V-W | 0x40fa...b6d | 2 | true |

All 5 multisig accounts are healthy and require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

All three endpoints probed:
- `https://testnet.mnx.fi/api/markets` — returns Next.js SPA HTML (no JSON)
- `https://testnet.mnx.fi/api/v1/markets` — returns Next.js SPA HTML (no JSON)
- `https://testnet.mnx.fi/api/tickers` — returns Next.js SPA HTML (no JSON)

**MNX market data unavailable** — site is a client-rendered SPA with no public REST API endpoints. No rows inserted into `mnx_snapshots`.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
