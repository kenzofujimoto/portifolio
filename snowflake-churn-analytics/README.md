# ❄️ SaaS Churn & Revenue Analytics | Snowflake SQL

## 📌 Visão Geral
Neste projeto, atuei como Engenheiro de Dados focado em Analytics, processando uma base de clientes de Telecomunicações/SaaS (Telco Customer Churn) para extrair insights financeiros e operacionais sobre retenção e faturamento.

Todo o processamento e modelagem dos dados foi realizado em **Snowflake**, utilizando SQL Avançado (CTEs e Window Functions) para transformar dados brutos em métricas de negócio.

## 🛠️ Arquitetura e Tecnologias
- **Data Warehouse:** Snowflake (Cloud)
- **Linguagem:** SQL Puro
- **Técnicas Aplicadas:** Window Functions (`SUM OVER`, `NTILE`, `DENSE_RANK`), Common Table Expressions (CTEs), Agregações Complexas.
- **Dataset:** Telco Customer Churn (7.043 registros)

## 📊 Perguntas de Negócio e Insights

### 1. Curva de Receita Acumulada (Running Total)
**Objetivo:** Mapear o crescimento do faturamento mês a mês (`tenure`), segmentado por tipo de contrato.
- **Insight:** Contratos de longo prazo demoram mais para tracionar o faturamento bruto, mas oferecem maior estabilidade na curva de receita em comparação aos contratos mensais.
- [🔗 Ver código SQL](sql/01_revenue_running_total.sql)

### 2. Mapeamento de Risco por Faixa de Preço (Quartis)
**Objetivo:** Descobrir se clientes que pagam as mensalidades mais caras apresentam maior taxa de cancelamento.
- **Insight:** A análise revelou que clientes do Quartil 4 (mensalidades mais altas) apresentam um volume de cancelamento quase 3x maior que clientes de entrada (Quartil 1). O serviço Premium exige revisão de percepção de valor.
- [🔗 Ver código SQL](sql/02_churn_risk_quartiles.sql)

### 3. Ranking de Fidelidade (Top Customers)
**Objetivo:** Identificar os 3 clientes mais valiosos dentro de cada categoria de serviço de internet.
- **Insight:** Mapeamento concluído com sucesso para criação de campanhas VIP hiper-personalizadas de retenção.
- [🔗 Ver código SQL](sql/03_top_customers_ranking.sql)