-- 11-best_score.sql
-- Select records with a score >= 10 from the table second_table ordered by score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
