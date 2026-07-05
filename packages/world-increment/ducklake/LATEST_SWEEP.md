# World-Increment Sweep + Hamming Snapshot
**Timestamp:** 2026-07-05 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul graph) | 19 |
| DJedamski | user (zubyul graph) | 6 |
| wasita | user (zubyul graph) | 11 |
| kristinezheng | user (zubyul graph) | 5 |
| M1shaaa | user (zubyul graph) | 8 |
| AustinCStone | user (zubyul graph) | 40 |
| **Total** | | **391 repos** |

### Notable Recent Activity (as of 2026-07-05)

**plurigrid/gorj** (Clojure) — pushed 2026-07-05 — `forj + Rama topology nREPL routing + GF(3) gay trit coloring` — 976 open issues  
**bmorphism/Gay.jl** (Julia) — pushed 2026-07-05 — `Wide-gamut color sampling with splittable determinism` — 187 open issues  
**plurigrid/asi** (HTML) — 28★ — `everything is topological chemputer!`  
**kubeflow/kubeflow** — 15761★ / 2683 forks — main ML-on-Kubernetes project  
**kubeflow/spark-operator** — 3132★ / 1496 forks  
**kubeflow/trainer** (Go) — 2129★ — Distributed AI Model Training  
**bmorphism/ocaml-mcp-sdk** (OCaml) — 61★ — Jane Street oxcaml_effect-based MCP SDK  
**migalkin/NodePiece** (Python) — 144★ — KG embeddings, ICLR'22  
**AustinCStone/TextGAN** (Python) — 92★ — GAN text generation in TensorFlow  
**bmorphism/anti-bullshit-mcp-server** (JavaScript) — 23★  
**wasita/wasita.github.io** (Svelte) — active 2026-07-02  
**kristinezheng/kristinezheng.github.io** (HTML) — active 2026-07-01  
**M1shaaa/M1shaaa** — pushed 2026-07-04  

### GF(3) World-Increment Chain
- **ERGODIC** (trit=0, #d3869b): IDs 0,3,6,...
- **PLUS** (trit=1, #b8bb26): IDs 1,4,7,...
- **MINUS** (trit=-1, #cc241d): IDs 2,5,8,...

Total increments recorded this sweep: **391**  
Total repo_snapshots in ducklake (cumulative): **1335** across **646 distinct repos**

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Hamming A-Z + alice/bob)

All 28 wallets queried against `fullnode.mainnet.aptoslabs.com`. All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version 6108337854. This indicates either zero-balance accounts or accounts using the Fungible Asset (FA) standard rather than the legacy Coin standard.

| World | Address (prefix) | Balance (APT) |
|-------|------------------|---------------|
| alice | 0xc793...cc7b | 0.0 (not found) |
| bob | 0x0a3c...512d | 0.0 (not found) |
| A | 0x8699...9d7a | 0.0 (not found) |
| B | 0x3f89...b13 | 0.0 (not found) |
| C | 0x38b9...535e | 0.0 (not found) |
| D | 0xf776...fdd1 | 0.0 (not found) |
| E | 0xdc1d...8d36 | 0.0 (not found) |
| F | 0x18a1...cf71 | 0.0 (not found) |
| G | 0x69a3...7f32 | 0.0 (not found) |
| H | 0xce67...300f | 0.0 (not found) |
| I | 0x070f...1fc9 | 0.0 (not found) |
| J | 0x4d96...7f54 | 0.0 (not found) |
| K | 0xa732...5dc4 | 0.0 (not found) |
| L | 0x7c2e...ba9 | 0.0 (not found) |
| M | 0x6fed...2e9 | 0.0 (not found) |
| N | 0xe7dd...1b2c | 0.0 (not found) |
| O | 0x7325...a89d | 0.0 (not found) |
| P | 0x6218...c948 | 0.0 (not found) |
| Q | 0xac40...89a9 | 0.0 (not found) |
| R | 0x7ce6...6e10 | 0.0 (not found) |
| S | 0xb875...0386 | 0.0 (not found) |
| T | 0x3578...4588 | 0.0 (not found) |
| U | 0x7586...f956 | 0.0 (not found) |
| V | 0xb59d...f2c3 | 0.0 (not found) |
| W | 0x5f32...c7b0 | 0.0 (not found) |
| X | 0xa95c...047d | 0.0 (not found) |
| Y | 0xd8e3...44c4 | 0.0 (not found) |
| Z | 0x7af0...97c | 0.0 (not found) |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Status |
|------|------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

All 5 multisig accounts require 2-of-2 signatures. All contracts healthy.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` is behind Vercel deployment authentication (requires auth bypass token or Trusted Sources OIDC). No market data extractable without credentials.

---

## DuckDB Schema Summary

```
world_increments: 414 rows (GF3 color chain, one per repo increment)
repo_snapshots:  1335 rows (646 distinct repos across all sweeps)
aptos_snapshots:   28 rows (all 0.0 APT, ledger v6108337854)
multisig_probes:    5 rows (all 2-of-2, all healthy)
mnx_snapshots:      0 rows (auth-blocked)
```
