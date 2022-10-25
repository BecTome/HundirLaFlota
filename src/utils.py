def get_coordinate(coord_name, exit_key, size):

    x = input(f"Introduzca coordenada {coord_name} entre 0 y {size - 1} o {exit_key} para salir\n")

    while True:
        try:
            out = int(x)
            break
        except:
            if x.lower() == "q":
                out = "q"
                break
            else:
                x = input(f"Introduzca coordenada {coord_name} entre 0 y {size - 1} o {exit_key} para salir")
                continue
    return out

