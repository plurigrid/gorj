# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-06-08T08:14Z  
**DuckDB:** `world-increments.duckdb`  
**GF(3) color chain:** trit=0 → ERGODIC #d3869b | trit=1 → PLUS #b8bb26 | trit=-1 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 156 |
| kubeflow | org | 48 | 102,046 |
| TeglonLabs | org | 5 | 14 |
| bmorphism | user | 97 | 262 |
| zubyul | user | 49 | 40 |
| migalkin | user | 19 | 834 |
| DJedamski | user | 6 | 17 |
| wasita | user | 11 | 11 |
| kristinezheng | user | 5 | 0 |
| M1shaaa | user | 8 | 0 |
| AustinCStone | user | 40 | 324 |

### Top Repos by Stars

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,707 | — | 2026-05-24 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-06 |
| kubeflow/spark-operator | 3,126 | Python | 2026-06-04 |
| kubeflow/trainer | 2,112 | Go | 2026-06-05 |
| kubeflow/katib | 1,685 | Python | 2026-06-05 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,020 | YAML | 2026-06-05 |
| kubeflow/arena | 812 | Go | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| plurigrid/asi | 25 | HTML | 2026-04-26 |

### Notable Activity (pushed 2026-06-08)

- **plurigrid/gorj** (437 open issues): MCP server + GF(3) trit coloring for Clojure REPL orchestration — pushed today
- **TeglonLabs/jank-crane** (C++): crane-jank converged-IR hub with GF3 convergence maps — pushed today
- **kubeflow/dashboard** (TypeScript): Kubeflow Central Dashboard — pushed today
- **bmorphism/Gay.jl** (189 open issues): Wide-gamut color sampling with splittable determinism — pushed today

### Zubyul Social Graph Highlights

- **zubyul**: `nash-tui`, `nash-web` (NASH token TUI/WASM), `Gay.jl`, `tilelang-kernels` (TileLang GPU kernels for GF(3) trit classification on NVIDIA GB10 Blackwell)
- **migalkin**: knowledge graph embeddings (NodePiece, StarE, RWL, NBFNet_mlx for Apple Silicon)
- **wasita**: Svelte/SvelteKit personal site, `magic-garden` Discord bot
- **AustinCStone**: `TextGAN` (92★ text GAN), `StereoVisionMRF`, ML/CV research repos

### GF(3) World Increment Distribution

| Name | Color | Trit | Count |
|------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 21 |
| PLUS | #b8bb26 | +1 | 23 |
| MINUS | #cc241d | -1 | 23 |

Total world increments (cumulative including prior sweeps): **67**  
New increments this run: **44** (11 github sweeps + 28 aptos wallets + 5 multisig probes)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Result:** All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

Wallets exist on-chain but have no registered APT CoinStore — these are Move-native accounts that have not activated the coin module. Balance = 0 APT (unregistered).

| World | Address (prefix) | Balance |
|-------|-----------------|---------|
| alice | 0xc793acde... | null (no CoinStore) |
| bob | 0x0a3c00c5... | null (no CoinStore) |
| A | 0x8699edc0... | null (no CoinStore) |
| B–Z | ... | null (no CoinStore) |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts respond and require **2 of N signatures** (healthy).

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — `testnet.mnx.fi` is protected by Vercel deployment authentication (HTTP 401). Market data requires a visitor password or OIDC bypass token. No data extracted.

---

## DuckDB Schema Summary

| Table | Rows |
|-------|------|
| world_increments | 67 |
| repo_snapshots | 1,127 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

Database: `packages/world-increment/ducklake/world-increments.duckdb`

## GF(3) Assignment Rule

- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=**MINUS**
