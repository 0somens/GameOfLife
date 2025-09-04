import json

# 1) Nombres consistentes y sin sombras
sintomas = ["Problema a la garganta", "Mucosidad", "Sangrado", "Dolor abdominal", "Dolor en el pecho", "Dolor de cabeza"]

sintoma_peso = {
    "Problema a la garganta": 1,
    "Mucosidad": 1,
    "Sangrado": 6,
    "Dolor abdominal": 5,
    "Dolor en el pecho": 6,
    "Dolor de cabeza": 3,
}

# 2) No uses json.loads sobre un dict
data = sintoma_peso

print("Seleccione su(s) síntoma(s) por número. Cuando termine, escriba -1.")
for i, s in enumerate(sintomas):
    print(f"{i}) {s}")

lista_indices = []
diagnostico = True
while diagnostico:
    try:
        eleccion = int(input("Opción: "))
    except ValueError:
        print("Ingrese un número válido.")
        continue

    if eleccion == -1:
        diagnostico = False
        break
    if 0 <= eleccion < len(sintomas):
        lista_indices.append(eleccion)
        print(f"Seleccionados (índices): {lista_indices}")
    else:
        print("Índice fuera de rango.")

# 3) Convertir índices a nombres y sumar pesos
seleccion = [sintomas[i] for i in lista_indices]
peso_total = sum(data.get(nombre, 0) for nombre in seleccion)

print(f"Síntomas seleccionados: {seleccion}")
print(f"Peso total: {peso_total}")

# 4) Decisión
if peso_total < 4:
    print("Por favor, diríjase a la sala de espera.")
elif 4 <= peso_total <= 6:
    print("Por favor, vaya a salón B.")
else:  # peso_total > 6
    print("Vaya inmediatamente a urgencias.")


# tengo una lista de sintomas
# tengo un json ajustando cada 
# el usuario seleccionar los sintomas y se agregan en una nueva lista


 

# Pseudo-código
# El usuario selecciona un sintoma
# Posee otro?
# Selecciona otro sintoma
# Se le da un peso a cada sintoma? 
# Si el peso es mayor a 7 es crítico
# Si el peso es entre 4 y 6 es medio
# Si el peso es menor a 4 no es emergencia