"""
Control de flujo (II): https://docs.python.org/es/3/tutorial/controlflow.html
     
4. Más herramientas para control de flujo
    4.6. Definiendo funciones
    4.7. Más sobre definición de funciones

    4.7.1. Argumentos con valores por omisión
    4.7.2. Palabras claves como argumentos
    4.7.3. Parámetros especiales
        4.7.3.1. Argumentos posicionales o de palabras claves
        4.7.3.2. Parámetros únicamente posicionales
        4.7.3.3. Argumentos únicamente de palabras clave
        4.7.3.4. Ejemplos de Funciones
        4.7.3.5. Resumen
    4.7.4. Listas de argumentos arbitrarios
    4.7.5. Desempaquetando una lista de argumentos
    4.7.6. Expresiones lambda
    4.7.7. Cadenas de texto de documentación
    4.7.8. Anotación de funciones

    4.8. Intermezzo: Estilo de programación
"""
# ----------  Definiendo funciones ------------
# Ya hemos trabajado con funciones, en esta sección repasaremos los conceptos
# elementales e introduciremos algunos nuevos. Para definir funciones se emplea
# la palabra reservada DEF. Las funciones son uno de los elementos fundamentales
# de Python (y de casi cualquier lenguaje). Son tan importantes como las clases
# e incluso hay paradigmas de programación como la programación funcional que 
# directamente prescide de las clases y se enfoca en el uso de funciones.

# REPASO: De manera muy elemental hemos visto que las funciones pueden recibir un
# número arbitrario de argumentos y devolver de igual forma un número arbitario.

# EJEMPLO: Función con un argumento y que retorna dos argumentos:
def ejemplo_fun1(n):
    cuadrado_n = n ** 2
    return n, cuadrado_n

# EJEMPLO: función que toma dos argumentos y que retorna un argumento:
def ejemplo_fun2(n, potencia):
    potencia_n = n ** potencia
    return potencia_n

# De esta forma podemos definir el número de argumentos de entrada y salida
# que se quieran. Es importante señalar que esto es la definción, para invocar
# (para usar) la función debemos hacer lo siguiente:
n = 10
n, cuadrado_n = ejemplo_fun1(n)
print(n, cuadrado_n)

n = 7
potencia = 4
potencia_n = ejemplo_fun2(n, potencia)

print("------------\n")

# También es posible definir funciones sin argumentos y sin retorno.
def funcion_ejemplo3():
    print("Soy una funcion!")
    
funcion_ejemplo3()

print("------------\n")

# INFO: En otros lenguajes de programacióna a las funciones sin retorno 
# se las denomina Procedimientos.

# Ejemplo función sin RETURN.
# Declaramos la función (la creamos, la DEFinimos).
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Si queremos usarla basta con llamarla por su nombre, con parentesis y pasarle
# los parámetros adecuados.
n = 10
fib(n)

print("------------\n")

# Podriamos haberle pasado directamenete el argumento como 
# un valor en lugar de una variable
fib(10)

print("------------\n")

# Es IMPORTANTE recalcar que a las fuciones se las llama, se las usa, se las invoca
# siempre empleando parentesis. Si no usamos parentesis lo que hacemos es hacer una
# referencia a la función igual que podriamos hacer una referecnia a un valor o a
# una clase.
# Ejemplo:
f = fib
print(f)
print(f(10))

print("------------\n")

# La ejecución de una función introduce una nueva tabla de símbolos usada para las 
# variables locales de la función. Más precisamente, todas las asignaciones de 
# variables en la función almacenan el valor en la tabla de símbolos local; así mismo
# la referencia a variables primero mira la tabla de símbolos local, luego en la tabla
# de símbolos local de las funciones externas, luego la tabla de símbolos global, y 
# finalmente la tabla de nombres predefinidos. Así, a variables globales y a variables
# de funciones que engloban a una función no se les puede asignar directamente un valor
# dentro de una función (a menos que se las nombre en la sentencia global), aunque 
# si pueden ser referenciadas.

# Algunos ejemplos (DEBUG):

# Ejemplo de variable global y variable local de la función (no son la misma,
# son indepentientes).
variable = 100
print(variable)

def funcion1():
    variable = 10
    print(variable)

funcion1() # IMPORTANTE hasta que no se llama a la funcion no se crea el espacio de nombres local
print(variable)

print("------------\n")

# Ejemplo de acceso desde una función a una variable global
variable_global = "Soy global"
def funcion2():
    print(variable_global)

funcion2()

print("------------\n")

