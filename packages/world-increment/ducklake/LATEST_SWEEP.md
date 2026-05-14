# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-14T00:00:00Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Snapshots Ingested: 373

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | social (zubyul graph) | 22 |
| migalkin | social (zubyul graph) | 19 |
| wasita | social (zubyul graph) | 11 |
| M1shaaa | social (zubyul graph) | 8 |
| kristinezheng | social (zubyul graph) | 6 |
| DJedamski | social (zubyul graph) | 6 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **373** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 124 |
| 1 | `#b8bb26` | PLUS | 125 |
| -1 | `#cc241d` | MINUS | 124 |

### Notable Repos

**plurigrid** (100 repos): Active Clojure/multi-language org; gorj, zig-syrup, asi (21 stars)  
**kubeflow** (48 repos): manifests (1017 stars), website (184 stars), mcp-apache-spark-history-server (168 stars)  
**bmorphism** (100 repos): boxxy (Move), nanoclj-zig (Zig), Gay.jl (Julia)  
**zubyul** (49 repos): voice-observatory, ghostel-emacs-worlds (GLSL), nash-web (Rust/WASM)  
**TeglonLabs** (4 repos): mathpix-gem (Ruby, 2 stars), monad-mcp-server, topoi (Python), coin-flip-mcp (JS, 2 forks)  
**migalkin** (19 repos): NodePiece (144 stars KG repr), StarE (89 stars EMNLP), NBFNet_mlx (Apple Silicon)  
**AustinCStone** (22 repos): TextGAN (92 stars TF text generation), StereoVisionMRF (11 stars)  

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 wallets queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
**Result: All accounts return no CoinStore resource** — accounts are either uninitialized or hold no APT in the standard coin store.

| World Label | Status |
|-------------|--------|
| alice | no CoinStore resource |
| bob | no CoinStore resource |
| A-Z (26 addrs) | no CoinStore resource |

### Multisig Contract Probes (5 pairs)

All probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428...987003 | 2 | YES |
| A-G | 0xf56c4a1c...c0096 | 2 | YES |
| Y-Z | 0xd3ffe181...b883 | 2 | YES |
| S-T | 0x3b1c3ae9...7883 | 2 | YES |
| V-W | 0x40fad7b4...eb6d | 2 | YES |

**5/5 multisig contracts healthy** — all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

The site returns a Next.js SPA (HTTP 200). No JSON API found at `/api/markets` or `/api/v1/markets`. Market data is client-side rendered and unavailable via curl. Recorded as unavailable in `mnx_snapshots` table.

---

## DuckDB Schema Summary

```
world_increments  -- 373 rows  (GF3-tagged event log)
repo_snapshots    -- 373 rows  (GitHub repo metadata)
aptos_snapshots   --  28 rows  (Hamming swarm wallet balances)
multisig_probes   --   5 rows  (Aptos multisig health)
mnx_snapshots     --   1 row   (MNX unavailability note)
```
