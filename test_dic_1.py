# Datos de entrada originales
procesos_originales = [
    {"nombre": "P1", "llegada": 0, "rafaga": 5},
    {"nombre": "P2", "llegada": 1, "rafaga": 4},
    {"nombre": "P3", "llegada": 3, "rafaga": 9},
    {"nombre": "P4", "llegada": 4, "rafaga": 6},
    {"nombre": "P5", "llegada": 5, "rafaga": 7}
]
quantum = 3

procesos = [dict(p) for p in procesos_originales]

tiempo_actual = 0
cola = []
tiempos_finalizacion = {}
tiempos_espera = {}
tiempos_restantes = {p["nombre"]: p["rafaga"] for p in procesos}
orden_gantt = []

# Inicialización de los tiempos de espera
for p in procesos:
    tiempos_espera[p["nombre"]] = 0

# Ordenar procesos por llegada
procesos = sorted(procesos, key=lambda x: x["llegada"])
indice_proceso_actual = 0

# Bucle de planificación
while procesos or cola:
    while procesos and procesos[0]["llegada"] <= tiempo_actual:
        cola.append(procesos.pop(0)["nombre"])

    if cola:
        proceso = cola.pop(0)
        orden_gantt.append((proceso, tiempo_actual))

        if tiempos_restantes[proceso] > quantum:
            tiempo_actual += quantum
            tiempos_restantes[proceso] -= quantum
            while procesos and procesos[0]["llegada"] <= tiempo_actual:
                cola.append(procesos.pop(0)["nombre"])
            cola.append(proceso)  # Reagregar proceso al final de la cola
        else:
            tiempo_actual += tiempos_restantes[proceso]
            tiempos_finalizacion[proceso] = tiempo_actual
            tiempos_restantes[proceso] = 0

        for p in cola:
            tiempos_espera[p] += quantum if tiempos_restantes[proceso] >= quantum else tiempos_restantes[proceso]
    else:
        tiempo_actual += 1

tiempos_entrega = {proceso: tiempos_finalizacion[proceso] - next(p["llegada"] for p in procesos_originales if p["nombre"] == proceso) for proceso in tiempos_finalizacion}
tiempo_espera_promedio = sum(tiempos_espera.values()) / len(tiempos_espera)
tiempo_entrega_promedio = sum(tiempos_entrega.values()) / len(tiempos_entrega)

print("Diagrama de planificación (Gantt):")
for proceso, tiempo in orden_gantt:
    print(f"{tiempo} - {proceso}")

print("\nTiempos de espera:")
for proceso, tiempo in tiempos_espera.items():
    print(f"{proceso}: {tiempo} unidades")

print("\nTiempos de entrega:")
for proceso, tiempo in tiempos_entrega.items():
    print(f"{proceso}: {tiempo} unidades")

print(f"\nTiempo de espera promedio: {tiempo_espera_promedio:.2f} unidades")
print(f"Tiempo de entrega promedio: {tiempo_entrega_promedio:.2f} unidades")