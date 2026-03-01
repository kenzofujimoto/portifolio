import requests
import pandas as pd
from datetime import datetime, timedelta, timezone

def run_etl():
    print("Começando extração...")
    hoje = datetime.now(timezone.utc)
    semana_passada = hoje - timedelta(days=7)

    # Formato exato que a API do NVD exige: YYYY-MM-DDTHH:MM:SS.000%2B00:00
    fmt = "%Y-%m-%dT%H:%M:%S.000%%2B00:00"
    data_inicio = semana_passada.strftime(fmt)
    data_fim = hoje.strftime(fmt)

    # API do NVD
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?pubStartDate={data_inicio}&pubEndDate={data_fim}&resultsPerPage=50"

    r = requests.get(url)
    if r.status_code != 200:
        print(f"Erro na API: {r.status_code}")
        return
    
    dados_json = r.json()
    vulnerabilidades = dados_json.get("vulnerabilities", [])

    print("Iniciando transformação...")

    lista_limpa = []
    for item in vulnerabilidades:
        cve_data = item.get("cve", {})

        cve_id = cve_data.get("id", "Desconhecido")
        status = cve_data.get("vulnStatus", "Desconhecido")
        descricoes = cve_data.get("descriptions", [])
        descricao_texto = descricoes[0].get("value", "") if descricoes else "Sem descrição"

        score = 0.0
        metricas = cve_data.get("metrics", {})
        cvss_v31 = metricas.get("cvssMetricV31", [])
        if cvss_v31:
            cvss_data = cvss_v31[0].get("cvssData", {})
            score = cvss_data.get("baseScore", 0.0)
    
        lista_limpa.append({
            "cve_id": cve_id,
            "score": score,
            "status": status,
            "descricao": descricao_texto
            })
    
    df = pd.DataFrame(lista_limpa)
    print("Transformação concluída!/n")
    print(df.head())

    print("Iniciando load...")
    # Salvando em parquet (orientado a colunas para analises em data lake)
    output = "vulnerabilidades_cve.parquet"
    df.to_parquet(output, index=False)
    print(f"Pipeline finalizado. Dados salvos em {output}")

if __name__ == "__main__":
    run_etl()