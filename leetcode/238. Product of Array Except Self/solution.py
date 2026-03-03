"""
LeetCode #238 - Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/

Regras do Jogo:
1. Você NÃO PODE usar a operação de divisão (/).
2. O algoritmo precisa rodar em tempo O(N).

Abordagem: Prefix e Suffix Arrays (Ida e Volta)
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Inicializando os arrays com 1s (já que 1 é o elemento neutro da multiplicação)
        resposta = [1] * n
        acumulador = 1
        
        for i in range(n):
            resposta[i] = acumulador
            acumulador *= nums[i]
            

        acumulador = 1
        for i in range(n - 1, -1, -1):
            resposta[i] *= acumulador
            acumulador *= nums[i]
            
        return resposta


# ==========================================
# ÁREA DE TESTES LOCAIS (Test Cases)
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    
    # Casos de Teste (Cobrindo cenários padrão e edge cases brutais)
    testes = [
        # Caso Padrão do LeetCode
        {"nums": [1, 2, 3, 4], "esperado": [24, 12, 8, 6]},
        
        # Edge Case: Presença de um Zero (se dividir por zero, o código explode)
        {"nums": [-1, 1, 0, -3, 3], "esperado": [0, 0, 9, 0, 0]},
        
        # Edge Case: Apenas dois elementos (tamanho mínimo permitido)
        {"nums": [2, 3], "esperado": [3, 2]},
        
        # Edge Case: Múltiplos Zeros
        {"nums": [0, 4, 0], "esperado": [0, 0, 0]}
    ]

    print("🚀 Iniciando Testes de Array Except Self...\n")
    
    for idx, teste in enumerate(testes):
        resultado = sol.productExceptSelf(teste["nums"])
        
        # Trava para não quebrar o teste enquanto você não implementar o return
        if resultado is None:
            print(f"Teste {idx + 1}: nums={teste['nums']}")
            print("   -> ❌ FALHOU (Função retornou None. Implemente a lógica!)\n")
            continue
            
        status = "✅ PASSOU" if resultado == teste["esperado"] else "❌ FALHOU"
        
        print(f"Teste {idx + 1}: nums={teste['nums']}")
        print(f"   -> Esperado: {teste['esperado']} | Retornado: {resultado} | {status}\n")