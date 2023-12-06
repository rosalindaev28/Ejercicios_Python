# Calcular el factorial de un número

print('Calcula el factorial de un número')

num = int(input('Escribe un número: '))
c = 1
factor = 1

if num < 0 :
	print('El número ', num, ' no tiene factorial porque es negativo.')
	if num == 0:
		print('El factorial del número ", num, " es 1.')
else:
	while c <= num:
		factor = factor * c
		c =  c + 1
	print('El factorial del número ', num, ' es ', factor)