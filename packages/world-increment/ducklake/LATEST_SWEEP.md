# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-04

## Sweep Metadata
- **Date:** 2026-08-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| World Increments (this run) | 68 |
| Repo Snapshots (cumulative) | 989 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | SPA-only (unavailable) |

---

## GF(3) Color Chain

- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**

---

## JOB 1: GitHub Social Graph Sweep

### plurigrid (30+ repos)
| Repo | Language | Stars | Open Issues | Last Push |
|------|----------|-------|-------------|-----------|
| gorj | Clojure | 1 | 1616 | 2026-08-04 |
| eirobri | Clojure | 0 | 31 | 2026-08-04 |
| place | TeX | 1 | 15 | 2026-08-02 |
| zig-syrup | Zig | 2 | 0 | 2026-07-28 |
| asi | HTML | 58 | 4 | 2026-07-10 |
| nanoclj-zig | Zig | 1 | 20 | 2026-04-25 |
| asi-skills | Julia | 3 | 0 | 2026-04-26 |
| nash-portal | Rust | 2 | 1 | 2026-05-19 |

Notable: gorj has 1616 open issues (active dev); asi now at 58★ (↑ from 16★ in April).

### kubeflow (49 repos)
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow | — | 15804 | 2026-08-03 |
| pipelines | Python | 4174 | 2026-08-04 |
| spark-operator | Python | 3143 | 2026-08-04 |
| trainer | Go | 2165 | 2026-07-31 |
| katib | Python | 1694 | 2026-08-01 |
| community-distribution | YAML | 1029 | 2026-07-29 |
| mcp-apache-spark-history-server | Python | 185 | 2026-08-01 |
| hub | Go | 180 | 2026-08-03 |
| sdk | Python | 132 | 2026-08-04 |
| mcp-server | Python | 31 | 2026-08-03 |

Notable: kubeflow/kubeflow now 15804★ (↑239 since April). Two active MCP servers.

### TeglonLabs (5 repos)
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

Low activity; significant reduction from 53→5 publicly indexed repos since April sweep.

### bmorphism (106 repos)
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-08-02 |
| Gay.jl | Julia | 2 | 2026-07-21 |
| gay-chat | Scheme | 0 | 2026-07-14 |
| satreadout | HTML | 0 | 2026-06-20 |
| flox-mcp-bb | Clojure | 0 | 2026-06-05 |
| open-location-code-zig | Zig | 3 | 2026-03-24 |

Most recent: anti-bullshit-mcp-server (23★, pushed 2026-08-02).

### zubyul (49 repos)
Most recent: voice-observatory + ghostel-emacs-worlds (2026-04-24); activity quieter since then.

### Social Graph (migalkin, wasita, AustinCStone)
| User | Notable Repos | Last Push |
|------|--------------|-----------|
| migalkin | NodePiece 144★, StarE 89★, kgcourse2021 | 2026-07-10 |
| wasita | joint-planning-lit (new!), wasita.github.io | 2026-08-04 |
| AustinCStone | byteruckus (HTML), EpsteinSearch | 2026-07-15 |

Highlight: wasita just created `joint-planning-lit` on 2026-08-04 (today).

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets queried at 2026-08-04. **Total swarm APT: 0.0**

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793ac... | 0.0 |
| bob   | 0x0a3c00... | 0.0 |
| A–Z   | 26 wallets      | 0.0 each |

CoinStore resources returned 0 for all addresses. Wallets appear unfunded on mainnet.

### Multisig Contract Probes (Aptos Mainnet)

All 5 contracts healthy, all require 2-of-2 signatures:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe1... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3a... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7... | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: SPA-only — market data unavailable via REST**  
The endpoint returns a Next.js SPA. No `/api/markets` or `/api/v1/markets` routes are accessible without a browser runtime. Recorded as unavailable marker in `mnx_snapshots`.

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

## Notable Highlights
- **plurigrid/gorj**: 1616 open issues — highly active
- **plurigrid/asi**: 58★ (↑ from 16★ April sweep, +262%)
- **kubeflow/kubeflow**: 15804★ (↑239 since April)
- **wasita**: Created `joint-planning-lit` today (2026-08-04)
- **All 5 multisig contracts**: Healthy, 2-of-2 sigs required
- **Hamming swarm**: 28 wallets all at 0.0 APT on mainnet
