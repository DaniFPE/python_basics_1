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

    