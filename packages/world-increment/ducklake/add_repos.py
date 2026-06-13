#!/usr/bin/env python3
"""Add plurigrid, bmorphism, kubeflow repos to world-increments DuckDB."""
import duckdb, json, hashlib

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB_PATH)

GF3 = [(0,"#d3869b","ERGODIC"),(1,"#b8bb26","PLUS"),(-1,"#cc241d","MINUS")]
def gf3(id_): t=id_%3; return GF3[t]
def snap_hash(d): return hashlib.sha256(json.dumps(d,sort_keys=True).encode()).hexdigest()[:16]

cur_inc = con.execute("SELECT COALESCE(MAX(id),0) FROM world_increments").fetchone()[0]
cur_rep = con.execute("SELECT COALESCE(MAX(id),0) FROM repo_snapshots").fetchone()[0]
inc_id = cur_inc + 1
repo_id = cur_rep + 1

plurigrid_repos = [
  {"org_or_user":"plurigrid","repo_name":"asi","full_name":"plurigrid/asi","language":"HTML","stars":26,"forks":8,"open_issues":4,"pushed_at":"2026-06-10T12:51:42Z","description":"everything is topological chemputer!"},
  {"org_or_user":"plurigrid","repo_name":"place","full_name":"plurigrid/place","language":"TeX","stars":1,"forks":2,"open_issues":8,"pushed_at":"2026-06-10T16:25:05Z","description":None},
  {"org_or_user":"plurigrid","repo_name":"eirobri","full_name":"plurigrid/eirobri","language":"Clojure","stars":0,"forks":0,"open_issues":29,"pushed_at":"2026-06-03T20:43:46Z","description":"EiRoBri replay world"},
  {"org_or_user":"plurigrid","repo_name":"nash-portal","full_name":"plurigrid/nash-portal","language":"Rust","stars":2,"forks":3,"open_issues":1,"pushed_at":"2026-05-19T01:49:59Z","description":"NASH token TUI in the browser"},
  {"org_or_user":"plurigrid","repo_name":"gorj","full_name":"plurigrid/gorj","language":"Clojure","stars":0,"forks":0,"open_issues":539,"pushed_at":"2026-06-13T04:10:33Z","description":"forj + Rama topology nREPL routing + GF(3) gay trit coloring"},
  {"org_or_user":"plurigrid","repo_name":"zig-syrup","full_name":"plurigrid/zig-syrup","language":"Zig","stars":2,"forks":2,"open_issues":0,"pushed_at":"2026-04-30T03:52:16Z","description":"High-performance Zig OCapN Syrup"},
  {"org_or_user":"plurigrid","repo_name":"asi-skills","full_name":"plurigrid/asi-skills","language":"Julia","stars":3,"forks":1,"open_issues":0,"pushed_at":"2026-04-26T08:09:26Z","description":"69 skills with Galois Hole Type accessibility"},
  {"org_or_user":"plurigrid","repo_name":"bci-blue-share","full_name":"plurigrid/bci-blue-share","language":"JavaScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-26T07:08:03Z","description":"BCI signal infrastructure"},
  {"org_or_user":"plurigrid","repo_name":"nanoclj-zig","full_name":"plurigrid/nanoclj-zig","language":"Zig","stars":1,"forks":2,"open_issues":20,"pushed_at":"2026-04-25T07:29:09Z","description":"NaN-boxed Clojure interpreter in Zig 0.15"},
  {"org_or_user":"plurigrid","repo_name":"spi-race","full_name":"plurigrid/spi-race","language":"Swift","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-21T19:31:56Z","description":"Splitmix Parallel Integrity — deterministic color generation"},
  {"org_or_user":"plurigrid","repo_name":"reafference","full_name":"plurigrid/reafference","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-16T05:21:49Z","description":"Reafference adaptation workspace"},
  {"org_or_user":"plurigrid","repo_name":"web-browser","full_name":"plurigrid/web-browser","language":"Rust","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-10T02:54:47Z","description":"web-browser from prepostweb lineage"},
  {"org_or_user":"plurigrid","repo_name":"vivarium","full_name":"plurigrid/vivarium","language":"Clojure","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-04-08T08:38:37Z","description":None},
  {"org_or_user":"plurigrid","repo_name":"forester","full_name":"plurigrid/forester","language":"XSLT","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-30T01:32:26Z","description":"CatColab mathematical documentation forest"},
  {"org_or_user":"plurigrid","repo_name":"gatomic","full_name":"plurigrid/gatomic","language":"Clojure","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-30T00:54:48Z","description":"Deterministic color identity store with sonification"},
  {"org_or_user":"plurigrid","repo_name":"nblm-flashcards","full_name":"plurigrid/nblm-flashcards","language":"Hy","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T08:23:01Z","description":"NotebookLM Enterprise flashcard pipeline"},
  {"org_or_user":"plurigrid","repo_name":"graded-optic","full_name":"plurigrid/graded-optic","language":"Haskell","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-08T16:10:16Z","description":"Semiring-graded bidirectional processes"},
  {"org_or_user":"plurigrid","repo_name":"shepherd","full_name":"plurigrid/shepherd","language":"Scheme","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-23T07:47:28Z","description":"Spritely Shepherd - Service manager"},
  {"org_or_user":"plurigrid","repo_name":"goblinshare","full_name":"plurigrid/goblinshare","language":"Scheme","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-23T07:47:12Z","description":"P2P filesharing demo for Goblins"},
  {"org_or_user":"plurigrid","repo_name":"hoot","full_name":"plurigrid/hoot","language":"Scheme","stars":0,"forks":1,"open_issues":1,"pushed_at":"2026-01-23T07:47:10Z","description":"Spritely Hoot - Scheme to WebAssembly compiler"},
  {"org_or_user":"plurigrid","repo_name":"leprechauns","full_name":"plurigrid/leprechauns","language":"Racket","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-23T07:46:46Z","description":"Spritely Goblins + Gay.jl semantic colors"},
  {"org_or_user":"plurigrid","repo_name":"gay-tofu","full_name":"plurigrid/gay-tofu","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-08T15:14:34Z","description":"Low-discrepancy color sequences for visual TOFU authentication"},
  {"org_or_user":"plurigrid","repo_name":"lazygay","full_name":"plurigrid/lazygay","language":"Go","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-08T14:19:25Z","description":"lazygit fork with Gay.jl deterministic commit coloring"},
  {"org_or_user":"plurigrid","repo_name":"gay-rs","full_name":"plurigrid/gay-rs","language":"Rust","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-08T14:19:22Z","description":"Rust crate for Gay.jl deterministic coloring with GF(3) trits"},
  {"org_or_user":"plurigrid","repo_name":"lazybjj","full_name":"plurigrid/lazybjj","language":"Rust","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-08T14:19:19Z","description":"TUI for jj with Gay.jl GF(3) coloring"},
  {"org_or_user":"plurigrid","repo_name":"ontology","full_name":"plurigrid/ontology","language":"JavaScript","stars":8,"forks":9,"open_issues":16,"pushed_at":"2025-05-27T18:18:34Z","description":"autopoietic ergodicity and embodied gradualism"},
  {"org_or_user":"plurigrid","repo_name":"Plurigraph","full_name":"plurigrid/Plurigraph","language":"JavaScript","stars":3,"forks":5,"open_issues":4,"pushed_at":"2025-01-05T08:39:09Z","description":"Plurigrid knowledge base for Obsidian.md"},
  {"org_or_user":"plurigrid","repo_name":"agent","full_name":"plurigrid/agent","language":"Python","stars":5,"forks":1,"open_issues":6,"pushed_at":"2023-03-31T18:45:23Z","description":"Framework for agency amplification"},
  {"org_or_user":"plurigrid","repo_name":"vcg-auction","full_name":"plurigrid/vcg-auction","language":"Rust","stars":7,"forks":2,"open_issues":1,"pushed_at":"2023-03-16T21:53:08Z","description":"a simple contract that performs a VCG auction"},
  {"org_or_user":"plurigrid","repo_name":"microworlds","full_name":"plurigrid/microworlds","language":"Rust","stars":3,"forks":5,"open_issues":3,"pushed_at":"2023-05-13T03:54:56Z","description":"👽"},
  {"org_or_user":"plurigrid","repo_name":"VPP","full_name":"plurigrid/VPP","language":"Julia","stars":0,"forks":1,"open_issues":0,"pushed_at":"2023-01-11T18:41:07Z","description":"Hyperreal Power Plant 🏭⚡️"},
  {"org_or_user":"plurigrid","repo_name":"StochFlow","full_name":"plurigrid/StochFlow","language":"Python","stars":4,"forks":1,"open_issues":0,"pushed_at":"2024-03-20T23:34:57Z","description":"Stochastic interpolant models and algorithms"},
  {"org_or_user":"plurigrid","repo_name":"act","full_name":"plurigrid/act","language":"Python","stars":3,"forks":1,"open_issues":4,"pushed_at":"2024-07-26T08:27:08Z","description":"building blocks for cognitive category theory"},
  {"org_or_user":"plurigrid","repo_name":"duck-kanban","full_name":"plurigrid/duck-kanban","language":"Rust","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-09-26T20:18:38Z","description":"Duck intelligence kanban system"},
]

