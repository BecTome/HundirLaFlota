import numpy as np
import time

from src import constants
from src.crear_tablero import crear_tablero
from src.disparo import disparo
from src.utils import get_coordinate

####################### CREACION DE TABLEROS ##################################

tablero_jugador = crear_tablero(constants.SIZE, constants.BOATS)
tablero_maquina = crear_tablero(constants.SIZE, constants.BOATS)

tab_shot_maq = np.full(shape=(constants.SIZE, constants.SIZE), fill_value=" ")

n_boats = np.sum(constants.BOATS)
print(tablero_maquina)
######################### BIENVENIDA USUARIO ##################################
# Damos la bienvenida al jugador
print(constants.WELCOME_STR)

# Pide el nombre del usuario
user = input("\nIntroduzca nombre de usuario\n")
print(f"\n\nBienvenido {user}\n\n")

time.sleep(2)

print("\n\nEmpieza el juego\n\n")

time.sleep(2)

print(tab_shot_maq, "\n")
print(tablero_jugador, "\n\n")

####################### COMIENZAN LOS TURNOS ####################################
while True:
    ########################### DISPARO JUGADOR ##################################
    print(f"TURNO DE {user.upper()}")
    while True:

        # SOLICITUD Y COMPROBACIÓN DE COORDENADAS
        # Si introducimos la letra q (o Q) salimos.
        x = get_coordinate("x", constants.EXIT_KEY, size=constants.SIZE)
        if str(x).lower() == constants.EXIT_KEY:
            print(f"\nHAS DECIDIDO ABANDONAR EL JUEGO. ADIÓS {user.upper()}.")
            y = constants.EXIT_KEY
            break
        
        # En caso de no ser q, comprobamos que esté dentro del tablero.
        while (not (0 <= x < constants.SIZE)):
            x = get_coordinate("x", constants.EXIT_KEY, size=constants.SIZE)

        # Si introducimos la letra q (o Q) salimos.
        y = get_coordinate("y", constants.EXIT_KEY, size=constants.SIZE)
        if str(y).lower() == constants.EXIT_KEY:
            print(f"\nHAS DECIDIDO ABANDONAR EL JUEGO. ADIÓS {user.upper()}.")
            break

        while (not (0 <= y < constants.SIZE)):
            y = get_coordinate("y", constants.EXIT_KEY, size=constants.SIZE)

        # DISPARO AL TABLERO ENEMIGO
        if tab_shot_maq[x, y] not in [constants.HIT_KEY, constants.WATER_KEY]:
            # El jugador dispara y sobrescribimos el tablero de la maquina
            time.sleep(2)
            tab_shot_maq = disparo(tablero_maquina, tab_shot_maq, x, y)

            print(tab_shot_maq, "\n")
            print(tablero_jugador, "\n\n")

            if (tab_shot_maq[x, y] == "X")&(np.sum(tab_shot_maq == "X") < n_boats):
                print(f"{user.upper()} VUELVE A TIRAR")
                continue

            elif (np.sum(tab_shot_maq == "X") == n_boats):
                print(f"{user.upper()} GANA!!")
                break

            else:
                break
        else:
            print("\nYa has disparado aquí. Vuelve a introducir las coordenadas.\n")
            continue

    if (np.sum(tab_shot_maq == "X") == n_boats)|(str(x).lower()==constants.EXIT_KEY)|(str(y).lower()==constants.EXIT_KEY):
        break
    ########################### DISPARO MAQUINA ##################################

    # La maquina apunta aleatoriamente pero debemos tener cuidado de que no lo haga
    # en sitios donde ya se ha disparado
    print("TURNO DE LA MÁQUINA")

    time.sleep(2)

    x, y = np.random.randint(constants.SIZE, size=2)

    while True:
        if tablero_jugador[x, y] not in [constants.HIT_KEY, constants.WATER_KEY]:
            # La maquina dispara y sobrescribimos el tablero del jugador
            tablero_jugador = disparo(tablero_jugador, tablero_jugador, x, y)

            print(tab_shot_maq, "\n")
            print(tablero_jugador, "\n\n")

            if (tablero_jugador[x, y] == "X")&(np.sum(tablero_jugador == "X") < n_boats):
                print(f"LA MÁQUINA VUELVE A TIRAR")
                continue
            elif (np.sum(tablero_jugador == "X") == n_boats):
                print(f"\n\nLA MÁQUINA GANA :(((((\n\n")
                break
            else:
                break
        else:
            x, y = np.random.randint(constants.SIZE, size=2)
    
    if (np.sum(tablero_jugador == "X") == n_boats):
        break
