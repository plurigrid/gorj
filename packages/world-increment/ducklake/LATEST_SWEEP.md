# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-06-14  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (v1.5.3 Variegata)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found | Notable |
|--------|------|------------|---------|
| plurigrid | org | 101 | gorj (560 open issues!), ontology (8★), vcg-auction (7★) |
| kubeflow | org | 48 | kubeflow/kubeflow (15,721★), pipelines (4,153★), spark-operator (3,128★) |
| TeglonLabs | org | 5 | jank-crane (C++ GF3 convergence maps, pushed 2026-06-08) |
| bmorphism | user | 104 | Gay.jl (189 open issues, pushed 2026-06-14), ocaml-mcp-sdk (61★) |
| zubyul | user | 49 | nash-tui, gay-world, openbci-visualizer |
| migalkin | social | 19 | NodePiece (144★ ICLR'22), StarE (89★ EMNLP'20) |
| wasita | social | 11 | wasita.github.io (active 2026-06-01) |
| AustinCStone | social | 40 | TextGAN (92★) |
| DJedamski | social | 6 | kaggle, R coursera projects |
| kristinezheng | social | 5 | kristinezheng.github.io (active 2026-06-07) |
| M1shaaa | social | 8 | lab-bookshelf, Python-Lookit-Uploads |

**Total sources:** 3 orgs + 8 users  
**Total repos discovered:** ~396 across all sources

### Top Repos by Stars

| Repo | Language | Stars | Forks | Open Issues | Pushed |
|------|----------|-------|-------|-------------|--------|
| kubeflow/kubeflow | — | 15,721 | 2,673 | 3 | 2026-06-11 |
| kubeflow/pipelines | Python | 4,153 | 2,007 | 488 | 2026-06-13 |
| kubeflow/spark-operator | Python | 3,128 | 1,490 | 102 | 2026-06-12 |
| kubeflow/trainer | Go | 2,114 | 969 | 113 | 2026-06-13 |
| kubeflow/katib | Python | 1,683 | 527 | 116 | 2026-06-12 |
| kubeflow/examples | Jsonnet | 1,461 | 756 | 111 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1,023 | 1,065 | 22 | 2026-06-12 |
| kubeflow/arena | Go | 812 | 190 | 44 | 2026-05-07 |
| kubeflow/kale | Python | 694 | 154 | 48 | 2026-06-12 |
| migalkin/NodePiece | Python | 144 | 21 | 0 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 30 | 5 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 16 | 1 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 0 | 2026-03-16 |
| plurigrid/vcg-auction | Rust | 7 | 2 | 1 | 2023-03-16 |
| plurigrid/ontology | JavaScript | 8 | 9 | 16 | 2025-05-27 |

### Most Active Repos (by open issues)

| Repo | Open Issues |
|------|------------|
| plurigrid/gorj | **560** |
| kubeflow/pipelines | 488 |
| bmorphism/Gay.jl | 189 |
| kubeflow/docs-agent | 151 |
| kubeflow/sdk | 132 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` (pink) | ERGODIC | 79 |
| +1 | `#b8bb26` (lime) | PLUS | 81 |
| -1 | `#cc241d` (red) | MINUS | 81 |

Assignment rule: `id % 3 == 0` → ERGODIC, `id % 3 == 1` → PLUS, `id % 3 == 2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (26 Hamming worlds A–Z + alice, bob)

Queried Aptos mainnet via `fullnode.mainnet.aptoslabs.com` (ledger ~v5,724,404,651).

**Result: All 28 wallets return `resource_not_found`** for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

All wallets are unfunded — no APT CoinStore initialized. Balance = **0.00 APT** for all.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0xc793...cc7b | 0.00 |
| bob | 0x0a3c...12d5d | 0.00 |
| A | 0x8699...9d7a | 0.00 |
| B | 0x3f89...cb13 | 0.00 |
| C | 0x38b9...535e | 0.00 |
| D–Z | (remaining 22 addresses) | 0.00 each |

### Multisig Contract Probes (5 pairs)

All 5 probed via POST `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

**5/5 multisig contracts operational**, all require exactly **2-of-N signatures**.

### MNX Testnet Markets

`https://testnet.mnx.fi` — **UNAVAILABLE**  
All paths return Vercel authentication gate. No market data extractable without credentials.  
`mnx_snapshots` table remains empty.

---

## DuckDB Schema

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

## Row Counts

| Table | Rows |
|-------|------|
| world_increments | 241 |
| repo_snapshots | 1,172 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## Key Findings

1. **plurigrid/gorj** has **560 open issues** (2026-06-14) — highest in entire sweep, suggests heavy backlog
2. **bmorphism/Gay.jl** pushed today with 189 open issues — active GF(3) color research in flight
3. **All 28 Hamming Swarm wallets unfunded** — Aptos CoinStore never initialized for these addresses
4. **All 5 multisig contracts healthy** — A-B, A-G, Y-Z, S-T, V-W all require exactly 2 sigs
5. **MNX testnet gated** — Vercel auth required, no public API
6. **kubeflow/kubeflow** dominates stars (15,721) in the sweep — thriving ML-on-K8s ecosystem
7. **TeglonLabs/jank-crane** is newest repo (created 2026-06-08) — GF3 convergence maps for jank compiler IR
8. **kubeflow/mcp-apache-spark-history-server** (177★) notable: MCP integration for Spark debug workflows