bmorphism_repos = [
  {"org_or_user":"bmorphism","repo_name":"satreadout","full_name":"bmorphism/satreadout","language":"Lean","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-06-10T22:47:47Z","description":"Machine-checked saturating non-Riemannian perceptual readout"},
  {"org_or_user":"bmorphism","repo_name":"Gay.jl","full_name":"bmorphism/Gay.jl","language":"Julia","stars":1,"forks":1,"open_issues":189,"pushed_at":"2026-06-13T00:44:15Z","description":"Wide-gamut color sampling with splittable determinism"},
  {"org_or_user":"bmorphism","repo_name":"world","full_name":"bmorphism/world","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-06-02T06:49:02Z","description":"Local worlds launcher for SA3, jank, and world proofs."},
  {"org_or_user":"bmorphism","repo_name":"oxgame","full_name":"bmorphism/oxgame","language":"OCaml","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-15T09:53:27Z","description":"Stellar resolution and open-game composition for OCaml"},
  {"org_or_user":"bmorphism","repo_name":"nanoclj-zig","full_name":"bmorphism/nanoclj-zig","language":"Zig","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-05-07T20:12:15Z","description":None},
  {"org_or_user":"bmorphism","repo_name":"zig-syrup","full_name":"bmorphism/zig-syrup","language":"Zig","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-07T19:49:05Z","description":"Embeddable OCapN Syrup encoder/decoder in Zig"},
  {"org_or_user":"bmorphism","repo_name":"ocaml-mcp-sdk","full_name":"bmorphism/ocaml-mcp-sdk","language":"OCaml","stars":61,"forks":2,"open_issues":0,"pushed_at":"2026-03-16T05:24:25Z","description":"OCaml SDK for Model Context Protocol"},
  {"org_or_user":"bmorphism","repo_name":"anti-bullshit-mcp-server","full_name":"bmorphism/anti-bullshit-mcp-server","language":"JavaScript","stars":23,"forks":7,"open_issues":1,"pushed_at":"2026-01-16T08:54:58Z","description":"MCP server for analyzing claims and detecting manipulation"},
  {"org_or_user":"bmorphism","repo_name":"vibespace-mcp-go-ternary","full_name":"bmorphism/vibespace-mcp-go-ternary","language":"HTML","stars":0,"forks":1,"open_issues":3,"pushed_at":"2026-01-11T12:50:40Z","description":"Go MCP for vibes and worlds with NATS and balanced ternary"},
  {"org_or_user":"bmorphism","repo_name":"shitcoin","full_name":"bmorphism/shitcoin","language":"Python","stars":5,"forks":0,"open_issues":0,"pushed_at":"2026-04-08T08:07:08Z","description":"gets denom for cw20 assets for permissionless degeneracy in IBC"},
  {"org_or_user":"bmorphism","repo_name":"say-mcp-server","full_name":"bmorphism/say-mcp-server","language":"JavaScript","stars":20,"forks":9,"open_issues":3,"pushed_at":"2025-01-07T03:15:18Z","description":"MCP server for macOS text-to-speech"},
  {"org_or_user":"bmorphism","repo_name":"manifold-mcp-server","full_name":"bmorphism/manifold-mcp-server","language":"JavaScript","stars":14,"forks":9,"open_issues":5,"pushed_at":"2025-01-11T10:36:58Z","description":"MCP server for Manifold Markets prediction markets"},
  {"org_or_user":"bmorphism","repo_name":"babashka-mcp-server","full_name":"bmorphism/babashka-mcp-server","language":"JavaScript","stars":19,"forks":6,"open_issues":3,"pushed_at":"2025-01-05T11:09:42Z","description":"MCP server for Babashka native Clojure"},
  {"org_or_user":"bmorphism","repo_name":"penrose-mcp","full_name":"bmorphism/penrose-mcp","language":"JavaScript","stars":10,"forks":4,"open_issues":0,"pushed_at":"2025-01-20T21:44:55Z","description":"Penrose server for the Infinity-Topos environment"},
  {"org_or_user":"bmorphism","repo_name":"marginalia-mcp-server","full_name":"bmorphism/marginalia-mcp-server","language":"JavaScript","stars":8,"forks":6,"open_issues":0,"pushed_at":"2025-01-06T05:47:24Z","description":"MCP server for marginalia and annotations"},
  {"org_or_user":"bmorphism","repo_name":"nats-mcp-server","full_name":"bmorphism/nats-mcp-server","language":None,"stars":7,"forks":3,"open_issues":2,"pushed_at":"2025-01-06T23:33:41Z","description":"MCP server for NATS messaging system"},
  {"org_or_user":"bmorphism","repo_name":"hypernym-mcp-server","full_name":"bmorphism/hypernym-mcp-server","language":"JavaScript","stars":6,"forks":5,"open_issues":0,"pushed_at":"2025-04-02T21:21:08Z","description":None},
  {"org_or_user":"bmorphism","repo_name":"penumbra-mcp","full_name":"bmorphism/penumbra-mcp","language":"JavaScript","stars":5,"forks":6,"open_issues":3,"pushed_at":"2025-01-07T01:15:23Z","description":"MCP server for Penumbra blockchain"},
  {"org_or_user":"bmorphism","repo_name":"risc0-cosmwasm-example","full_name":"bmorphism/risc0-cosmwasm-example","language":"Rust","stars":23,"forks":2,"open_issues":1,"pushed_at":"2022-10-20T23:50:40Z","description":"CosmWasm + zkVM RISC-V EFI template"},
  {"org_or_user":"bmorphism","repo_name":"graphistry-mcp","full_name":"bmorphism/graphistry-mcp","language":"Python","stars":2,"forks":0,"open_issues":0,"pushed_at":"2025-05-06T17:34:24Z","description":"Graphistry MCP integration for graph visualization"},
  {"org_or_user":"bmorphism","repo_name":"monero-rental-hash-war","full_name":"bmorphism/monero-rental-hash-war","language":"Haskell","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-10-05T23:08:54Z","description":"Compositional OpenGame analysis of Monero rental hash war"},
  {"org_or_user":"bmorphism","repo_name":"magic-world-org","full_name":"bmorphism/magic-world-org","language":"Python","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-04-05T07:03:50Z","description":"Magic World Org (Local MLX)"},
  {"org_or_user":"bmorphism","repo_name":"open-location-code-zig","full_name":"bmorphism/open-location-code-zig","language":"Zig","stars":3,"forks":0,"open_issues":0,"pushed_at":"2025-12-30T19:33:45Z","description":"Open Location Code (Plus Codes) for Zig"},
  {"org_or_user":"bmorphism","repo_name":"bafishka","full_name":"bmorphism/bafishka","language":"Clojure","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-12-19T09:38:00Z","description":"Rust-native Fish shell-friendly file operations with Steel-backed SCI Clojure"},
  {"org_or_user":"bmorphism","repo_name":"open-games-agda","full_name":"bmorphism/open-games-agda","language":"Agda","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-12-22T11:16:29Z","description":"A formalization of open games in Agda"},
  {"org_or_user":"bmorphism","repo_name":"flox-mcp-bb","full_name":"bmorphism/flox-mcp-bb","language":"Clojure","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-12T02:45:43Z","description":"Open-source MCP server for Flox"},
  {"org_or_user":"bmorphism","repo_name":"whale","full_name":"bmorphism/whale","language":"MATLAB","stars":2,"forks":0,"open_issues":0,"pushed_at":"2025-09-04T06:55:21Z","description":"omniglot + sperm whale codas = metawhaling"},
  {"org_or_user":"bmorphism","repo_name":"slowtime-mcp-server","full_name":"bmorphism/slowtime-mcp-server","language":"TypeScript","stars":3,"forks":5,"open_issues":6,"pushed_at":"2025-01-02T01:23:33Z","description":"MCP for secure time-based operations with timing attack protection"},
  {"org_or_user":"bmorphism","repo_name":"lumon-tui","full_name":"bmorphism/lumon-tui","language":"Python","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-02-02T11:24:21Z","description":"Terminal-based parallel worlds implementation"},
  {"org_or_user":"bmorphism","repo_name":"GeoACSets.jl","full_name":"bmorphism/GeoACSets.jl","language":"Julia","stars":0,"forks":1,"open_issues":1,"pushed_at":"2026-01-19T13:57:13Z","description":"Categorical data structures with geospatial capabilities"},
]

