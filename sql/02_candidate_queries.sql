-- =============================================================================
-- SOHAG STAR Investigation (M31 / HST PHAST)
-- File: sql/02_candidate_queries.sql
-- Purpose: Schema-templated queries for UV-bright hot star and luminous red
--          star candidate shortlists across PHAST Bricks B24-B36.
-- Note: Replace <PHAST_TABLE> and <..._COL> with exact column names
--       verified from tap_schema.columns before running.
--
-- Salsabilah Ecosystem
-- (Powered by Gemini)
-- =============================================================================

-- -----------------------------------------------------------------------------
-- A. UV-Bright Hot Star Candidates (Bricks B24-B36)
-- -----------------------------------------------------------------------------
SELECT TOP 50
    <ID_COL>                        AS source_id,
    <RA_COL>                        AS ra_deg,
    <DEC_COL>                       AS dec_deg,
    <BRICK_COL>                     AS brick,
    <F275W_MAG_COL>                 AS mag_f275w,
    <F336W_MAG_COL>                 AS mag_f336w,
    <F475W_MAG_COL>                 AS mag_f475w,
    <F814W_MAG_COL>                 AS mag_f814w,
    (<F475W_MAG_COL> - <F814W_MAG_COL>) AS color_f475w_f814w,
    (<F275W_MAG_COL> - <F475W_MAG_COL>) AS color_f275w_f475w
FROM <PHAST_TABLE>
WHERE <BRICK_COL> BETWEEN 'B24' AND 'B36'
  AND <F275W_MAG_COL> IS NOT NULL
  AND <F336W_MAG_COL> IS NOT NULL
  AND <F475W_MAG_COL> IS NOT NULL
  AND <F814W_MAG_COL> IS NOT NULL
  AND <F275W_SNR_COL> > 10
  AND <F336W_SNR_COL> > 10
  AND <F475W_SNR_COL> > 15
  AND <CROWDING_COL> < <MAX_CROWDING>
  AND ABS(<SHARPNESS_COL>) < <MAX_SHARPNESS>
  AND (<F475W_MAG_COL> - <F814W_MAG_COL>) < 0.3
ORDER BY <F275W_MAG_COL> ASC;

-- -----------------------------------------------------------------------------
-- B. Luminous Red Star Candidates (Bricks B24-B36)
-- -----------------------------------------------------------------------------
SELECT TOP 50
    <ID_COL>                        AS source_id,
    <RA_COL>                        AS ra_deg,
    <DEC_COL>                       AS dec_deg,
    <BRICK_COL>                     AS brick,
    <F275W_MAG_COL>                 AS mag_f275w,
    <F336W_MAG_COL>                 AS mag_f336w,
    <F475W_MAG_COL>                 AS mag_f475w,
    <F814W_MAG_COL>                 AS mag_f814w,
    (<F475W_MAG_COL> - <F814W_MAG_COL>) AS color_f475w_f814w
FROM <PHAST_TABLE>
WHERE <BRICK_COL> BETWEEN 'B24' AND 'B36'
  AND <F475W_MAG_COL> IS NOT NULL
  AND <F814W_MAG_COL> IS NOT NULL
  AND <F475W_SNR_COL> > 15
  AND <F814W_SNR_COL> > 15
  AND <CROWDING_COL> < <MAX_CROWDING>
  AND ABS(<SHARPNESS_COL>) < <MAX_SHARPNESS>
  AND (<F475W_MAG_COL> - <F814W_MAG_COL>) > 1.5
ORDER BY <F814W_MAG_COL> ASC;
