#suma el numero total de libros


def totalPaginas(libros):
    if len(libros) == 1:
        return libros[0]

    return libros[0] + totalPaginas(libros[1:])


libros = [50, 100, 150]
print(totalPaginas(libros))