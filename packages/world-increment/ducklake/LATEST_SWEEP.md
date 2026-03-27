# World-Increment Sweep — 2026-03-27

## GF(3) Color Chain

| Trit | id mod 3 | Label | Color |
|------|-----------|-------|-------|
| 0 | ERGODIC | #d3869b (pink) |
| 1 | PLUS | #b8bb26 (yellow-green) |
| -1 | MINUS | #cc241d (red) |

## Summary

- **Sweep date:** 2026-03-27
- **Total repos indexed:** 97
- **Sources:** 11 (3 orgs, 8 users)
- **Total stars across corpus:** 32,114

## GF(3) Distribution

| Label | Color | Count | Stars |
|-------|-------|-------|-------|
| ERGODIC (trit=0) | #d3869b | 33 | 7,020 |
| PLUS (trit=1) | #b8bb26 | 32 | 5,632 |
| MINUS (trit=-1) | #cc241d | 32 | 19,462 |

## By Source

| Source | Repos | Stars |
|--------|-------|-------|
| org:kubeflow | 16 | 31,481 |
| user:migalkin | 6 | 276 |
| user:bmorphism | 16 | 185 |
| user:AustinCStone | 5 | 106 |
| org:plurigrid | 20 | 50 |
| user:zubyul | 12 | 9 |
| user:DJedamski | 5 | 3 |
| user:wasita | 5 | 2 |
| org:TeglonLabs | 3 | 2 |
| user:kristinezheng | 4 | 0 |
| user:M1shaaa | 5 | 0 |

## Top 10 Repos by Stars

| Repo | Stars | Language | GF3 |
|------|-------|----------|-----|
| kubeflow/kubeflow | 15,536 | — | MINUS (#cc241d) |
| kubeflow/pipelines | 4,113 | Python | ERGODIC (#d3869b) |
| kubeflow/spark-operator | 3,111 | Python | PLUS (#b8bb26) |
| kubeflow/trainer | 2,067 | Go | MINUS (#cc241d) |
| kubeflow/katib | 1,670 | Python | ERGODIC (#d3869b) |
| kubeflow/examples | 1,459 | Jsonnet | PLUS (#b8bb26) |
| kubeflow/manifests | 1,004 | YAML | MINUS (#cc241d) |
| kubeflow/arena | 810 | Go | ERGODIC (#d3869b) |
| kubeflow/kale | 680 | Python | PLUS (#b8bb26) |
| kubeflow/mpi-operator | 519 | Go | MINUS (#cc241d) |

## Notable Highlights

- **plurigrid/gorj** (this repo) — Clojure, pushed 2026-03-27 — active development of forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **plurigrid/asi** — HTML, 12 stars — "everything is topological chemputer!" pushed 2026-03-26
- **bmorphism/ocaml-mcp-sdk** — OCaml, 59 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **zubyul/gay-world** — Python, 1 star — Goblin world builder: each goblin is a world. MLX task decomposition
- **zubyul/Gay.jl** — active development 2026-03-26 — Wide-gamut color sampling with splittable determinism
- **kubeflow/mcp-apache-spark-history-server** — Python, 143 stars — MCP Server for Apache Spark, pushed 2026-03-27
- **migalkin/NodePiece** — Python, 143 stars — Compositional representations for Large Knowledge Graphs (ICLR'22)

## DuckDB Schema

```sql
CREATE TABLE repo_snapshots (
    id INTEGER PRIMARY KEY,
    full_name VARCHAR,
    name VARCHAR,
    source VARCHAR,
    language VARCHAR,
    stars INTEGER,
    forks INTEGER,
    open_issues INTEGER,
    pushed_at VARCHAR,
    description VARCHAR,
    trit INTEGER,        -- GF(3): 0=ERGODIC, 1=PLUS, 2=MINUS
    gf3_label VARCHAR,   -- ERGODIC | PLUS | MINUS
    gf3_color VARCHAR,   -- #d3869b | #b8bb26 | #cc241d
    sweep_date VARCHAR
);
```

Database file: `packages/world-increment/ducklake/sweep.db`
