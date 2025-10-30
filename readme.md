# Controle de Estoque com Programação Dinâmica

Este projeto implementa um modelo simples de **controle de estoque diário** para unidades de diagnóstico, onde o consumo de insumos não é registrado com precisão.

## Conceito

* **Estado:** quantidade de estoque disponível no início do dia.
* **Decisão:** quantidade de insumos a comprar a cada dia.
* **Função de transição:** o estoque do dia seguinte = estoque atual + compras − consumo do dia.
* **Objetivo:** minimizar o custo total considerando:

  * custo de compra dos insumos,
  * custo por falta de insumo (quando o consumo excede o estoque disponível),
  * evitar excesso de estoque.

## Implementações

1. **Versão recursiva com memoização** (`dp_rec`)
   Calcula o custo mínimo esperado usando recursão e cache para evitar recalcular estados já visitados.

2. **Versão iterativa (bottom-up)** (`dp_bottom_up`)
   Preenche uma tabela de custos de forma iterativa, do último dia para o primeiro, garantindo eficiência computacional.

## Exemplo de uso

```python
consumo = [3, 2, 4, 5]
custo_compra = 2
custo_falta = 7
estoque_inicial = 5

# Custo mínimo usando recursão
print("Recursivo:", dp_rec(0, estoque_inicial))

# Custo mínimo usando bottom-up
print("Bottom up:", dp_bottom_up(consumo, custo_compra, custo_falta, estoque_inicial))
```

Ambas as implementações retornam o mesmo valor, mostrando a consistência do modelo.