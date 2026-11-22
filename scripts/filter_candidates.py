"""
SOHAG STAR Investigation (M31 / HST PHAST)
File: scripts/filter_candidates.py
Purpose: Filter candidate shortlists exported from NOIRLab Astro Data Lab /
         MAST PHAST and generate an initial verification ledger CSV.

Salsabilah Ecosystem
(Powered by Gemini)
"""

from pathlib import Path
import pandas as pd


def filter_shortlist(
    input_csv: str,
    output_csv: str,
    regime: str = "uv_bright",
    min_snr: float = 10.0,
) -> pd.DataFrame:
    """Filter a PHAST candidate CSV and attach initial verification columns."""
    df = pd.read_csv(input_csv)

    required_cols = {"source_id", "ra_deg", "dec_deg", "brick", "mag_f475w", "mag_f814w"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    df["color_f475w_f814w"] = df["mag_f475w"] - df["mag_f814w"]

    filtered = df.dropna(subset=["source_id", "ra_deg", "dec_deg", "mag_f475w", "mag_f814w"]).copy()

    if "snr_ref" in filtered.columns:
        filtered = filtered[filtered["snr_ref"] >= min_snr]

    if regime == "uv_bright":
        filtered = filtered[filtered["color_f475w_f814w"] < 0.3]
        if "mag_f275w" in filtered.columns:
            filtered = filtered.dropna(subset=["mag_f275w"]).sort_values("mag_f275w", ascending=True)
    elif regime == "luminous_red":
        filtered = filtered[filtered["color_f475w_f814w"] > 1.5]
        filtered = filtered.sort_values("mag_f814w", ascending=True)
    else:
        raise ValueError("regime must be 'uv_bright' or 'luminous_red'")

    filtered["verification_status"] = "pending_cutout_and_catalog_check"
    filtered["commemorative_label"] = "SOHAG STAR (informal; post-verification only)"

    out_path = Path(output_csv)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    filtered.to_csv(out_path, index=False)
    return filtered


if __name__ == "__main__":
    print("SOHAG STAR candidate filter module ready. Pass your query export CSV to filter_shortlist().")
  
