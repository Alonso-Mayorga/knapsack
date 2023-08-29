# Knapsack problem solver

This repository cointains a Python function which solves the knapsack problem using dynamic programming.


##    Inputs:
        - value: List containing the value of each element
        - weights: List containing the weight of each element
        - capacity: Maximum capacity of the knapsack
        
##    Outputs:
        - selected_elements: List of indices of the elements in the knapsack
        - total_value: Total value of the elements in the knapsack
##Example

```python
from knapsack import knapsack
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
selected_elements, total_value = knapsack(values, weights, capacity)
print("Selected element indices:", selected_elements)
print("Total value:", total_value)
```
##Expected output:
```python
"Selected element indices": [2, 1]
"Total value": 220
```
## Contributing

Feel free to contribute to this repository by suggesting improvements, reporting issues, or adding new methods for solving linear equations.

## License

This project is licensed under the [MIT License](license.txt).




