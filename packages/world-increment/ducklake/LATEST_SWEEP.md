# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-07

## Sweep Metadata
- **Date:** 2026-07-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 323 |
| Total Repo Snapshots | 323 |
| Aptos Wallet Snapshots | 28 |
| Multisig Probes | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 107 |
| +1 | `#b8bb26` | PLUS | 108 |
| -1 | `#cc241d` | MINUS | 108 |

GF(3) assignment: `id%3==0 → ERGODIC`, `id%3==1 → PLUS`, `id%3==2 → MINUS`

---

## Top Repos by Stars (2026-07-07)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,769 | — | 2026-07-06 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-07 |
| kubeflow/spark-operator | 3,132 | Python | 2026-07-02 |
| kubeflow/trainer | 2,130 | Go | 2026-07-07 |
| kubeflow/katib | 1,690 | Python | 2026-07-07 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-07 |
| AustinCStone/TextGAN | 92 | Python | 2016-09-19 |
| migalkin/NodePiece | 144 | Python | 2021-06-14 |
| migalkin/StarE | 89 | Python | 2020-09-17 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| plurigrid/asi | 28 | HTML | 2026-06-29 |
| plurigrid/ontology | 8 | JavaScript | 2025-05-27 |

---

## Repo Counts by Source

| Source | Type | Repos Fetched |
|--------|------|---------------|
| plurigrid | org | 100 (of 103) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 (of 105) |
| zubyul | user | 49 |
| migalkin | user (social graph) | 5 |
| wasita | user (social graph) | 4 |
| DJedamski | user (social graph) | 3 |
| kristinezheng | user (social graph) | 3 |
| AustinCStone | user (social graph) | 3 |
| M1shaaa | user (social graph) | 2 |
| **TOTAL** | | **323** |

---

## Notable Today Activity (pushed 2026-07-07)

- `plurigrid/gorj` — Clojure, 1038 open issues, forj + Rama nREPL + GF(3) trit coloring
- `plurigrid/place` — TeX, 12 open issues
- `kubeflow/hub` — Go, Model Registry
- `kubeflow/pipelines` — Python, 4169★
- `kubeflow/trainer` — Go, 2130★, Distributed AI/LLM Training
- `kubeflow/katib` — Python, 1690★, AutoML on Kubernetes
- `kubeflow/dashboard` — TypeScript, 83 open issues
- `kubeflow/sdk` — Python, universal SDK for K8s AI workloads
- `bmorphism/Gay.jl` — Julia, 187 open issues, GF(3) splittable determinism
- `wasita/wasita.github.io` — Svelte personal site

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 Hamming-alphabet addresses)

**API:** `https://fullnode.mainnet.aptoslabs.com/v1`  
**Ledger version at query:** ~6,160,909,045 (Aptos mainnet)

**Result:** All 28 addresses returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

The CoinStore resource is absent on all wallets, indicating these accounts either hold no APT or use the Fungible Asset (FA) standard. All recorded as 0.0 APT.

| World | Address (truncated) |
|-------|---------------------|
| alice | 0xc793...cc7b |
| bob | 0x0a3c...2d5d |
| A | 0x8699...9d7a |
| B | 0x3f89...b13 |
| C–Z | (24 more addresses) |

### Multisig Contract Probes — 5/5 Healthy ✓

All 5 swarm pairs probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | **2** | ✓ healthy |
| A-G | 0xf56c...0096 | **2** | ✓ healthy |
| Y-Z | 0xd3ff...b883 | **2** | ✓ healthy |
| S-T | 0x3b1c...7883 | **2** | ✓ healthy |
| V-W | 0x40fa...eb6d | **2** | ✓ healthy |

All multisig contracts require 2-of-N signatures. Network: **Aptos Mainnet**.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — site protected by Vercel deployment authentication (password required). No market data extracted. `mnx_snapshots` table empty.

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
