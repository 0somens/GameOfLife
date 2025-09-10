cell1 = [0,0,0,0,0,0,0,0,0]
cell2 = [0,0,0,0,0,0,0,0,0]
cell3 = [0,0,0,0,0,0,0,0,0]
cell4 = [0,0,0,0,0,0,0,0,0]
cell5 = [0,0,0,0,0,0,0,0,0]
cell6 = [0,0,0,0,0,0,0,0,0]
cell7 = [0,0,0,0,0,0,0,0,0]
cell8 = [0,0,0,0,0,0,0,0,0]
cell9 = [0,0,0,0,0,0,0,0,0]

# Bien, voy a intentar automatizar la resolución de los sudokus usando IA
# lo primero es hacer la "interfaz"
# se me ocurre: 9 listas, cada una con nueve ceros y en cada lista deben ir los números del 1 al 9 se ordenarian de izquierda a derecha, 
# para el tema de no repetir en la misma linea se me ocurren los indices
# será por fuerza bruta un buen método?

# # se vería algo así
# ____________|____________|____________
# ___cell1____|__cell2_____|___cell3____
# ____________|____________|____________
# ____________|____________|____________
# ___cell4____|__cell5_____|___cell6____
# ____________|____________|____________
# ____________|____________|____________
# ___cell7____|___cell8____|___cell9____
# ____________|____________|____________


# Class inicializador | donde se inserte una N cantidad de números del 1 al 9 en las casillas
# Pero ojo, esos números deben respetar la clase rules de otra manera está roto el sudoku


# Asignar reglas
class Rules:
    def __init__(self):
        pass


class initializer: #inserta un set de números N cantidad respetando Rules, pero espera, por qué seria una clase si puede ser una función?
    def __init__(self):
        pass

# Tal vez ni necesite crear 9 varaibles, pueden ser creadas mediante código // pero entonces como asigno un numero a cada celda?
def main():