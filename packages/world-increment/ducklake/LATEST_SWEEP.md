# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-26

## Sweep Metadata
- **Date:** 2026-07-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned

| Source | Type | Repos Selected |
|--------|------|---------------|
| plurigrid | org | 12 (of ~50 total) |
| kubeflow | org | 10 (of ~30 total) |
| TeglonLabs | org | 5 |
| bmorphism | user | 7 (of ~50 total) |
| zubyul | user | 5 (of ~49 total) |
| migalkin | user | 5 (of 19 total) |
| AustinCStone | user | 3 (of 41 total) |
| DJedamski | user | 2 (of 6 total) |
| wasita | user | 5 (of 12 total) |

### Most Recently Pushed Repos (top 10, this sweep)

| Org/User | Repo | Pushed At | Stars |
|----------|------|-----------|-------|
| kubeflow | pipelines | 2026-07-26T15:01:44Z | 4169 |
| plurigrid | gorj | 2026-07-26T14:16:53Z | 1 |
| kubeflow | kale | 2026-07-25T15:57:48Z | 697 |
| kubeflow | sdk | 2026-07-25T13:50:51Z | 128 |
| kubeflow | trainer | 2026-07-25T03:08:10Z | 2154 |
| kubeflow | spark-operator | 2026-07-25T03:02:55Z | 3142 |
| kubeflow | arena | 2026-07-24T18:18:51Z | 815 |
| kubeflow | mcp-server | 2026-07-24T11:45:11Z | 29 |
| kubeflow | katib | 2026-07-22T02:20:01Z | 1692 |
| zubyul | wasita.github.io | 2026-07-21T15:55:45Z | 1 |

### Notable Highlights

- **plurigrid/gorj** pushed today (2026-07-26) — 1417 open issues, active dev
- **kubeflow/kubeflow** at 15,793 stars — flagship repo, very active
- **kubeflow/spark-operator** at 3,142 stars pushed yesterday
- **bmorphism/Gay.jl** — 188 open issues on `gay` branch, active
- **bmorphism/anti-bullshit-mcp-server** — 22 stars, 7 forks
- **TeglonLabs/jank-crane** — new repo (2026-06-08), C++, crane-jank GF3 convergence maps
- **migalkin/NodePiece** — 144 stars (ICLR'22 KG embeddings paper)
- **wasita/wasita.github.io** — recently active (2026-07-21)

### GF(3) Color Chain Distribution (this sweep batch — 78 increments in DB)

| GF(3) Name | Color | Trit | Count |
|------------|-------|------|-------|
| PLUS | `#b8bb26` | +1 | 27 |
| MINUS | `#cc241d` | -1 | 26 |
| ERGODIC | `#d3869b` | 0 | 25 |

Distribution: balanced — near-uniform across all three trits.

### DuckDB Ducklake State

- **world_increments:** 78 rows (this sweep)
- **repo_snapshots:** 999 rows (cumulative across all sweeps)
- **Cumulative orgs/users:** plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul, migalkin, DJedamski, wasita, AustinCStone, kristinezheng, M1shaaa (11 total)

### GF(3) Assignment Rule

```
id mod 3 == 0  →  trit=0,  color=#d3869b,  name=ERGODIC
id mod 3 == 1  →  trit=+1, color=#b8bb26,  name=PLUS
id mod 3 == 2  →  trit=-1, color=#cc241d,  name=MINUS
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 wallets)

Queried against `fullnode.mainnet.aptoslabs.com` at ledger version **6,463,495,310**.

**Result:** All 28 wallets (alice, bob, A–Z) returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — no APT coin resources on-chain for these addresses.

| World | Balance (APT) | Status |
|-------|---------------|--------|
| alice | 0.0 | resource_not_found |
| bob | 0.0 | resource_not_found |
| A–Z (26 wallets) | 0.0 each | resource_not_found |
| **Total** | **0.0 APT** | |

### Multisig Contract Probes (5 contracts)

All probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...4987003 | **2** | ✓ |
| A-G | 0xf56c4a1c...bc0096 | **2** | ✓ |
| Y-Z | 0xd3ffe181...75b883 | **2** | ✓ |
| S-T | 0x3b1c3ae9...ed7883 | **2** | ✓ |
| V-W | 0x40fad7b4...80eb6d | **2** | ✓ |

**All 5 multisig contracts healthy** — consistent 2-of-N signature requirement.

### MNX Markets (testnet.mnx.fi)

Site is a Next.js SPA (client-side rendered). No REST API endpoints accessible at common paths (`/api/markets`, `/api/v1/markets`). Market data loaded client-side.  
**Status: unavailable via direct API probe** — 0 rows in `mnx_snapshots`.

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

---

## Run Summary

| Component | Status |
|-----------|--------|
| GitHub sweep (3 orgs + 8 users) | ✓ Complete — 999 cumulative repos in ducklake |
| Aptos wallet balances (28 wallets) | ✓ Queried — all 0 APT (no coin resources) |
| Multisig probes (5 contracts) | ✓ All healthy — 2 sigs required each |
| MNX Markets | ⚠ SPA, no REST API accessible |
| DuckDB ducklake | ✓ Updated |
