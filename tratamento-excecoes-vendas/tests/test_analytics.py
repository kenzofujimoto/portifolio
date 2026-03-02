import pytest
import pandas as pd
from src.sales_analytics import calcular_soma_quantidades, calcular_media_precos


def test_soma_quantidades_sucesso():
    """Testa o caminho feliz: dados normais."""
    dados_mock = pd.Series([10, 20, 30])
    resultado = calcular_soma_quantidades(dados_mock)
    assert resultado == 60

def test_soma_quantidades_valor_negativo():
    """Testa se a função levanta ValueError ao encontrar número negativo."""
    dados_mock = pd.Series([10, -5, 20])
    
    # O pytest.raises verifica se a função "grita" o erro correto
    with pytest.raises(ValueError, match="Quantidade negativa detectada"):
        calcular_soma_quantidades(dados_mock)


# ==========================================
# Testes para get_price_each_average()
# ==========================================

def test_media_precos_sucesso():
    """Testa o cálculo da média com dados perfeitos e arredondamento."""
    dados_mock = pd.Series([10.555, 20.111, 30.000]) # Média exata é 20.222
    resultado = calcular_media_precos(dados_mock, num_places=2)
    assert resultado == 20.22  # O arredondamento deve funcionar

def test_media_precos_texto_no_meio():
    """Testa se a função levanta TypeError ao achar texto no meio do preço."""
    # Série do Pandas misturando números e uma string
    dados_mock = pd.Series([10.50, "vinte reais", 30.00])
    
    with pytest.raises(TypeError, match="valores não numéricos"):
        calcular_media_precos(dados_mock)