import pandas as pd
from pathlib import Path

def get_quantity_ordered_sum(sales_quantity_ordered):
    """Calculates the total sum on the 'quantity_ordered' column.

    Args:
        sales_quantity_ordered (pd.core.series.Series): The pandas Series for the 'quantity_ordered' column.

    Returns:
        total_quantity_ordered (int): The total sum of the 'quantity_ordered' column.
    """

    total_quantity_ordered = 0
    for quantity in sales_quantity_ordered:
        if quantity < 0:
            raise ValueError(f"Erro de Integridade: Quantidade negativa detectada ({quantity}).")
        total_quantity_ordered += quantity
    return total_quantity_ordered

def get_price_each_average(sales_price_each, num_places=2):
    """Calculates the average on the 'price_each' column
        using pandas built in methods and rounds to the desired number of places.

    Args:
        sales_price_each (pd.core.series.Series): The pandas Series for the 'price_each' column.
        num_of_places (int): The number of decimal places to round.

    Returns:
        average_price_each (float): The average of the 'price_each' column.
    """

    if not pd.api.types.is_numeric_dtype(sales_price_each):
        raise TypeError("Data Quality Error: A coluna 'price_each' contém valores não numéricos (ex: textos).")

    total_of_price_each = sales_price_each.sum()
    len_of_price_each = len(sales_price_each)

    if len_of_price_each == 0:
        return 0.0

    average_price_each = round(
        total_of_price_each / len_of_price_each, num_places
    )
    return average_price_each

if __name__ == "__main__":
    
    DIRETORIO_ATUAL = Path(__file__).resolve().parent
    CAMINHO_CSV = DIRETORIO_ATUAL.parent / "data" / "sales_data_sample.csv"
    
    try:
        sales_df = pd.read_csv(CAMINHO_CSV)
        
        total_qtd = get_quantity_ordered_sum(sales_df['quantity_ordered'])
        print(f"✅ Total de Quantidades Pedidas: {total_qtd}")
        
        media_preco = get_price_each_average(sales_df['price_each'])
        print(f"✅ Média de Preço (Price Each): {media_preco}")
        
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo não foi encontrado no caminho {CAMINHO_CSV}")
    except Exception as e:
        print(f"❌ O pipeline parou devido a um erro de dados: {e}")