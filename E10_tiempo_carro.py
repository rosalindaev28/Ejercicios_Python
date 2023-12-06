# Reciba la velocidad y la distancia que tiene que recorrer un carro y entrega cuánto tiempo le tomaría recorrer esa distancia.

print('¿Cuánto tardará el carro en recorrer una distancia? ')

d = float(input('Indica la distancia que tiene que recorrer el carro (km): '))
          
v = float(input('¿A qué velocidad se transporta el carro? (km/h)'))

t = d / v

print('El carro tardará ', t, ' horas en recorrer ', d, ' kilómetros.')