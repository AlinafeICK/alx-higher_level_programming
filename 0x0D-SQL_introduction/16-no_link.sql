-- 16-no_link.sql
-- List all records of the table with non-null names, display score & name, descending order by score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
