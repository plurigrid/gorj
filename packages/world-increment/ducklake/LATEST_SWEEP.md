# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep Date:** 2026-07-07
**GF(3) Color Chain:** id%3==0→ERGODIC #d3869b | id%3==1→PLUS #b8bb26 | id%3==2→MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

Sources targeted:
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Users:** bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone
- **Events:** Recent public events for bmorphism and zubyul

**Status:** GitHub API via this environment's proxy only permits repository-scoped endpoints
(`repos/{owner}/{repo}/...`). Cross-org/user list endpoints return HTTP 403. New repo snapshot
queries were blocked; the DB retains 944 cumulative repo_snapshots from prior sweeps.

### DB Cumulative Coverage (all sweeps)
| Table            | Total Rows |
|------------------|------------|
| world_increments | 35         |
| repo_snapshots   | 944        |

This run added **11 new world_increment** markers (GF(3) sweep events, one per source) and a
`sweep_complete` marker.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-07-07)

All 28 addresses queried against `fullnode.mainnet.aptoslabs.com/v1`. Every account returned
`resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — meaning these
addresses have not yet been funded / initialized with an APT coin store. Balance = 0.000000 APT for all.

| World  | Address (prefix)   | Balance (APT) |
|--------|--------------------|---------------|
| alice  | 0xc793acde...      | 0.000000      |
| bob    | 0x0a3c00c5...      | 0.000000      |
| A      | 0x8699edc0...      | 0.000000      |
| B      | 0x3f892ebe...      | 0.000000      |
| C      | 0x38b99e63...      | 0.000000      |
| D      | 0xf7765624...      | 0.000000      |
| E      | 0xdc1d9d53...      | 0.000000      |
| F      | 0x18a14b5b...      | 0.000000      |
| G      | 0x69a394c0...      | 0.000000      |
| H      | 0xce67c327...      | 0.000000      |
| I      | 0x070fe5d7...      | 0.000000      |
| J      | 0x4d964db8...      | 0.000000      |
| K      | 0xa732040a...      | 0.000000      |
| L      | 0x7c2eaeaf...      | 0.000000      |
| M      | 0x6fed37a7...      | 0.000000      |
| N      | 0xe7dde6da...      | 0.000000      |
| O      | 0x73252b60...      | 0.000000      |
| P      | 0x62187924...      | 0.000000      |
| Q      | 0xac40fa50...      | 0.000000      |
| R      | 0x7ce605cc...      | 0.000000      |
| S      | 0xb8753014...      | 0.000000      |
| T      | 0x35781dc0...      | 0.000000      |
| U      | 0x75860da4...      | 0.000000      |
| V      | 0xb59dd817...      | 0.000000      |
| W      | 0x5f32aef7...      | 0.000000      |
| X      | 0xa95cbbd1...      | 0.000000      |
| Y      | 0xd8e32848...      | 0.000000      |
| Z      | 0x7af0ef6e...      | 0.000000      |

### Multisig Contract Probes

All 5 multisig contracts responded successfully to `0x1::multisig_account::num_signatures_required`.

| Pair  | Address (prefix)   | Sigs Required | Healthy |
|-------|--------------------|---------------|---------|
| A-B   | 0x0da4f428...      | 2             | true    |
| A-G   | 0xf56c4a1c...      | 2             | true    |
| Y-Z   | 0xd3ffe181...      | 2             | true    |
| S-T   | 0x3b1c3ae9...      | 2             | true    |
| V-W   | 0x40fad7b4...      | 2             | true    |

All multisigs healthy -- 2-of-N threshold across all probed pairs.

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable. API paths `/api/markets`, `/api/v1/markets`, `/api/ticker` all return
HTTP 401 Unauthorized. The testnet is a gated SPA; no public market data was extractable.

---

## DuckDB Totals (post-sweep)

| Table             | Rows |
|-------------------|------|
| world_increments  | 35   |
| repo_snapshots    | 944  |
| aptos_snapshots   | 28   |
| multisig_probes   | 5    |
| mnx_snapshots     | 0    |

DB path: `packages/world-increment/ducklake/world-increments.duckdb`

---

## Key Findings

1. **GitHub proxy** restricts this session to `plurigrid/gorj`-scoped endpoints -- cross-org sweeps blocked (403). Historical 944 repo snapshots retained from prior runs.
2. **Hamming swarm (A-Z + alice/bob)**: All 28 Aptos addresses unfunded on mainnet -- `CoinStore` resource not found. Pre-funding state.
3. **Multisig health**: All 5 pair contracts live on Aptos mainnet, threshold = 2 signatures required, all responsive.
4. **MNX testnet**: Gated (401) -- no public data surface available.
