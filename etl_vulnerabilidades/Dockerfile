# Usa uma imagem oficial do Python (versão slim para ser mais leve)
FROM python:3.11-slim

# Cria uma pasta de trabalho dentro do container
WORKDIR /app

# Copia os arquivos da máquina para o container
COPY requirements.txt .
COPY etl_cve.py .

# Instala as bibliotecas
RUN pip install --no-cache-dir -r requirements.txt

# O comando que o container vai rodar quando for ligado
CMD ["python", "etl_cve.py"]