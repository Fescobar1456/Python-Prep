# BubbleSort()

import random

array = random.sample(range(1, 21), 10)

print(' - BubbleSort -')
print(f'Array desordenado ->    {array}')

value = 0
operaciones = 0

n = len(array)

for i in range(len(array) - 2):
    n -= 1
    for j in range(n):
        if array[j] > array[j + 1]:
            operaciones += 1    # Cuantas veces entra al if
            value = array[j + 1]
            array[j + 1] = array[j]
            array[j] = value
            
print(f'Array ordenado ->       {array}')
print(f'Veces que entro al if:  {operaciones}')