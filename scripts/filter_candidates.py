#!/usr/bin/env python3
"""
SOHAG STAR Investigation (M31 / HST PHAST)
File: scripts/filter_candidates.py
Purpose: Filter queried PHAST candidates across M31 Bricks B24-B36 and write
         a structured shortlist CSV for astrometric/photometric verification.

Salsabilah Ecosystem
(Powered by Gemini)
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd

TARGET_BRICKS = [
    "B24", "B25", "B26", "B27", "B28", "B29",
    "B30", "B31", "B32", "B33", "B34", "B35", "B36",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Filter PHAST candidate rows for SOHAG STAR verification."
    )
    parser.add_argument(
        "--in-csv",
        type=Path,
        required=True,
        help="Input CSV of queried PHAST sources.",
    )
    parser.add_argument(
        "--out-csv",
        type=Path,
        required=True,
        help="Output CSV for filtered candidates.",
    )
    parser.add_argument(
        "--max-f275w",
        type=float,
        default=24.0,
        help="Maximum (brightest) F275W magnitude threshold (default: 24.0).",
    )
    parser.add_argument(
        "--max-f336w",
        type=float,
        default=24.0,
        help="Maximum (brightest) F336W magnitude threshold (default: 24.0).",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=50,
        help="Maximum number of ranked candidates to export (default: 50).",
    )
    return parser.parse_args()


def filter_candidates(
    df: pd.DataFrame,
    max_f275w: float,
    max_f336w: float,
    top_n: int,
) -> pd.DataFrame:
    required_cols = {"source_id", "brick", "ra_deg", "dec_deg", "mag_f275w", "mag_f336w"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns in input CSV: {sorted(missing)}")

    out = df.copy()
    out["brick"] = out["brick"].astype(str).str.strip()
    out = out[out["brick"].isin(TARGET_BRICKS)]

    for col in ("ra_deg", "dec_deg", "mag_f275w", "mag_f336w"):
        out[col] = pd.to_numeric(out[col], errors="coerce")

    out = out.dropna(subset=["source_id", "ra_deg", "dec_deg", "mag_f275w", "mag_f336w"])
    out = out[(out["mag_f275w"] <= max_f275w) & (out["mag_f336w"] <= max_f336w)]

    if "mag_f475w" in out.columns:
        out["mag_f475w"] = pd.to_numeric(out["mag_f475w"], errors="coerce")
        out["uv_optical_color_f275_f475"] = out["mag_f275w"] - out["mag_f475w"]

    out = out.sort_values(by=["mag_f275w", "mag_f336w"], ascending=[True, True]).head(top_n)
    return out.reset_index(drop=True)


def main() -> int:
    args = parse_args()
    try:
        if not args.in_csv.exists():
            raise FileNotFoundError(f"Input CSV not found: {args.in_csv}")
        df = pd.read_csv(args.in_csv)
        filtered = filter_candidates(
            df=df,
            max_f275w=args.max_f275w,
            max_f336w=args.max_f336w,
            top_n=args.top_n,
        )
        args.out_csv.parent.mkdir(parents=True, exist_ok=True)
        filtered.to_csv(args.out_csv, index=False)
        print(f"Exported {len(filtered)} filtered candidates to {args.out_csv}")
        return 0
    except Exception as exc:
        print(f"Error filtering candidates: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())


# Salsabilah Ecosystem
# (Powered by Gemini)
