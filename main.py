import random

nombre_arc = 'diccionario.txt'
arc_sa = 'arc_t.txt'
palabras = []
num_pa = 30
with open(nombre_arc, 'r') as archivo:
    Palabras = [linea.strip() for linea in archivo]
    pal_ale = random.sample(palabras, min(num_pa, len(palabras)))

palabras_por_linea = 6
grupos = [pal_ale[i:i + palabras_por_linea] for i in range(0, len(pal_ale), palabras_por_linea)]

with open(arc_sa, "w") as salida:
    for grupo in grupos:
        salida.write(' : '.join(grupo) + '\n')
