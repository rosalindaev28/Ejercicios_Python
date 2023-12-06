# Ordena los número de menor a mayor

print('Ordena los números de menor a mayor')

# Creación de una lista vacía para almacenar los datos ingresados por el usuario

list=[]
num = int(input('Escribe un número (presiona la tecla 0 para finalizar): '))

while num!=0:
    list.append(num)
    num = int(input('Escribe un número (presiona la tecla 0 para finalizar): '))

# Método sort para ordenar los elementos de la lista de menor a mayor
list.sort()

print('La lista de números ordenados de menor a mayor es:', list)