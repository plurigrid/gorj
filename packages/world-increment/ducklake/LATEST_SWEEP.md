# World Increment Sweep + Hamming Snapshot — 2026-07-25

## Sweep Metadata
- **Date:** 2026-07-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GF(3) Chain — Increment #13 PLUS `#b8bb26`

| ID | timestamp | gf3_trit | gf3_name | gf3_color | source | event |
|----|-----------|----------|----------|-----------|--------|-------|
| 13 | 2026-07-25 | +1 | **PLUS** | `#b8bb26` | plurigrid/gorj | sweep_complete |

GF(3) chain position: `...ERGODIC(12) → **PLUS(13)** → MINUS(14)...`

---

## JOB 1: GitHub Social Graph Sweep

**Scope note:** Session MCP access is restricted to `plurigrid/gorj`. Queries to other orgs (kubeflow, TeglonLabs, plurigrid org-wide) and users (bmorphism, zubyul social graph) are outside session scope — prior data for those sources remains in ducklake from the 2026-04-12 sweep. The gorj repo itself was re-snapshotted this run.

### plurigrid/gorj snapshot (2026-07-25)

| field | value |
|-------|-------|
| full_name | plurigrid/gorj |
| language | Clojure |
| last_pushed | 2026-05-08T14:04:34Z |
| head SHA | 5b28fe016e0e3d0b0f22e35e01f7db0722d988e1 |
| description | MCP server + hooks that give AI coding agents a Clojure REPL |
| open sweep branches | 20 (oldest: 2026-04-27, newest: 2026-04-30) |

**Activity delta:** Last commit was `chore: ignore duckdb binary in repo root` (2026-05-08). Repo has been quiet for ~77 days.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

Queried 28 addresses (alice, bob, A–Z) via Aptos fullnode mainnet API.

| result | count |
|--------|-------|
| addresses queried | 28 |
| with APT balance | 0 |
| null (CoinStore not registered) | 28 |

All 28 addresses returned no `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource. Accounts are unfunded or not registered on mainnet. Consistent with all prior sweep runs.

### Multisig Contract Probes (mainnet)

Probed via `0x1::multisig_account::num_signatures_required`.

| pair | address | sigs_required | healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✅ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✅ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✅ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✅ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed on all pairs.**

### MNX Markets (testnet.mnx.fi)

Probed `https://testnet.mnx.fi` and API paths `/api/markets`, `/api/v1/markets`.

- **Status: unavailable** — Next.js SPA, no public REST API detected. Requires client-side JS execution.

---

## Cumulative Database State

| table | rows |
|-------|------|
| world_increments | 24 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## Historical GF(3) Chain

| ID | Source | gf3_name | gf3_color |
|----|--------|----------|-----------|
| 1  | plurigrid (org) | PLUS | `#b8bb26` |
| 2  | kubeflow (org) | MINUS | `#cc241d` |
| 3  | TeglonLabs (org) | ERGODIC | `#d3869b` |
| 4  | bmorphism (user) | PLUS | `#b8bb26` |
| 5  | zubyul (user) | MINUS | `#cc241d` |
| 6  | migalkin (user) | ERGODIC | `#d3869b` |
| 7  | DJedamski (user) | PLUS | `#b8bb26` |
| 8  | wasita (user) | MINUS | `#cc241d` |
| 9  | kristinezheng (user) | ERGODIC | `#d3869b` |
| 10 | M1shaaa (user) | PLUS | `#b8bb26` |
| 11 | AustinCStone (user) | MINUS | `#cc241d` |
| 12 | bmorphism (sweep_complete) | ERGODIC | `#d3869b` |
| **13** | **plurigrid/gorj (sweep_complete)** | **PLUS** | **`#b8bb26`** |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
