from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if len(nums) == 1: return nums[0]

        if k == len(nums): return sum(nums)/k

        soma = sum(nums[0:k])
        soma_max = soma

        for i in range(k, len(nums)):
            soma = soma + nums[i] - nums[i - k]
            if soma > soma_max:
                soma_max = soma

        return soma_max/k

if __name__ == "__main__":
    sol = Solution()
    
    # Casos de Teste (Cobrindo cenários padrão e edge cases)
    testes = [
        # Caso Padrão do LeetCode
        {"nums": [1, 12, -5, -6, 50, 3], "k": 4, "esperado": 12.75000},
        
        # Edge Case: Array com apenas 1 elemento
        {"nums": [5], "k": 1, "esperado": 5.00000},
        
        # Edge Case: Todos os números negativos
        {"nums": [-1, -2, -3, -4], "k": 2, "esperado": -1.50000},
        
        # Edge Case: A janela (k) é o tamanho exato do array
        {"nums": [4, 2, 1, 3], "k": 4, "esperado": 2.50000}
    ]

    print("🚀 Iniciando Testes da Janela Deslizante...\n")
    
    for idx, teste in enumerate(testes):
        resultado = sol.findMaxAverage(teste["nums"], teste["k"])
        
        # Trava para não quebrar o teste enquanto você não implementar o return
        if resultado is None:
            print(f"Teste {idx + 1}: nums={teste['nums']}, k={teste['k']}")
            print("   -> ❌ FALHOU (Função retornou None. Implemente a lógica!)\n")
            continue
            
        # Como é float, usamos uma precisão de 5 casas decimais para comparar
        status = "✅ PASSOU" if round(resultado, 5) == round(teste["esperado"], 5) else "❌ FALHOU"
        
        print(f"Teste {idx + 1}: nums={teste['nums']}, k={teste['k']}")
        print(f"   -> Esperado: {teste['esperado']} | Retornado: {resultado} | {status}\n")