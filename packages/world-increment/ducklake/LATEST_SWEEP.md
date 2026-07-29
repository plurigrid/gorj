# World-Increment Sweep — 2026-07-29

## Sweep Metadata
- **Date:** 2026-07-29
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (today) | 321 |
| New Increment ID Range | 13 → 333 |
| Total Increments (all-time) | 344 |
| Total Repo Snapshots | 1265 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | SPA — no API data |

---

## GF(3) Color Chain — Today's Sources

| Source | Type | Repos | First Inc ID | GF3 Trit | Color | Name |
|--------|------|-------|-------------|-----------|-------|------|
| plurigrid | org | 100 | 13 | +1 | `#b8bb26` | **PLUS** |
| bmorphism | user | 100 | 113 | +1 | `#b8bb26` | **PLUS** |
| zubyul | user | 49 | 213 | +1 | `#b8bb26` | **PLUS** |
| kubeflow | org | 49 | 262 | 1 | `#b8bb26` | **PLUS** |
| TeglonLabs | org | 5 | 311 | -1 | `#cc241d` | **MINUS** |
| migalkin | user | 5 | 316 | 1 | `#b8bb26` | **PLUS** |
| DJedamski | user | 3 | 321 | 0 | `#d3869b` | **ERGODIC** |
| wasita | user | 3 | 324 | 0 | `#d3869b` | **ERGODIC** |
| kristinezheng | user | 2 | 327 | 0 | `#d3869b` | **ERGODIC** |
| M1shaaa | user | 2 | 329 | -1 | `#cc241d` | **MINUS** |
| AustinCStone | user | 3 | 331 | +1 | `#b8bb26` | **PLUS** |

GF(3) assignment rule: `id%3==0` → ERGODIC `#d3869b`, `id%3==1` → PLUS `#b8bb26`, `id%3==2` → MINUS `#cc241d`

---

## Top Repos by Stars (All-Time High)

| Repo | Stars | Language | Latest Push |
|------|-------|----------|------------|
| kubeflow/kubeflow | 15,794 | — | 2026-07-10 |
| kubeflow/pipelines | 4,171 | Python | 2026-07-29 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-25 |
| kubeflow/trainer | 2,160 | Go | 2026-07-27 |
| kubeflow/katib | 1,693 | Python | 2026-07-26 |
| kubeflow/examples | 1,461 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-28 |
| kubeflow/arena | 815 | Go | 2026-07-29 |
| kubeflow/kale | 698 | Python | 2026-07-27 |
| kubeflow/mpi-operator | 530 | Go | 2026-07-28 |
| migalkin/NodePiece | 144 | Python | 2021-06-14 |
| migalkin/StarE | 89 | Python | 2020-09-17 |
| AustinCStone/TextGAN | 92 | Python | 2016-09-19 |
| plurigrid/asi | 53 | HTML | 2026-07-10 |
| bmorphism/Gay.jl | 2 | Julia | 2026-07-29 |

---

## Notable Activity (plurigrid social graph)

### plurigrid (103 repos total, 100 snapshotted)
- `gorj` — 1,478 open issues, pushed **2026-07-29** (active today)
- `asi` — 53 stars, topological chemputer, pushed 2026-07-10
- `zig-syrup` — 2 stars, OCapN Syrup in Zig, pushed 2026-07-28
- `eirobri` — EiRoBri replay world, pushed 2026-07-21

### bmorphism (106 repos total, 100 snapshotted)
- `Gay.jl` — 188 open issues, pushed **2026-07-29**
- `ocaml-mcp-sdk` — 61 stars, Jane Street oxcaml_effect
- `anti-bullshit-mcp-server` — 22 stars

### kubeflow (49 repos)
- Active across CI, SDK, dashboard, trainer — multiple repos pushed 2026-07-29
- `mcp-server` — 30 stars, MCP server for Kubeflow AI tools

### TeglonLabs (5 repos)
- `jank-crane` — C++ converged-IR hub, GF3 convergence maps, pushed 2026-06-08
- `mathpix-gem` — Ruby gem for math OCR, 2 stars

### Zubyul social graph
- migalkin: Knowledge graph research (NodePiece 144★, StarE 89★)
- wasita: Svelte personal site pushed 2026-07-21
- AustinCStone: TextGAN 92★, byteruckus pushed 2026-07-15
- DJedamski: R/Kaggle data science repos (inactive since 2018)
- kristinezheng: Personal site pushed 2026-07-01
- M1shaaa: Profile updated 2026-02-04

---

## Hamming Swarm Snapshot — Aptos Mainnet

**Probed:** 28 wallets (alice, bob, A–Z)
**Result:** All 28 wallets returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

This indicates the monitored Hamming swarm addresses do not currently hold native APT in their CoinStore. Wallets may hold other assets or be uninitialized.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...` | 2 | ✓ |
| A-G | `0xf56c4a1c...` | 2 | ✓ |
| Y-Z | `0xd3ffe181...` | 2 | ✓ |
| S-T | `0x3b1c3ae9...` | 2 | ✓ |
| V-W | `0x40fad7b4...` | 2 | ✓ |

All 5 multisig contracts healthy — 2-of-2 threshold confirmed on Aptos mainnet.

---

## MNX Markets

`https://testnet.mnx.fi` returns a Next.js SPA (HTML/JS bundle). No structured `/api/markets` endpoint is publicly accessible. Market data unavailable for this sweep — noted as `mnx_snapshots` table empty.

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

- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
