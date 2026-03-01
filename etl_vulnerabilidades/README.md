# 🛡️ Pipeline ETL: Threat Intelligence (NVD API)

## 📌 Visão Geral
No cenário atual de Segurança da Informação (AppSec/Blue Team), o tempo de resposta entre a descoberta de uma vulnerabilidade e a sua mitigação é crítico. 

Este projeto é um pipeline **ETL (Extract, Transform, Load)** projetado para consumir dados da API pública do *National Vulnerability Database (NVD)*. Ele extrai as CVEs (Common Vulnerabilities and Exposures) mais recentes, limpa o JSON complexo para reter apenas as métricas essenciais (ID, Status e Descrição) e carrega os resultados localmente no formato **.parquet**, preparando o terreno para análises avançadas em ferramentas de Big Data.

## 🏗️ Arquitetura e Fluxo de Dados
1. **Extract:** Requisição HTTP (`GET`) na API RESTful do NVD para capturar as vulnerabilidades recém-publicadas.
2. **Transform:** Processamento do JSON utilizando `Pandas`, isolando chaves aninhadas e padronizando os tipos de dados em um DataFrame estruturado.
3. **Load:** Conversão e compressão do DataFrame para o formato colunar Apache Parquet (via `pyarrow`), reduzindo custos de armazenamento e otimizando a leitura por motores analíticos.

## 🚀 Como Executar (Modo DevOps)
Este projeto está containerizado para garantir consistência em qualquer ambiente.

**Pré-requisitos:** Ter o [Docker](https://www.docker.com/) instalado.

1. Clone o repositório e acesse a pasta do projeto:
   ```bash
   cd etl-vulnerabilidades