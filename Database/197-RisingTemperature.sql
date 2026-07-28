SELECT
    d1.id
FROM Weather d1
JOIN Weather d2
    ON d1.recordDate = d2.recordDate + INTERVAL '1 day'
WHERE
    d1.temperature > d2.temperature;