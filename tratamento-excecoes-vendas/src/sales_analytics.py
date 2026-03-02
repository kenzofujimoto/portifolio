import pandas as pd
from pathlib import Path

def calcular_soma_quantidades(serie_quantidades):
    """
    Calcula a soma total da coluna de quantidades pedidas.

    Args:
        serie_quantidades (pd.Series): A série do Pandas contendo as quantidades.

    Returns:
        int: O valor total das quantidades pedidas.
    
    Raises:
        ValueError: Se encontrar algum valor negativo na série.
    """
    total_quantidades = 0
    
    for quantidade in serie_quantidades:
        if quantidade < 0:
            raise ValueError(f"Erro de Integridade: Quantidade negativa detectada ({quantidade}).")
        total_quantidades += quantidade
        
    return total_quantidades


def calcular_media_precos(serie_precos, casas_decimais=2):
    """
    Calcula a média da coluna de preços unitários e arredonda o resultado.

    Args:
        serie_precos (pd.Series): A série do Pandas contendo os preços.
        casas_decimais (int): O número de casas decimais para o arredondamento.

    Returns:
        float: A média calculada dos preços.
        
    Raises:
        TypeError: Se a coluna contiver valores não numéricos.
    """
    if not pd.api.types.is_numeric_dtype(serie_precos):
        raise TypeError("Erro de Qualidade: A coluna de preços contém valores não numéricos (ex: textos).")

    soma_total_precos = serie_precos.sum()
    quantidade_itens = len(serie_precos)

    if quantidade_itens == 0:
        return 0.0

    media_precos = round(soma_total_precos / quantidade_itens, casas_decimais)
    return media_precos


if __name__ == "__main__":
    # Navegação de pastas profissional
    DIRETORIO_ATUAL = Path(__file__).resolve().parent
    CAMINHO_CSV = DIRETORIO_ATUAL.parent / "data" / "sales_data_sample.csv"
    
    try:
        df_vendas = pd.read_csv(CAMINHO_CSV)
        
        # Chamando as funções com os nomes padronizados
        total_qtd = calcular_soma_quantidades(df_vendas['quantity_ordered'])
        print(f"✅ Total de Quantidades Pedidas: {total_qtd}")
        
        media_preco = calcular_media_precos(df_vendas['price_each'])
        print(f"✅ Média de Preço Unitário: {media_preco}")
        
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo não foi encontrado no caminho {CAMINHO_CSV}")
    except Exception as e:
        print(f"❌ O pipeline parou devido a um erro de dados: {e}")