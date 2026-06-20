# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-20

## Sweep Metadata
- **Date:** 2026-06-20T07:07 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts (this run)

| Metric | Value |
|--------|-------|
| World Increments (this run) | 11 |
| Repo Snapshots (this run) | 312 |
| Sources Covered | 3 orgs + 8 users |
| DB Cumulative Increments | 34 |
| DB Cumulative Repo Snapshots | 1,256 |

---

### GF(3) Color Chain — 11 Increments This Run

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| +1 | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| +2 | kubeflow | org | 48 | -1 | `#cc241d` | **MINUS** |
| +3 | TeglonLabs | org | 5 | 0 | `#d3869b` | **ERGODIC** |
| +4 | bmorphism | user | 100 | +1 | `#b8bb26` | **PLUS** |
| +5 | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |
| +6 | migalkin | user | 19 | 0 | `#d3869b` | **ERGODIC** |
| +7 | DJedamski | user | 6 | +1 | `#b8bb26` | **PLUS** |
| +8 | wasita | user | 11 | -1 | `#cc241d` | **MINUS** |
| +9 | kristinezheng | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| +10 | M1shaaa | user | 8 | +1 | `#b8bb26` | **PLUS** |
| +11 | AustinCStone | user | 40 | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

### Top Repos by Stars

| Repo | Language | Stars | Forks | Pushed |
|------|----------|-------|-------|--------|
| kubeflow/kubeflow | — | 15,736 | 2,680 | 2026-06-18 |
| kubeflow/pipelines | Python | 4,154 | 2,008 | 2026-06-19 |
| kubeflow/spark-operator | Python | 3,127 | 1,490 | 2026-06-18 |
| kubeflow/trainer | Go | 2,117 | 970 | 2026-06-19 |
| kubeflow/katib | Python | 1,683 | 528 | 2026-06-15 |
| kubeflow/examples | Jsonnet | 1,460 | 756 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1,025 | 1,065 | 2026-06-18 |
| kubeflow/arena | Go | 813 | 190 | 2026-05-07 |
| kubeflow/kale | Python | 694 | 155 | 2026-06-17 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2016-09-19 |
| migalkin/NodePiece | Python | 144 | 21 | 2021-06-14 |
| migalkin/StarE | Python | 89 | 16 | 2020-09-17 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 | 2026-01-16 |
| plurigrid/asi | HTML | 26 | 8 | 2026-06-10 |

**Aggregate sweep:** ~103,822 stars, ~40,729 forks

---

### Same-Day Activity (2026-06-20)

| Repo | Pushed | Notes |
|------|--------|-------|
| plurigrid/gorj | 06:12 UTC | 689 open issues — this repo |
| bmorphism/Gay.jl | 00:40 UTC | 187 open issues, wide-gamut color SPI |
| bmorphism/satreadout | 01:12 UTC | saturating non-Riemannian perceptual readout |
| bmorphism/bci-preview | 00:20 UTC | bci.place forester preview redirect |
| bmorphism/oxcaml-mcp | 04:04 UTC | high-perf MCP with categorical sonification |
| bmorphism/oxcaml-sci | 03:48 UTC | zero-alloc scientific computing OCaml |
| kubeflow/pipelines-components | 03:06 UTC | active KFP development |
| kubeflow/sdk | 03:05 UTC | universal Python SDK for AI on k8s |

---

### Social Graph Notes

- **migalkin**: Knowledge graph researcher (NodePiece ICLR'22, StarE EMNLP'20). 19 repos, mostly Python/ML.
- **DJedamski**: 6 repos, mostly R/data science from 2014-2018.
- **wasita**: 11 repos, active 2026-06-19 (proj-template). Svelte/Python developer.
- **kristinezheng**: 5 repos, active 2026-06-07, cognitive/neuro researcher (MIT).
- **M1shaaa**: 8 repos, active 2026-02-04, lab research tools (Yale).
- **AustinCStone**: 40 repos, TextGAN (92 stars), ML/control theory focus.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances

All 28 addresses (alice, bob, A–Z) probed via Aptos mainnet fullnode.

**Result: All wallets — 0.0 APT**

Addresses exist on-chain but hold no APT in the `CoinStore<AptosCoin>` resource. This indicates either:
1. Accounts not yet funded with APT
2. Assets held in other coin types or NFTs
3. Accounts created but not used

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793ac... | 0.0 |
| bob   | 0x0a3c00... | 0.0 |
| A–Z (26 addrs) | 0x8699ed...→0x7af0ef... | 0.0 each |

---

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a... | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe1... | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3a... | 2 | ✅ HEALTHY |
| V-W | 0x40fad7... | 2 | ✅ HEALTHY |

**All 5 contracts live, responsive, 2-of-N threshold. No anomalies.**

---

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE**

`testnet.mnx.fi` returns HTTP 401 — behind Vercel deployment protection requiring a visitor password or bypass token. No market data extractable. Logged in `mnx_snapshots` as `auth-required`.

---

## Executive Summary

| Category | Status | Detail |
|----------|--------|--------|
| GitHub sweep (11 sources) | ✅ Complete | 312 repos, 103K+ stars aggregated |
| Same-day activity | 🔥 Hot | 8 repos pushed on 2026-06-20 |
| Aptos swarm (28 wallets) | ✅ Probed | All 0.0 APT — unfunded |
| Multisig health (5 pairs) | ✅ All healthy | 2-of-N, all responding |
| MNX Markets | ❌ Auth-gated | Vercel protection, no bypass |
| DuckDB ducklake | ✅ Updated | world-increments.duckdb |

**Key signal:** plurigrid/bmorphism ecosystem showing intense same-day session activity across Gay.jl, OxCaml-MCP, BCI tooling, and the gorj repo itself. kubeflow actively shipping pipelines and SDK. Hamming swarm multisigs all healthy.

---

## Schema Reference
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
