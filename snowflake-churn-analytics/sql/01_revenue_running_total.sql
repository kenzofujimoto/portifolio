/*
===============================================================================
Description: Calculates the running total of revenue (MonthlyCharges) 
             partitioned by Contract type and ordered by Tenure (months).
Author:      Kenzo Fujimoto
===============================================================================
*/

WITH receita_mensal AS (
    SELECT 
        contract,
        tenure,
        SUM(monthlycharges) AS receita
    FROM SNOWFLAKE_LEARNING_DB.PUBLIC.TELCO
    GROUP BY contract, tenure
)

SELECT
    contract,
    tenure,
    receita,
    SUM(receita) OVER(PARTITION BY contract ORDER BY tenure) AS receita_acumulada
FROM receita_mensal
ORDER BY contract, tenure;