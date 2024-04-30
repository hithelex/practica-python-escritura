datos = ("hola", "mundo", "ejemplo", "código", "python", "desarrollo", "web", "tecnología", "innovación", "aprendizaje",
         "educación", "escritura", "inteligencia", "artificial", "modelo", "computadora", "programación", "variable",
         "función", "condicional",
         "iteración", "lista", "diccionario", "objeto", "clase", "método", "herencia", "polimorfismo",
         "encapsulamiento", "abstracción",
         "importar", "librería", "framework", "plataforma", "servidor", "cliente", "usuario", "experiencia", "diseño",
         "interfaz",
         "usuario", "prueba", "calidad", "rendimiento", "seguridad", "acceso", "datos", "almacenamiento", "nube",
         "servicio")

with open("new_carp.txt", "w") as file:
    for i in range(0, len(datos),5):
        linea = " ; ".join(datos[i:i+5])
        file.write(linea + '\n')