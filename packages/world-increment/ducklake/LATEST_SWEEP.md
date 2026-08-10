# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-08-10
**Agent:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Status: Restricted

The GitHub API proxy in this environment restricts all calls to `repos/{owner}/{repo}/...` endpoints only.
Org-level and user-level repo list endpoints (`/orgs/{org}/repos`, `/users/{user}/repos`) are blocked.

**Attempted sources:**
- plurigrid (org)
- kubeflow (org)
- TeglonLabs (org)
- bmorphism (user)
- zubyul (user)
- Social graph: migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

**Recorded in DuckDB:** `plurigrid/gorj` (the single in-scope repository) added to `repo_snapshots`.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses probed against Aptos mainnet. All returned `resource_not_found` for the APT CoinStore resource — interpreted as **0.000000000 APT** (unfunded accounts).

| World | Address (prefix)   | Balance (APT) | Status              |
|-------|--------------------|---------------|---------------------|
| alice | 0xc793acdec12b4a… | 0.0           | resource_not_found  |
| bob   | 0x0a3c00c58fdf90… | 0.0           | resource_not_found  |
| A     | 0x8699edc0960dd5… | 0.0           | resource_not_found  |
| B     | 0x3f892ebe6e4516… | 0.0           | resource_not_found  |
| C     | 0x38b99e63ada9b6… | 0.0           | resource_not_found  |
| D     | 0xf77656248f64d5… | 0.0           | resource_not_found  |
| E     | 0xdc1d9d533bac35… | 0.0           | resource_not_found  |
| F     | 0x18a14b5b4bec11… | 0.0           | resource_not_found  |
| G     | 0x69a394c0b0ac84… | 0.0           | resource_not_found  |
| H     | 0xce67c327a7844e… | 0.0           | resource_not_found  |
| I     | 0x070fe5d74e4eda… | 0.0           | resource_not_found  |
| J     | 0x4d964db8f53837… | 0.0           | resource_not_found  |
| K     | 0xa732040a6b0d55… | 0.0           | resource_not_found  |
| L     | 0x7c2eaeafad9725… | 0.0           | resource_not_found  |
| M     | 0x6fed37a7553ef1… | 0.0           | resource_not_found  |
| N     | 0xe7dde6da0a65f5… | 0.0           | resource_not_found  |
| O     | 0x73252b6011a751… | 0.0           | resource_not_found  |
| P     | 0x6218792de4a9bc… | 0.0           | resource_not_found  |
| Q     | 0xac40fa50b81b4c… | 0.0           | resource_not_found  |
| R     | 0x7ce605cc8fda4f… | 0.0           | resource_not_found  |
| S     | 0xb8753014e4888e… | 0.0           | resource_not_found  |
| T     | 0x35781dc0e42fef… | 0.0           | resource_not_found  |
| U     | 0x75860da47565f6… | 0.0           | resource_not_found  |
| V     | 0xb59dd8170321df… | 0.0           | resource_not_found  |
| W     | 0x5f32aef70f5ba5… | 0.0           | resource_not_found  |
| X     | 0xa95cbbd116548a… | 0.0           | resource_not_found  |
| Y     | 0xd8e32848f1dffa… | 0.0           | resource_not_found  |
| Z     | 0x7af0ef6e1bd706… | 0.0           | resource_not_found  |

**Total APT across swarm:** 0.000000000 APT

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.
All returned **2 signatures required** and are **healthy**.

| Pair | Address (prefix)   | Sigs Required | Healthy |
|------|--------------------|---------------|---------|
| A-B  | 0x0da4f428a0c007… | 2             | ✓       |
| A-G  | 0xf56c4a1c090621… | 2             | ✓       |
| Y-Z  | 0xd3ffe1812b2df4… | 2             | ✓       |
| S-T  | 0x3b1c3ae905d44c… | 2             | ✓       |
| V-W  | 0x40fad7b423a843… | 2             | ✓       |

**All 5 multisig contracts are live and responding correctly (2-of-2 threshold).**

### MNX Markets

`testnet.mnx.fi` returned 404 on all probed API paths:
- `/api/markets` → 404
- `/api/v1/markets` → 404
- `/api/tickers` → 404

**MNX testnet is currently unavailable.** No market data recorded.

---

## DuckDB State

| Table             | Rows |
|-------------------|------|
| world_increments  | 25   |
| repo_snapshots    | 945  |
| aptos_snapshots   | 28   |
| multisig_probes   | 5    |
| mnx_snapshots     | 0    |

GF(3) color chain for this sweep: id%3==1 → trit=1 **PLUS** `#b8bb26`

---

## Key Findings

1. **Hamming swarm wallets (A–Z + alice/bob): all unfunded** — 0 APT across all 28 addresses on mainnet.
2. **Multisig fabric: fully healthy** — all 5 two-of-two contracts respond correctly on mainnet.
3. **MNX testnet: offline** — API returning 404, likely not yet deployed or behind a different path.
4. **GitHub sweep: blocked by environment scope** — only `plurigrid/gorj` is accessible; org-wide queries are restricted by the proxy.
