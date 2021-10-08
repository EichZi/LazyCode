#Algoritmo Bubble Sort (Ordenamiento de burbuja)
#Complejidad: O(n^2)

#Método de ordenamiento
def bubble_sort(number_list):
  for i in range(len(number_list) - 1):
    for j in range(len(number_list) - i - 1):
      if number_list[j] > number_list[j + 1]:
        temp = number_list[j]
        number_list[j] = number_list[j + 1]
        number_list[j + 1] = temp
        
my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(f'Lista original: {my_list}')
bubble_sort(my_list)
print(f'Lista ordenada: {my_list}')
  
