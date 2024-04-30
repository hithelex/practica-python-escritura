import random

entra = "diccionario.txt"
sale = "hola_up.txt"
palabra = []

with open(entra,'r') as arc_entrada:
    palabra = [line.strip() for line in arc_entrada]

random.shuffle(palabra)
por_fila = 5
grupo = [palabra[i:i+por_fila] for i in range(0,len(palabra),por_fila)]

with open(sale,'w') as arc_salida:
    for grup in grupo:
        arc_salida.write(' ; '.join(grup) + '\n')