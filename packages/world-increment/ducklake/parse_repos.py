#!/usr/bin/env python3
"""Parse GitHub search result files and generate DuckDB INSERT SQL."""

import json
import os
import sys

TOOL_RESULTS_DIR = "/root/.claude/projects/-home-user-gorj/e0f931f8-ccc6-54f7-8a4c-5dfd3db6a322/tool-results"

FILES = [
    ("mcp-github-search_repositories-1780725962182.txt", "plurigrid"),
    ("mcp-github-search_repositories-1780725960811.txt", "kubeflow"),
    ("mcp-github-search_repositories-1780725964116.txt", "bmorphism"),
    ("mcp-github-search_repositories-1780725963502.txt", "zubyul"),
    ("mcp-github-search_repositories-1780725963336.txt", "migalkin"),
    ("mcp-github-search_repositories-1780725968393.txt", "AustinCStone"),
    ("toolu_01SVq7FriAZN2Dxo98aFo3yF.json", "wasita"),
]

OUTPUT_SQL = "/home/user/gorj/packages/world-increment/ducklake/repo_inserts.sql"


def resolve_filepath(directory, filename):
    """Resolve a file path by scanning the directory listing.

    On some filesystems the path built from a literal string fails even though
    the file exists.  Building the path via os.listdir() + os.path.join()
    always works.
    """
    try:
        for entry in os.listdir(directory):
            if entry == filename:
                return os.path.join(directory, entry)
    except OSError:
        pass
    return None


def extract_items_from_data(data):
    """Extract the list of repository items from various JSON structures."""
    # Structure 1: {"total_count": N, "items": [...]}
    if isinstance(data, dict) and "items" in data:
        return data["items"]

    # Structure 2: MCP content envelope as a list of blocks
    # [{"type": "text", "text": "{\"items\": [...]}"}]
    if isinstance(data, list):
        for block in data:
            if isinstance(block, dict) and block.get("type") == "text":
                try:
                    inner = json.loads(block["text"])
                    if isinstance(inner, dict) and "items" in inner:
                        return inner["items"]
                except (json.JSONDecodeError, KeyError):
                    pass
        # If no MCP block found, treat the list as items directly
        # (only if items look like repo dicts)
        if data and isinstance(data[0], dict) and "full_name" in data[0]:
            return data

    # Structure 3: {"content": [...]}
    if isinstance(data, dict) and "content" in data:
        content = data["content"]
        if isinstance(content, list):
            for block in content:
                if isinstance(block, dict) and block.get("type") == "text":
                    try:
                        inner = json.loads(block["text"])
                        if isinstance(inner, dict) and "items" in inner:
                            return inner["items"]
                    except (json.JSONDecodeError, KeyError):
                        pass
        elif isinstance(content, str):
            try:
                inner = json.loads(content)
                if isinstance(inner, dict) and "items" in inner:
                    return inner["items"]
            except json.JSONDecodeError:
                pass

    # Structure 4: {"result": {"items": [...]}}
    if isinstance(data, dict) and "result" in data:
        inner = data["result"]
        if isinstance(inner, dict) and "items" in inner:
            return inner["items"]

    return None


def parse_file(filepath, label):
    """Parse a JSON file and extract repo records."""
    if filepath is None:
        print(f"  SKIPPING (not found): {label}", file=sys.stderr)
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read().strip()

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"  ERROR parsing {label} ({os.path.basename(filepath)}): {e}", file=sys.stderr)
        return []

    items = extract_items_from_data(data)

    if items is None:
        top = list(data.keys()) if isinstance(data, dict) else type(data).__name__
        print(f"  WARNING: Could not find 'items' in {label} (top-level: {top})", file=sys.stderr)
        return []

    repos = []
    for item in items:
        if not isinstance(item, dict):
            print(f"  WARNING: skipping non-dict item in {label}: {item!r}", file=sys.stderr)
            continue
        owner = item.get("owner", {})
        org_or_user = owner.get("login") if isinstance(owner, dict) else None
        repo = {
            "org_or_user": org_or_user,
            "repo_name": item.get("name"),
            "full_name": item.get("full_name"),
            "language": item.get("language"),
            "stars": item.get("stargazers_count", 0),
            "forks": item.get("forks_count", 0),
            "open_issues": item.get("open_issues_count", 0),
            "pushed_at": item.get("pushed_at"),
            "description": item.get("description"),
        }
        repos.append(repo)

    print(f"  [{label}] Parsed {len(repos)} repos from {os.path.basename(filepath)}", file=sys.stderr)
    return repos


def escape_sql_string(s):
    """Escape single quotes for SQL string literals."""
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"


def main():
    all_repos = []

    for filename, label in FILES:
        filepath = resolve_filepath(TOOL_RESULTS_DIR, filename)
        repos = parse_file(filepath, label)
        all_repos.extend(repos)

    total = len(all_repos)
    print(f"\nTotal repos collected: {total}", file=sys.stderr)

    # Build SQL
    lines = []
    lines.append("-- GitHub repository snapshots")
    lines.append(f"-- Total repos: {total}")
    lines.append("-- Generated by parse_repos.py")
    lines.append("")

    if not all_repos:
        lines.append("-- No repos found.")
    else:
        value_rows = []
        for repo in all_repos:
            org_or_user = escape_sql_string(repo["org_or_user"])
            repo_name = escape_sql_string(repo["repo_name"])
            full_name = escape_sql_string(repo["full_name"])
            language = escape_sql_string(repo["language"])
            stars = repo["stars"] if repo["stars"] is not None else 0
            forks = repo["forks"] if repo["forks"] is not None else 0
            open_issues = repo["open_issues"] if repo["open_issues"] is not None else 0
            pushed_at = escape_sql_string(repo["pushed_at"])
            description = escape_sql_string(repo["description"])

            row = (
                f"(nextval('repo_seq'), 1, {org_or_user}, {repo_name}, {full_name}, "
                f"{language}, {stars}, {forks}, {open_issues}, {pushed_at}, {description})"
            )
            value_rows.append(row)

        insert_header = (
            "INSERT INTO repo_snapshots "
            "(id, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description) VALUES"
        )
        lines.append(insert_header)
        for i, row in enumerate(value_rows):
            if i < len(value_rows) - 1:
                lines.append(row + ",")
            else:
                lines.append(row + ";")

    lines.append("")
    lines.append(f"-- Total repos inserted: {total}")

    sql_content = "\n".join(lines)

    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write(sql_content)

    print(f"SQL written to: {OUTPUT_SQL}", file=sys.stderr)
    print(f"Total: {total} repos", file=sys.stderr)


if __name__ == "__main__":
    main()
