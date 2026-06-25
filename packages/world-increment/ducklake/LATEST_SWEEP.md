# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-25

## Sweep Metadata
- **Date:** 2026-06-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 8 |
| Total Repo Snapshots | 362 |
| Sources Covered | 3 orgs + 5 users (+ 6 social graph users) |

---

### GF(3) Color Chain — All 8 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | org | 1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | bmorphism | user | 0 | `#d3869b` | **ERGODIC** |
| 4  | zubyul | user | 1 | `#b8bb26` | **PLUS** |
| 5  | migalkin | user | -1 | `#cc241d` | **MINUS** |
| 6  | AustinCStone | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | wasita | user | 1 | `#b8bb26` | **PLUS** |
| 8  | TeglonLabs | org | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

### Repo Counts by Source

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| kubeflow | org | 48 | 34,254 | 2026-06-24 |
| migalkin | user | 19 | 280 | 2025-08-04 |
| bmorphism | user | 100 | 247 | 2026-06-25 |
| AustinCStone | user | 30 | 108 | 2026-02-11 |
| plurigrid | org | 100 | 77 | 2026-06-25 |
| zubyul | user | 49 | 14 | 2026-04-24 |
| wasita | user | 11 | 5 | 2026-06-19 |
| TeglonLabs | org | 5 | 2 | 2026-06-08 |
| **TOTAL** | | **362** | **34,987** | |

Social graph users also swept: DJedamski (6 repos), kristinezheng (5 repos), M1shaaa (8 repos) — noted, not persisted in this increment batch.

---

### Notable Repos (2026-06-25)

**plurigrid** (most active, pushed today):
- `gorj` — Clojure, 801 open issues, pushed 2026-06-25 — *forj + Rama topology nREPL routing + GF(3) gay trit coloring*
- `eirobri` — Clojure, 30 issues, pushed 2026-06-23 — *EiRoBri replay world*
- `asi` — HTML, 26★, pushed 2026-06-10 — *everything is topological chemputer!*
- `nanoclj-zig` — Zig, 1★, NaN-boxed Clojure + interaction nets

**bmorphism** (active researcher, pushed today):
- `Gay.jl` — Julia, 2★, 187 issues, pushed 2026-06-25 — *Wide-gamut color sampling with splittable determinism (Pigeon)*
- `ocaml-mcp-sdk` — OCaml, 61★ — *OCaml SDK for MCP using Jane Street's oxcamel*
- `anti-bullshit-mcp-server` — JavaScript, 23★ — *claim validation MCP server*

**kubeflow** (largest by stars):
- `kubeflow` — 15,742★, 2,680 forks
- `pipelines` — Python, 4,157★, pushed 2026-06-24
- `spark-operator` — Python, 3,128★, pushed 2026-06-24
- `trainer` — Go, 2,121★ — *Distributed AI Model Training and LLM Fine-Tuning on K8s*

**TeglonLabs**:
- `jank-crane` — C++, pushed 2026-06-08 — *crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow*

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-25)

All 28 addresses (alice, bob, A–Z) returned **0.0 APT** from Aptos mainnet CoinStore. Accounts either have zero balance or CoinStore resource not initialized.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793ac...4cc7b | 0.0 |
| bob | 0x0a3c00...512d5d | 0.0 |
| A | 0x8699ed...e9d7a | 0.0 |
| B | 0x3f892e...b13 | 0.0 |
| C | 0x38b99e...535e | 0.0 |
| D | 0xf77656...cdd1 | 0.0 |
| E | 0xdc1d9d...8d36 | 0.0 |
| F | 0x18a14b...cf71 | 0.0 |
| G | 0x69a394...7f32 | 0.0 |
| H | 0xce67c3...300f | 0.0 |
| I–Z | (18 more addresses) | 0.0 each |

Total APT across swarm: **0.0 APT**

---

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`. All healthy:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f4...87003 | 2 | ✓ |
| A-G | 0xf56c4a...c0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1...5b883 | 2 | ✓ |
| S-T | 0x3b1c3a...d7883 | 2 | ✓ |
| V-W | 0x40fad7...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy** — 2-of-N threshold confirmed on mainnet.

---

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` returns **Vercel authentication required** (deployment protection active). Market data unavailable — SPA behind auth gate. 0 rows in `mnx_snapshots`.

---

## DuckDB Tables Summary

| Table | Rows |
|-------|------|
| world_increments | 8 |
| repo_snapshots | 362 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth-gated) |

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
