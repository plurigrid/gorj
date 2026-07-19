# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-19

## Sweep Metadata
- **Date:** 2026-07-19
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 346 |
| Total Repo Snapshots (cumulative) | 1267 |
| New increments this sweep | 323 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution

| Name | Color | Count (cumulative) |
|------|-------|---------------------|
| ERGODIC | #d3869b | 114 |
| PLUS | #b8bb26 | 116 |
| MINUS | #cc241d | 116 |

GF(3) rule: `id%3==0 → ERGODIC` · `id%3==1 → PLUS` · `id%3==2 → MINUS`

---

## Top Repos by Source (this sweep)

### plurigrid (103 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-19 |
| place | TeX | 1 | 2026-07-14 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15781 | 2026-07-10 |
| pipelines | Python | 4167 | 2026-07-19 |
| spark-operator | Python | 3139 | 2026-07-17 |
| trainer | Go | 2151 | 2026-07-18 |
| katib | Python | 1691 | 2026-07-16 |
| mcp-server | Python | 28 | 2026-07-19 |
| sdk | Python | 126 | 2026-07-19 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (106 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gay-chat | Scheme | 0 | 2026-07-14 |
| Gay.jl | Julia | 2 | 2026-07-14 |
| satreadout | HTML | 0 | 2026-06-20 |

### Social Graph

| User | Top Repo | Stars |
|------|----------|-------|
| migalkin | NodePiece (KG embedding ICLR'22) | 144 |
| AustinCStone | TextGAN | 92 |
| wasita | wasita.github.io (Svelte) | 1 |
| kristinezheng | auditory-illusion | 0 |
| DJedamski | Getting-and-Cleaning-Data | 1 |
| M1shaaa | M1shaaa (profile) | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-07-19)

All 28 addresses queried (alice, bob, A–Z). All returned **0.0 APT**.  
CoinStore resources responded but coin values are zero — either unfunded or drained.

### Multisig Contract Probes

All 5 contracts **healthy**, all requiring **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — returns authentication-required SPA. No public API endpoint reachable. mnx_snapshots table remains empty this sweep.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,781★ — up 216★ since last sweep (2026-04-12)
- **kubeflow/pipelines**: 4,167★ — up 48★ since last sweep
- **plurigrid/asi**: 31★ — up 15★, pushed 2026-07-10
- **migalkin/NodePiece**: 144★ — ICLR'22 KG embedding, up 1★
- **AustinCStone/TextGAN**: 92★ — TensorFlow text GAN
- **TeglonLabs/jank-crane**: new repo (2026-06-08), C++, GF3 convergence maps
- **kubeflow/mcp-server**: new repo, 28★, pushed 2026-07-19
- **Hamming swarm**: 28/28 addresses at 0.0 APT; all 5 multisigs online at 2-of-N
