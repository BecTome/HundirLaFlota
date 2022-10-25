import numpy as np
from src import constants
from src.crear_tablero import crear_tablero
from src.disparo import disparo
from src.utils import get_coordinate

np.random.seed(0)
tablero_jugador = crear_tablero(constants.SIZE, constants.BOATS)
tablero_maquina = crear_tablero(constants.SIZE, constants.BOATS)

tab_shot_jug = np.full(shape=(constants.SIZE, constants.SIZE), fill_value=" ")
tab_shot_maq = np.full(shape=(constants.SIZE, constants.SIZE), fill_value=" ")

# Damos la bienvenida al jugador
print(constants.WELCOME_STR)

# Pide el nombre del usuario
name = input("\nIntroduzca nombre de usuario\n")
print(f"Bienvenido {name}\n\n")

tablero_maquina[4, 4] = "-"

while True:
    x = get_coordinate("x", constants.EXIT_KEY, size=constants.SIZE)
    while (not (0 <= x < constants.SIZE)):
        x = get_coordinate("x", constants.EXIT_KEY, size=constants.SIZE)

    y = get_coordinate("y", constants.EXIT_KEY, size=constants.SIZE)
    while (not (0 <= y < constants.SIZE)):
        y = get_coordinate("y", constants.EXIT_KEY, size=constants.SIZE)

    if tablero_maquina[x, y] not in [constants.HIT_KEY, constants.WATER_KEY]:
        # El jugador dispara y sobrescribimos el tablero de la maquina
        tab_shot_maq = disparo(tablero_maquina, tab_shot_maq, x, y)
        break
    else:
        print("Ya has disparado aquí. Vuelve a introducir las coordenadas.\n")
        continue
        
x, y = np.random.randint(constants.SIZE)

# La maquina dispara y sobrescribimos el tablero del jugador
tab_shot_jug = disparo(tablero_jugador, tab_shot_jug, x, y)

print(tab_shot_maq)
print(tab_shot_jug)