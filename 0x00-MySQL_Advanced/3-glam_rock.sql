-- script that lists all bands with GLAM rock as their main style,
-- ranked by their longevity

SELECT
    band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';
