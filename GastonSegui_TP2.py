def problema_1(lista):
    for n in lista:
        if n % 2 != 0:
            lista.append(n + 1)
            lista.remove(n)
    listaPares = [n for n in lista if n % 2 == 0]
    for n in lista:
        if n % 2 != 0:
            lista.append(n + 1)
            lista.remove(n)
    listaPares = [n for n in lista if n % 2 == 0]
    listaPares.sort()
    return(listaPares)

def problema_2(numeroSerie):
    numeroSerie.sort()
    a = sum(numeroSerie) / len(numeroSerie)
    a = round(a)

    b = None
    for n in numeroSerie:
        if (b is None or n > b):
            b = n

    c = None
    for n in numeroSerie:
        if (c is None or n < c):
            c = n

    d = numeroSerie[min(range(len(numeroSerie)), key=lambda i: abs(numeroSerie[i] - a))]

    clave = [a, b, c, d]
    return(clave)

def problema_3(palabra):
    invertida = palabra[::-1]
    return(invertida)

def problema_4(polinomio):
    a = polinomio[0]
    b = polinomio[1]
    c = polinomio[-1]

    d = pow(b, 2) - 4 * a * c

    X1 = -b + (b ** 2 - 4 * a * c) ** 0.5
    X2 = -b - (b ** 2 - 4 * a * c) ** 0.5
    listaRaices = []
    if d > 0:
        listaRaices = [X1, X2]
    elif d == 0:
        listaRaices = [X1]
    elif d < 0:
        listaRaices = []
    else:
        pass

    return(listaRaices)

def problema_5(clave):

    cantidad = 0

    for i in clave:
        if i.isnumeric():
            cantidad += 1
        else:
            pass

    return (cantidad)

def problema_6(lista_libros, lista_autores, eleccion):

    autor_libro = lista_autores.pop(lista_libros.index(eleccion)) + " - " + eleccion
    return(autor_libro)

def problema_7(mes):
    if mes == 1 or mes == 3 or mes == 5 or mes == 8 or mes == 7 or mes == 10 or mes == 12:
        dias = 31
    elif mes == 2:
        dias = 28
    else:
        dias = 30
    return(dias)


def problema_8(texto):
    texto_sin = texto.lower()

    vocales = ["a", "á","ä", "e", "é", "ë", "i", "í", "ï", "o", "ó", "ö", "u", "ú", "ü"]
    for n in vocales:
        texto_sin = texto_sin.replace(n, "")

    return(texto_sin)
