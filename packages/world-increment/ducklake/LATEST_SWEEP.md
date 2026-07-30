# World-Increment Sweep — 2026-07-30 (+ Hamming Swarm Snapshot)

## Sweep Metadata
- **Date:** 2026-07-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (This Sweep)

| Metric | Value |
|--------|-------|
| World Increments Added | 8 |
| Repo Snapshots Added | 55 |
| Sources Covered | 3 orgs + 5 users + 3 social graph |
| Total DB World Increments | 31 |
| Total DB Repo Snapshots | 999 |
| Aptos Wallets Probed | 28 (A–Z + alice + bob) |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — This Sweep (8 Increments)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 1 | plurigrid (org) | 1 | `#b8bb26` | **PLUS** |
| 2 | kubeflow (org) | 2 | `#cc241d` | **MINUS** |
| 3 | TeglonLabs (org) | 0 | `#d3869b` | **ERGODIC** |
| 4 | bmorphism (user) | 1 | `#b8bb26` | **PLUS** |
| 5 | zubyul (user) | 2 | `#cc241d` | **MINUS** |
| 6 | migalkin (user) | 0 | `#d3869b` | **ERGODIC** |
| 7 | wasita (user) | 1 | `#b8bb26` | **PLUS** |
| 8 | AustinCStone (user) | 2 | `#cc241d` | **MINUS** |

---

## Top Repos by Source

### plurigrid (103 repos, +3 since Apr sweep)
| Repo | Language | Stars | Pushed At | Note |
|------|----------|-------|-----------|------|
| gorj | Clojure | 1 | **2026-07-30** | This repo — active today! |
| zig-syrup | Zig | 2 | 2026-07-28 | OCapN Syrup + CapTP |
| asi | HTML | 55 | 2026-07-10 | +39★ since Apr |
| place | TeX | 1 | 2026-07-14 | |
| eirobri | Clojure | 0 | 2026-07-21 | EiRoBri replay world |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| pipelines | Python | 4171 | 2026-07-29 |
| spark-operator | Python | 3142 | 2026-07-29 |
| trainer | Go | 2162 | 2026-07-29 |
| katib | Python | 1694 | 2026-07-26 |
| mcp-server | Python | 31 | 2026-07-28 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JS | 0 | 2025-09-21 |

### bmorphism (106 repos, +6 since Apr)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | 2026-07-29 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JS | 22 | 2026-01-16 |

### Social Graph (zubyul connections)
| User | Repos | Notable |
|------|-------|---------|
| migalkin | 19 | NodePiece 144★ (ICLR'22), StarE 89★ (EMNLP'20) |
| wasita | 12 | Personal site active 2026-07-21, pnas-typst-template |
| DJedamski | 6 | Stats/ML background, last active 2018 |
| kristinezheng | 5 | Cognitive sci / MIT, active 2026-07 |
| M1shaaa | 8 | Yale psych / Lookit research, active 2026-02 |
| AustinCStone | 41 | TextGAN 92★, byteruckus active 2026-07 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 26 Hamming swarm nodes (A–Z) plus alice and bob probed via Aptos mainnet fullnode.

**All 28 wallets returned 0.0 APT.**

The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource is absent or returns zero balance for all probed addresses. Wallets may be on-chain but unfunded on mainnet.

### Multisig Contract Probes (5 pairs)

Probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428...87003 | **2** | ✅ |
| A-G | 0xf56c4a1c...0096 | **2** | ✅ |
| Y-Z | 0xd3ffe181...b883 | **2** | ✅ |
| S-T | 0x3b1c3ae9...7883 | **2** | ✅ |
| V-W | 0x40fad7b4...eb6d | **2** | ✅ |

**All 5 multisig accounts healthy — all require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi/api/markets` → HTTP 404  
Root SPA at `https://testnet.mnx.fi` → serves shell only, no extractable data  
**Status: UNAVAILABLE** — testnet appears offline or API paths changed.

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
- `id mod 3 == 2` → trit=2(-1), color=#cc241d, name=MINUS

## Notable Highlights This Sweep
- **plurigrid/gorj** pushed **today** (2026-07-30) — sweep catches live activity
- **plurigrid/asi**: 55★ (+39 since the Apr-12 sweep)
- **kubeflow/pipelines**: 4171★ (+52 since Apr) — pushed yesterday
- **bmorphism/Gay.jl** pushed 2026-07-29 — active development
- **All 5 Hamming multisigs healthy** with sigs_required=2
- **MNX testnet unavailable** — API 404 on all probed paths
