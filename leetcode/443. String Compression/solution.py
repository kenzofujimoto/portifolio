from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n <= 1: 
            return n
    
        aux, leitor = 0, 0

        while leitor < n:
            anterior = chars[leitor]
            k = 0

            # Conta as repetições do caractere atual
            while leitor < n and anterior == chars[leitor]:
                k += 1
                leitor += 1
                
            # Escreve o caractere no array
            chars[aux] = anterior
            aux += 1
            
            # Se repetiu mais de uma vez, escreve os dígitos da contagem
            if k > 1:
                for char in str(k):
                    chars[aux] = char  # 'char' já é string, não precisa de str()
                    aux += 1

        return aux

# ==========================================
# 🧪 TESTES LOCAIS PARA O VS CODE
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    
    # Teste 1: Compressão padrão
    chars1 = ["a","a","b","b","c","c","c"]
    tamanho1 = sol.compress(chars1)
    print(f"Teste 1: {chars1[:tamanho1]} | Tamanho: {tamanho1} (Esperado: 6)")

    # Teste 2: Array sem letras repetidas (Regra do número 1)
    chars2 = ["a","b","c"]
    tamanho2 = sol.compress(chars2)
    print(f"Teste 2: {chars2[:tamanho2]} | Tamanho: {tamanho2} (Esperado: 3)")

    # Teste 3: Compressão com múltiplos dígitos (12 letras 'b')
    chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    tamanho3 = sol.compress(chars3)
    print(f"Teste 3: {chars3[:tamanho3]} | Tamanho: {tamanho3} (Esperado: 4 -> ['a', 'b', '1', '2'])")