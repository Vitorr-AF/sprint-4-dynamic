from functools import lru_cache
# dp[dia][estoque] = custo mínimo a partir desse dia

# novo_estoque = max(E + q - c[dia], 0)

# novo_estoque = max(E + q - c[dia], 0)

# Objetivo: dp[1][estoque_inicial]


consumo = [3, 2, 4, 5]
custo_compra = 2
custo_falta = 7


# Versão recursiva com memoização
@lru_cache(None)
def dp_rec(dia, estoque):
    if dia == len(consumo):
        return 0
    
    melhor = float('inf')
    
    for q in range(0, 10):
        novo_estoque = estoque + q - consumo[dia]
        custo = q * custo_compra
        
        if novo_estoque < 0:
            custo += abs(novo_estoque) * custo_falta
            novo_estoque = 0
        
        melhor = min(melhor, custo + dp_rec(dia + 1, novo_estoque))
    
    return melhor

print("Recursivo:", dp_rec(0, 5))  # estoque inicial = 5


# Versão bottom-up

dias = len(consumo)
# limite máximo para representar a tabela
maxE = 10
dp = [[0]* (maxE+1) for _ in range(dias+1)]

for dia in reversed(range(dias)):
    for estoque in range(maxE+1):
        melhor = float('inf')
        for q in range(0, 10):
            novo_estoque = estoque + q - consumo[dia]
            custo = q * custo_compra
            
            if novo_estoque < 0:
                custo += abs(novo_estoque) * custo_falta
                novo_estoque = 0

            novo_estoque = min(novo_estoque, maxE)

            melhor = min(melhor, custo + dp[dia+1][novo_estoque])
        dp[dia][estoque] = melhor

print("Bottom-Up:", dp[0][5])
