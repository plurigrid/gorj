# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-25

## Sweep Metadata
- **Date:** 2026-07-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.2.2
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) this sweep:** trit=1 PLUS `#b8bb26`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 24 |
| Total Repo Snapshots (cumulative) | 1158 |
| Sources Covered | 3 orgs + 9 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain

| Source | Type | GF3 Trit | Color | Name |
|--------|------|-----------|-------|------|
| plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| kubeflow | org | -1 | `#cc241d` | **MINUS** |
| TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| zubyul | user | -1 | `#cc241d` | **MINUS** |
| migalkin | social graph | 0 | `#d3869b` | **ERGODIC** |
| wasita | social graph | +1 | `#b8bb26` | **PLUS** |
| kristinezheng | social graph | -1 | `#cc241d` | **MINUS** |
| AustinCStone | social graph | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

### Repos by Source (this sweep)

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 50 (top by pushed_at) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 12 |
| kristinezheng | social graph | 5 |
| AustinCStone | social graph | 20 |
| **TOTAL this sweep** | | **~214** |

### Notable Repos (July 2026)

**TeglonLabs (new since April):**
- `TeglonLabs/jank-crane` — C++, crane-jank converged-IR hub: loopify pass + GF3 convergence maps (pushed 2026-06-08)
- `TeglonLabs/mathpix-gem` — Ruby, mathematical OCR gem ★2 (pushed 2026-01-01)
- `TeglonLabs/coin-flip-mcp` — JS, MCP coin-flip with random.org, 2 forks (pushed 2025-09-21)

**Social Graph:**
- `migalkin/NodePiece` — Python, Knowledge Graph embeddings ★144, 21 forks (ICLR'22)
- `migalkin/StarE` — Python, Hyper-relational KG ★89, 16 forks (EMNLP 2020)
- `migalkin/kgcourse2021` — HTML, Knowledge Graphs course materials ★24 (active, updated 2026-07-10)
- `AustinCStone/TextGAN` — Python, text GAN in TensorFlow ★92, 30 forks
- `wasita/wasita.github.io` — Svelte, personal website ★1 (updated 2026-07-21)
- `wasita/magic-garden` — Python, Discord bot ★2 (active 2026)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 wallets (alice, bob, A–Z) queried via `https://fullnode.mainnet.aptoslabs.com`.

**Result: All 28 wallets returned 0 APT.**

The `CoinStore<0x1::aptos_coin::AptosCoin>` resource is absent on all queried accounts — wallets are either uninitialized or hold no APT on mainnet.

| Range | Count | Balance |
|-------|-------|---------|
| alice, bob | 2 | 0.0 APT |
| A – Z | 26 | 0.0 APT each |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428...87003` | 2 | ✓ healthy |
| A-G | `0xf56c4a1c...0096` | 2 | ✓ healthy |
| Y-Z | `0xd3ffe181...b883` | 2 | ✓ healthy |
| S-T | `0x3b1c3ae9...7883` | 2 | ✓ healthy |
| V-W | `0x40fad7b4...eb6d` | 2 | ✓ healthy |

**5/5 healthy** — all multisigs live as 2-of-2.

### MNX Markets

`https://testnet.mnx.fi` returns a Next.js SPA. No public REST API found at `/api/markets` or `/api/v1/markets`. Market data is client-side rendered.

**Status:** `unavailable` — recorded as placeholder in `mnx_snapshots`.

---

## DuckDB Table State

```
packages/world-increment/ducklake/world-increments.duckdb
├── world_increments    24 rows   (GF3-tagged sweep events, cumulative)
├── repo_snapshots    1158 rows   (GitHub repo snapshots, cumulative)
├── aptos_snapshots     28 rows   (this sweep — all 0 APT)
├── multisig_probes      5 rows   (this sweep — all healthy 2-of-2)
└── mnx_snapshots        1 row    (unavailable marker)
```

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

## Notable Highlights (July 2026)
- **migalkin/NodePiece**: ★144 — ICLR'22 paper, most active KG embedding repo in graph
- **migalkin/kgcourse2021**: updated 2026-07-10 — Knowledge Graphs course still maintained
- **TeglonLabs/jank-crane**: new C++ repo, crane-jank GF3 convergence maps (June 2026)
- **wasita/wasita.github.io**: updated 2026-07-21 — most recently touched social-graph repo
- **All Aptos wallets empty**: 0 APT across all 28 Hamming-swarm addresses
- **All multisigs healthy**: 5/5 probed multisig contracts responding as 2-of-2
