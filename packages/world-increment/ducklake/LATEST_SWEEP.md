# World Increment Sweep — Latest Snapshot

**Timestamp:** 2026-04-03T00:21:31Z

---

## GitHub Sweep Summary

**Sources queried:** 11 (3 orgs + 8 users)
- Orgs: plurigrid (100 repos), kubeflow (46 repos), TeglonLabs (API returned non-array, skipped)
- Users: bmorphism (100 repos), zubyul (23 repos), migalkin (30 repos), DJedamski (11 repos), wasita (skipped), kristinezheng (skipped), M1shaaa (16 repos), AustinCStone (43 repos)

**Total repos snapshotted:** 369
**Total world increments written:** 8

### GF(3) Color Chain Applied

| Increment | Source | GF3 Trit | Color | Name |
|-----------|--------|----------|-------|------|
| 1 | org/plurigrid | +1 | #b8bb26 | PLUS |
| 2 | org/kubeflow | -1 | #cc241d | MINUS |
| 3 | user/bmorphism | 0 | #d3869b | ERGODIC |
| 4 | user/zubyul | +1 | #b8bb26 | PLUS |
| 5 | user/migalkin | -1 | #cc241d | MINUS |
| 6 | user/DJedamski | 0 | #d3869b | ERGODIC |
| 7 | user/M1shaaa | +1 | #b8bb26 | PLUS |
| 8 | user/AustinCStone | -1 | #cc241d | MINUS |

### Top Repos by Stars

| Source | Repo | Stars | Language |
|--------|------|-------|----------|
| kubeflow | kubeflow | 15551 | N/A |
| kubeflow | pipelines | 4118 | Python |
| kubeflow | spark-operator | 3110 | Python |
| kubeflow | trainer | 2071 | Go |
| kubeflow | katib | 1674 | Python |
| kubeflow | examples | 1459 | Jsonnet |
| kubeflow | manifests | 1006 | YAML |
| kubeflow | arena | 809 | Go |
| kubeflow | kale | 681 | Python |
| kubeflow | mpi-operator | 519 | Go |

---

## Aptos Hamming Swarm Snapshot

All 28 addresses queried on Aptos mainnet. All balances returned 0 APT (accounts exist but have zero CoinStore balance at query time).

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793acd...624cc7b | 0.0 |
| bob | 0x0a3c00c...e05512d5d | 0.0 |
| A | 0x8699edc...ebe9d7a | 0.0 |
| B | 0x3f892eb...577cb13 | 0.0 |
| C | 0x38b99e6...691535e | 0.0 |
| D | 0xf776562...fcfdd1 | 0.0 |
| E | 0xdc1d9d5...958d36 | 0.0 |
| F | 0x18a14b5...4c3cf71 | 0.0 |
| G | 0x69a394c...cbcc7f32 | 0.0 |
| H | 0xce67c32...e5300f | 0.0 |
| I | 0x070fe5d...c00c1fc9 | 0.0 |
| J | 0x4d964db...3e87f54 | 0.0 |
| K | 0xa732040...7a425dc4 | 0.0 |
| L | 0x7c2eaea...6337eba9 | 0.0 |
| M | 0x6fed37a...49b7f2e9 | 0.0 |
| N | 0xe7dde6d...11551b2c | 0.0 |
| O | 0x73252b6...525a89d | 0.0 |
| P | 0x621879...1ec948 | 0.0 |
| Q | 0xac40fa5...5e5c89a9 | 0.0 |
| R | 0x7ce605c...36d76e10 | 0.0 |
| S | 0xb875301...4f99d0386 | 0.0 |
| T | 0x35781dc...2d3f4588 | 0.0 |
| U | 0x75860da...39ef9956 | 0.0 |
| V | 0xb59dd81...a89af2c3 | 0.0 |
| W | 0x5f32aef...45a6ccc7b0 | 0.0 |
| X | 0xa95cbbd...2cbe33047d | 0.0 |
| Y | 0xd8e3284...1fa2444c4 | 0.0 |
| Z | 0x7af0ef6...6e4e197c | 0.0 |

---

## Multisig Contract Probes

All 5 multisig contracts probed via Aptos fullnode view function `0x1::multisig_account::num_signatures_required`. All returned healthy status with 2-of-N signature requirements.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f42...4987003 | 2 | true |
| A-G | 0xf56c4a1...fbc0096 | 2 | true |
| Y-Z | 0xd3ffe18...e75b883 | 2 | true |
| S-T | 0x3b1c3ae...3ded7883 | 2 | true |
| V-W | 0x40fad7b...c80eb6d | 2 | true |

---

## MNX Markets Status

**Status: Unavailable (non-JSON response)**

Endpoints probed:
- `https://testnet.mnx.fi/api/markets` — returns HTML (SPA frontend)
- `https://testnet.mnx.fi/api/v1/markets` — returns HTML (SPA frontend)
- `https://testnet.mnx.fi/api/tickers` — returns HTML (SPA frontend)

The MNX testnet API endpoints return a web application frontend rather than JSON API responses. Market data could not be parsed or inserted.

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| World increments written | 8 |
| Repos snapshotted | 369 |
| Aptos addresses probed | 28 |
| Multisig contracts probed | 5 |
| Multisig contracts healthy | 5 |
| MNX markets available | 0 (unavailable) |
| GitHub sources (orgs) | 3 queried, 2 successful |
| GitHub sources (users) | 8 queried, 6 successful |

