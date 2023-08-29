"""
Created on Tue Aug 29 20:48:12 2023

@author: galgo
"""


def knapsack(values, weights, capacity):
    '''
    Function that solves the knapsack problem using dynamic programming.
    Inputs:
        - values: List containing the value of each element
        - weights: List containing the weight of each element
        - capacity: Maximum capacity of the knapsack
    Outputs:
        - selected_elements: List of indices of the elements in the knapsack
        - total_value: Total value of the elements in the knapsack
    '''
        
    n = len(values)
    matrix = [[0] * (capacity + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                matrix[i][w] = max(matrix[i - 1][w], matrix[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                matrix[i][w] = matrix[i - 1][w]
    total_value = matrix[n][capacity]
    selected_elements = []
    remaining_capacity = capacity
    for i in (range(n, -1, -1)):
        if matrix[i][remaining_capacity] != matrix[i - 1][remaining_capacity]:
            selected_elements.append(i - 1)
            remaining_capacity -= weights[i - 1]
    return selected_elements, total_value
