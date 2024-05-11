import pandas as pd
from tabulate import tabulate
datos = ("hola", "mundo", "ejemplo", "código", "python", "desarrollo", "web", "tecnología", "innovación", "aprendizaje","educación", "escritura", "inteligencia", "artificial", "modelo", "computadora", "programación", "variable","función", "condicional","iteración", "lista", "diccionario", "objeto", "clase", "método", "herencia", "polimorfismo","encapsulamiento", "abstracción","importar", "librería", "framework", "plataforma", "servidor", "cliente", "usuario", "experiencia", "diseño","interfaz","usuario", "prueba", "calidad", "rendimiento", "seguridad", "acceso", "datos", "almacenamiento", "nube","servicio")

archivo_salida = "Atest_txt1.txt"
tamaño_de_grupos = 5
grupos = [datos [i : i + tamaño_de_grupos] for i in range(0, len(datos), tamaño_de_grupos)]
columnas = [f'columna {i+1}' for i in range(tamaño_de_grupos)]
filas = [f'filas {i+1}' for i in range(len(grupos))]

df = pd.DataFrame(grupos, index=filas, columns=columnas)
tabla_bien = tabulate(df, headers='keys', tablefmt='pretty', showindex=True)

with open(archivo_salida, "w", encoding='utf-8') as file:
        file.write(tabla_bien + '\n')
print(tabla_bien)