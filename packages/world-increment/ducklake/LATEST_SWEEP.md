# World-Increment Sweep + Hamming Snapshot — 2026-04-17

## Sweep Metadata
- **Date:** 2026-04-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain
| id%3 | trit | color | name |
|------|------|-------|------|
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |
| 0 | 0 | `#d3869b` | ERGODIC |

### Sources Swept

| ID | Source | Type | GF3 | Color | Repos |
|----|--------|------|-----|-------|-------|
| 1 | plurigrid | org | PLUS | `#b8bb26` | 15 |
| 2 | kubeflow | org | MINUS | `#cc241d` | 15 |
| 3 | TeglonLabs | org | ERGODIC | `#d3869b` | 4 |
| 4 | bmorphism | user | PLUS | `#b8bb26` | 12 |
| 5 | zubyul | user | MINUS | `#cc241d` | 10 |
| 6 | migalkin | user (social) | ERGODIC | `#d3869b` | 7 |
| 7 | DJedamski | user (social) | PLUS | `#b8bb26` | 5 |
| 8 | wasita | user (social) | MINUS | `#cc241d` | 7 |
| 9 | kristinezheng | user (social) | ERGODIC | `#d3869b` | 5 |
| 10 | M1shaaa | user (social) | PLUS | `#b8bb26` | 5 |
| 11 | AustinCStone | user (social) | MINUS | `#cc241d` | 6 |
| 12 | hamming_swarm | event | ERGODIC | `#d3869b` | — |

**Total repo snapshots in DB:** 91

### Notable Repos (by stars)

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,580 | — | 2026-01-05 |
| kubeflow/pipelines | 4,121 | Python | 2026-04-17 |
| kubeflow/spark-operator | 3,117 | Python | 2026-04-16 |
| kubeflow/trainer | 2,085 | Go | 2026-04-17 |
| kubeflow/katib | 1,679 | Python | 2026-04-14 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,010 | YAML | 2026-04-11 |
| kubeflow/arena | 810 | Go | 2026-04-16 |
| migalkin/NodePiece | 143 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| migalkin/kgcourse2021 | 25 | HTML | 2025-08-04 |
| plurigrid/asi | 17 | HTML | 2026-04-13 |

### Most Active (plurigrid/bmorphism ecosystem)

- `plurigrid/gorj` — **214 open issues**, pushed 2026-04-17 (this very repo!)
- `bmorphism/Gay.jl` — **187 open issues**, wide-gamut splittable SPI color sampling
- `plurigrid/nanoclj-zig` — **21 open issues**, NaN-boxed Clojure in Zig 0.15
- `zubyul/plurigrid-site` — **11 open issues**, Svelte site

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z = 28 wallets)

Probed via Aptos mainnet: `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**All 28 addresses returned 0 APT** — CoinStore resource not found (accounts uncreated or hold no native APT).

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Probes (5 pairs)

All returned `num_signatures_required = 2` — **5/5 healthy**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

- `/api/markets` → DNS cache overflow (unreachable from this network)
- `/api/v1/markets` → DNS cache overflow
- `/markets` → Next.js SPA HTML (no SSR market data)

**Status: unavailable.** No rows inserted into `mnx_snapshots`.

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 12 |
| repo_snapshots | 91 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

## GF(3) Rule
- `id % 3 == 0` → trit=0, `#d3869b` ERGODIC
- `id % 3 == 1` → trit=1, `#b8bb26` PLUS
- `id % 3 == 2` → trit=-1, `#cc241d` MINUS
