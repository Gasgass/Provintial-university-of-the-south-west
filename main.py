def problema_1(base,altura):
    #Data Analysis
    """redondeo los valores para que no se ingresen numeros extensos al calculo del area"""
    base = round(base, 2)
    altura = round(altura, 2)

    # Calculo del Area
    area = (base * altura) / 2
    """paso el area a un resultado absoluto para que me de un area positiva"""
    area = abs(area)
    area = round(area, 2)

    return(area)

def problema_2(lado):
    #Data Analysis
    """Redondeo el valor de la variable para simplificar el resultado"""
    lado = round(lado, 2)

    # Calculo del Area
    """Al igual que antes redondeo el resultado y lo paso a un valor positivo"""
    area = lado * lado
    area = abs(area)
    area = round(area, 2)

    return(area)

def problema_3(edad):
    # Ingreso de datos
    """A la variable mayor le otorgo un valor booleano"""
    mayor = True

    # Analisis de datos
    """Considero que no existe una persona mayor a 110 años ni menor a 0 años"""
    if edad >= 18 and edad <= 110:
        mayor = True
    elif edad < 18 or edad > 110:
        mayor = False

    return(mayor)

def problema_4(r,l):
    # Ingreso de datos
    """Redondeo y paso a su absoluto el valor del lado y del radio"""
    l = abs(l)
    l = round(l, 2)
    r = abs(r)
    r = round(r, 2)
    """Calculo el Diametro"""
    d = r * 2

    # Anañisis de datos
    """Determino con la relacion de los valores del diametro del circulo y el lado del cuadrado si entra o no uno dentro del otro """
    entra = True
    if d > l:
        entra = False
    elif d == l:
        entra = True
    elif d < l:
        entra = True
    else:
        pass

    return(entra)