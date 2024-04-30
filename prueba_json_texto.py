import json
datos = {'Nombre': "luis edin", 'Apellidos' : "huingo ygnacio" , 'correo': "luis@gmail.com"}

archivo = "new_arc_json.json"

with open(archivo , "w") as file:
    json.dump(datos,file,indent=4)

with open(archivo) as filex:
    data = json.load(filex)

