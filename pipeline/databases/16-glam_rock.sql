-- Calculate the lifespan for each band and select the required columns
SELECT
    band_name,
    TIMESTAMPDIFF(YEAR, formed, IFNULL(split, CURDATE())) AS lifespan_until_2020
FROM
    bands
WHERE
    band_name IN (
        SELECT
            band_name
        FROM
            bands
        WHERE
            style = 'Glam rock'
    )
ORDER BY
    lifespan_until_2020 DESC;
