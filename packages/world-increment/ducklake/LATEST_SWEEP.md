# LATEST_SWEEP.md

## Timestamp
2026-04-12T00:00:00Z (automated sweep)

## GitHub Sweep Summary

### Orgs Queried (3)
- plurigrid — rate limited (no data)
- kubeflow — rate limited (no data)
- TeglonLabs — rate limited (no data)

### Users Queried (8)
- bmorphism — rate limited (no data)
- zubyul — rate limited for repos; 10 public events collected
- migalkin — rate limited (no data)
- DJedamski — 11 repos collected
- wasita — rate limited (no data)
- kristinezheng — rate limited (no data)
- M1shaaa — rate limited (no data)
- AustinCStone — rate limited (no data)

### Total Repos Found
11 repos (DJedamski, unauthenticated API rate limit applied to others)

### Total Public Events Found
10 events (zubyul, all related to plurigrid/gorj)

### Top Repos by Stars (DJedamski)
| repo | language | stars |
|------|----------|-------|
| DJedamski/awesome-ruby | N/A | 2 |
| DJedamski/kaggle-titanic | Python | 2 |
| DJedamski/Kaggle | N/A | 1 |
| DJedamski/Getting-and-Cleaning-Data | R | 1 |
| DJedamski/School | R | 1 |

## GF(3) Color Chain Summary

world_increments rows follow GF(3) color assignment by id%3:

| id%3 | trit | color   | name    | count |
|------|------|---------|---------|-------|
| 0    | 0    | #d3869b | ERGODIC | 7     |
| 1    | 1    | #b8bb26 | PLUS    | 7     |
| 2    | -1   | #cc241d | MINUS   | 7     |

Total world_increment rows: 21 (11 source sweeps + 10 zubyul events)

## Aptos Snapshot Table

| world | address (truncated) | balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793acdec12b4a6371... | resource_not_found |
| bob | 0x0a3c00c58fdf9020b2... | resource_not_found |
| A | 0x8699edc0960dd5b916... | resource_not_found |
| B | 0x3f892ebe6e45164e63... | resource_not_found |
| C | 0x38b99e63ada9b6fef1... | resource_not_found |
| D | 0xf77656248f64d5dd00... | resource_not_found |
| E | 0xdc1d9d533bac3507f9... | resource_not_found |
| F | 0x18a14b5b4bec118c1c... | resource_not_found |
| G | 0x69a394c0b0ac842127... | resource_not_found |
| H | 0xce67c327a7844e5488... | resource_not_found |
| I | 0x070fe5d74e4eda30e2... | resource_not_found |
| J | 0x4d964db8f538374034... | resource_not_found |
| K | 0xa732040a6b0d559041... | resource_not_found |
| L | 0x7c2eaeafad9725492e... | resource_not_found |
| M | 0x6fed37a7553ef16b2a... | resource_not_found |
| N | 0xe7dde6da0a65f51062... | resource_not_found |
| O | 0x73252b6011a75115a2... | resource_not_found |
| P | 0x6218792de4a9bc3891... | resource_not_found |
| Q | 0xac40fa50b81b4ca6b1... | resource_not_found |
| R | 0x7ce605cc8fda4f8e4a... | resource_not_found |
| S | 0xb8753014e4888ea48a... | resource_not_found |
| T | 0x35781dc0e42fef3f25... | resource_not_found |
| U | 0x75860da47565f6509b... | resource_not_found |
| V | 0xb59dd8170321dfab5a... | resource_not_found |
| W | 0x5f32aef70f5ba530d3... | resource_not_found |
| X | 0xa95cbbd116548ac990... | resource_not_found |
| Y | 0xd8e32848f1dffa811b... | resource_not_found |
| Z | 0x7af0ef6e1bd706f4b3... | resource_not_found |

> Note: All addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
> Accounts either hold no APT or use a different coin store structure.

## Multisig Probe Results

| pair | address (truncated) | sigs_required | healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a... | 2 | YES |
| A-G | 0xf56c4a1c0906214f3f859ccd8b49... | 2 | YES |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502... | 2 | YES |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a... | 2 | YES |
| V-W | 0x40fad7b423a843650fddcad36b7d... | 2 | YES |

All 5 multisig contracts are healthy and require 2 signatures.

## MNX Markets Status

Both endpoints returned HTTP 404 with HTML (Next.js app, no JSON API exposed):
- `https://testnet.mnx.fi/api/markets` → 404
- `https://testnet.mnx.fi/api/v1/markets` → 404

Status: **UNAVAILABLE** (no data inserted into mnx_snapshots)

## DuckDB Row Counts

| table            | rows |
|------------------|------|
| world_increments | 21   |
| repo_snapshots   | 11   |
| aptos_snapshots  | 28   |
| multisig_probes  | 5    |
| mnx_snapshots    | 0    |

Database: `/home/user/gorj/packages/world-increment/ducklake/world.db`