kubeflow_repos = [
  {"org_or_user":"kubeflow","repo_name":"trainer","full_name":"kubeflow/trainer","language":"Go","stars":2112,"forks":967,"open_issues":113,"pushed_at":"2026-06-13T03:19:28Z","description":"Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"},
  {"org_or_user":"kubeflow","repo_name":"notebooks","full_name":"kubeflow/notebooks","language":None,"stars":73,"forks":119,"open_issues":168,"pushed_at":"2026-06-13T00:38:04Z","description":"Kubeflow Notebooks for interactive development environments"},
  {"org_or_user":"kubeflow","repo_name":"hub","full_name":"kubeflow/hub","language":"Go","stars":173,"forks":182,"open_issues":42,"pushed_at":"2026-06-12T22:39:56Z","description":"Model Registry for ML model lifecycle management"},
  {"org_or_user":"kubeflow","repo_name":"katib","full_name":"kubeflow/katib","language":"Python","stars":1683,"forks":526,"open_issues":116,"pushed_at":"2026-06-12T19:56:00Z","description":"Automated Machine Learning on Kubernetes"},
  {"org_or_user":"kubeflow","repo_name":"spark-operator","full_name":"kubeflow/spark-operator","language":"Python","stars":3127,"forks":1490,"open_issues":102,"pushed_at":"2026-06-12T17:53:36Z","description":"Kubernetes operator for Apache Spark"},
  {"org_or_user":"kubeflow","repo_name":"mpi-operator","full_name":"kubeflow/mpi-operator","language":"Go","stars":528,"forks":236,"open_issues":103,"pushed_at":"2026-06-12T15:50:34Z","description":"Kubernetes Operator for MPI-based distributed training"},
  {"org_or_user":"kubeflow","repo_name":"community-distribution","full_name":"kubeflow/community-distribution","language":"YAML","stars":1023,"forks":1065,"open_issues":22,"pushed_at":"2026-06-12T15:28:04Z","description":"Kubeflow Community Distribution"},
  {"org_or_user":"kubeflow","repo_name":"kubeflow","full_name":"kubeflow/kubeflow","language":None,"stars":15720,"forks":2673,"open_issues":3,"pushed_at":"2026-06-11T16:32:05Z","description":"Machine Learning Toolkit for Kubernetes"},
  {"org_or_user":"kubeflow","repo_name":"pipelines","full_name":"kubeflow/pipelines","language":"Python","stars":4152,"forks":2007,"open_issues":494,"pushed_at":"2026-06-12T21:40:16Z","description":"Machine Learning Pipelines for Kubeflow"},
  {"org_or_user":"kubeflow","repo_name":"mcp-apache-spark-history-server","full_name":"kubeflow/mcp-apache-spark-history-server","language":"Python","stars":177,"forks":64,"open_issues":21,"pushed_at":"2026-06-10T18:49:04Z","description":"MCP Server and CLI for Apache Spark History Server"},
  {"org_or_user":"kubeflow","repo_name":"kale","full_name":"kubeflow/kale","language":"Python","stars":694,"forks":154,"open_issues":48,"pushed_at":"2026-06-12T22:05:05Z","description":"Kubeflow's superfood for Data Scientists"},
  {"org_or_user":"kubeflow","repo_name":"dashboard","full_name":"kubeflow/dashboard","language":"TypeScript","stars":16,"forks":59,"open_issues":75,"pushed_at":"2026-06-11T17:07:50Z","description":"Kubeflow Central Dashboard"},
  {"org_or_user":"kubeflow","repo_name":"sdk","full_name":"kubeflow/sdk","language":"Python","stars":120,"forks":180,"open_issues":133,"pushed_at":"2026-06-12T03:38:22Z","description":"Universal Python SDK to run AI workloads on Kubernetes"},
  {"org_or_user":"kubeflow","repo_name":"mcp-server","full_name":"kubeflow/mcp-server","language":"Python","stars":11,"forks":20,"open_issues":25,"pushed_at":"2026-05-12T10:14:24Z","description":"MCP Server for AI-Assisted Development with Kubeflow Tools"},
  {"org_or_user":"kubeflow","repo_name":"arena","full_name":"kubeflow/arena","language":"Go","stars":812,"forks":190,"open_issues":46,"pushed_at":"2026-05-07T06:46:17Z","description":"A CLI for Kubeflow."},
  {"org_or_user":"kubeflow","repo_name":"examples","full_name":"kubeflow/examples","language":"Jsonnet","stars":1461,"forks":756,"open_issues":111,"pushed_at":"2025-04-14T01:54:52Z","description":"Extended examples and tutorials"},
  {"org_or_user":"kubeflow","repo_name":"kfp-tekton","full_name":"kubeflow/kfp-tekton","language":"TypeScript","stars":182,"forks":123,"open_issues":79,"pushed_at":"2024-11-19T12:23:51Z","description":"Kubeflow Pipelines on Tekton"},
  {"org_or_user":"kubeflow","repo_name":"kfctl","full_name":"kubeflow/kfctl","language":"Go","stars":182,"forks":134,"open_issues":94,"pushed_at":"2023-08-15T20:19:22Z","description":"kfctl is a CLI for deploying and managing Kubeflow"},
  {"org_or_user":"kubeflow","repo_name":"fairing","full_name":"kubeflow/fairing","language":"Jsonnet","stars":337,"forks":143,"open_issues":134,"pushed_at":"2022-04-11T05:28:47Z","description":"Python SDK for building, training, and deploying ML models"},
  {"org_or_user":"kubeflow","repo_name":"pytorch-operator","full_name":"kubeflow/pytorch-operator","language":"Jsonnet","stars":310,"forks":143,"open_issues":63,"pushed_at":"2021-12-01T17:44:48Z","description":"PyTorch on Kubernetes"},
  {"org_or_user":"kubeflow","repo_name":"docs-agent","full_name":"kubeflow/docs-agent","language":"Python","stars":38,"forks":95,"open_issues":150,"pushed_at":"2026-06-11T18:43:15Z","description":"Kubeflow Documentation AI Agent"},
  {"org_or_user":"kubeflow","repo_name":"community","full_name":"kubeflow/community","language":"Jupyter Notebook","stars":194,"forks":260,"open_issues":23,"pushed_at":"2026-06-12T14:22:11Z","description":"Kubeflow community information and governance"},
  {"org_or_user":"kubeflow","repo_name":"website","full_name":"kubeflow/website","language":"HTML","stars":184,"forks":924,"open_issues":50,"pushed_at":"2026-06-12T03:12:34Z","description":"Kubeflow Website"},
  {"org_or_user":"kubeflow","repo_name":"pipelines-components","full_name":"kubeflow/pipelines-components","language":"Python","stars":11,"forks":43,"open_issues":33,"pushed_at":"2026-06-04T17:39:10Z","description":"Kubeflow Pipelines Components"},
]

