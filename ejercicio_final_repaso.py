"""
Obtención de los años bisiestos 
"""

def es_bisiesto(año):
    """Calcular año bisiesto

    Args:
        año (int): el año a calcular

    Returns:
        str: Indicaciones de si es o no bisiesto.
    """
    bisiesto = False
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                bisiesto = True
        else:
            bisiesto = True
    else:
        bisiesto = False
    
    bisiesto_str = "año no bisiesto"
    if bisiesto:
        bisiesto_str = "año bisiesto"

    return bisiesto_str


dict_años = {"año bisiesto": [],
             "año no bisiesto": []}

for año in range(0, 2025):
    biesto_key = es_bisiesto(año)
    dict_años[biesto_key].append(año)

print("Años pares bisiestos:")

for año_bisiesto in dict_años["año bisiesto"]:
    if año_bisiesto % 2 == 0:
        print(año_bisiesto, end=", ")

print("\n\nAños pares no bisiestos:")

for año_no_bisiesto in dict_años["año no bisiesto"]:
    if año_no_bisiesto % 2 == 0:
        print(año_no_bisiesto, end=", ")

print()

total_bisiestos = len(dict_años["año bisiesto"])
total_no_bisiestos = len(dict_años["año no bisiesto"])
proporcion = total_bisiestos / total_no_bisiestos

print("\n\nProporción de años bisiestos sobre no bisiestos:")
print(f"{total_bisiestos}/{total_no_bisiestos}={round(proporcion, 2)}")
