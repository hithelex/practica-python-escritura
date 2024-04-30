import json
entrada = "diccionario.txt"
salida = "new_prueba.json"
datos = []

with open(entrada, 'r') as lec_arc:
    for linea in lec_arc:
        datos = [linea.strip() for linea in lec_arc]

dicc = {str(i): datos for i,datos in enumerate(datos)}

with open(salida, 'w') as sa_arc:
    json.dump(dicc, sa_arc, indent=4)
