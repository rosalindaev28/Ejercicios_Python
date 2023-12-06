# Calcule los días que faltan para día de muertos y navidad.

print('¿Cuántos días faltan para Día de Muertos y Navidad?')

from datetime import datetime

hoy = datetime.today()
navidad = datetime(2024, 12, 25)
diamuer = datetime(2024,11, 2)
faltan_navi = navidad - hoy
faltan_muer = diamuer - hoy
print ('Faltan', faltan_navi.days, 'días para la Navidad de 2024.')
print ('Faltan', faltan_muer.days, 'días para el Día de Muertos de 2024.')