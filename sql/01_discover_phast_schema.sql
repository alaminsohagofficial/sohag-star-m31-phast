 -- SOHAG STAR Investigation (M31 / HST PHAST)
-- File: sql/01_discover_phast_schema.sql
-- Release: v0.1.0-proposal | Zenodo DOI: 10.5281/zenodo.24449978
-- Purpose: Discover PHAST catalog tables and available columns in
--          NOIRLab Astro Data Lab TAP before running candidate filters.
--
-- Salsabilah Ecosystem
-- (Powered by Gemini)
-----------------------------------------------------------------------

-- Step 1: List catalog tables matching PHAST in TAP schema
SELECT
    table_name
FROM tap_schema.tables
WHERE LOWER(table_name) LIKE '%phast%'
ORDER BY table_name;

-- Step 2A: Inspect targeted columns (coordinates, brick, photometry, flags)
-- Replace <PHAST_TABLE_NAME> with the exact table name returned in Step 1.
SELECT
    column_name,
    datatype,
    description
FROM tap_schema.columns
WHERE table_name = '<PHAST_TABLE_NAME>'
  AND (
       LOWER(column_name) LIKE '%ra%'
    OR LOWER(column_name) LIKE '%dec%'
    OR LOWER(column_name) LIKE '%brick%'
    OR LOWER(column_name) LIKE '%id%'
    OR LOWER(column_name) LIKE '%275%'
    OR LOWER(column_name) LIKE '%336%'
    OR LOWER(column_name) LIKE '%475%'
    OR LOWER(column_name) LIKE '%814%'
    OR LOWER(column_name) LIKE '%mag%'
    OR LOWER(column_name) LIKE '%flag%'
    OR LOWER(column_name) LIKE '%snr%'
    OR LOWER(column_name) LIKE '%chi%'
    OR LOWER(column_name) LIKE '%sharp%'
    OR LOWER(column_name) LIKE '%crowd%'
  )
ORDER BY column_name;

-- Step 2B: List all columns, data types, and descriptions for <PHAST_TABLE_NAME>
-- Replace <PHAST_TABLE_NAME> with the exact table name returned in Step 1.
SELECT
    column_name,
    datatype,
    description
FROM tap_schema.columns
WHERE table_name = '<PHAST_TABLE_NAME>'
ORDER BY column_name;

-- Salsabilah Ecosystem
-- (Powered by Gemini)
