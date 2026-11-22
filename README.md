# SOHAG STAR — M31 PHAST Investigation

Photometric and astrometric candidate investigation in the Andromeda Galaxy (M31) using the Panchromatic Hubble Andromeda Southern Treasury (PHAST, Bricks B24–B36, F275W, F336W, F475W, and F814W) and NOIRLab Astro Data Lab query workflows.

## Scientific Scope

- **Target Galaxy:** Andromeda Galaxy (M31) southern star-forming disk (Bricks B24–B36).
- **Historical Benchmark:** M31-V1 (used strictly as a historical reference for resolved stellar astronomy in M31).
- **Commemorative Label:** `SOHAG STAR` is an informal designation applied only after astrometric, photometric, quality-flag, and cross-verification checks are met.

## Archive & DOI

- **Initial Release (`v0.1.0-proposal`):** Archived on Zenodo — DOI: `10.5281/zenodo.24449978` (`https://doi.org/10.5281/zenodo.24449978`).
- **Publishing Sequence:** GitHub + Zenodo DOI -> Research Notes of the AAS (RNAAS) -> arXiv (`astro-ph`) if expanded.

## Repository Structure

- `README.md` — Project overview and workflow guide
- `CITATION.cff` — Citation metadata including Zenodo DOI `10.5281/zenodo.24449978`
- `sql/01_discover_phast_schema.sql` — Schema inspection query for NOIRLab Astro Data Lab
- `sql/02_candidate_queries.sql` — Candidate selection SQL template for M31 PHAST Bricks B24–B36
- `scripts/filter_candidates.py` — Shortlist filtering and verification ledger exporter
- `scripts/run_datalab_query.py` — NOIRLab Astro Data Lab query runner
- `scripts/verify_ledger.py` — Verification ledger audit script
- `data/verification_ledger_template.csv` — Candidate verification ledger template
- `docs/sohag_star_research_report.md` — Full research proposal and verification framework
- `docs/publication_roadmap.md` — Publication sequence and submission guide
- `docs/zenodo_release_checklist.md` — Zenodo release checklist

## Key References

- Chen et al. (2025), *ApJ*, 979, 35 (*PHAST. I. Ultraviolet and Optical Photometry of over 90 Million Stars in M31*), DOI: `10.3847/1538-4357/ad7e2b`
- MAST High Level Science Product — PHAST, DOI: `10.17909/t9-nr36`
- NOIRLab Astro Data Lab: `https://datalab.noirlab.edu/`

Salsabilah Ecosystem
(Powered by Gemini)
