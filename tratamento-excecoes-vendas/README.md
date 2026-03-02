# 🛒 Sales Analytics: Data Quality & Exception Handling

## 📌 Visão Geral
Em ambientes corporativos orientados a dados, a precisão das métricas de vendas (Analytics) depende diretamente da integridade do código que processa essas informações. Falhas silenciosas no tratamento de dados podem gerar relatórios financeiros incorretos e impactar a tomada de decisão.

Este projeto aplica conceitos de **Programação Defensiva e Data Quality** sobre uma base de dados de vendas de eletroeletrônicos. O objetivo é garantir que anomalias nos dados brutos (como valores negativos, nulos ou tipos incompatíveis de variáveis) sejam capturadas em tempo de execução através de um tratamento robusto de exceções e lógicas de validação.

## 🏗️ Estrutura e Boas Práticas Aplicadas
- **Modularização:** Separação estrita entre dados brutos (`/data`), código-fonte (`/src`) e testes (`/tests`).
- **Tratamento de Exceções:** Uso de `try/except` para levantar `TypeError` e `ValueError` quando a integridade do pipeline é ameaçada.
- **Testes Automatizados:** Cobertura de cenários de erro e de borda utilizando o framework `pytest`.

## 🚀 Como Executar
1. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt