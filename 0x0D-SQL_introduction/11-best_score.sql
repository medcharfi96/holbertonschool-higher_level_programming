-- affichage trié
SELECT score AS score, name AS name FROM second_table
WHERE score >= 10
ORDER BY score DESC;