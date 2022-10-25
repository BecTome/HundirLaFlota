
def disparo(tablero, tablero_shot, x, y):
    from src.constants import BOAT_KEY, EMPTY_KEY, WATER_KEY, HIT_KEY

    tabl = tablero.copy()
    tabl_shot = tablero_shot.copy()
    if (tabl[x, y] == BOAT_KEY):
        tabl_shot[x, y] = HIT_KEY
        print(f"\nDisparo en {x, y}.\t TOCADO!!!\n")
    elif (tabl[x, y] == EMPTY_KEY):
        tabl_shot[x, y] = WATER_KEY
        print(f"\nDisparo en {x, y}.\t AGUA\n")
    else:
        raise ValueError(f"Valor no esperado en posición {x, y}: {tabl[x, y]}")

    return tabl_shot

# import numpy as np
# tab_aux = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                     [' ', ' ', ' ', ' ', 'O', 'O', ' ', ' ', ' ', ' '],
#                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
#                     [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                     [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                     [' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' '],
#                     [' ', ' ', ' ', ' ', 'O', 'O', ' ', ' ', ' ', ' ']])

# print(disparo(tab_aux, 0, 0))
# print(disparo(tab_aux, 1, 4))
# print(disparo(tab_aux, 9, 9))