# Ejemplo de modificación de una variable global desde local
def funcion3():
    global variable_global
    print(variable_global)
    variable_global = "Soy global explicitamente en este entorno local."

funcion3()

print(variable_global)

print("------------\n")

# Con esto introducimos el concepto de SCOPE o ámbito. Este concepto es común 
# a distintos lenguajes de programación. El ámbito (scope) de una variable, 
# función o método es la región en la que estos existen o desde la cual se puede 
# acceder a ellos.

# Primero debemos entender que las variables en Python son locales por defecto. 
# Esto quiere decir que aquellas definidas y utilizadas en el bloque de código de 
# una función, sólo existen dentro de la misma, y no interfieren con otras variables 
# del resto del código. A su vez, aquellas existentes fuera de una función, no son 
# accesibles dentro de la misma. En caso de que sea conveniente o necesario, una variable 
# local puede convertirse en una global declarándola explícitamente como tal con la 
# sentencia «global».

# IMPORTANTE: Es muy común un caso como el siguiente.

def potencia_enteros(base, exponente):
    potencia = base ** exponente
    return potencia

base = 10
exponente = 3
potencia = potencia_enteros(base, exponente)

# Fijasrse que en este caso tenemos acceso a las variables globales en el entorno
# local de la función porque las hemos pasado como argumentos. De la misma forma
# el resultado (el retorno) es asignado a una variable global de igual nombre que
# la local de la función, pero no son lo mismo.

# Esta forma de programar es cómoda y comprensible pero no deja ver de manera explicita
# las diferencias en el scope global y local a la función. Es algo que en Python se hace
# a menudo y esta aceptado, pero es importante tener claro como y porque escribir el código
# de esta forma funciona y en que casos puede dar errores.

# Paa finalizar con el SCOPE o ambito vamos a hablar de lo que se conoce como "paso por
# valor" o "paso por referencia".


# -------- Paso por valor y por referencia -----------

# En muchos lenguajes de programación existen los conceptos de paso por valor y por 
# referencia que aplican a la hora de cómo trata una función a los parámetros que se 
# le pasan como entrada. Si usamos un parámetro pasado por valor, se creará una copia 
# local de la variable, lo que implica que cualquier modificación sobre la misma no tendrá 
# efecto sobre la original. Con una variable pasada como referencia, se actuará directamente 
# sobre la variable pasada, por lo que las modificaciones afectarán a la variable original.

# En Python las cosas son un poco distintas, y el comportamiento estará definido por el tipo 
# de variable con la que estamos tratando.

# Paso por valor: Se crea una copia local de la variable dentro de la función.
# Paso por referencia: Se maneja directamente la variable, los cambios realizados 
# dentro de la función le afectarán también fuera.

# Los tipos simples se pasan por valor: Enteros, flotantes, cadenas, lógicos...
# Los tipos compuestos se pasan por referencia: Listas, diccionarios, conjuntos...


# EJEMPLO, paso por valor:
def doblar_valor(numero):
    numero *= 2
    print(numero)

n = 10
doblar_valor(n)
print(n)

print("------------\n")

# EJEMPLO, paso por referencia:
def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2

ns = [10,50,100]
print(ns)

doblar_valores(ns)
print(ns)

print("------------\n")

# Si queremos que los tipos simples sean modificados devemos reasignar el valor
# a la salida que devuelve la función en el return. Es decir:
def doblar_valor(numero):
    numero *= 2
    print(numero)
    return numero

n = 10
n = doblar_valor(n)
print(n)

print("------------\n")

# Si lo que queremos es que un tipo compuesto no sea modificado lo más sencillo
# es pasar a una función una copia del mismo. Es decir:

def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2
    print(numeros)

ns = [10,50,100]
print(ns)

doblar_valores(ns.copy())
print(ns)

print("------------\n")

# TRUCO: Se puede crear también una copia de una lista haciendo un slice de la lista
# que comprenda la lista entera: lista_copia = lista[:]

# ----------- Más sobre definición de funciones -------------
# --------------- Argumentos nombrados ----------------
# En Python los argumentos de las funciones no solo tiene que ser pasados de manera posicional
# si no que se pueden especificar mediante un nombre (keywords). La sintaxis es:
def funcion_nombres(n_años, nombre="Pedro"):
    print(f"{nombre} tiene {n_años} años.")

funcion_nombres(10, nombre="Jeremias")

print("------------\n")

# En este caso la variable de accede por nombre y tiene Pedro como valor por defecto.
funcion_nombres(10)

print("------------\n")

