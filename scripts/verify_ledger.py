#!/usr/bin/env python3
"""
SOHAG STAR Investigation (M31 / HST PHAST)
File: scripts/verify_ledger.py
Purpose: Audit candidate verification ledger CSVs for required fields,
         valid J2000 coordinates, PHAST brick membership, and status values.

Salsabilah Ecosystem
(Powered by Gemini)
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd

REQUIRED_COLUMNS = [
    "candidate_id",
    "source_id",
    "brick",
    "ra_deg",
    "dec_deg",
    "verification_status",
]

VALID_BRICKS = {
    "B24", "B25", "B26", "B27", "B28", "B29",
    "B30", "B31", "B32", "B33", "B34", "B35", "B36",
}

VALID_STATUSES = {"pending", "verified", "rejected", "needs_review"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit a SOHAG STAR candidate verification ledger CSV."
    )
    parser.add_argument(
        "--ledger",
        type=Path,
        required=True,
        help="Path to verification ledger CSV file.",
    )
    return parser.parse_args()


def audit_ledger(df: pd.DataFrame) -> list[str]:
    errors: list[str] = []

    missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_cols:
        errors.append(f"Missing required columns: {missing_cols}")
        return errors

    if df.empty:
        errors.append("Ledger contains no candidate rows.")
        return errors

    for idx, row in df.iterrows():
        row_num = idx + 2  # Account for 1-based header line
        cid = str(row["candidate_id"]).strip()
        sid = str(row["source_id"]).strip()
        brick = str(row["brick"]).strip()
        status = str(row["verification_status"]).strip().lower()

        if not cid or cid.lower() == "nan":
            errors.append(f"Row {row_num}: missing candidate_id.")
        if not sid or sid.lower() == "nan":
            errors.append(f"Row {row_num}: missing source_id.")
        if brick not in VALID_BRICKS:
            errors.append(f"Row {row_num}: invalid brick '{brick}' (expected B24-B36).")

        ra = pd.to_numeric(row["ra_deg"], errors="coerce")
        dec = pd.to_numeric(row["dec_deg"], errors="coerce")
        if pd.isna(ra) or not (0.0 <= float(ra) <= 360.0):
            errors.append(f"Row {row_num}: invalid ra_deg '{row['ra_deg']}'.")
        if pd.isna(dec) or not (-90.0 <= float(dec) <= 90.0):
            errors.append(f"Row {row_num}: invalid dec_deg '{row['dec_deg']}'.")

        if status not in VALID_STATUSES:
            errors.append(
                f"Row {row_num}: invalid verification_status '{row['verification_status']}' "
                f"(allowed: {sorted(VALID_STATUSES)})."
            )

    return errors


def main() -> int:
    args = parse_args()
    try:
        if not args.ledger.exists():
            raise FileNotFoundError(f"Ledger file not found: {args.ledger}")
        df = pd.read_csv(args.ledger)
        errors = audit_ledger(df)
        if errors:
            for err in errors:
                print(f"AUDIT ERROR: {err}", file=sys.stderr)
            return 1
        print(f"Ledger audit passed ({len(df)} rows checked in {args.ledger}).")
        return 0
    except Exception as exc:
        print(f"Error auditing ledger: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())


# Salsabilah Ecosystem
# (Powered by Gemini)
