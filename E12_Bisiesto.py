#Reciba un año y te responda si es o no es bisiesto.


print('¿Será un año bisiesto?')

year = int(input('Escribe el número del año que quieres consultar: '))

if year % 4 == 0:
	print('El año ', year, ' es bisiesto.')
else:
	print('El año ', year, ' no es bisiesto.')