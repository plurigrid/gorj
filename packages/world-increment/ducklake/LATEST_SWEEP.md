# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-08 10:10 UTC
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GF(3) Color Chain

| trit | id%3 | color   | hex     | count (world_increments) |
|------|------|---------|---------|--------------------------|
| 0    | 0    | ERGODIC | #d3869b | 8 (this sweep)           |
| +1   | 1    | PLUS    | #b8bb26 | 9 (this sweep)           |
| -1   | 2    | MINUS   | #cc241d | 8 (this sweep)           |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| source_type | source_name    | repos_captured | top_stars |
|-------------|---------------|---------------|-----------|
| org         | plurigrid      | 19            | 16 (asi)  |
| org         | kubeflow       | 15            | 4119 (pipelines) |
| org         | TeglonLabs     | 13            | 2 (mathpix-gem, vibespace) |
| user        | bmorphism      | 10            | 60 (ocaml-mcp-sdk) |
| user        | zubyul         | 15            | 2 (gay-world, WGCNA) |
| user        | migalkin       | 8             | 143 (NodePiece) |
| user        | DJedamski      | 5             | 2 (awesome-ruby) |
| user        | wasita         | 11            | 1 (magic-garden, dartbrains) |
| user        | kristinezheng  | 7             | 0 |
| user        | M1shaaa        | 8             | 0 |
| user        | AustinCStone   | 8             | 92 (TextGAN) |

### Top Repos by Stars

| repo                     | stars | language   | last_push  |
|--------------------------|-------|------------|------------|
| kubeflow/pipelines       | 4119  | Python     | 2026-04-08 |
| kubeflow/spark-operator  | 3111  | Python     | 2026-04-06 |
| kubeflow/trainer         | 2076  | Go         | 2026-04-06 |
| kubeflow/katib           | 1675  | Python     | 2026-04-02 |
| kubeflow/manifests       | 1009  | YAML       | 2026-04-05 |
| migalkin/NodePiece       | 143   | Python     | 2022-02-02 |
| migalkin/StarE           | 88    | Python     | 2023-12-01 |
| AustinCStone/TextGAN     | 92    | Python     | 2016-10-04 |
| bmorphism/ocaml-mcp-sdk  | 60    | OCaml      | 2026-03-16 |
| plurigrid/asi            | 16    | HTML       | 2026-04-08 |

### Most Active Right Now (2026-04-08)

- **bmorphism**: 30 PushEvents to plurigrid/asi, plurigrid/horse, plurigrid/nanoclj-zig, plurigrid/flowglad-rs, bmorphism/shitcoin
- **zubyul**: 30 events to plurigrid/gorj (multiple PRs + branch creates) + push to plurigrid/horse

### Notable Repos

- **plurigrid/gorj** (this repo): 121 open issues, Clojure, forj + GF(3) trit coloring
- **plurigrid/nanoclj-zig**: NaN-boxed Clojure in Zig 0.15, GF(3) trit conservation
- **bmorphism/ocaml-mcp-sdk**: OCaml SDK for MCP using Jane Street oxcaml_effect (60★)
- **kubeflow/mcp-apache-spark-history-server**: MCP bridge for Apache Spark History Server (149★)
- **TeglonLabs/vibespace**: Go MCP experience with NATS + binary data + balanced ternary
- **zubyul/tilelang-kernels**: GPU kernels for SplitMix64 GF(3) trit classification on GB10 Blackwell

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets (alice, bob, A–Z) queried against Aptos mainnet fullnode.

| status | count |
|--------|-------|
| funded (>0 APT) | 0 |
| unfunded / not initialized | 28 |

All addresses returned 0.0 APT — accounts not initialized or unfunded on mainnet.

**Addresses probed:**
- alice: `0xc793...cc7b`
- bob: `0x0a3c...2d5d`
- A–Z: 26 Hamming-swarm wallets (see aptos_snapshots table)

### Multisig Contract Probes

All 5 multisig pairs healthy — each requires **2-of-N signatures**.

| pair | address (truncated)  | sigs_required | healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4...7003       | 2             | ✓       |
| A-G  | 0xf56c...0096       | 2             | ✓       |
| Y-Z  | 0xd3ff...b883       | 2             | ✓       |
| S-T  | 0x3b1c...7883       | 2             | ✓       |
| V-W  | 0x40fa...eb6d       | 2             | ✓       |

### MNX Testnet Markets

**Source:** `https://testnet.mnx.fi` (prediction market platform)

| ticker  | name                   | category  | price         | 24h change |
|---------|------------------------|-----------|--------------|-----------|
| TSM     | Taiwan Semiconductor   | Stocks    | $363.51     | +6.03%    |
| DPREZ   | Dem President 2028     | Politics  | 51%          | +2.41%    |
| INVADE27| Taiwan Invasion 2027   | Politics  | 18%          | +1.69%    |
| OAI26   | OpenAI Valuation 2026  | AI        | $528B       | +1.34%    |
| H100    | GPU Rental Index       | Compute   | $2.80       | +0.86%    |
| AAPL    | Apple Inc              | Stocks    | $258.80     | +0.77%    |
| ANT26   | Anthropic Valuation    | AI        | $420B       | -1.18%    |
| CPI26   | US Inflation 2026      | Financial | 3%           | -7.86%    |
| VIX     | Volatility Index       | Financial | 20.77        | -15.33%   |

**Notable signals:** TSM +6% (geopolitical), VIX -15% (risk-off unwinding), OAI26 vs ANT26 divergence (OAI +1.34% vs ANT -1.18%).

---

## DuckDB Schema Summary

```sql
world_increments   -- GF(3) trit-colored event log
repo_snapshots     -- GitHub repo metadata snapshots
aptos_snapshots    -- Aptos mainnet wallet balances (APT)
multisig_probes    -- Aptos multisig sigs_required health check
mnx_snapshots      -- MNX prediction market prices
```

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent*
