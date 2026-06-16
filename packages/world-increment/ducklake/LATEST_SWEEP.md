# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-16

## Sweep Metadata
- **Date:** 2026-06-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 362 |
| Aptos Wallets Probed | 28 |
| Multisig Pairs Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — All 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name | Repos | Stars |
|----|--------|------|----------|-------|------|-------|-------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** | 100 | 77 |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** | 48 | 34,212 |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** | 5 | 2 |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** | 100 | 247 |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** | 49 | 14 |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** | 14 | 280 |
| 7  | wasita | user | +1 | `#b8bb26` | **PLUS** | 11 | 5 |
| 8  | AustinCStone | user | -1 | `#cc241d` | **MINUS** | 16 | 108 |
| 9  | M1shaaa | user | 0 | `#d3869b` | **ERGODIC** | 8 | 0 |
| 10 | DJedamski | user | +1 | `#b8bb26` | **PLUS** | 6 | 3 |
| 11 | kristinezheng | user | -1 | `#cc241d` | **MINUS** | 5 | 0 |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### GF(3) Assignment Rule
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=**PLUS** (generative)
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS** (contractive)
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC** (stable)

---

### Top Repos by Stars (2026-06-16 snapshot)

| Source | Repo | Stars | Language | Last Pushed |
|--------|------|-------|----------|-------------|
| kubeflow | kubeflow/kubeflow | 15,725 | — | 2026-06-11 |
| kubeflow | kubeflow/pipelines | 4,154 | Python | 2026-06-16 |
| kubeflow | kubeflow/spark-operator | 3,127 | Python | 2026-06-15 |
| kubeflow | kubeflow/trainer | 2,115 | Go | 2026-06-16 |
| kubeflow | kubeflow/katib | 1,683 | Python | 2026-06-15 |
| migalkin | migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin | migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone | AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism | bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism | bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |

### Most Recently Active Repos
- `wasita/wasita.github.io` — pushed 2026-06-15T20:14Z (Svelte site, 8 open issues)
- `plurigrid/gorj` — pushed 2026-06-16T09:12Z, 615 open issues (Rama topology nREPL + GF(3))
- `kubeflow/hub` — pushed 2026-06-16T09:51Z (Model Registry)
- `kubeflow/dashboard` — pushed 2026-06-16T09:46Z (TypeScript Central Dashboard)
- `bmorphism/Gay.jl` — pushed 2026-06-16T00:49Z, 187 open issues (wide-gamut color sampling)
- `TeglonLabs/jank-crane` — pushed 2026-06-08 (crane-jank converged-IR hub, GF3 maps)

### Zubyul Social Graph Nodes
| User | Activity | Notable Repos |
|------|----------|---------------|
| migalkin | Knowledge Graph researcher | NodePiece ★144, StarE ★89, RWL ★8 |
| wasita | Svelte/UI dev | wasita.github.io (active 2026-06-15), wm-cv, send2kobo |
| DJedamski | Data science / Kaggle | 6 repos, last active 2023 |
| kristinezheng | MIT cognitive science | site updated 2026-06-07, lookit studies |
| M1shaaa | Yale research lab | 8 repos, lab-bookshelf TypeScript |
| AustinCStone | ML/CV researcher | TextGAN ★92, bmfork, EpsteinSearch |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-16)

All 28 wallets queried: `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result: All 28 addresses — NULL balance** (CoinStore resource not initialized)

These accounts have never had APT deposited or have not registered a CoinStore on mainnet. This is expected for freshly derived or purpose-specific addresses that hold non-APT assets or are chain-agnostic key pairs.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | NULL |
| bob | 0x0a3c...512d | NULL |
| A–Z (26 worlds) | various | NULL |

### Multisig Contract Probes

All 5 pairs healthy with 2-of-2 threshold (fully decentralized control).

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — Vercel deployment-protection gate active on testnet. No market data accessible without authorized OIDC token. `mnx_snapshots` table has 0 rows.

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)          -- 11 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)           -- 362 rows

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)  -- 0 rows
```

## Notable Highlights
- **kubeflow/kubeflow**: 15,725 ★ — up 160 since Apr 12 sweep
- **plurigrid/gorj**: 615 open issues (this repo) — forj + Rama nREPL + GF(3) trit routing
- **bmorphism/Gay.jl**: 187 open issues — wide-gamut SplittableRandoms color sampling
- **All multisig pairs healthy**: 2-of-2 sigs required across all 5 Aptos multisig accounts
- **All Hamming swarm wallets**: NULL balance — no on-chain APT CoinStore initialized
