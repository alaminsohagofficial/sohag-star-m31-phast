-- SOHAG STAR Investigation (M31 / HST PHAST)
-- File: sql/02_candidate_queries.sql
-- Purpose: Query candidate resolved sources in M31 PHAST Bricks B24-B36
--          after confirming exact schema columns via 01_discover_phast_schema.sql.
--
-- Salsabilah Ecosystem
-- (Powered by Gemini)
-----------------------------------------------------------------------

SELECT TOP 500
    <obj_id_col>      AS source_id,
    <brick_col>       AS brick,
    <ra_col>          AS ra_deg,
    <dec_col>         AS dec_deg,
    <mag_f275w_col>   AS mag_f275w,
    <mag_f336w_col>   AS mag_f336w,
    <mag_f475w_col>   AS mag_f475w,
    <mag_f814w_col>   AS mag_f814w
FROM <PHAST_TABLE_NAME>
WHERE <brick_col> IN (
    'B24', 'B25', 'B26', 'B27', 'B28', 'B29',
    'B30', 'B31', 'B32', 'B33', 'B34', 'B35', 'B36'
);

-- Salsabilah Ecosystem
-- (Powered by Gemini)