# Aunque sean argumentos nombrados, pueden pasarse también por posición.
funcion_nombres(10, "Rigoberto")

print("------------\n")

# Lo bueno de este tipo de argumentos nombrados es que nos permite establecer valores
# por defecto lo que permite establecer que algunos argumentos sean opcionales.

# ---------- Los ASTERISCOS (* y **) -------------
# Esta sintaxis es propia de Python y permite aún mayor flexibilidad en la definición 
# de funciones. Con el uso de * podemos especificar que los argumentos a continuación
# son de número variable. De esta forma la función puede recibir un número variable de
# argumentos. Todos los argumentos se asignan en forma de tupla a ese argumento que
# tiene delante el *. Ejemplo:

def funcion_multiples_argumentos(*args):
    for item in args:
        print(item)

funcion_multiples_argumentos("a", "b", "c", "d", "e")
print("------------\n")

# Es uno de los casos de definción de funciones menos común pero no esta de más conocerlo
# porque puede haber ciertas situaciones en que sea útil. Basicamente esta sintaxis nos
# permite recibir argumentos multiples de manera posicional. La sintaxis ** permite recibir
# argumentos multiples por argumento nombrado (keywords). Al igual que antes los argumentos
# se almacenaban en una tupla, en este caso se almacenan en un diccionario.
# EJEMPLO:

def funcion_multiples_keywords(**kwargs):
    print(kwargs)
    print(type(kwargs))
    

funcion_multiples_keywords(key1=1, key2=2, nombre="Federico")
print("------------\n")

# -------------  Desempaquetando una lista de argumento ----------
# En los casos anteriores, los argumentos de entrada estaban de alguna forma empaquetados
# dentro de una tupla o de un diccionario y asigandos a un único valor. ¿Pero que ocurre si
# yo necsito el proceso contraio? La situación inversa ocurre cuando los argumentos ya están
# en una lista o tupla pero necesitan ser desempaquetados para llamar a una función que 
# requiere argumentos posicionales separados.

# EJEMPLO: Usamos la función range que necesita dos parametros inicio y fin.
inicio_fin = [0, 100]
rango = range(*inicio_fin)

print(rango)
print("------------\n")

# Lo mismo se puede hacer para una función de arguemntos nombrados usando un diccionario:
def funcion_keywords(nombre="Daniela", edad=22, sexo="F"):
    print(nombre)
    print(edad)
    print(sexo)

informacion_dict = {"nombre": "Manuel", "edad": 15, "sexo":"M"}
funcion_keywords(**informacion_dict)
print("------------\n")

# -------------- Funciones Lambda ------------
# Veremos a continuación un caso especial de uso de funciones muy
# relevante en lo que se conoce como programación funcional. Se trata
# de las funciones lambda que se emplean principalmente para definir una
# función anónima que se aplicará de manera reiterada sobre un conjunto
# de datos o una secuencia. Muy empleadas en la librería Panda.
# Puede emplearse también para crear una función que devuelva funciones.

# Sintaxis:
lambda x: x*2

# Ejemplo:
def generador_potencias(n):
    return lambda x: x**n

potencia_2 = generador_potencias(2)
print(type(potencia_2))

cuadrado = potencia_2(10)
print(cuadrado)

print("------------\n")

# Ejemplo, como argumento de un método o función
# Por ejemplo para indicarle a sort el criterio de ordenación.
pairs = [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
pairs.sort(key=lambda pair: pair[0])
print(pairs)

print("------------\n")


# ------------- RECURSIVIDAD Y FUNCIONES INTERNAS ---------------
# Lo visto hasta ahora no pone limites a la creación de funciones dentro de otras
# funciones o a que una función se llame a sí misma, este último fenómeno se conoce
# como recursividad y puede acarrear problemas cuando se crea un bucle infinito.

# EJEMPLO:
def super_funcion(base, exponente):
    print("Soy la función maestra.")
    def potencia():
        resultado = base ** exponente
        return resultado
    print("calculemos el resultado con mis funciones esclavas...")
    resultado = potencia()
    print(resultado)
        
super_funcion(2, 6)
print("------------\n")

# EJEMPLO RECURSIVIDAD:
def funcion_recursiva(a, b):
    c = a + b
    if c > 100:
        return c
    else:
        print(c)
        c = funcion_recursiva(b, c)

funcion_recursiva(1, 10)

# Algunas normas de estilo.
# ver el enlace en https://docs.python.org/es/3.8/tutorial/controlflow.html#intermezzo-coding-style
# para empezar a emplear algunas normas de estilo sencillas en Python


