# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-28

## Sweep Metadata
- **Date:** 2026-07-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 320 |
| Total Repo Snapshots | 320 |
| Aptos Wallet Snapshots | 28 |
| Multisig Probes | 5 (all healthy) |
| Sources Covered | 3 orgs + 8 users (incl. zubyul social graph) |

---

## GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 106 |
| 1 | `#b8bb26` | PLUS | 107 |
| 2 (−1) | `#cc241d` | MINUS | 107 |

GF(3) rule: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`

---

## Repo Counts by Source (2026-07-28)

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| TeglonLabs | org | 5 |
| migalkin | user (social graph) | 5 |
| wasita | user (social graph) | 3 |
| AustinCStone | user (social graph) | 3 |
| kristinezheng | user (social graph) | 2 |
| DJedamski | user (social graph) | 2 |
| M1shaaa | user (social graph) | 2 |
| **TOTAL** | | **320** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — 28 Addresses

All 28 addresses (alice, bob, A–Z) returned **0.0 APT** — no `CoinStore<AptosCoin>` resource registered. Accounts are unfunded or use alternative coin types.

### Multisig Contract Probes — 5 Pairs

All 5 multisig contracts are **healthy** (num_signatures_required = 2).

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...7003 | 2 | ✓ |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ |

### MNX Markets

`https://testnet.mnx.fi` is a **Next.js SPA** — API endpoints return empty responses. Market data is client-rendered and unavailable via direct probe.

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

## Notable Highlights
- **migalkin/NodePiece**: ★144 Python, ICLR'22 knowledge graph embeddings
- **AustinCStone/TextGAN**: ★92 Python, GAN text generation (TensorFlow)
- **migalkin/StarE**: ★89 Python, EMNLP 2020 hyper-relational KG message passing
- **TeglonLabs/jank-crane**: C++, GF3 convergence maps — pushed 2026-06-08
- **wasita/wasita.github.io**: Svelte, pushed 2026-07-21 (freshest social-graph node)
- **All 5 multisig pairs** (A-B, A-G, Y-Z, S-T, V-W): healthy, sigs=2
- **Hamming swarm wallets**: 28 addresses, all at 0 APT — no live mainnet funds detected
