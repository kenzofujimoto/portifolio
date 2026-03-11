/*
===============================================================================
Description: Divides the customer base into 4 quartiles based on MonthlyCharges 
             to analyze the Churn volume in the cheapest vs. most expensive tiers.
Author:      Kenzo Fujimoto
===============================================================================
*/

WITH quartis AS (
    SELECT
        monthlycharges,
        churn,
        NTILE(4) OVER(ORDER BY monthlycharges) AS quartil
    FROM SNOWFLAKE_LEARNING_DB.PUBLIC.TELCO
)

SELECT 
    churn,
    quartil, 
    COUNT(churn) AS qtd_clientes
FROM quartis
WHERE quartil IN (1, 4)
GROUP BY quartil, churn
ORDER BY quartil, churn;