# Calcule el volumen de una esfera	

# Importar el número pi de la librería math
from math import pi

print('Calcula el volumen de una esfera (cm3)\n')
resp = input('¿Qué dato tienes? Escribe r para radio o d para diámetro: ')

if resp == 'r':
	r = int(input('Escribe el radio: '))
	Vol = ((4/3)*(pi)*(r**3))
	print('El volumen de la esfera es ', Vol, 'cm3.')
else:
	d = int(input('Escribe el diámetro: '))
	r = d/2
	Vol = ((4/3)*(pi)*(r**3))
	print('El volumen de la esfera es ', Vol, 'cm3.')