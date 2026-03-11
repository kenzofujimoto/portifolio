"""
LeetCode #1004 - Max Consecutive Ones III
Link: https://leetcode.com/problems/max-consecutive-ones-iii/

Missão: Dado um array binário nums e um inteiro k, retornar o número máximo 
de 1s consecutivos no array se você puder transformar no máximo k zeros em uns.

Complexidade exigida:
- Tempo: O(N)
- Espaço: O(1)
"""

from typing import List

class Solution:
    def maxConsecutiveOnes(self, nums: List[int], k: int) -> int:
        esquerda = 0
        max_tamanho = 0
        preenchimento = 0

        for direita in range(len(nums)):
            if nums[direita] == 0:
                preenchimento += 1

            while preenchimento > k:
                if nums[esquerda] == 0:
                    preenchimento -= 1
                esquerda += 1

            tamanho_atual = direita - esquerda + 1
            max_tamanho = max(max_tamanho, tamanho_atual)

        return max_tamanho
    
# ==========================================
# ÁREA DE TESTES LOCAIS (Test Cases)
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    
    # Casos de Teste
    testes = [
        # Caso 1: Exemplo clássico do LeetCode
        {"nums": [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], "k": 2, "esperado": 6},
        
        # Caso 2: Array longo com vários buracos
        {"nums": [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], "k": 3, "esperado": 10},
        
        # Caso 3: Edge Case (Não precisa inverter nada, já é tudo 1)
        {"nums": [1, 1, 1, 1], "k": 0, "esperado": 4},
        
        # Caso Pegadinha: k = 0 (Não pode inverter nada, só contar os 1s reais)
        {"nums": [0, 1, 1, 0, 1], "k": 0, "esperado": 2},
        
        # Edge Case extremo: Tudo zero, limitando ao tamanho do k
        {"nums": [0, 0, 0, 0], "k": 2, "esperado": 2}
    ]

    print("🚀 Iniciando Testes de Max Consecutive Ones III...\n")
    
    for idx, teste in enumerate(testes):
        resultado = sol.maxConsecutiveOnes(teste["nums"], teste["k"])
        
        if resultado is None:
            print(f"Teste {idx + 1}: k={teste['k']} | nums={teste['nums']}")
            print("   -> ❌ FALHOU (Função retornou None. Implemente a lógica!)\n")
            continue
            
        status = "✅ PASSOU" if resultado == teste["esperado"] else "❌ FALHOU"
        
        print(f"Teste {idx + 1}: k={teste['k']} | nums={teste['nums']}")
        print(f"   -> Esperado: {teste['esperado']} | Retornado: {resultado} | {status}\n")