# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Total Repo Snapshots | 1,326 |
| Sources Covered | 3 orgs + 8 users + social graph |
| Aptos Wallets Snapshotted | 28 |
| Multisig Probes | 5/5 healthy |
| MNX Markets | unavailable (Vercel auth) |

---

## GF(3) Color Chain — Increment #12 (this run)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 12 | multi-source sweep + hamming snapshot | 0 | `#d3869b` | **ERGODIC** |

GF(3) id%3=0 → trit=0 → **ERGODIC** `#d3869b`

---

## Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | social | 30 |
| migalkin | social | 19 |
| wasita | social | 11 |
| M1shaaa | social | 8 |
| DJedamski | social | 6 |
| kristinezheng | social | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **382** |

## Top Repos by Stars (this sweep)

| Repo | Stars | Language | Pushed At |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,777 | — | 2026-07-14 |
| kubeflow/pipelines | 4,165 | Python | 2026-07-14 |
| kubeflow/spark-operator | 3,135 | Python | 2026-07-11 |
| kubeflow/trainer | 2,139 | Go | 2026-07-11 |
| kubeflow/katib | 1,690 | Python | 2026-07-10 |
| migalkin/NodePiece | 144 | Python | 2024-09 |
| AustinCStone/TextGAN | 92 | Python | 2018 |
| migalkin/StarE | 89 | Python | 2023 |
| plurigrid/asi | 30 | HTML | 2026-07-10 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-07-14)

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.43643352 |
| bob | 0x0a3c...2d5d | **12.657007** |
| A | 0x8699...9d7a | 0.051767 |
| B | 0x3f89...b13 | 0.036256 |
| C | 0x38b9...35e | 0.010185 |
| D | 0xf776...dd1 | 0.011629 |
| E | 0xdc1d...d36 | 0.009372 |
| F | 0x18a1...f71 | **1.960516** |
| G | 0x69a3...f32 | 0.000681 |
| H | 0xce67...00f | 0.001681 |
| I | 0x070f...c9 | 0.000681 |
| J | 0x4d96...f54 | **1.895093** |
| K | 0xa732...dc4 | 0.161961 |
| L | 0x7c2e...ba9 | **1.927269** |
| M | 0x6fed...e9 | 0.112285 |
| N | 0xe7dd...b2c | 0.106121 |
| O | 0x7325...89d | 0.210136 |
| P | 0x6218...948 | 0.140136 |
| Q | 0xac40...a9 | 0.103240 |
| R | 0x7ce6...e10 | 0.090217 |
| S | 0xb875...386 | 0.091788 |
| T | 0x3578...588 | 0.073713 |
| U | 0x7586...956 | 0.055773 |
| V | 0xb59d...2c3 | 0.048833 |
| W | 0x5f32...7b0 | 0.040705 |
| X | 0xa95c...47d | 0.042577 |
| Y | 0xd8e3...4c4 | 0.044449 |
| Z | 0x7af0...97c | 0.024268 |

**Total across 28 wallets:** 20.3448 APT  
**Largest:** bob (12.657 APT) · F (1.961) · L (1.927) · J (1.895)  
**Dust (<0.01 APT):** G, H, I, Z  

### Multisig Probes (5/5 healthy, all 2-of-N)

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ |
| A-G | 0xf56c...096 | 2 | ✅ |
| Y-Z | 0xd3ff...883 | 2 | ✅ |
| S-T | 0x3b1c...883 | 2 | ✅ |
| V-W | 0x40fa...b6d | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)

**Status: unavailable** — protected by Vercel deployment authentication.

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

### GitHub
- **kubeflow/kubeflow**: 15,777 stars — ML platform, actively pushed today
- **plurigrid/asi**: 30★ — "everything is topological chemputer!" pushed 2026-07-10
- **TeglonLabs/jank-crane**: new C++ repo, "GF3 convergence maps" — June 2026
- **wasita/wm-cv** and **wasita.github.io**: both pushed today 2026-07-14
- **migalkin** focus: knowledge graph embedding research (NodePiece 144★, StarE 89★)

### Aptos Hamming Swarm
- All 28 wallets responsive; total swarm balance 20.34 APT
- `bob` dominates at 12.657 APT (62% of swarm)
- `F`, `L`, `J` each hold ~1.9 APT; rest are small/dust
- All 5 multisig pairs require exactly 2-of-N — no config drift detected

### Increment 12 (this run): ERGODIC `#d3869b`
