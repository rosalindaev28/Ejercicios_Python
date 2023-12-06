# Valide si una palabra o frase es palíndromo.

print('¿Será palíndromo?')

def sipalindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(' ', '')
    palabra = palabra.replace('á', 'a')
    palabra = palabra.replace('é', 'e')
    palabra = palabra.replace('í', 'i')
    palabra = palabra.replace('ó', 'o')
    palabra = palabra.replace('ú', 'u')

    a = 0
    b = len(palabra) - 1

    for i in range(0, len(palabra)):
        if palabra[a] == palabra[b]:
            a += 1
            b -= 1
        else:
            return False
    return True

palabra = input('Escribe una palabra o frase: ')

if sipalindromo(palabra):
    print('Es una palabra o frase palíndroma.')
else:
    print('No es una palabra o frase palíndroma.')