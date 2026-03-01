"""
LeetCode #392 - Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/

Abordagem: Two Pointers (Dois Ponteiros)
- O ponteiro 'i' age como um "Guarda-Volumes" rastreando as letras da string menor 's'.
- O loop 'for' age como um "Explorador", varrendo a string maior 't'.
- Utilizamos a técnica de "Curto-Circuito" para parar a execução assim que todas as letras são encontradas.

Complexidade:
- Tempo: O(N), onde N é o tamanho da string 't'. No pior dos casos, percorremos 't' apenas uma vez.
- Espaço: O(1). Nenhuma estrutura de dados extra na memória foi criada.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        
        # Trava de segurança 1: String vazia é sempre subsequência de qualquer coisa
        if len(s) == 0: 
            return True

        # Loop Explorador
        for char in t:
            if s[i] == char:
                i += 1
            
            # Trava de segurança 2: Achou todas as letras? Curto-circuito (Para o loop na hora)
            if i == len(s): 
                return True

        return False


# ==========================================
# ÁREA DE TESTES LOCAIS
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    
    # Casos de Teste (Cenários do LeetCode)
    testes = [
        {"s": "abc", "t": "ahbgdc", "esperado": True},   # Caso Padrão (Sucesso)
        {"s": "axc", "t": "ahbgdc", "esperado": False},  # Caso Padrão (Falha)
        {"s": "", "t": "ahbgdc", "esperado": True},      # Edge Case: String 's' vazia
        {"s": "b", "t": "c", "esperado": False}          # Edge Case: Ambas pequenas
    ]

    print("🚀 Iniciando Testes Locais...\n")
    
    for idx, teste in enumerate(testes):
        resultado = sol.isSubsequence(teste["s"], teste["t"])
        status = "✅ PASSOU" if resultado == teste["esperado"] else "❌ FALHOU"
        print(f"Teste {idx + 1}: s='{teste['s']}', t='{teste['t']}'")
        print(f"   -> Esperado: {teste['esperado']} | Retornado: {resultado} | {status}\n")