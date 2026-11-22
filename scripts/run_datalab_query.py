#!/usr/bin/env python3
"""
SOHAG STAR Investigation (M31 / HST PHAST)
File: scripts/run_datalab_query.py
Purpose: Execute SQL/ADQL queries against NOIRLab Astro Data Lab and save
         results to CSV for reproducible schema discovery and candidate selection.

Salsabilah Ecosystem
(Powered by Gemini)
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd

try:
    from dl import authClient as ac
    from dl import queryClient as qc
except ImportError:
    ac = None
    qc = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run SQL/ADQL query in NOIRLab Astro Data Lab and export CSV."
    )
    parser.add_argument(
        "--sql-file",
        type=Path,
        required=True,
        help="Path to .sql file containing the query to execute.",
    )
    parser.add_argument(
        "--out-csv",
        type=Path,
        required=True,
        help="Destination path for query results CSV.",
    )
    parser.add_argument(
        "--profile",
        type=str,
        default="anonymous",
        help="Astro Data Lab login token or 'anonymous' (default: anonymous).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional row limit passed to Astro Data Lab queryClient.",
    )
    return parser.parse_args()


def load_sql(sql_path: Path) -> str:
    if not sql_path.exists():
        raise FileNotFoundError(f"SQL file not found: {sql_path}")
    query = sql_path.read_text(encoding="utf-8").strip()
    if not query:
        raise ValueError(f"SQL file is empty: {sql_path}")
    return query


def execute_query(sql: str, profile: str = "anonymous", limit: int | None = None) -> pd.DataFrame:
    if qc is None or ac is None:
        raise RuntimeError(
            "NOIRLab Astro Data Lab client ('dl') is not installed in this environment. "
            "Install 'astro-datalab' or run this script inside Astro Data Lab."
        )

    token = "anonymous" if profile == "anonymous" else ac.login(profile)
    kwargs = {"sql": sql, "fmt": "csv", "token": token}
    if limit is not None:
        kwargs["limit"] = limit

    csv_text = qc.query(**kwargs)
    if isinstance(csv_text, bytes):
        csv_text = csv_text.decode("utf-8")

    from io import StringIO

    return pd.read_csv(StringIO(csv_text))


def main() -> int:
    args = parse_args()
    try:
        sql = load_sql(args.sql_file)
        df = execute_query(sql=sql, profile=args.profile, limit=args.limit)
        args.out_csv.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(args.out_csv, index=False)
        print(f"Saved {len(df)} rows to {args.out_csv}")
        return 0
    except Exception as exc:
        print(f"Error executing query: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())


# Salsabilah Ecosystem
# (Powered by Gemini)
