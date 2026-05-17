# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-17 (UTC)  
**GF(3) Color Chain:** PLUS #b8bb26 → MINUS #cc241d → ERGODIC #d3869b → …

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| ID | GF3 Trit | Color | Name | Type | Source | Repos |
|----|----------|-------|------|------|--------|-------|
| 1 | +1 | `#b8bb26` PLUS | PLUS | org | plurigrid | 31 |
| 2 | -1 | `#cc241d` MINUS | MINUS | org | kubeflow | 27 |
| 3 | 0 | `#d3869b` ERGODIC | ERGODIC | org | TeglonLabs | 4 |
| 4 | +1 | `#b8bb26` PLUS | PLUS | user | bmorphism | 30 |
| 5 | -1 | `#cc241d` MINUS | MINUS | user | zubyul | 19 |
| 6 | 0 | `#d3869b` ERGODIC | ERGODIC | user | migalkin | 6 |
| 7 | +1 | `#b8bb26` PLUS | PLUS | user | DJedamski | 5 |
| 8 | -1 | `#cc241d` MINUS | MINUS | user | wasita | 5 |
| 9 | 0 | `#d3869b` ERGODIC | ERGODIC | user | kristinezheng | 4 |
| 10 | +1 | `#b8bb26` PLUS | PLUS | user | M1shaaa | 3 |
| 11 | -1 | `#cc241d` MINUS | MINUS | user | AustinCStone | 7 |

**Total repos snapshotted:** 141

### Notable Repos (by stars)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,636 | — | 2026-05-07 |
| kubeflow/pipelines | 4,139 | Python | 2026-05-15 |
| kubeflow/spark-operator | 3,125 | Python | 2026-05-15 |
| kubeflow/katib | 1,682 | Python | 2026-05-09 |
| kubeflow/examples | 1,463 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,017 | YAML | 2026-05-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| plurigrid/gorj | 0 | Clojure | 2026-05-16 (220 open issues) |
| bmorphism/Gay.jl | 1 | Julia | 2026-05-16 (189 open issues) |

### Hot Activity (pushed within 48h of sweep)

- `plurigrid/gorj` — pushed 2026-05-16 (this repo, 220 open issues)
- `bmorphism/Gay.jl` — pushed 2026-05-16 (189 open issues)
- `kubeflow/manifests` — pushed 2026-05-16
- `kubeflow/dashboard` — pushed 2026-05-16
- `bmorphism/oxgame` — pushed 2026-05-15 (OCaml open-games)

### Zubyul Social Graph Snapshot

| User | Repos | Top Language | Most Recent Repo |
|------|-------|-------------|-----------------|
| migalkin | 6 | Python | NodePiece (KG research, ICLR'22) |
| DJedamski | 5 | R/Jupyter | kaggle_ncaa18 |
| wasita | 5 | Svelte | wasita.github.io, wm-cv |
| kristinezheng | 4 | HTML | kristinezheng.github.io |
| M1shaaa | 3 | TypeScript | lab-bookshelf- |
| AustinCStone | 7 | Python | EpsteinSearch, TextGAN (92★) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (APT)

All 28 wallets queried via `https://fullnode.mainnet.aptoslabs.com/v1`.  
**Result:** All addresses return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — no APT CoinStore registered on mainnet at any of these addresses.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C–Z (24) | various | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts healthy. All require **2-of-2** signatures (`num_signatures_required = 2`).

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

Site is a Next.js SPA. All API path probes (`/api/markets`, `/api/v1/markets`) return the HTML shell — no REST API accessible without browser JS execution. Recorded as `SPA-unavailable`.

---

## DuckDB Schema

```
packages/world-increment/ducklake/world-increments.duckdb
├── world_increments     (11 rows — one per source, GF3 color-chained)
├── repo_snapshots       (141 rows — full repo metadata)
├── aptos_snapshots      (28 rows — hamming swarm wallets A-Z + alice + bob)
├── multisig_probes      (5 rows — A-B, A-G, Y-Z, S-T, V-W; all 2-of-2)
└── mnx_snapshots        (1 row — SPA-unavailable)
```
