"""
SOHAG STAR Investigation (M31 / HST PHAST)
File: scripts/run_datalab_query.py
Purpose: Execute schema discovery or candidate SQL/ADQL queries against
         NOIRLab Astro Data Lab via dl.queryClient and save results.

Salsabilah Ecosystem
(Powered by Gemini)
"""

from pathlib import Path
from dl import queryClient as qc


def run_sql_file(sql_path: str, output_csv: str, fmt: str = "csv", async_: bool = False):
    """Read a SQL/ADQL file, execute it on Astro Data Lab, and save output."""
    sql_text = Path(sql_path).read_text(encoding="utf-8")

    # Strip comment-only lines to avoid sending empty query blocks
    statements = [
        stmt.strip()
        for stmt in sql_text.split(";")
        if any(line.strip() and not line.strip().startswith("--") for line in stmt.splitlines())
    ]
    if not statements:
        raise ValueError(f"No executable SQL statements found in {sql_path}")

    query = statements[0]
    result = qc.query(sql=query, fmt=fmt, async_=async_)

    out_path = Path(output_csv)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if isinstance(result, str):
        out_path.write_text(result, encoding="utf-8")
    else:
        result.to_csv(out_path, index=False)

    return out_path


if __name__ == "__main__":
    print("SOHAG STAR Astro Data Lab query runner ready.")
    print("Verify exact PHAST table/column names before running candidate queries.")
  