ALL_REPOS = plurigrid_repos + bmorphism_repos + kubeflow_repos

for r in ALL_REPOS:
    trit, color, name = gf3(inc_id)
    h = snap_hash(r)
    con.execute("INSERT INTO world_increments VALUES (?,now(),?,?,?,'github',?,'repo_snapshot',?,?,?)",
                [inc_id, trit, color, name, r["org_or_user"], r["repo_name"], r["org_or_user"], h])
    con.execute("INSERT INTO repo_snapshots VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)",
                [repo_id, inc_id, r["org_or_user"], r["repo_name"], r["full_name"],
                 r["language"], r["stars"], r["forks"], r["open_issues"],
                 r["pushed_at"], r["description"]])
    inc_id += 1
    repo_id += 1

print(f"Added {len(ALL_REPOS)} repos")
r = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
print(f"Total repo_snapshots: {r}")
r = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
print(f"Total world_increments: {r}")

# Final stats by org
rows = con.execute("""
    SELECT org_or_user, COUNT(*) as cnt, SUM(stars) as total_stars
    FROM repo_snapshots
    GROUP BY org_or_user
    ORDER BY cnt DESC
""").fetchall()
print("\nRepos per source:")
for row in rows:
    print(f"  {row[0]}: {row[1]} repos, {row[2]} stars")

con.close()
print("Done.")
