# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-19 (automated sweep)  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Source Coverage

| Source | Type | Sample | Notable |
|--------|------|--------|---------|
| plurigrid | org | 10 repos | gorj(668 issues, pushed today), asi(26★), nanoclj-zig, zig-syrup |
| kubeflow | org | 10 repos | kubeflow(15,736★), pipelines(4,154★), spark-operator(3,127★) |
| TeglonLabs | org | 5 repos | jank-crane(C++, GF3 convergence maps, 2026-06-08) |
| bmorphism | user | 10 repos | Gay.jl(187 issues, pushed today!), ocaml-mcp-sdk(61★), satreadout(Lean) |
| zubyul | user | 10 repos | gay-world, nash-tui, quantum-telephone, ghostel-emacs-worlds |
| migalkin | user | 5 repos | NodePiece(144★), StarE(89★) — knowledge graph ML |
| DJedamski | user | 3 repos | stats/ML repos, last active 2023 |
| wasita | user | 5 repos | wasita.github.io(Svelte, 2026-06-15), send2kobo, magic-garden |
| kristinezheng | user | 2 repos | MIT cognitive science |
| M1shaaa | user | 2 repos | Yale/MIT research |
| AustinCStone | user | 4 repos | TextGAN(92★), bmfork, EpsteinSearch |

**Total: 66 world increments, 66 repo snapshots**

### GF(3) Trit Color Chain

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 22 |
| +1 | `#b8bb26` | PLUS | 22 |
| -1 | `#cc241d` | MINUS | 22 |

Perfect trit balance across 66 increments.

### Top Repos by Stars

| Repo | Stars | Lang | Last Push |
|------|-------|------|-----------|
| kubeflow/kubeflow | 15,736 | — | 2026-06-18 |
| kubeflow/pipelines | 4,154 | Python | 2026-06-19 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-18 |
| kubeflow/trainer | 2,116 | Go | 2026-06-18 |
| kubeflow/katib | 1,683 | Python | 2026-06-15 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,025 | YAML | 2026-06-18 |
| kubeflow/arena | 813 | Go | 2026-05-07 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| plurigrid/asi | 26 | HTML | 2026-06-10 |

### Notable Activity (Today, 2026-06-19)

- **plurigrid/gorj**: 668 open issues, pushed 08:10 UTC — most active plurigrid repo
- **bmorphism/Gay.jl**: 187 open issues, pushed 00:48 UTC — GF(3) color engine active
- **kubeflow/pipelines**: pushed 08:33 UTC
- **kubeflow/mcp-apache-spark-history-server**: pushed 00:32 UTC, 177★

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

Ledger version at query time: **~5,813,713,833** (epoch 16229, block 841,826,872)

### Wallet Balances (28 addresses: alice, bob, A–Z)

All 28 addresses return `resource_not_found` for `0x1::coin::CoinStore<AptosCoin>`.
Wallets exist on mainnet but have no APT coin store initialized (unfunded or using FA standard).

| World | Balance |
|-------|---------|
| alice, bob, A–Z (all 28) | no CoinStore / 0 APT |

### Multisig Contract Probes

| Pair | Address (short) | Threshold | Status |
|------|-----------------|-----------|--------|
| A-B | 0x0da4...7003 | 2-of-N | ✅ HEALTHY |
| A-G | 0xf56c...0096 | 2-of-N | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2-of-N | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | 2-of-N | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | 2-of-N | ✅ HEALTHY |

**All 5 multisig contracts healthy at threshold=2.**

### MNX Markets

**UNAVAILABLE** — `testnet.mnx.fi` requires Vercel deployment protection password. No market data accessible.

---

## DuckDB Tables

```
world_increments   66 rows  (GF3 color-chained push events)
repo_snapshots     66 rows  (repo metadata: stars, forks, language, pushed_at)
aptos_snapshots    28 rows  (all balance_apt=NULL — no CoinStore)
multisig_probes     5 rows  (all threshold=2, healthy=TRUE)
mnx_snapshots       0 rows  (unavailable)
```

---

*world-increment-sweep + hamming-swarm-snapshot agent | 2026-06-19*
