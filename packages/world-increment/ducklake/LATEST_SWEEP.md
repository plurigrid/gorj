# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-12

## Sweep Metadata
- **Date:** 2026-06-12T00:13Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb` (2.1 MB)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social-graph | 19 |
| DJedamski | social-graph | 6 |
| wasita | social-graph | 11 |
| kristinezheng | social-graph | 5 |
| M1shaaa | social-graph | 8 |
| AustinCStone | social-graph | 40 |
| **TOTAL** | | **391** |

### Top Repos by Stars

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,714 | — | 2026-06-11 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-11 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-09 |
| kubeflow/trainer | 2,111 | Go | 2026-06-11 |
| kubeflow/community | 194 | Jupyter Notebook | 2026-06-11 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| plurigrid/asi | 25 | HTML | 2026-06-10 |
| migalkin/kgcourse2021 | 25 | HTML | 2026-02-16 |

### Most Recently Pushed

| Repo | Pushed At | Description |
|------|-----------|-------------|
| plurigrid/gorj | 2026-06-11 | forj + Rama topology nREPL + GF(3) trit coloring |
| kubeflow/trainer | 2026-06-11 | Distributed AI Model Training on Kubernetes |
| kubeflow/community | 2026-06-11 | Kubeflow community proposals & governance |
| bmorphism/Gay.jl | 2026-06-11 | Wide-gamut color sampling with splittable determinism (Julia) |
| bmorphism/satreadout | 2026-06-10 | Machine-checked saturating perceptual readout (Lean 4.28) |
| plurigrid/asi | 2026-06-10 | everything is topological chemputer! |
| TeglonLabs/jank-crane | 2026-06-08 | crane-jank converged-IR hub, GF3 convergence maps |
| kristinezheng/kristinezheng.github.io | 2026-06-07 | personal site |

### Notable Highlights
- **kubeflow/kubeflow**: 15,714 stars (+149 since last sweep) — ML platform for Kubernetes
- **kubeflow/trainer**: 2,111 stars — "Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"
- **plurigrid/gorj**: 511 open issues — most issue-active plurigrid repo, active as of 2026-06-11
- **bmorphism/satreadout**: Lean 4.28 + mathlib, Aristotle-assisted saturating non-Riemannian perceptual readout
- **bmorphism/Gay.jl**: 189 open issues, Pigeons.jl SPI pattern + LispSyntax
- **TeglonLabs/jank-crane**: newest TeglonLabs repo (2026-06-08), C++ with GF3 convergence maps
- **zubyul/voice-observatory**: Python TUI observing voice-download pathways on macOS

### GF(3) Color Chain

World-increments are assigned in repeating trit sequence over `id`:

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

**Total world_increments stored:** 342  
**Total repo_snapshots stored:** 1,263

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`  
Endpoint: `https://fullnode.mainnet.aptoslabs.com`

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...5d5d | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B | 0x3f89...b13 | 0.00000000 |
| C | 0x38b9...35e | 0.00000000 |
| D | 0xf776...dd1 | 0.00000000 |
| E | 0xdc1d...d36 | 0.00000000 |
| F | 0x18a1...f71 | 0.00000000 |
| G | 0x69a3...f32 | 0.00000000 |
| H | 0xce67...00f | 0.00000000 |
| I | 0x070f...fc9 | 0.00000000 |
| J | 0x4d96...f54 | 0.00000000 |
| K | 0xa732...dc4 | 0.00000000 |
| L | 0x7c2e...ba9 | 0.00000000 |
| M | 0x6fed...e9 | 0.00000000 |
| N | 0xe7dd...b2c | 0.00000000 |
| O | 0x7325...89d | 0.00000000 |
| P | 0x6218...948 | 0.00000000 |
| Q | 0xac40...9a9 | 0.00000000 |
| R | 0x7ce6...e10 | 0.00000000 |
| S | 0xb875...386 | 0.00000000 |
| T | 0x3578...588 | 0.00000000 |
| U | 0x7586...956 | 0.00000000 |
| V | 0xb59d...2c3 | 0.00000000 |
| W | 0x5f32...7b0 | 0.00000000 |
| X | 0xa95c...47d | 0.00000000 |
| Y | 0xd8e3...4c4 | 0.00000000 |
| Z | 0x7af0...97c | 0.00000000 |

**All 28 wallets: 0 APT.** Addresses exist on-chain (API returned valid resource responses) but `CoinStore` balances are zero.

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ healthy |
| A-G | 0xf56c...096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✅ healthy |
| S-T | 0x3b1c...883 | 2 | ✅ healthy |
| V-W | 0x40fa...b6d | 2 | ✅ healthy |

All 5 multisig contracts return `["2"]` — 2-of-N threshold, all responding and healthy.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection. All paths (`/api/markets`, `/api/v1/markets`, `/`) return 401 authentication required. No market data extracted. `mnx_snapshots` table is empty.

---

## DuckDB Schema Summary

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)
-- 342 rows: one per repo snapshot, GF(3) trit-colored

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
-- 1,263 rows: full metadata per repo

aptos_snapshots(timestamp, world, address, balance_apt)
-- 28 rows: alice, bob, A-Z hamming swarm wallets

multisig_probes(timestamp, pair, address, sigs_required, healthy)
-- 5 rows: A-B, A-G, Y-Z, S-T, V-W — all 2-of-N, all healthy

mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
-- 0 rows: MNX testnet unavailable (Vercel auth gate)
```

---

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

Chain repeats: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → …`

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent — 2026-06-12*
