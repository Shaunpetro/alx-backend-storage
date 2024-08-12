--  script that ranks the country origins of bands, ordered
-- by the num of non-unique fans
SELECT origin, SUM(fans) as nb_fans from metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
