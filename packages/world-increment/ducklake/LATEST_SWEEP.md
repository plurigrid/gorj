# World-Increment Sweep + Hamming Snapshot — 2026-07-13

## Sweep Metadata
- **Date:** 2026-07-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (via pip)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 135 (+52 this sweep) |
| Total Repo Snapshots | 1056 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Pairs Probed | 5 (all healthy, 2-of-N) |
| MNX Markets | unavailable (auth-gated) |

---

## GF(3) Color Chain — All 12 Increments

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
| 12 | bmorphism (org) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4119 | 2026-04-10 |
| spark-operator | Python | 3111 | 2026-04-10 |
| trainer | Go | 2080 | 2026-04-10 |
| katib | Python | 1676 | 2026-04-02 |

### TeglonLabs (53 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (43 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

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
- **kubeflow/kubeflow**: 15,774 stars (+209 since April sweep)
- **kubeflow/pipelines**: 4,165 stars — active (pushed 2026-07-13)
- **kubeflow/sdk**: new repo ⭐124 — Universal Python SDK for AI workloads (2025-04-23)
- **kubeflow/mcp-server**: new repo ⭐26 — Kubeflow MCP server (2026-04-08)
- **bmorphism/anti-bullshit-mcp-server**: ⭐22, pushed 2026-07-12 (latest activity)
- **bmorphism/ocaml-mcp-sdk**: ⭐61 (was 60 in April sweep)
- **bmorphism/satreadout**: new — Lean 4.28 + mathlib machine-checked subadditivity
- **plurigrid/gorj**: 1157 open issues, pushed 2026-07-13 (this very repo, most active)
- **plurigrid/asi**: ⭐30 (+14 since April sweep)
- **TeglonLabs/jank-crane**: new C++ repo with GF3 convergence maps (2026-06-08)
- **zubyul/tilelang-kernels**: TileLang GPU kernels for GF(3) trit classification (targeting NVIDIA GB10 Blackwell)

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

All 28 addresses queried via `https://fullnode.mainnet.aptoslabs.com/v1/`.

**Finding:** Zero CoinStore resources found across all addresses. Accounts alice/bob/A–I return `resource_not_found` (no account or no CoinStore). Addresses Q–Z exist on-chain with sequence numbers confirming prior transactions, but hold no legacy APT CoinStore (likely using FungibleAsset module or empty).

| World | Seq# | Status |
|-------|------|--------|
| alice, bob, A–I | absent | No account / no CoinStore |
| Q | 9 | Exists, no CoinStore |
| R | 15 | Exists, no CoinStore (most active) |
| S | 11 | Exists, no CoinStore |
| T | 9 | Exists, no CoinStore |
| U | 7 | Exists, no CoinStore |
| V | 5 | Exists, no CoinStore |
| W | 4 | Exists, no CoinStore |
| X | 3 | Exists, no CoinStore |
| Y | 2 | Exists, no CoinStore |
| Z | 2 | Exists, no CoinStore |

### Multisig Contract Probes — ALL HEALTHY

| Pair | Address (truncated) | Sigs Required |
|------|---------------------|---------------|
| A-B | 0x0da4...7003 | 2 |
| A-G | 0xf56c...0096 | 2 |
| Y-Z | 0xd3ff...b883 | 2 |
| S-T | 0x3b1c...7883 | 2 |
| V-W | 0x40fa...eb6d | 2 |

All 5 multisig contracts responded with `["2"]` — 2-of-N threshold, healthy.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection active. The endpoint returns a password-gated SPA; no market data accessible without visitor credentials. Zero rows in `mnx_snapshots`.
