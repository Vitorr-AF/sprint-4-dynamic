from functools import lru_cache
"""
Nas unidades de diagnóstico, o consumo diário de insumos não é registrado com precisão, 
o que dificulta o controle de estoque. Para resolver isso, modelamos o problema como uma decisão diária de compra. 
O estado do sistema é a quantidade de estoque disponível no início de cada dia. 
A decisão é a quantidade de insumos a ser comprada naquele dia. 
A função de transição descreve como o estoque evolui: o estoque do dia seguinte é igual ao estoque atual mais a quantidade comprada, 
menos o consumo do dia. Por fim, o objetivo é minimizar o custo total ao longo do período analisado, considerando custos de compra, 
possíveis faltas de insumo e eventual excesso de estoque.
"""


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

print("Recursivo:", dp_rec(0, 5))


# Versão bottom-up

def dp_bottom_up(consumo, custo_compra, custo_falta, estoque_inicial, maxE=10):
    dias = len(consumo)
    dp = [[0]*(maxE+1) for _ in range(dias+1)]
    
    for dia in range(dias-1, -1, -1):
        for estoque in range(maxE+1):
            melhor = float('inf')
            for q in range(10):
                novo_estoque = estoque + q - consumo[dia]
                custo = q * custo_compra
                if novo_estoque < 0:
                    custo += -novo_estoque * custo_falta
                    novo_estoque = 0
                novo_estoque = min(novo_estoque, maxE)
                melhor = min(melhor, custo + dp[dia+1][novo_estoque])
            dp[dia][estoque] = melhor
    return dp[0][estoque_inicial]

print("Bottom up:", dp_bottom_up(consumo, custo_compra, custo_falta, 5))
