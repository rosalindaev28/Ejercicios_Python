# Calcule el incremento salarial de una persona: 
#Si su salario es menor a 15mil el incremento será del 20% y si es mayor a 15mil el incremento será del 15%

print('Calcula tu incremento salarial: ')

oldsal = float(input('¿Cuál es tu salario actual? '))

if oldsal < 15000:
    print('Tu incremento salarial será del 20%. ')
    newsal = ((oldsal)*(0.2)) + oldsal
    print('Tu nuevo salario será de ', newsal, ' pesos.')
else:
    print('Tu incremento salarial será del 15%. ')
    newsal = ((oldsal)*(0.15)) + oldsal
    print('Tu nuevo salario será de ', newsal, ' pesos.')