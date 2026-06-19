# World Increment Sweep + Hamming Swarm Snapshot — 2026-06-19

**Timestamp:** 2026-06-19 UTC  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.4 (Variegata) — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | API Total |
|--------|------|----------------|-----------|
| plurigrid | org | 100 | 101 |
| kubeflow | org | 48 | 48 |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 100 | 104 |
| zubyul | user | 49 | 49 |
| migalkin | social (zubyul graph) | 5 | 19 |
| DJedamski | social (zubyul graph) | 3 | 6 |
| wasita | social (zubyul graph) | 5 | 11 |
| kristinezheng | social (zubyul graph) | 3 | 5 |
| M1shaaa | social (zubyul graph) | 3 | 8 |
| AustinCStone | social (zubyul graph) | 4 | 40 |
| **TOTAL** | | **325** | **~396** |

### GF(3) Color Chain

Each world increment `i` is assigned a GF(3) trit by `i mod 3`:

| id mod 3 | Trit | Name | Hex Color |
|----------|------|------|-----------|
| 0 | 0 | ERGODIC | `#d3869b` |
| 1 | +1 | PLUS | `#b8bb26` |
| 2 | -1 | MINUS | `#cc241d` |

With 325 repos: **108 ERGODIC**, **109 PLUS**, **108 MINUS** — balanced GF(3) chain.

### Notable Active Repos (June 2026)

| Repo | Stars | Lang | Last Push |
|------|-------|------|-----------|
| kubeflow/kubeflow | ~15565 | — | 2026+ |
| kubeflow/pipelines | ~4119 | Python | 2026-06 |
| kubeflow/spark-operator | ~3111 | Python | 2026-06 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| plurigrid/gorj | 0 | Clojure | **2026-06-18** |
| plurigrid/asi | 26 | HTML | 2026-06-10 |
| TeglonLabs/jank-crane | 0 | C++ | 2026-06-08 |
| wasita/wasita.github.io | 1 | Svelte | 2026-06-15 |

### Social Graph Character

- **migalkin** — ML researcher; knowledge graphs, GNNs (NodePiece 144★, StarE 89★)
- **wasita** — Svelte/cognitive science; personal site active June 2026
- **AustinCStone** — ML/CV; TextGAN (92★), StereoVisionMRF (11★), recent bmfork activity
- **M1shaaa / kristinezheng** — cognitive lab (Yale/MIT adjacent, Lookit studies)
- **DJedamski** — data science; Kaggle competition work

### TeglonLabs Update

| Repo | Lang | Stars | Issues | Last Push |
|------|------|-------|--------|-----------|
| jank-crane | C++ | 0 | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | **11** | 2026-01-01 |
| coin-flip-mcp | JS | 0 | 1 | 2025-09-21 |
| monad-mcp-server | — | 0 | 0 | 2025-05-14 |
| topoi | Python | 0 | 1 | 2025-01-24 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried 28 wallets (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`.

**All 28 wallets: 0.0 APT balance**

The `CoinStore<0x1::aptos_coin::AptosCoin>` resource returned `value=0` for every address. Wallets may hold assets in other token types or remain unfunded on mainnet.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addrs) | 0.0 each |

### Multisig Contract Probes

Probed `0x1::multisig_account::num_signatures_required` for 5 pairs.  
**All 5 contracts: HEALTHY — 2-of-N signatures required.**

| Pair | Contract Address | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428...7003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ healthy |

All multisig pairs are live on Aptos mainnet with 2-of-N threshold. No anomalies detected.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE**

`testnet.mnx.fi` and all API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) are behind Vercel deployment protection. Authentication is required (Vercel CLI token, Trusted Sources OIDC, or bypass token). No market data extracted.

---

## DuckDB Table Summary

```
world_increments   325 rows  (one per repo, GF3-colored, source_type='repo')
repo_snapshots     325 rows  (org_or_user, full_name, language, stars, forks, open_issues, pushed_at, description)
aptos_snapshots     28 rows  (world=alice/bob/A-Z, all balance_apt=0.0)
multisig_probes      5 rows  (all healthy, sigs_required=2)
mnx_snapshots        0 rows  (endpoint unavailable)
```

---

## Key Findings

1. **Hamming swarm wallets all zero** — All 28 Aptos mainnet wallets have 0 APT. Either
   not funded on mainnet, or assets live in non-native token stores.
2. **All multisig pairs confirmed healthy** — A-B, A-G, Y-Z, S-T, V-W each require
   exactly 2 signatures; contracts are responsive on mainnet.
3. **MNX testnet blocked** — Vercel auth gate prevents automated market data pull;
   requires human-provided bypass token.
4. **plurigrid/gorj most recently active** — Pushed 2026-06-18 (yesterday), 659 open
   issues; this sweep ran against the actively developed repo.
5. **TeglonLabs/jank-crane** — New C++ repo (created 2026-06-08) with GF3 convergence
   maps and loopify pass spec; fits the GF(3) theme of this sweep directly.
6. **Social graph is research-dense** — migalkin (KG/GNN, ICLR papers), wasita
   (cognitive neuro, Svelte), AustinCStone (CV/ML, bmorphism-adjacent forks).
