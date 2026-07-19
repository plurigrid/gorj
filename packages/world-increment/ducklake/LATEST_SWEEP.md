# World-Increment Sweep + Hamming Swarm Snapshot
## 2026-07-19

**Increment:** #13 — GF(3)=PLUS `#b8bb26` (trit=1)
**Snapshot hash:** `f7fb412ed5a63eda`

---

## JOB 1: GitHub Social Graph

> **Note:** GitHub API in this session is proxy-scoped to `plurigrid/gorj` only.
> Cross-org sweep (kubeflow, TeglonLabs, bmorphism, zubyul social graph) was not
> available. Captured `plurigrid/gorj` metadata and branch state instead.

### plurigrid/gorj
- Language: Clojure
- Description: MCP server + hooks giving AI coding agents a Clojure REPL
- Last pushed: 2026-07-16
- Branches observed: 5+ world-increment sweep branches

**Cumulative DB state:**
- World increments: 24
- Repo snapshots: 945

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-07-19)

| World | Address | Balance (APT) |
|-------|---------|---------------|
| A        | 0x8699edc0960dd5b916... | 0.00000000 APT |
| B        | 0x3f892ebe6e45164e63... | 0.00000000 APT |
| C        | 0x38b99e63ada9b6fef1... | 0.00000000 APT |
| D        | 0xf77656248f64d5dd00... | 0.00000000 APT |
| E        | 0xdc1d9d533bac3507f9... | 0.00000000 APT |
| F        | 0x18a14b5b4bec118c1c... | 0.00000000 APT |
| G        | 0x69a394c0b0ac842127... | 0.00000000 APT |
| H        | 0xce67c327a7844e5488... | 0.00000000 APT |
| I        | 0x070fe5d74e4eda30e2... | 0.00000000 APT |
| J        | 0x4d964db8f538374034... | 0.00000000 APT |
| K        | 0xa732040a6b0d559041... | 0.00000000 APT |
| L        | 0x7c2eaeafad9725492e... | 0.00000000 APT |
| M        | 0x6fed37a7553ef16b2a... | 0.00000000 APT |
| N        | 0xe7dde6da0a65f51062... | 0.00000000 APT |
| O        | 0x73252b6011a75115a2... | 0.00000000 APT |
| P        | 0x6218792de4a9bc3891... | 0.00000000 APT |
| Q        | 0xac40fa50b81b4ca6b1... | 0.00000000 APT |
| R        | 0x7ce605cc8fda4f8e4a... | 0.00000000 APT |
| S        | 0xb8753014e4888ea48a... | 0.00000000 APT |
| T        | 0x35781dc0e42fef3f25... | 0.00000000 APT |
| U        | 0x75860da47565f6509b... | 0.00000000 APT |
| V        | 0xb59dd8170321dfab5a... | 0.00000000 APT |
| W        | 0x5f32aef70f5ba530d3... | 0.00000000 APT |
| X        | 0xa95cbbd116548ac990... | 0.00000000 APT |
| Y        | 0xd8e32848f1dffa811b... | 0.00000000 APT |
| Z        | 0x7af0ef6e1bd706f4b3... | 0.00000000 APT |
| alice    | 0xc793acdec12b4a6371... | 0.00000000 APT |
| bob      | 0x0a3c00c58fdf9020b2... | 0.00000000 APT |

**Summary:**
- Total wallets probed: 28
- Active wallets (>0 APT): 0
- Total APT tracked: 0.00000000 APT
- All queried wallets show 0 APT (accounts exist on-chain but CoinStore not initialized or empty)

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f... | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f3f... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df40622... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a49... | 2 | ✓ |
| V-W | 0x40fad7b423a843650f... | 2 | ✓ |

**Summary:** 5/5 multisig accounts healthy

### MNX Markets (testnet.mnx.fi)

MNX testnet returned no REST API data — SPA architecture with no public JSON endpoints accessible from this environment.

---

## Cumulative DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 24 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

*DB: `packages/world-increment/ducklake/world-increments.duckdb`*
