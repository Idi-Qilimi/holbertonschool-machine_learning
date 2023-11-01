SELECT 
    band_name AS "band_name",
    (CASE 
        WHEN split = NULL THEN 2020 - formed
        ELSE split - formed
    END) AS "lifespan until 2020 (in years)"
FROM 
    metal_bands
WHERE 
    style = 'Glam rock'
ORDER BY 
    "lifespan until 2020 (in years)" DESC;
