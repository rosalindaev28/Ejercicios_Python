# Calcule el número de días que alguien ha vivido tomando en cuenta su fecha de nacimiento

print('Calcula cuántos días has vivido hasta el día de hoy.')

import datetime

a = int(input('Escribe tu año de nacimiento: '))
m = int(input('Escribe tu mes de nacimiento: '))
d = int(input('Escribe tu día de nacimiento: '))

fecha_nacimiento = datetime.datetime(a,m,d)
fecha_hoy = datetime.datetime.now()

diferencia = fecha_hoy - fecha_nacimiento

print('Has vivido', diferencia.days, ' días hasta hoy.')