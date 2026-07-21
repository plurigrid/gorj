# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-21

## Sweep Metadata
- **Date:** 2026-07-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (This Run)

| Metric | Value |
|--------|-------|
| New World Increments | 121 |
| Cumulative Repo Snapshots | 1,042 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 pairs |
| MNX Markets | Auth-blocked |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — New Increments

GF(3) assignment: `id mod 3 == 0` → ERGODIC `#d3869b` | `id mod 3 == 1` → PLUS `#b8bb26` | `id mod 3 == 2` → MINUS `#cc241d`

**This run:** 39 ERGODIC | 41 PLUS | 41 MINUS (121 total new increments)

### Top Repos by Source (2026-07-21 snapshot)

#### plurigrid (50 repos, last pushed 2026-07-21)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-17 |
| gorj | Clojure | 1 | 2026-07-07 |
| shrimp | — | 0 | 2026-07-03 |
| place | TeX | 1 | 2026-06-27 |

#### kubeflow (49 repos, most active today)
| Repo | Language | Stars | Updated |
|------|----------|-------|---------|
| kubeflow | — | 15,789 | 2026-07-21 |
| pipelines | Python | 4,168 | 2026-07-21 16:28 UTC |
| spark-operator | Python | 3,142 | 2026-07-21 |
| trainer | Go | 2,152 | 2026-07-21 |
| katib | Python | 1,692 | 2026-07-20 |
| mcp-server | Python | 29 | 2026-07-21 |

#### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 | GF3 convergence maps, loopify pass |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |

#### bmorphism (50+ repos)
| Repo | Language | Stars | Notes |
|------|----------|-------|-------|
| ocaml-mcp-sdk | OCaml | 61 | +1 star since April sweep |
| anti-bullshit-mcp-server | JavaScript | 22 | active 2026-07-12 |
| Gay.jl | Julia | 2 | 187 open issues — spike! |
| gay-chat | Scheme | 0 | new 2026-07-14 |

#### zubyul (49 repos)
| Repo | Language | Stars |
|------|----------|-------|
| voice-observatory | Python | 0 | companion to bmorphism/say-mcp-server |
| big-bad-plurigrid-quiz | Emacs Lisp | 0 |
| gay-world | Python | 1 |
| tilelang-kernels | Python | 0 | GF(3) trit GPU kernels |

#### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 | +1 since April |
| StarE | Python | 89 | +1 since April |
| kgcourse2021 | HTML | 24 | updated 2026-07-10 |

#### wasita (12 repos, active today)
| Repo | Language | Stars |
|------|----------|-------|
| wasita.github.io | Svelte | 1 | updated 15:55 UTC today |
| magic-garden | Python | 2 |
| send2kobo | TypeScript | 1 |

#### AustinCStone (41 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| byteruckus | HTML | 0 | new 2026-07-15 |
| StereoVisionMRF | Python | 11 |

### Social Graph Observations
- **bmorphism ↔ zubyul**: Direct collaboration — `zubyul/gay-world` forks `bmorphism`; `voice-observatory` is companion to `bmorphism/say-mcp-server`
- **bmorphism ↔ AustinCStone**: `AustinCStone/bmfork*` repos are direct forks of bmorphism work
- **zubyul ↔ wasita ↔ kristinezheng**: Likely BCI/cognitive science cluster (OpenBCI, Lookit studies, connectome)
- **migalkin**: KG/GNN research — `kgcourse2021` active today; `NodePiece` +1⭐ since April
- **Gay.jl issue spike** (bmorphism): 187 open issues on julia color sampling repo — worth investigating

### Star Growth Since 2026-04-12
| Repo | April | July | Δ |
|------|-------|------|---|
| kubeflow/kubeflow | 15,565 | 15,789 | +224 |
| kubeflow/pipelines | 4,119 | 4,168 | +49 |
| kubeflow/spark-operator | 3,111 | 3,142 | +31 |
| kubeflow/trainer | 2,080 | 2,152 | +72 |
| bmorphism/ocaml-mcp-sdk | 60 | 61 | +1 |
| migalkin/NodePiece | 143 | 144 | +1 |
| migalkin/StarE | 88 | 89 | +1 |
| plurigrid/asi | 16 | 31 | +15 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

**Ledger version at probe:** 6,387,663,737

**Result:** All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

Wallets alice, bob, A–Z do not hold native APT in the standard CoinStore. Possible causes:
- Accounts hold FA (Fungible Asset) balances post-migration
- Accounts initialized but not funded with APT
- Different token standard in use

| Range | Status |
|-------|--------|
| alice, bob | `resource_not_found` |
| A–M (13 addresses) | `resource_not_found` |
| N–Z (12 addresses) | `resource_not_found` |

### Multisig Contract Probes

All 5 pairs probed via `0x1::multisig_account::num_signatures_required` — **all healthy**, all require 2-of-N:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428a0c007da...` | 2 | ✅ HEALTHY |
| A-G | `0xf56c4a1c09062...` | 2 | ✅ HEALTHY |
| Y-Z | `0xd3ffe1812b2df4...` | 2 | ✅ HEALTHY |
| S-T | `0x3b1c3ae905d44c...` | 2 | ✅ HEALTHY |
| V-W | `0x40fad7b423a843...` | 2 | ✅ HEALTHY |

No anomalies — all contracts are live and properly configured.

### MNX Markets (`testnet.mnx.fi`)

**Status:** HTTP 401 — Vercel deployment protection active.  
API endpoints `/api/markets` and `/api/v1/markets` both gate-protected.  
No market data extractable without visitor password, Vercel CLI, or Trusted Sources OIDC token.  
`mnx_snapshots` table: **0 rows inserted**.

---

## DuckDB Ducklake State

**Path:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Cumulative Rows |
|-------|-----------------|
| `world_increments` | 121 (this sweep) |
| `repo_snapshots` | 1,042 total |
| `aptos_snapshots` | 28 (this sweep, all NULL) |
| `multisig_probes` | 5 (this sweep, all healthy) |
| `mnx_snapshots` | 0 (auth blocked) |

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

## Flags
1. **bmorphism/Gay.jl**: 187 open issues on a Julia color-sampling repo — unexpected spike, may need triage
2. **Hamming swarm wallets**: All 28 Aptos addresses have no native APT CoinStore — check FA balances or funding status
3. **MNX testnet gated**: Vercel auth protection prevents automated market data extraction
4. **All multisig pairs healthy**: 2-of-N confirmed on all 5 contract pairs — no anomalies
5. **plurigrid/asi surge**: +15 stars since April (16→31), most active plurigrid repo
