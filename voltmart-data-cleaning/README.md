# 🛒 E-commerce Data Cleaning Pipeline (PySpark)

## 📌 Sobre o Projeto
Este projeto foi desenvolvido para a Voltmart, uma empresa de e-commerce de eletrônicos. O objetivo do pipeline é processar e higienizar um *dataset* bruto de pedidos do último ano, transformando-o em uma base confiável e estruturada para que a equipe de Machine Learning possa treinar um modelo de previsão de demanda (*Demand Forecasting*).

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Processamento de Big Data:** Apache Spark (PySpark)
* **Armazenamento:** Formato Parquet (Colunar)

## 🗃️ Transformações Aplicadas (ETL)
O script `cleaning_pipeline.py` realiza as seguintes operações nativas e distribuídas:
1. **Tratamento de Datas:** Conversão de colunas *Timestamp* para *Date* e extração de regras temporais.
2. **Regex (Expressões Regulares):** Extração automatizada e segura da sigla do Estado americano (ex: `OR`, `CA`) a partir de *strings* complexas de endereços de entrega.
3. **Filtros e Regras de Negócio:**
   - Remoção de compras realizadas durante a madrugada (00:00 às 04:59).
   - Remoção completa do histórico de vendas do produto "TV" (descontinuado pela empresa).
4. **Engenharia de Atributos (*Feature Engineering*):** Criação da coluna `time_of_day`, categorizando compras dinamicamente em `morning`, `afternoon` e `evening`.
5. **Padronização:** Aplicação de *lowercase* em categorias e produtos para evitar duplicidades no treinamento do modelo preditivo.

## 🚀 Como Executar

1. Clone o repositório.
2. Certifique-se de ter o PySpark instalado (`pip install pyspark`).
3. Coloque o arquivo bruto `orders_data.parquet` na raiz do projeto.
4. Execute o pipeline:
   ```bash
   python cleaning_pipeline.py