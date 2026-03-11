/*
===============================================================================
Description: Identifies the Top 3 most valuable customers (TotalCharges) 
             within each Internet Service category using DENSE_RANK.
Author:      Kenzo Fujimoto
===============================================================================
*/

WITH aux AS (
    SELECT 
        customerid,
        internetservice,
        totalcharges,
        DENSE_RANK() OVER(PARTITION BY internetservice ORDER BY totalcharges DESC) AS rank
    FROM SNOWFLAKE_LEARNING_DB.PUBLIC.TELCO
    WHERE totalcharges IS NOT NULL
)

SELECT * FROM aux
WHERE rank <= 3
ORDER BY internetservice, rank;