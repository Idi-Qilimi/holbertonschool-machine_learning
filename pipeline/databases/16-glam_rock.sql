-- Ranks Glam rock bands by longevity
SELECT
    band_name,
    COALESCE(split, CURRENT_DATE()) - formed AS lifespan_until_2020
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan_until_2020 DESC;
