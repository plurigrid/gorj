# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-03

## Sweep Metadata
- **Date:** 2026-07-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 342 |
| Total Repo Snapshots | 342 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution

| GF3 Name | Trit | Hex | Count |
|----------|------|-----|-------|
| ERGODIC | 0 | `#d3869b` | 113 |
| PLUS | +1 | `#b8bb26` | 115 |
| MINUS | -1 | `#cc241d` | 114 |

GF(3) rule: `id mod 3 == 0` → ERGODIC · `id mod 3 == 1` → PLUS · `id mod 3 == 2` → MINUS

---

## Top Repos by Source

### plurigrid (100 repos, pushed as of 2026-07-03)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 28 | 2026-06-29 |
| place | TeX | 1 | 2026-06-29 |
| shrimp | — | 0 | 2026-07-03 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,758 | 2026-06-18 |
| pipelines | Python | 4,167 | 2026-07-03 |
| spark-operator | Python | 3,131 | 2026-07-02 |
| trainer | Go | 2,129 | 2026-07-02 |
| community-distribution | YAML | 1,028 | 2026-07-03 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

### bmorphism (100 repos)
| Repo | Language | Pushed |
|------|----------|--------|
| Gay.jl | Julia | 2026-07-03 |
| satreadout | HTML | 2026-06-20 |
| bci-preview | HTML | 2026-06-20 |

### Social Graph
| User | Notable Repo | Stars |
|------|-------------|-------|
| migalkin | NodePiece (ICLR'22 KG embeddings) | 144 |
| migalkin | StarE (EMNLP 2020) | 89 |
| AustinCStone | TextGAN | 92 |
| wasita | wasita.github.io | 1 |
| kristinezheng | Green-Machine (HackMIT) | 0 |
| DJedamski | Getting-and-Cleaning-Data | 1 |
| M1shaaa | lab-bookshelf- | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 swarm addresses probed via `https://fullnode.mainnet.aptoslabs.com`. Every address returned **0.0 APT** — no active `0x1::coin::CoinStore<AptosCoin>` resource found (accounts uninitialized or unfunded on mainnet).

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A–Z (26) | 0x8699...→ 0x7af0... | 0.0 each |

**Total APT in swarm: 0.0**

### Multisig Contract Probes

All 5 pairs return `num_signatures_required = 2` — **all healthy**.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ healthy |
| A-G | 0xf56c...096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✅ healthy |
| S-T | 0x3b1c...883 | 2 | ✅ healthy |
| V-W | 0x40fa...b6d | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — HTTP 401, Vercel deployment protection active. No market data retrievable without auth bypass token.

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
- **kubeflow/kubeflow**: 15,758 stars (+193 since 2026-04-12) — ML platform for K8s growing fast
- **kubeflow/pipelines**: 4,167 stars — pushed 2026-07-03 (active today)
- **plurigrid/asi**: 28 stars (+12 since April) — strong growth
- **plurigrid/shrimp**: pushed 2026-07-03 — newest/hottest plurigrid repo
- **bmorphism/Gay.jl**: Julia — pushed 2026-07-03
- **TeglonLabs/jank-crane**: new since April — GF3 convergence maps + simonw workflow
- **All 5 multisig pairs**: 2-of-N healthy, contracts live on Aptos mainnet
- **Hamming swarm wallets A–Z**: all show 0 APT balance on mainnet
