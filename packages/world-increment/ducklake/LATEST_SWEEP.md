# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-26

## Sweep Metadata
- **Date:** 2026-06-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this run) | 324 |
| Total World Increments (cumulative) | 347 |
| Total Repo Snapshots (cumulative) | 1268 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Wallets Probed | 28 |
| Multisig Accounts Probed | 5 |

---

## GF(3) Color Chain Distribution (this run: 324 increments)

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 115 |
| PLUS | +1 | `#b8bb26` | 116 |
| MINUS | -1 | `#cc241d` | 116 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 40 |
| **TOTAL (new)** | | **391** |

### Top Repos by Source

**plurigrid (100 repos, most active 2026-06-26):**
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 26 | 2026-06-26 |
| gorj | Clojure | 0 | 2026-06-26 (839 issues!) |
| ontology | JavaScript | 8 | 2025-05-27 |
| nash-portal | Rust | 2 | 2026-05-19 |
| zig-syrup | Zig | 2 | 2026-04-30 |

**kubeflow (48 repos):**
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,745 | 2026-06-18 |
| pipelines | Python | 4,156 | 2026-06-26 |
| spark-operator | Python | 3,128 | 2026-06-26 |
| trainer | Go | 2,122 | 2026-06-26 |
| katib | Python | 1,685 | 2026-06-23 |
| mcp-server | Python | 17 | 2026-06-24 |

**TeglonLabs (5 repos):**
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |

**bmorphism (100 repos):**
| Repo | Language | Stars |
|------|----------|-------|
| Gay.jl | Julia | 2 (187 issues) |
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 23 |

**Social graph highlights:**
- `migalkin/NodePiece` — 144★ (ICLR'22 KG representation learning)
- `migalkin/StarE` — 89★ (EMNLP 2020 hyper-relational KGs)
- `AustinCStone/TextGAN` — 92★ (TF text generation GAN)
- `wasita` — active 2026, Svelte/Python/TypeScript stack

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses — alice, bob, A–Z)

All 28 wallets queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 addresses returned 0 APT.**

Addresses are query-reachable on mainnet but have either zero balance or no initialized CoinStore resource. No non-zero balances detected in the Hamming swarm.

### Multisig Contract Probes

All 5 probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

**All 5 multisig accounts healthy — 2-of-2 threshold across the board.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — site requires Vercel authentication. Both root `/` and `/api/markets` return an HTML auth gate. No market data extractable without credentials.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
