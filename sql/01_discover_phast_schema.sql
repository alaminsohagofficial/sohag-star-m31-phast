-- SOHAG STAR Investigation (M31 / HST PHAST)
-- File: sql/01_discover_phast_schema.sql
-- Purpose: Discover PHAST catalog tables and available columns in
--          NOIRLab Astro Data Lab TAP before running candidate filters.
--
-- Salsabilah Ecosystem
-- (Powered by Gemini)
-----------------------------------------------------------------------

-- 1. List catalog tables matching PHAST in TAP schema
SELECT
    table_name
FROM tap_schema.tables
WHERE LOWER(table_name) LIKE '%phast%'
ORDER BY table_name;

-- 2. Inspect columns, data types, and descriptions for a confirmed table
--    Replace <PHAST_TABLE_NAME> with the exact table returned above.
SELECT
    column_name,
    datatype,
    description
FROM tap_schema.columns
WHERE table_name = '<PHAST_TABLE_NAME>'
ORDER BY column_name;

-- Salsabilah Ecosystem
-- (Powered by Gemini)
