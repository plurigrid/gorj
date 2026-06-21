# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-06-21  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted | Top Repo (Stars) |
|--------|------|-------------------|------------------|
| plurigrid | org | 20 | `plurigrid/gorj` — forj + Rama topology nREPL |
| kubeflow | org | 20 | `kubeflow/kubeflow` — 15,737 ★ |
| TeglonLabs | org | 5 | `TeglonLabs/jank-crane` — crane-jank converged-IR |
| bmorphism | user | 20 | `bmorphism/Gay.jl` — wide-gamut color sampling (187 issues) |
| zubyul | user | 12 | `zubyul/gay-world` — goblin world builder |
| migalkin | social | 10 | `migalkin/NodePiece` — 144 ★ Compositional KG |
| DJedamski | social | 6 | `DJedamski/School` — grad school R projects |
| wasita | social | 8 | `wasita/wasita.github.io` — personal site |
| kristinezheng | social | 5 | `kristinezheng/kristinezheng.github.io` |
| M1shaaa | social | 8 | `M1shaaa/M1shaaa` — GitHub profile config |
| AustinCStone | social | 8 | `AustinCStone/TextGAN` — 92 ★ TF text GAN |

**Total this run:** 122 new repo snapshots inserted  
**DB cumulative:** 145 world_increments, 1066 repo_snapshots

### Notable Activity (last 7 days)

- `plurigrid/gorj` pushed **2026-06-21** (today) — 710 open issues, active Clojure/REPL work
- `plurigrid/place` pushed **2026-06-20** — TeX, 9 open issues
- `kubeflow/dashboard` pushed **2026-06-21** — TypeScript UI, active
- `kubeflow/katib` pushed **2026-06-20** — AutoML on K8s, 116 issues
- `bmorphism/Gay.jl` pushed **2026-06-21** — 187 open issues (most active repo in swarm)
- `wasita/proj-template` pushed **2026-06-19** — recently active
- `bmorphism/satreadout` pushed **2026-06-20** — HTML saturating readout

### GF(3) Color Chain (id%3 assignment)

| Trit | Color | Name | Meaning |
|------|-------|------|---------|
| 0 | `#d3869b` | ERGODIC | stationary / baseline |
| 1 | `#b8bb26` | PLUS | positive increment |
| -1 | `#cc241d` | MINUS | negative / decrement |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm addresses (alice, bob, A–Z) queried against  
`fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All 28 addresses returned **0 APT** — `CoinStore` resource not registered or wallets unfunded on mainnet. This is consistent with fresh/test addresses that have not yet received an on-chain APT deposit.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793ac… | 0.0 |
| bob | 0x0a3c00… | 0.0 |
| A–Z (26) | 0x8699ed… → 0x7af0ef… | 0.0 each |

### Multisig Contract Probes

All 5 Hamming pair multisig accounts probed via  
`POST /v1/view → 0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4… | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a… | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe1… | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3a… | 2 | ✅ HEALTHY |
| V-W | 0x40fad7… | 2 | ✅ HEALTHY |

All multisig contracts require **2-of-N** signatures. All responsive and healthy.

### MNX Markets (`testnet.mnx.fi`)

Status: **UNAVAILABLE** — Vercel authentication required. The SPA returns an auth wall for all routes including `/api/markets` and `/api/v1/markets`. No market data extractable without Vercel credentials.

---

## DuckDB Schema Summary

```
world_increments   — 145 rows (GF3-colored repo push events)
repo_snapshots     — 1066 rows (cumulative across all sweeps)
aptos_snapshots    — 28 rows (this run; all 0 APT)
multisig_probes    — 5 rows (all healthy, 2 sigs)
mnx_snapshots      — 0 rows (auth wall)
```

---

## Top Repos by Stars (this sweep)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,737 | — |
| kubeflow/pipelines | 4,155 | Python |
| kubeflow/spark-operator | 3,127 | Python |
| kubeflow/trainer | 2,118 | Go |
| kubeflow/katib | 1,683 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
