def get_coordinate(coord_name, exit_key, size):

    x = input(f"Introduzca coordenada {coord_name} entre 0 y {size - 1} o {exit_key} para salir\n")

    while True:
        try:
            out = int(x)
            break
        except:
            if x.lower() == exit_key:
                out = exit_key
                break
            else:
                x = input(f"Introduzca coordenada {coord_name} entre 0 y {size - 1} o {exit_key} para salir")
                continue
    return out
    
if __name__ == "__main__":
    get_coordinate("x", "q", 10)