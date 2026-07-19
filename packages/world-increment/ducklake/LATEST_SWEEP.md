# World-Increment Sweep — 2026-07-19 (+ Hamming Swarm Snapshot)

## Sweep Metadata
- **Date:** 2026-07-19
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos ledger:** version 6353123420, epoch 16593, block height 910294496

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all sweeps) | 72 |
| Total Repo Snapshots (all sweeps) | 993 |
| This sweep — repos indexed | 49 |
| Sources Covered | 3 orgs + 8 users |
| Aptos wallets probed | 28 |
| Multisig contracts probed | 5 |
| MNX markets | unavailable (Vercel auth) |

---

## GF(3) Color Chain — This Sweep (49 new increments, IDs 24–72)

GF(3) rule: `id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d`

Cycle continues from prior sweeps. 49 new repo_snapshot increments added, covering plurigrid (11), kubeflow (10), TeglonLabs (5), bmorphism (6), zubyul (4), migalkin (4), DJedamski (2), wasita (2), kristinezheng (1), M1shaaa (1), AustinCStone (3).

---

## Top Repos by Source (2026-07-19)

### plurigrid (103 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-26 |
| nash-portal | Rust | 2 | 2026-05-19 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| gorj | Clojure | 1 | 2026-07-19 (today, 1259 open issues) |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,781 | 2026-07-10 |
| pipelines | Python | 4,167 | 2026-07-19 |
| spark-operator | Python | 3,139 | 2026-07-17 |
| trainer | Go | 2,151 | 2026-07-18 |
| katib | Python | 1,691 | 2026-07-16 |
| mcp-server | Python | 29 | 2026-07-19 (new) |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 (new: GF3 convergence maps) |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (106 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |
| Gay.jl | Julia | 2 | 2026-07-14 (187 open issues) |
| shitcoin | Python | 5 | 2026-04-08 |

### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 24 | 2026-07-10 |

### AustinCStone (41 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TextGAN | Python | 92 | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |
| byteruckus | HTML | 0 | 2026-07-15 (new) |

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 worlds queried at ledger version 6353123420 (epoch 16593, block 910294496).

| World | Address | APT |
|---|---|---|
| alice | 0xc793...cc7b | 0.00 (CoinStore not registered) |
| bob–Z | 0x0a3c...–0x7af0... | 0.00 each (all 27) |

**Finding:** All 28 Hamming swarm wallets hold 0 APT. `alice` (0xc793…) returns `resource_not_found` — the account has no CoinStore registered, meaning it has never received APT on mainnet.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4…7003 | 2 | ✅ |
| A-G | 0xf56c…0096 | 2 | ✅ |
| Y-Z | 0xd3ff…b883 | 2 | ✅ |
| S-T | 0x3b1c…7883 | 2 | ✅ |
| V-W | 0x40fa…eb6d | 2 | ✅ |

All 5 contracts healthy — 2-of-N multisig, all live on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Protected by Vercel deployment authentication. No market data accessible.

---

## Repo Counts by Source (as of 2026-07-19)

| Source | Type | Total Repos |
|--------|------|-------|
| bmorphism | user | 106 |
| plurigrid | org | 103 |
| AustinCStone | user | 41 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| M1shaaa | social | 8 |
| wasita | social | 12 |
| DJedamski | social | 6 |
| kristinezheng | social | 5 |
| TeglonLabs | org | 5 |

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

## Notable Highlights (2026-07-19)

- **kubeflow/kubeflow**: 15,781★ (+216 since Apr sweep) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,167★ — updated today
- **kubeflow/spark-operator**: 3,139★ — updated Jul 17
- **migalkin/NodePiece**: 144★ — ICLR'22 compositional KG embeddings
- **bmorphism/ocaml-mcp-sdk**: 61★ — OCaml SDK for MCP (Jane Street oxcaml_effect)
- **AustinCStone/TextGAN**: 92★ — text GAN
- **plurigrid/asi**: 31★ (+15 since Apr sweep) — growing fast
- **plurigrid/gorj**: 1,259 open issues — this repo, most active in sweep
- **bmorphism/Gay.jl**: 187 open issues — high activity
- **TeglonLabs/jank-crane**: New repo (Jun 2026) — C++, GF3 convergence maps, crane-jank IR
- **AustinCStone/byteruckus**: New repo (Jul 15 2026) — HTML
- **kubeflow/mcp-server**: New MCP server (29★, 35 forks) — active Jul 19
- **Hamming swarm**: All 28 wallets at 0 APT; all 5 multisigs healthy (2-of-N)
