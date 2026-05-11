# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-11

## Sweep Metadata
- **Date:** 2026-05-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Ledger version (Aptos mainnet):** 5223277157

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this run) | 29 |
| Total Increments (cumulative) | 52 |
| Repo Snapshots Added | 19 (plurigrid) |
| Total Repo Snapshots (cumulative) | 963 |
| Sources Fully Snapshotted | 1 (plurigrid) |
| Sources Rate-Limited | 10 (kubeflow, TeglonLabs, bmorphism, zubyul + 6 social graph) |

**Note:** GitHub unauthenticated API rate limit (60 req/hr) was hit. Only `plurigrid` org data was retrieved via WebFetch cache. All other sources recorded as `rate_limited` increments.

---

### GF(3) Color Chain — New Increments (IDs 23–51)

Chain cycles: `ERGODIC(0) → PLUS(1) → MINUS(-1) → ...`

| ID Range | Source | Count | GF3 Distribution |
|----------|--------|-------|-----------------|
| 23–41 | plurigrid repos (org) | 19 | ERGODIC×6, PLUS×7, MINUS×6 |
| 42–51 | Rate-limited sources | 10 | ERGODIC×3, PLUS×3, MINUS×4 |

#### GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**

---

### plurigrid Org Snapshot (19 repos, sorted by push date)

| Repo | Language | Stars | Forks | Issues | Last Push |
|------|----------|-------|-------|--------|-----------|
| gorj | Clojure | 0 | 0 | 148 | 2026-05-11 |
| horse | TeX | 1 | 1 | 9 | 2026-05-07 |
| zig-syrup | Zig | 2 | 2 | 0 | 2026-04-30 |
| UnwiringDiagrams.jl | Julia | 1 | 0 | 0 | 2026-04-26 |
| asi | HTML | 21 | 5 | 4 | 2026-04-26 |
| nash-portal | Rust | 2 | 2 | 0 | 2026-04-26 |
| causal | Emacs Lisp | 0 | 0 | 0 | 2026-04-26 |
| asi-skills | Julia | 3 | 1 | 0 | 2026-04-26 |
| bci-blue-share | JavaScript | 0 | 0 | 0 | 2026-04-26 |
| nanoclj-zig | Zig | 1 | 2 | 20 | 2026-04-25 |
| spi-race | Swift | 0 | 0 | 0 | 2026-04-21 |
| brainmacs-skills | — | 0 | 0 | 0 | 2026-04-21 |
| reafference | HTML | 0 | 0 | 0 | 2026-04-16 |
| web-browser | Rust | 0 | 0 | 0 | 2026-04-10 |
| graywall | Go | 0 | 0 | 0 | 2026-04-10 |
| vivarium | Clojure | 1 | 0 | 0 | 2026-04-08 |
| flowglad-rs | Rust | 0 | 0 | 0 | 2026-04-08 |
| tree-sitter-nanoclj-zig | C | 0 | 0 | 0 | 2026-04-04 |
| gatomic | Clojure | 0 | 0 | 0 | 2026-03-30 |

**plurigrid totals:** 32 stars, 13 forks, 181 open issues across 19 repos

### Notable plurigrid Highlights
- **gorj**: 148 open issues — most active repo, forj + Rama topology nREPL routing + GF(3) trit coloring (pushed today)
- **asi**: 21 stars — "everything is topological chemputer!"
- **asi-skills**: 3 stars — 69 skills with Galois Hole Type accessibility
- **nanoclj-zig**: NaN-boxed Clojure interpreter with GF(3) trit conservation, 20 open issues

### Rate-Limited Sources
The following were attempted but returned 403 (unauthenticated rate limit):

| Source | Type | Status |
|--------|------|--------|
| kubeflow | org | rate_limited |
| TeglonLabs | org | rate_limited |
| bmorphism | user | rate_limited |
| zubyul | user | rate_limited |
| migalkin | user (social graph) | rate_limited |
| DJedamski | user (social graph) | rate_limited |
| wasita | user (social graph) | rate_limited |
| kristinezheng | user (social graph) | rate_limited |
| M1shaaa | user (social graph) | rate_limited |
| AustinCStone | user (social graph) | rate_limited |

*From previous sweep (2026-04-12): kubeflow had 47 repos (15,565⭐ flagship), TeglonLabs 53 repos, bmorphism 100 repos (60⭐ ocaml-mcp-sdk).*

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet — Wallet Balances

**Ledger version:** 5223277157 | **Timestamp:** 2026-05-11T12:36 UTC

All 28 Hamming swarm addresses (alice, bob, A–Z) returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — accounts exist on-chain but carry no funded APT CoinStore.

| World | Address (truncated) | Balance (APT) | Status |
|-------|--------------------|--------------:|--------|
| alice | 0xc793…cc7b | 0.0 | no CoinStore |
| bob | 0x0a3c…2d5d | 0.0 | no CoinStore |
| A | 0x8699…9d7a | 0.0 | no CoinStore |
| B | 0x3f89…b13 | 0.0 | no CoinStore |
| C | 0x38b9…535e | 0.0 | no CoinStore |
| D | 0xf776…fdd1 | 0.0 | no CoinStore |
| E | 0xdc1d…8d36 | 0.0 | no CoinStore |
| F | 0x18a1…f71 | 0.0 | no CoinStore |
| G | 0x69a3…7f32 | 0.0 | no CoinStore |
| H | 0xce67…300f | 0.0 | no CoinStore |
| I | 0x070f…1fc9 | 0.0 | no CoinStore |
| J | 0x4d96…7f54 | 0.0 | no CoinStore |
| K | 0xa732…5dc4 | 0.0 | no CoinStore |
| L | 0x7c2e…ba9 | 0.0 | no CoinStore |
| M | 0x6fed…2e9 | 0.0 | no CoinStore |
| N | 0xe7dd…1b2c | 0.0 | no CoinStore |
| O | 0x7325…89d | 0.0 | no CoinStore |
| P | 0x6218…c948 | 0.0 | no CoinStore |
| Q | 0xac40…89a9 | 0.0 | no CoinStore |
| R | 0x7ce6…6e10 | 0.0 | no CoinStore |
| S | 0xb875…0386 | 0.0 | no CoinStore |
| T | 0x3578…4588 | 0.0 | no CoinStore |
| U | 0x7586…f956 | 0.0 | no CoinStore |
| V | 0xb59d…f2c3 | 0.0 | no CoinStore |
| W | 0x5f32…7b0 | 0.0 | no CoinStore |
| X | 0xa95c…047d | 0.0 | no CoinStore |
| Y | 0xd8e3…44c4 | 0.0 | no CoinStore |
| Z | 0x7af0…197c | 0.0 | no CoinStore |

**Total swarm APT:** 0.0 (all unfunded)

---

### Multisig Contract Probes — 5/5 Healthy ✓

All probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|--------------------|--------------:|---------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

All multisig accounts operate as **2-of-2** threshold. No degraded contracts detected.

---

### MNX Testnet Markets

`https://testnet.mnx.fi` — **Unavailable as data source**

Site is a Next.js SPA. All paths (`/`, `/api/markets`, `/api/v1/markets`, `/api/tickers`) return rendered HTML. No public REST/JSON market API was detected. Data recorded as `N/A` in `mnx_snapshots`.

---

## DuckDB Schema (ducklake)

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

## Cumulative DB State

| Table | Row Count |
|-------|-----------|
| world_increments | 52 |
| repo_snapshots | 963 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |
