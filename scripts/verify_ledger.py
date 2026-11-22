"""
SOHAG STAR Investigation (M31 / HST PHAST)
File: scripts/verify_ledger.py
Purpose: Audit a candidate verification ledger CSV to ensure required
         catalog, astrometric, photometric, and check fields are populated
         before marking a candidate verified.

Salsabilah Ecosystem
(Powered by Gemini)
"""

from pathlib import Path
import pandas as pd

REQUIRED_FIELDS = [
    "regime",
    "source_id",
    "brick",
    "ra_deg",
    "dec_deg",
    "mag_f475w",
    "mag_f814w",
    "snr_check",
    "quality_flags_check",
    "cutout_check",
    "literature_check",
]


def audit_ledger(ledger_csv: str) -> pd.DataFrame:
    """Return a summary DataFrame flagging incomplete rows in a ledger CSV."""
    df = pd.read_csv(ledger_csv)
    missing_cols = set(REQUIRED_FIELDS) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Ledger is missing required columns: {sorted(missing_cols)}")

    audit_rows = []
    for idx, row in df.iterrows():
        incomplete = []
        for col in REQUIRED_FIELDS:
            val = row[col]
            if pd.isna(val) or str(val).strip().lower() in {"", "pending", "pending_live_query", "none", "nan"}:
                incomplete.append(col)

        audit_rows.append(
            {
                "row_index": idx,
                "source_id": row.get("source_id", ""),
                "brick": row.get("brick", ""),
                "ready_for_review": len(incomplete) == 0,
                "incomplete_fields": ", ".join(incomplete) if incomplete else "none",
            }
        )

    return pd.DataFrame(audit_rows)


if __name__ == "__main__":
    default_path = Path("data/verification_ledger_template.csv")
    if default_path.exists():
        summary = audit_ledger(str(default_path))
        print(summary.to_string(index=False))
    else:
        print("Pass a ledger CSV path to audit_ledger().")
      
