import random

archivo_entrada = "diccionario.txt"
archivo_salida = "new_test_del_dic;1.0;.txt"
palabra = []
num_pala = 59
with open(archivo_entrada, 'r') as archivo:
    palabra = [linea.strip() for linea in archivo]
random.shuffle(palabra)
pa_por_linea = 4

grupos = [palabra[i:i+pa_por_linea] for i in range(0, len(palabra), pa_por_linea)]
with open(archivo_salida, 'w') as salida:
    for grupo in grupos:
        salida.write(' ; (.)(.) ; '.join(grupo)+'\n')