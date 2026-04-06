# World-Increment Sweep + Hamming Snapshot

**Sweep Date/Time:** 2026-04-06T12:00:00Z (UTC)
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts per Org/User

| Source        | Type | Total Repos (public) | Repos Snapshotted |
|---------------|------|---------------------|-------------------|
| plurigrid     | org  | 95                  | 10                |
| kubeflow      | org  | 46                  | 10                |
| TeglonLabs    | org  | 3                   | 3                 |
| bmorphism     | user | 98                  | 10                |
| zubyul        | user | 44                  | 7                 |
| migalkin      | user | 19                  | 5                 |
| DJedamski     | user | 6                   | 4                 |
| wasita        | user | 9                   | 4                 |
| kristinezheng | user | 6                   | 3                 |
| M1shaaa       | user | 8                   | 3                 |
| AustinCStone  | user | 40                  | 4                 |

### Top Repos by Stars

| full_name                          | stars  | language   | description                                      |
|------------------------------------|--------|------------|--------------------------------------------------|
| kubeflow/kubeflow                  | 15,553 | —          | Machine Learning Toolkit for Kubernetes          |
| kubeflow/pipelines                 | 4,118  | Python     | Machine Learning Pipelines for Kubeflow          |
| kubeflow/spark-operator            | 3,111  | Python     | Kubernetes operator for Apache Spark             |
| kubeflow/trainer                   | 2,074  | Go         | Distributed AI Model Training                    |
| kubeflow/katib                     | 1,674  | Python     | Automated Machine Learning on Kubernetes         |
| kubeflow/examples                  | 1,459  | Jsonnet    | Extended examples and tutorials                  |
| kubeflow/manifests                 | 1,009  | YAML       | Kubeflow AI Reference Platform Deployment        |
| kubeflow/arena                     | 808    | Go         | A CLI for Kubeflow                               |
| kubeflow/kale                      | 682    | Python     | Kubeflow superfood for Data Scientists           |
| AustinCStone/TextGAN               | 92     | Python     | GAN for text generation in TensorFlow            |
| migalkin/NodePiece                 | 143    | Python     | Compositional KG Representations (ICLR22)        |
| migalkin/StarE                     | 88     | Python     | Message Passing for Hyper-Relational KGs         |
| bmorphism/ocaml-mcp-sdk            | 60     | OCaml      | OCaml SDK for Model Context Protocol             |
| bmorphism/anti-bullshit-mcp-server | 23     | JavaScript | MCP server for analyzing claims                  |
| bmorphism/risc0-cosmwasm-example   | 23     | Rust       | CosmWasm + zkVM RISC-V EFI template              |
| bmorphism/say-mcp-server           | 20     | JavaScript | MCP server for macOS text-to-speech              |
| bmorphism/babashka-mcp-server      | 18     | JavaScript | MCP server for Babashka Clojure                  |
| plurigrid/asi                      | 16     | HTML       | everything is topological chemputer!             |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 wallets queried against Aptos mainnet (`fullnode.mainnet.aptoslabs.com`).
The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource was not found on any address
(endpoint returned error/null), recorded as 0.0 APT.

| World | Address (truncated)   | Balance (APT) |
|-------|-----------------------|---------------|
| alice | 0xc793...cc7b         | 0.0           |
| bob   | 0x0a3c...2d5d         | 0.0           |
| A     | 0x8699...9d7a         | 0.0           |
| B     | 0x3f89...b13          | 0.0           |
| C     | 0x38b9...35e          | 0.0           |
| D     | 0xf776...dd1          | 0.0           |
| E     | 0xdc1d...d36          | 0.0           |
| F     | 0x18a1...f71          | 0.0           |
| G     | 0x69a3...f32          | 0.0           |
| H     | 0xce67...00f          | 0.0           |
| I     | 0x070f...fc9          | 0.0           |
| J     | 0x4d96...f54          | 0.0           |
| K     | 0xa732...dc4          | 0.0           |
| L     | 0x7c2e...ba9          | 0.0           |
| M     | 0x6fed...2e9          | 0.0           |
| N     | 0xe7dd...b2c          | 0.0           |
| O     | 0x7325...89d          | 0.0           |
| P     | 0x6218...948          | 0.0           |
| Q     | 0xac40...89a9         | 0.0           |
| R     | 0x7ce6...e10          | 0.0           |
| S     | 0xb875...386          | 0.0           |
| T     | 0x3578...588          | 0.0           |
| U     | 0x7586...956          | 0.0           |
| V     | 0xb59d...2c3          | 0.0           |
| W     | 0x5f32...7b0          | 0.0           |
| X     | 0xa95c...47d          | 0.0           |
| Y     | 0xd8e3...4c4          | 0.0           |
| Z     | 0x7af0...97c          | 0.0           |

### Multisig Contract Probes

All 5 multisig contracts responded successfully via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4...003        | 2             | true    |
| A-G  | 0xf56c...096        | 2             | true    |
| Y-Z  | 0xd3ff...883        | 2             | true    |
| S-T  | 0x3b1c...883        | 2             | true    |
| V-W  | 0x40fa...b6d        | 2             | true    |

### MNX Markets

`https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/tickers` returned HTML
(Next.js frontend rendered page), not JSON API data.

**MNX markets: unavailable** — no machine-readable API endpoint exposed at those paths.

---

## GF(3) Color Chain Legend

The `id % 3` trit determines color assignment for each record:

| id % 3 | GF(3) Trit | Color  | Hex Code | Name    |
|--------|-----------|--------|----------|---------|
| 0      | 0         | Pink   | #d3869b  | ERGODIC |
| 1      | +1        | Yellow | #b8bb26  | PLUS    |
| 2      | -1        | Red    | #cc241d  | MINUS   |

Colors drawn from the Gruvbox palette, mapped to GF(3) arithmetic:
- **ERGODIC (0):** Neutral/identity element — pink/mauve
- **PLUS (+1):** Positive trit — chartreuse/yellow-green
- **MINUS (-1):** Negative trit — deep red

Applied to `world_increments` (11 rows) and `repo_snapshots` (63 rows) via `id % 3`.

---

*Generated by autonomous sweep agent.*
*Session: https://claude.ai/code/session_01NKUDigJnjtSkFC4ipoYJbG*
