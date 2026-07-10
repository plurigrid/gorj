# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-10

**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.4  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GF(3) Color Chain

- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried This Run

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 20 (top active) |
| zubyul | user | 14 (top active) |
| migalkin | user | 7 |
| DJedamski | user | 4 |
| wasita | user | 7 |
| kristinezheng | user | 4 |
| M1shaaa | user | 4 |
| AustinCStone | user | 5 |
| **TOTAL new** | | **219** |

### Notable Activity (pushed 2026-07-10)

- **plurigrid/asi** (HTML, ★30) — most-starred plurigrid repo, pushed today
- **plurigrid/gorj** (Clojure, ★1) — this repo, active today
- **kubeflow/community** (Jupyter Notebook, ★195) — active today
- **kubeflow/kubeflow** (★15,771) — flagship ML platform, active today
- **kubeflow/mpi-operator** (Go, ★529) — active today
- **kubeflow/trainer** (Go, ★2,134) — active today
- **kubeflow/pipelines** (Python, ★4,169) — active today
- **migalkin/kgcourse2021** (HTML, ★24) — updated today
- **wasita/wasita.github.io** (Svelte, updated 2026-07-06)

### Top Stars This Run

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,771 | — |
| kubeflow/pipelines | 4,169 | Python |
| kubeflow/trainer | 2,134 | Go |
| kubeflow/community-distribution | 1,029 | YAML |
| kubeflow/kale | 695 | Python |
| kubeflow/mpi-operator | 529 | Go |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| bmorphism/say-mcp-server | 20 | JavaScript |
| bmorphism/babashka-mcp-server | 19 | JavaScript |
| plurigrid/asi | 30 | HTML |

### Cumulative DB State

| Metric | Value |
|--------|-------|
| Total world_increments | 34 |
| Total repo_snapshots | 1163 |
| Sweeps performed | 3 (2026-04-12, prev, 2026-07-10) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

Queried 28 wallets (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`.  
APT unit: divide raw `value` by `100,000,000`.

**Result: All 28 wallets show 0.0000 APT** in the `0x1::aptos_coin::AptosCoin` CoinStore.  
Wallets may be unfunded, or assets are held in staked/wrapped form not visible via this resource path.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793acdec12b... | 0.0000 |
| bob   | 0x0a3c00c58fdf... | 0.0000 |
| A     | 0x8699edc09600... | 0.0000 |
| B     | 0x3f892ebe6e45... | 0.0000 |
| C     | 0x38b99e63ada9... | 0.0000 |
| D     | 0xf77656248f64... | 0.0000 |
| E     | 0xdc1d9d533bac... | 0.0000 |
| F     | 0x18a14b5b4bec... | 0.0000 |
| G     | 0x69a394c0b0ac... | 0.0000 |
| H     | 0xce67c327a784... | 0.0000 |
| I     | 0x070fe5d74e4e... | 0.0000 |
| J     | 0x4d964db8f538... | 0.0000 |
| K     | 0xa732040a6b0d... | 0.0000 |
| L     | 0x7c2eaeafad97... | 0.0000 |
| M     | 0x6fed37a75530... | 0.0000 |
| N     | 0xe7dde6da0a65... | 0.0000 |
| O     | 0x73252b601145... | 0.0000 |
| P     | 0x62187920de4a... | 0.0000 |
| Q     | 0xac40fa50b81b... | 0.0000 |
| R     | 0x7ce605cc8fda... | 0.0000 |
| S     | 0xb8753014e488... | 0.0000 |
| T     | 0x35781dc0e42f... | 0.0000 |
| U     | 0x75860da47565... | 0.0000 |
| V     | 0xb59dd8170321... | 0.0000 |
| W     | 0x5f32aef70f5b... | 0.0000 |
| X     | 0xa95cbbd11654... | 0.0000 |
| Y     | 0xd8e32848f1df... | 0.0000 |
| Z     | 0x7af0ef6e1bd7... | 0.0000 |

**Total Hamming swarm APT: 0.0000**

### Multisig Contract Probes — 5/5 HEALTHY

All 5 multisig pairs respond with `sigs_required=2` via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | ✅ |
| A-G | 0xf56c4a1c0906214f... | 2 | ✅ |
| Y-Z | 0xd3ffe1812b2df406... | 2 | ✅ |
| S-T | 0x3b1c3ae905d44c3a... | 2 | ✅ |
| V-W | 0x40fad7b423a84365... | 2 | ✅ |

**Multisig health: 5/5 (100%)** — all 2-of-2 multisigs operational.

### MNX Markets

`https://testnet.mnx.fi/api/markets` → `401 Protected deployment`  
Vercel password protection is active. Market data **unavailable** this run.

---

## Database Summary

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1163 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (N/A sentinel) |

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
