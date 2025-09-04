from typing import List #

class Paciente:
    def __init__(self, nombre: str, edad: int, sintomas: List[str]):
        self.nombre = nombre
        self.edad = edad
        self.sintomas = sintomas
        self.departamento = None
    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - Síntomas: {', '.join(self.sintomas)} → Departamento: {self.departamento}"

class Regla:
    def __init__(self, sintomas_clave: List[str], departamento: str):
        self.sintomas_clave = set(sintomas_clave)
        self.departamento = departamento

    def aplica(self, sintomas_paciente: List[str]) -> bool:
        # Retorna True si alguno de los síntomas clave está en los síntomas del paciente
        return bool(self.sintomas_clave.intersection(sintomas_paciente))

class Clasificador:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, regla: Regla):
        self.reglas.append(regla)

    def clasificar(self, paciente: Paciente):
        for regla in self.reglas:
            if regla.aplica(paciente.sintomas):
                paciente.departamento = regla.departamento
                return paciente
        paciente.departamento = "Evaluación general"
        return paciente

def main():
    clasificador = Clasificador()

    # Definir reglas
    clasificador.agregar_regla(Regla(["dolor en el pecho", "dificultad para respirar"], "Emergencia"))
    clasificador.agregar_regla(Regla(["fiebre", "tos", "dolor de garganta"], "Consulta General"))
    clasificador.agregar_regla(Regla(["sarpullido", "comezón"], "Dermatología"))
    clasificador.agregar_regla(Regla(["dolor abdominal", "náuseas"], "Gastroenterología"))
    clasificador.agregar_regla(Regla(["fiebre", "llanto", "irritabilidad"], "Pediatría"))

    pacientes = [
        Paciente("Juan Perez", 30, ["fiebre", "tos"]),
        Paciente("MAria Soto", 65, ["dolor en el pecho"]),
        Paciente("Antonieta de las nieves", 5, ["fiebre", "irritabilidad"]),
        Paciente("Carlos González", 40, ["mareo"])
    ]

    for paciente in pacientes:
        clasificador.clasificar(paciente)
        print(paciente)

if __name__ == "__main__":
    main()


# Posee
 
# Base de conocimiento
#   Reglas
# Motor de inferencia
#   Clasificación
# Interfaz
#   main
