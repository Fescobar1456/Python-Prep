# SelectionSort()

import random

array = random.sample(range(1, 21), 10)

print(' - SelectionSort -')
print(f'Array desordenado ->    {array}')

minimo = 0	# Guarda el valor minimo
value = 0	# Variable cache
index = 0	# Guarda el indice del valor minimo

for i in range(len(array) - 1):
    minimo = array[i]
    for j in range(i + 1, len(array)):
        if (minimo > array[j]):
            minimo = array[j]
            index = j
    if minimo < array[i]:
        value = array[i]
        array[index] = value
        array[i] = minimo
        
print(f'Array ordenado ->       {array}')