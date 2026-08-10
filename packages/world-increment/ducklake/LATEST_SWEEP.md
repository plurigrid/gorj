# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep date:** 2026-08-10  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried

| Source | Type | Repos snapshotted |
|--------|------|-------------------|
| plurigrid | org | 53 |
| kubeflow | org | 16 |
| TeglonLabs | org | 5 |
| bmorphism | user | 45 |
| zubyul | user | 30 |
| migalkin | user | 5 |
| DJedamski | user | 2 |
| wasita | user | 6 |
| kristinezheng | user | 2 |
| M1shaaa | user | 3 |
| AustinCStone | user | 7 |
| **Total** | | **175** |

### Notable recent pushes (as of 2026-08-10)

**plurigrid:**
- `plurigrid/gorj` (Clojure) — pushed 2026-08-10, 1767 open issues, GF(3) trit REPL orchestration
- `plurigrid/zig-syrup` (Zig) — pushed 2026-08-10, OCapN Syrup implementation
- `plurigrid/eirobri` (Clojure) — pushed 2026-08-04, EiRoBri replay world

**kubeflow:**
- `kubeflow/mpi-operator` (Go) — pushed 2026-08-10, 531★
- `kubeflow/hub` (Go) — pushed 2026-08-10, Model Registry
- `kubeflow/pipelines-components` (Python) — pushed 2026-08-10
- `kubeflow/spark-operator` (Python) — 3146★, pushed 2026-08-09
- `kubeflow/pipelines` (Python) — 4180★, pushed 2026-08-09
- `kubeflow/kubeflow` — 15809★ (most starred in sweep)

**TeglonLabs:**
- `jank-crane` (C++) — pushed 2026-06-08, crane-jank converged-IR hub

**bmorphism:**
- `bmorphism/nashator-h1` (Clojure) — pushed 2026-08-10, Cech-H1 triangular-arbitrage detector GF(3)
- `bmorphism/attention-heat-capacity` (Python) — pushed 2026-08-10, GPT-2 attention heat capacity
- `bmorphism/oldies-clearing` (Agda) — pushed 2026-08-10, cut-elimination = obligation clearing
- `bmorphism/paraoptic` (Lean) — pushed 2026-08-10, Para(C)-Optic(C) formalized Lean4/Agda/Dafny
- `bmorphism/keywire` (Clojure) — pushed 2026-08-10, key-addressed service proxy over iroh QUIC
- `bmorphism/Gay.jl` (Julia) — 2★, 188 open issues, pushed 2026-08-07

**zubyul:**
- `zubyul/xoxowasita-analysis` (Python) — pushed 2026-08-10 [via wasita]
- `zubyul/from-possible-worlds` (TeX) — pushed 2026-07-18

### GF(3) color chain distribution (175 increments)

| trit | color | name | count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 59 |
| 1 | `#b8bb26` | PLUS | 58 |
| -1 | `#cc241d` | MINUS | 58 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Hamming alphabet A–Z + alice/bob)

All 28 wallets queried against `fullnode.mainnet.aptoslabs.com`.

**Result:** All 28 addresses returned `null` — no `CoinStore<AptosCoin>` resource found on mainnet. Addresses are either testnet-only, not yet funded, or the resource path has not been initialized.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | null |
| bob | 0x0a3c...512d | null |
| A–Z | 0x8699...–0x7af0... | null (all) |

### Multisig Contract Probes

All 5 multisig contracts probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | **2** | ✅ |
| A-G | 0xf56c...0096 | **2** | ✅ |
| Y-Z | 0xd3ff...b883 | **2** | ✅ |
| S-T | 0x3b1c...7883 | **2** | ✅ |
| V-W | 0x40fa...eb6d | **2** | ✅ |

All 5 multisig contracts returned `sigs_required=2` and are healthy.

### MNX Markets (`testnet.mnx.fi`)

Site is a Next.js SPA — `/api/markets` and `/api/v1/markets` returned no JSON data. Market data unavailable via HTTP fetch; requires JavaScript execution. **Status: unavailable (SPA only).**

---

## DuckDB Schema Summary

| Table | Rows |
|-------|------|
| `world_increments` | 175 |
| `repo_snapshots` | 175 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 (SPA unavailable) |

**GF(3) encoding:** `id%3==0` → trit=0 `ERGODIC` `#d3869b`; `id%3==1` → trit=1 `PLUS` `#b8bb26`; `id%3==2` → trit=-1 `MINUS` `#cc241d`.
