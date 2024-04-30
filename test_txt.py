datos = ("hola", "mundo", "ejemplo", "código", "python", "desarrollo", "web", "tecnología", "innovación", "aprendizaje",
         "educación", "escritura", "inteligencia", "artificial", "modelo", "computadora", "programación", "variable",
         "función", "condicional",
         "iteración", "lista", "diccionario", "objeto", "clase", "método", "herencia", "polimorfismo",
         "encapsulamiento", "abstracción",
         "importar", "librería", "framework", "plataforma", "servidor", "cliente", "usuario", "experiencia", "diseño",
         "interfaz",
         "usuario", "prueba", "calidad", "rendimiento", "seguridad", "acceso", "datos", "almacenamiento", "nube",
         "servicio")

archivo_salida = "hola_mundo.txt"
with open(archivo_salida, "w") as file:
    for palabra in datos:
        file.write(palabra + '\n')
