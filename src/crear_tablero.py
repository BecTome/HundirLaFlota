import numpy as np

def crear_tablero(size, ls_esloras):
    tablero = np.full(fill_value=" ", shape=(size, size))
    for eslora in ls_esloras:
        while True:
            # 'N' - 'S' - 'E' - 'O'
            orient = np.random.choice(['N', 'S', 'E', 'O'])

            # Posicion inicial del barco
            current_pos = np.random.randint(size, size = 2)
            
            fila = current_pos[0]
            col = current_pos[1]
            
            # Recogemos las 4 posiciones colindantes a current_pos
            coors_posiN = tablero[fila:fila - eslora:-1, col]
            coors_posiE = tablero[fila, col: col + eslora]
            coors_posiS = tablero[fila:fila + eslora, col]
            coors_posiO = tablero[fila, col: col - eslora:-1]
            
            # Comprobamos si esas posiciones son validas
            # Orientacion Norte
            if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                tablero[fila:fila - eslora:-1, col] = 'O'
                break

            # Orientacion Este
            elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
                tablero[fila, col: col + eslora] = 'O'
                break

            # Orientacion Sur
            elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                tablero[fila:fila + eslora, col] = 'O'
                break

            # Orientacion Oeste
            elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
                tablero[fila, col: col - eslora:-1] = 'O'
                break

            # No cumple con las dimensiones del tablero, o hay un barco ahi
            # Probamos con otra coordenada
            else:
                continue
    return tablero

if __name__ == "__main__":
    print(crear_tablero(10, [1, 1, 2, 2, 2]))