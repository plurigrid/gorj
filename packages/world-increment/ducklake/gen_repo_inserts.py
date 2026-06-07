#!/usr/bin/env python3
"""
Parse GitHub search result JSON files and generate SQL INSERT statements
for a DuckDB repo_snapshots table.
"""

import json
import os
import sys

BASE_DIR = "/root/.claude/projects/-home-user-gorj/912f0641-ac6d-590d-9a74-8a8eba7ef987/tool-results"

SOURCES = [
    {
        "label": "plurigrid (org)",
        "path": os.path.join(BASE_DIR, "mcp-github-search_repositories-1780808755975.txt"),
        "format": "plain_json",
    },
    {
        "label": "kubeflow (org)",
        "path": os.path.join(BASE_DIR, "mcp-github-search_repositories-1780808755032.txt"),
        "format": "plain_json",
    },
    {
        "label": "bmorphism (user)",
        "path": os.path.join(BASE_DIR, "mcp-github-search_repositories-1780808757579.txt"),
        "format": "plain_json",
    },
    {
        "label": "zubyul (user)",
        "path": os.path.join(BASE_DIR, "mcp-github-search_repositories-1780808756942.txt"),
        "format": "plain_json",
    },
    {
        "label": "migalkin (user)",
        "path": os.path.join(BASE_DIR, "mcp-github-search_repositories-1780808756640.txt"),
        "format": "plain_json",
    },
    {
        "label": "wasita (user)",
        "path": os.path.join(BASE_DIR, "toolu_01V5N1NJs5MAffvawzWMtAK5.json"),
        "format": "wrapped_json",  # JSON array with one element having a "text" field
    },
    {
        "label": "AustinCStone (user)",
        "path": os.path.join(BASE_DIR, "mcp-github-search_repositories-1780808760100.txt"),
        "format": "plain_json",
    },
]

OUTPUT_PATH = "/home/user/gorj/packages/world-increment/ducklake/repo_inserts.sql"


def escape_sql(value):
    """Escape a string value for SQL: double single quotes, wrap in single quotes.
    Returns NULL if value is None."""
    if value is None:
        return "NULL"
    return "'" + str(value).replace("'", "''") + "'"


def load_items(source):
    """Load repo items from a source file. Returns (items, error_or_None)."""
    path = source["path"]
    fmt = source["format"]

    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
    except FileNotFoundError:
        return [], f"File not found: {path}"
    except Exception as e:
        return [], f"Error reading {path}: {e}"

    try:
        if fmt == "wrapped_json":
            # JSON array with one element that has a "text" field containing the real JSON
            outer = json.loads(raw)
            if isinstance(outer, list):
                inner_text = outer[0]["text"]
            else:
                inner_text = outer["text"]
            data = json.loads(inner_text)
        else:
            data = json.loads(raw)

        items = data.get("items", [])
        return items, None
    except Exception as e:
        return [], f"Parse error for {path}: {e}"


def repo_to_sql_row(repo):
    """Convert a repo dict to a SQL values tuple string."""
    org_or_user = escape_sql(repo.get("owner", {}).get("login"))
    repo_name = escape_sql(repo.get("name"))
    full_name = escape_sql(repo.get("full_name"))
    language = escape_sql(repo.get("language"))  # may be None
    stars = repo.get("stargazers_count")
    forks = repo.get("forks_count")
    open_issues = repo.get("open_issues_count")
    pushed_at = escape_sql(repo.get("pushed_at"))
    description = escape_sql(repo.get("description"))  # may be None

    stars_sql = str(stars) if stars is not None else "NULL"
    forks_sql = str(forks) if forks is not None else "NULL"
    issues_sql = str(open_issues) if open_issues is not None else "NULL"

    return (
        f"(nextval('repo_seq'), 1, {org_or_user}, {repo_name}, {full_name}, "
        f"{language}, {stars_sql}, {forks_sql}, {issues_sql}, {pushed_at}, {description})"
    )


def main():
    all_rows = []
    summary = []
    errors = []

    for source in SOURCES:
        items, err = load_items(source)
        if err:
            errors.append(f"  ERROR [{source['label']}]: {err}")
            summary.append(f"  {source['label']}: 0 repos (ERROR)")
            continue

        rows = []
        for repo in items:
            try:
                row = repo_to_sql_row(repo)
                rows.append(row)
            except Exception as e:
                errors.append(f"  ERROR [{source['label']}] repo '{repo.get('full_name', '?')}': {e}")

        all_rows.extend(rows)
        summary.append(f"  {source['label']}: {len(rows)} repos")

    # Build SQL output
    lines = [
        "-- Auto-generated repo_snapshots INSERT statements",
        "-- Sources: plurigrid org, kubeflow org, bmorphism user, zubyul user,",
        "--          migalkin user, wasita user, AustinCStone user",
        "--",
    ]

    if all_rows:
        lines.append(
            "INSERT INTO repo_snapshots (id, increment_id, org_or_user, repo_name, full_name, "
            "language, stars, forks, open_issues, pushed_at, description) VALUES"
        )
        for i, row in enumerate(all_rows):
            suffix = "," if i < len(all_rows) - 1 else ";"
            lines.append(row + suffix)
    else:
        lines.append("-- No rows generated (all sources failed)")

    sql_content = "\n".join(lines) + "\n"

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(sql_content)

    print(f"Written: {OUTPUT_PATH}")
    print(f"Total rows: {len(all_rows)}")
    print()
    print("Per-source counts:")
    for s in summary:
        print(s)

    if errors:
        print()
        print("Errors:")
        for e in errors:
            print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
