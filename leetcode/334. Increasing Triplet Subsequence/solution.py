"""
LeetCode #334 - Increasing Triplet Subsequence
Link: https://leetcode.com/problems/increasing-triplet-subsequence/

Missão: Retornar True se existem 3 índices (i, j, k) tais que i < j < k 
e nums[i] < nums[j] < nums[k]. Senão, retornar False.

Complexidade exigida:
- Tempo: O(N)
- Espaço: O(1)
"""

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        if len(nums) < 3: return False

        menor = float('inf')
        medio = float('inf')

        for num in nums:
            if num <= menor:
                menor = num
            elif num <= medio:
                medio = num
            else:
                return True
        
        return False

# ==========================================
# ÁREA DE TESTES LOCAIS (Test Cases)
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    
    # Casos de Teste
    testes = [
        # Caso 1: Sequência perfeita logo de cara
        {"nums": [1, 2, 3, 4, 5], "esperado": True},
        
        # Caso 2: Ordem decrescente (impossível achar um trio crescente)
        {"nums": [5, 4, 3, 2, 1], "esperado": False},
        
        # Caso 3: Trio escondido e espalhado (1 < 4 < 6)
        {"nums": [2, 1, 5, 0, 4, 6], "esperado": True},
        
        # Caso Pegadinha: Atualiza o menor, mas o trio ainda é válido conceitualmente
        {"nums": [20, 100, 10, 12, 5, 13], "esperado": True},
        
        # Edge Case: Array pequeno demais
        {"nums": [1, 2], "esperado": False}
    ]

    print("🚀 Iniciando Testes de Triplet Subsequence...\n")
    
    for idx, teste in enumerate(testes):
        resultado = sol.increasingTriplet(teste["nums"])
        
        # Trava para não quebrar o teste enquanto você não implementar o return
        if resultado is None:
            print(f"Teste {idx + 1}: nums={teste['nums']}")
            print("   -> ❌ FALHOU (Função retornou None. Implemente a lógica!)\n")
            continue
            
        status = "✅ PASSOU" if resultado == teste["esperado"] else "❌ FALHOU"
        
        print(f"Teste {idx + 1}: nums={teste['nums']}")
        print(f"   -> Esperado: {teste['esperado']} | Retornado: {resultado} | {status}\n")