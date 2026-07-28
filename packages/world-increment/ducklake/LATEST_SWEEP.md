# World-Increment Sweep — 2026-07-28

## Sweep Metadata
- **Date:** 2026-07-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Branch:** `world-increment/sweep-2026-07-28-0907`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots (detail) | 111 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | SPA only (no JSON API) |

---

## GF(3) Color Chain — 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## GitHub Social Graph — Repo Counts

| Source | Type | Total Repos | Most Recent Push |
|--------|------|-------------|-----------------|
| plurigrid | org | 100 | 2026-07-28 (gorj) |
| kubeflow | org | 49 | 2026-07-28 (sdk, trainer) |
| TeglonLabs | org | 5 | 2026-06-08 (jank-crane) |
| bmorphism | user | 106 | 2026-07-21 (Gay.jl) |
| zubyul | user | 49 | 2026-04-24 (voice-observatory) |
| migalkin | user | 19 | 2026-07-10 (kgcourse2021) |
| DJedamski | user | 6 | 2018-02-26 (kaggle_ncaa18) |
| wasita | user | 12 | 2026-07-21 (wasita.github.io) |
| kristinezheng | user | 5 | 2026-07-01 (kristinezheng.github.io) |
| M1shaaa | user | 8 | 2026-02-04 (M1shaaa profile) |
| AustinCStone | user | 41 | 2026-07-15 (byteruckus) |

---

## Top Repos by Source (Stars)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| plurigrid/asi | HTML | 52 | 2026-07-10 |
| plurigrid/ontology | JavaScript | 8 | 2025-05-27 |
| plurigrid/vcg-auction | Rust | 7 | 2023-03-16 |
| plurigrid/gorj | Clojure | 1 | 2026-07-28 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| kubeflow/kubeflow | — | 15,794 | 2026-07-28 |
| kubeflow/pipelines | Python | 4,171 | 2026-07-27 |
| kubeflow/spark-operator | Python | 3,142 | 2026-07-26 |
| kubeflow/trainer | Go | 2,156 | 2026-07-28 |
| kubeflow/katib | Python | 1,692 | 2026-07-20 |

### bmorphism (106 repos, top by recent activity)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| bmorphism/anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| bmorphism/Gay.jl | Julia | 2 | 2026-07-21 |
| bmorphism/gay-chat | Scheme | 0 | 2026-07-14 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| bmorphism/penrose-mcp | JavaScript | 9 | 2026-06-24 |

### zubyul (49 repos, top by recent activity)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| zubyul/voice-observatory | Python | 0 | 2026-04-24 |
| zubyul/ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |
| zubyul/gay-world | Python | 1 | 2026-04-05 |
| zubyul/big-bad-plurigrid-quiz | Emacs Lisp | 0 | 2026-04-09 |

---

## Hamming Swarm — Aptos Wallet Snapshot

**All 28 addresses (alice, bob, A–Z) returned 0 APT balance.**
The `CoinStore<AptosCoin>` resource was absent for all wallets, indicating either unfunded addresses or no on-chain initialization.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793acde… | 0.00 |
| bob | 0x0a3c00c5… | 0.00 |
| A–Z | (all 26) | 0.00 each |

---

## Hamming Swarm — Multisig Contract Probes

All 5 multisig contracts responded and are **healthy** (2-of-N threshold).

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428… | 2 | ✓ |
| A-G | 0xf56c4a1c… | 2 | ✓ |
| Y-Z | 0xd3ffe181… | 2 | ✓ |
| S-T | 0x3b1c3ae9… | 2 | ✓ |
| V-W | 0x40fad7b4… | 2 | ✓ |

---

## MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a **Next.js SPA** — `/api/markets`, `/api/v1/markets`, `/api/tickers` return HTML. No JSON market data extractable this sweep.

---

## Notable Activity Since Last Sweep (2026-04-12)

- **plurigrid/gorj** pushed 2026-07-28 (active development)
- **plurigrid/eirobri** pushed 2026-07-21 (Clojure)
- **plurigrid/asi** pushed 2026-07-10 (52 stars, top plurigrid property)
- **bmorphism/Gay.jl** pushed 2026-07-21 (wide-gamut color library, 188 open issues)
- **bmorphism/gay-chat** created 2026-07-14 (Spritely Brassica / Scheme)
- **wasita** added pnas-typst-template + wm-cv (July 2026)
- **AustinCStone/byteruckus** created 2026-07-15
- **kubeflow/sdk** now 130 stars (universal Python SDK for AI on K8s)
- **kubeflow/mcp-server** 29 stars (MCP integration for Kubeflow)
