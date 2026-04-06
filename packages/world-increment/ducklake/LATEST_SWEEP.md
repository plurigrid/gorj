# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep Date/Time:** 2026-04-06T00:00:00Z (UTC)
**DuckDB Version:** v1.5.1 (Variegata)

---

## GitHub Sources Queried

| Source | Type | Total Repos Captured |
|--------|------|---------------------|
| plurigrid | org | 18 |
| kubeflow | org | 12 |
| TeglonLabs | org | 3 |
| bmorphism | user | 13 |
| zubyul | user | 7 |
| migalkin | user | 6 |
| DJedamski | user | 3 |
| wasita | user | 5 |
| kristinezheng | user | 3 |
| M1shaaa | user | 2 |
| AustinCStone | user | 6 |

**Total repos captured: 78**

---

## Top Repos by Source

### kubeflow (org)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15553 | - |
| kubeflow/pipelines | 4118 | Python |
| kubeflow/spark-operator | 3111 | Python |
| kubeflow/trainer | 2074 | Go |
| kubeflow/katib | 1674 | Python |
| kubeflow/manifests | 1009 | YAML |

### plurigrid (org)

| Repo | Stars | Language |
|------|-------|----------|
| plurigrid/asi | 16 | HTML |
| plurigrid/ontology | 7 | JavaScript |
| plurigrid/vcg-auction | 7 | Rust |
| plurigrid/agent | 5 | Python |
| plurigrid/asi-skills | 3 | Julia |
| plurigrid/nanoclj-zig | 0 | Zig |

### TeglonLabs (org)

| Repo | Stars | Language |
|------|-------|----------|
| TeglonLabs/mathpix-gem | 2 | Ruby |
| TeglonLabs/topoi | 0 | Python |
| TeglonLabs/coin-flip-mcp | 0 | JavaScript |

### bmorphism (user)

| Repo | Stars | Language |
|------|-------|----------|
| bmorphism/ocaml-mcp-sdk | 60 | OCaml |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |
| bmorphism/say-mcp-server | 20 | JavaScript |
| bmorphism/babashka-mcp-server | 18 | JavaScript |
| bmorphism/manifold-mcp-server | 13 | JavaScript |

### zubyul (user)

| Repo | Stars | Language |
|------|-------|----------|
| zubyul/WGCNA | 2 | HTML |
| zubyul/jonikas_lab_data_analysis_misc | 2 | Jupyter Notebook |
| zubyul/Nikolova_lab_data_analysis | 2 | R |
| zubyul/gay-world | 1 | Python |
| zubyul/Gay.jl | 0 | Julia |

### migalkin (user)

| Repo | Stars | Language |
|------|-------|----------|
| migalkin/NodePiece | 143 | Python |
| migalkin/StarE | 88 | Python |
| migalkin/kgcourse2021 | 25 | HTML |
| migalkin/NBFNet_mlx | 10 | Python |
| migalkin/RWL | 7 | Python |

### AustinCStone (user)

| Repo | Stars | Language |
|------|-------|----------|
| AustinCStone/TextGAN | 92 | Python |
| AustinCStone/StereoVisionMRF | 11 | Python |
| AustinCStone/SpectralClustering | 3 | Python |

---

## GF(3) Color Chain Stats

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| PLUS | +1 | #b8bb26 | 30 |
| ERGODIC | 0 | #d3869b | 29 |
| MINUS | -1 | #cc241d | 29 |

**Total increments: 88** (78 new + 10 pre-existing)

The GF(3) chain assigns colors cyclically:
- id%3==1 → PLUS (#b8bb26, yellow-green)
- id%3==2 → MINUS (#cc241d, red)
- id%3==0 → ERGODIC (#d3869b, pink)

---

## Aptos Wallet Balances (Hamming Swarm)

All 28 wallets queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...25dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

Note: All wallets returned 0 balance. This indicates accounts may not have been initialized with CoinStore resources on mainnet, or the raw value was 0.

---

## Multisig Probe Results

All probes returned sigs_required=2, all healthy.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

API: `POST https://fullnode.mainnet.aptoslabs.com/v1/view` with `0x1::multisig_account::num_signatures_required`

---

## MNX Markets Status

Both endpoints tried:
- `GET https://testnet.mnx.fi/api/markets` → Returns HTML (Next.js frontend, no JSON API at this path)
- `GET https://testnet.mnx.fi/api/v1/markets` → Returns HTML (same result)

**Status: MNX API not accessible via these endpoints (returns HTML frontend)**. No market data captured.

---

## Errors Encountered

1. **Aptos wallet balances**: All wallets returned 0. The Aptos mainnet API responded successfully but coin values were 0 for all addresses. This may indicate these are testnet/placeholder addresses or accounts with no APT balance.
2. **MNX Markets**: Both API endpoints returned HTML page (Next.js SSR), not JSON. No machine-readable market data available.
3. **Pre-existing DuckDB data**: The database file had pre-existing rows (10 world_increments, 451 repo_snapshots) before this sweep. New data was appended correctly.

---

## Summary

- **GitHub sources**: 11 sources (3 orgs, 8 users)
- **Total repos captured and stored**: 78
- **Aptos wallets probed**: 28 (all 0 APT)
- **Multisig contracts probed**: 5 (all healthy, sigs_required=2)
- **GF(3) color chain**: 88 world_increments (PLUS=30, ERGODIC=29, MINUS=29)
- **MNX status**: Unreachable via JSON API
