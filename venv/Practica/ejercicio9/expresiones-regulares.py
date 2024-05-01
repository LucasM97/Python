texto = 'Hoy es 6/8/2020. Mañana será 7/8/2020.'
# Encontrar las apariciones de una fecha en el texto
import re
fechas = re.findall(r'\d+/\d+/\d+', texto)
print(fechas)