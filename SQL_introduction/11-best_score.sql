-- Select the best
SELECT score, name
FROM second_table
WHERE score > 9
ORDER BY score DESC;