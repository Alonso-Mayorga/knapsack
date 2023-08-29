# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:48:12 2023

@author: galgo
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 11:43:50 2023

@author: galgo

"""
def knapsack(values, weights, capacity):
    '''
    Function that solves the knapsack problem using dynamic programming.
    Inputs:
        - value: List containing the value of each element
        - weights: List containing the weight of each element
        - capacity: Maximum capacity of the knapsack
    Outputs:
        - selected_elements: List of indices of the elements in the knapsack
        - total_value: Total value of the elements in the knapsack
    '''
        
    n = len(valor)
    matriz = [[0] * (capacidad + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacidad + 1):
            if pesos[i - 1] <= w:
                matriz[i][w] = max(matriz[i - 1][w], matriz[i - 1][w - pesos[i - 1]] + valor[i - 1])
            else:
                matriz[i][w] = matriz[i - 1][w]
    valor_total = matriz[n][capacidad]
    elementos_seleccionados = []
    capacidad_restante = capacidad
    for i in (range(n, -1, -1)):
        if matriz[i][capacidad_restante] != matriz[i-1][capacidad_restante]:
            elementos_seleccionados.append(i-1)
            capacidad_restante -= pesos[i-1]
    return selected_elements, total_value

