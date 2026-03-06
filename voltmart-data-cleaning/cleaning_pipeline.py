"""
Projeto: E-commerce Data Cleaning Pipeline (Voltmart)
Descrição: Script PySpark para ingestão, tratamento e limpeza de dados de vendas,
preparando a base para modelos de Machine Learning (Demand Forecasting).
"""

import os
from pathlib import Path
from pyspark.sql import SparkSession, functions as F

# ==========================================
# WORKAROUND PARA AMBIENTE WINDOWS
# ==========================================
# O Apache Spark (desenhado para Linux/HDFS) exige os binários 'winutils.exe' e 
# 'hadoop.dll' para interagir corretamente com o sistema de arquivos NTFS no Windows.
# Esta validação garante que o pipeline seja executável em qualquer SO (Cross-Platform).

if os.name == 'nt':  # Verifica se o Sistema Operacional atual é o Windows
    print("⚠️ Ambiente Windows detectado. Configurando variáveis do Hadoop...")
    HADOOP_PATH = "C:\\hadoop"
    os.environ["HADOOP_HOME"] = HADOOP_PATH
    os.environ["PATH"] += os.pathsep + os.path.join(HADOOP_PATH, "bin")
# ==========================================

# ==========================================
# CONFIGURAÇÃO DE CAMINHOS (Cross-Platform)
# ==========================================
# Descobre a pasta atual onde o script está rodando
BASE_DIR = Path(__file__).resolve().parent
INPUT_PATH = str(BASE_DIR / "orders_data.parquet")
OUTPUT_PATH = str(BASE_DIR / "orders_data_clean.parquet")

def main():
    print("🚀 Iniciando a Sessão do Spark...")
    spark = (
        SparkSession
        .builder
        .appName('cleaning_orders_dataset_with_pyspark')
        .getOrCreate()
    )

    # ==========================================
    # EXTRACT (Ingestão)
    # ==========================================
    print(f"Lendo os dados sujos de: {INPUT_PATH}")
    orders_data = spark.read.parquet(INPUT_PATH)
    
    # Exibe as primeiras linhas para validação visual no terminal
    print("\nVisualização inicial (Sujo):")
    orders_data.show(5, truncate=False)

    # ==========================================
    # TRANSFORM (Limpeza e Regras de Negócio)
    # ==========================================
    print("Iniciando processamento e limpeza dos dados...")
    
    # 1. Extração de Hora e Data
    orders_data = orders_data.withColumn("hour", F.hour("order_date"))
    orders_data = orders_data.withColumn("order_date", F.to_date("order_date"))
    
    # 2. Extração do Estado via Regex
    orders_data = orders_data.withColumn(
        "purchase_state", 
        F.regexp_extract(F.col("purchase_address"), r"([A-Z]{2})\s+\d{5}", 1)
    )
    
    # 3. Filtro de Madrugada (Mantendo apenas vendas das 5h em diante)
    orders_data = orders_data.filter(F.col("hour") >= 5)
    
    # 4. Classificação de Turnos (Morning/Afternoon/Evening)
    orders_data = orders_data.withColumn(
        "time_of_day", 
        F.when(F.col("hour") < 12, "morning")
        .when(F.col("hour") < 18, "afternoon")
        .otherwise("evening")
    )
    
    # 5. Tratamento de Strings e Filtro de Produto
    orders_data = orders_data.where(~F.col("product").contains("TV"))
    orders_data = orders_data.withColumn("product", F.lower("product"))
    orders_data = orders_data.withColumn("category", F.lower("category"))
    
    # 6. Limpeza de Colunas Auxiliares
    orders_data = orders_data.drop("hour")

    print("\nVisualização final (Limpo):")
    orders_data.show(5, truncate=False)

    # ==========================================
    # LOAD (Persistência)
    # ==========================================
    print(f"Salvando a base limpa em Parquet...")
    orders_data.write.mode("overwrite").parquet(OUTPUT_PATH)
    print(f"Arquivo salvo em: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()