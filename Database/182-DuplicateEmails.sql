SELECT
    email AS Email
FROM
    Person
GROUP BY
    email
HAVING
    Count(email) > 1;