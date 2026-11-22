# SOHAG STAR — M31 PHAST Investigation

Photometric and astrometric candidate investigation in the Andromeda Galaxy (M31) using the Panchromatic Hubble Andromeda Southern Treasury (**PHAST**, Bricks `B24`–`B36`, `F275W`, `F336W`, `F475W`, and `F814W`) and **NOIRLab Astro Data Lab** query workflows.

## Scientific Scope
- **Target Galaxy:** Andromeda Galaxy (M31) southern star-forming disk (`B24`–`B36`).
- **Historical Benchmark:** `M31-V1` (used strictly as a historical reference for resolved stellar astronomy in M31).
- **Commemorative Label:** `SOHAG STAR` is an informal designation applied only after astrometric, photometric, quality-flag, and cross-verification checks are met.

## Planned Repository Structure
- `README.md` — Project overview and workflow guide
- `sql/01_discover_phast_schema.sql` — Schema inspection query for NOIRLab Astro Data Lab
- `sql/02_candidate_queries.sql` — UV-bright hot star and luminous red star selection templates
- `scripts/filter_candidates.py` — Shortlist filtering and verification ledger exporter
- `docs/sohag_star_research_report.md` — Full research proposal and verification framework

## Key References
- Chen et al. (2025), *ApJ*, 979, 35 (`PHAST. I. Ultraviolet and Optical Photometry of over 90 Million Stars in M31`), DOI: `10.3847/1538-4357/ad7e2b`
- MAST High Level Science Product — PHAST, DOI: `10.17909/aa43-mt38`
- NOIRLab Astro Data Lab: https://datalab.noirlab.edu/

Salsabilah Ecosystem
(Powered by Gemini)
