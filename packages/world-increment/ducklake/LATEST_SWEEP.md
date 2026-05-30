# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-30T22:00:00Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| GF(3) | Color | Source | Type | Repos | Total Stars |
|-------|-------|--------|------|-------|-------------|
| PLUS | #b8bb26 | TeglonLabs | org | 4 | 2 |
| MINUS | #cc241d | kubeflow | org | 26 | 33,114 |
| ERGODIC | #d3869b | plurigrid | org | 43 | 75 |
| PLUS | #b8bb26 | migalkin | user | 5 | 276 |
| MINUS | #cc241d | DJedamski | user | 3 | 3 |
| ERGODIC | #d3869b | wasita | user | 4 | 5 |
| PLUS | #b8bb26 | kristinezheng | user | 3 | 0 |
| MINUS | #cc241d | M1shaaa | user | 3 | 0 |
| ERGODIC | #d3869b | AustinCStone | user | 5 | 106 |
| PLUS | #b8bb26 | bmorphism | user | 22 | 209 |
| MINUS | #cc241d | zubyul | user | 16 | 10 |

**Total:** 134 repo snapshots across 11 world_increments

### Notable Repos by Source

**kubeflow** — 33K+ stars, 48 repos. Flagship: `kubeflow/kubeflow` (15,692★), `pipelines` (4,149★), `spark-operator` (3,124★), `trainer` (2,106★, LLM fine-tuning), `mcp-apache-spark-history-server` (173★, recently active)

**plurigrid** — 43 repos, GF(3)/Gay.jl color theme throughout. Flagship: `asi` (23★, "topological chemputer"), `ontology` (8★), `gorj` (267 open issues, pushed today). Active: `nanoclj-zig`, `nash-portal`, `zig-syrup`, `reafference`. Gay.jl ecosystem: `gay-rs`, `gay-go`, `gay-terminal`, `lazygay`, `lazybjj`, `gatomic`

**bmorphism** — 22 repos, heavy MCP server focus: `ocaml-mcp-sdk` (61★, Jane Street oxcaml_effect), `anti-bullshit-mcp-server` (23★), `babashka-mcp-server` (18★), `manifold-mcp-server` (14★). Also: `Gay.jl` (189 open issues), `monero-rental-hash-war` (Haskell OpenGame), `oxgame` (OCaml, active)

**zubyul** — 16 repos including `gay-world`, `ghostty-modifications`, `tilelang-kernels` (GPU kernels for SplitMix64/GF(3)), `big-bad-plurigrid-quiz`, `nash-tui`/`nash-web` (NASH token TUIs)

**migalkin** — Knowledge Graph research: `NodePiece` (144★, ICLR'22), `StarE` (89★, EMNLP 2020), active through 2026

**AustinCStone** — `TextGAN` (92★), `bmfork`/`bmforkupdate` (connections to bmorphism)

**TeglonLabs** — `mathpix-gem` (Ruby OCR SDK), `coin-flip-mcp` (random.org MCP)

**wasita** — Active web developer: personal site (Svelte), `magic-garden` bot, `send2kobo`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 Hamming swarm wallets (alice, bob, A–Z) were probed on the Aptos mainnet.

**Result:** All wallets return **0 APT** — `CoinStore<AptosCoin>` resource not initialized (accounts exist but have never held APT, or balances were transferred out).

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C–Z | (22 more) | 0.0 each |

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4...003 | **2** | ✓ HEALTHY |
| A-G | 0xf56c...096 | **2** | ✓ HEALTHY |
| Y-Z | 0xd3ff...883 | **2** | ✓ HEALTHY |
| S-T | 0x3b1c...883 | **2** | ✓ HEALTHY |
| V-W | 0x40fa...b6d | **2** | ✓ HEALTHY |

All 5 multisigs require **2-of-N** signatures. All contracts respond and are healthy.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA — no REST market API is available at standard paths (`/api/markets`). The site renders client-side only. **No market data extractable.** Status: `UNAVAILABLE_SPA`.

---

## DuckDB Schema Summary

```sql
world_increments  -- 11 rows  (GF3 color chain per source)
repo_snapshots    -- 134 rows (full repo metadata)
aptos_snapshots   -- 28 rows  (all Hamming swarm wallet balances)
multisig_probes   -- 5 rows   (all 2-of-N, all healthy)
mnx_snapshots     -- 0 rows   (SPA, no API)
```

## GF(3) Color Chain

```
id%3 == 0 → trit=0  ERGODIC  #d3869b  (pink)
id%3 == 1 → trit=1  PLUS     #b8bb26  (green)
id%3 == 2 → trit=-1 MINUS    #cc241d  (red)
```

Sources assigned in insertion order:
`TeglonLabs(+) → kubeflow(-) → plurigrid(E) → migalkin(+) → DJedamski(-) → wasita(E) → kristinezheng(+) → M1shaaa(-) → AustinCStone(E) → bmorphism(+) → zubyul(-)`
