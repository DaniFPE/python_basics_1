"""
Control de flujo (I): https://docs.python.org/es/3/tutorial/controlflow.html
     
4. Más herramientas para control de flujo
    4.1. La sentencia if
    4.2. La sentencia for
    4.3. La función range()
    4.4. Las sentencias break, continue, y else en bucles
    4.5. La sentencia pass
"""
# ------- IF, ELIF, ELSE -----------
# Uno de los elementos fundamenetales para el control del flujo
# es la sentencia IF y los elementos ELIF y ELSE que podemos usar con ella.
# Para usar una sentencia IF normalmenete necesitamos evaluar una condición.
# P. ej:
condicion = 10 > 5
print(condicion)
print("------------\n")

if condicion:
    print("Se cumple la condicción!!")
    
print("------------\n")

# If simplemente actua como una especie de llave,
# si lo que hay después de if es verdadero la llave
# se abre y el código anidado bajo el if se ejecuta.
if True:
    print("Este codigo siempre se ejecuta")

if 10>5: 
    print("Este codigo siempre se ejecuta")

if 10 == 10:
    print("Este codigo siempre se ejecuta")

print("------------\n")

# Las condicones ganan mayor relevancia cuando hay una variable en juego:
a = 5
if a > 10:
    print("Yo solo me ejecuto si a > 10")

a = 11
if a > 10:
    print("Yo solo me ejecuto si a > 10")

print("------------\n")

# Para ganas mayor flexibilidad podemos añadir un ELSE. El ELSE se ejecuta
# cuando la condición del if no es cierta.

if False:
    print("Esto jamas se ejecutará (IF)")
else:
    print("Esto siempre se ejecuta (ELSE)")

print("------------\n")

# La otra sentencia que puede entrar en juego es ELIF. Esta sentencia permite
# evaluar condiciones extra en caso de que la condición anterior no se haya cumplido.
if False:
    print("Esto jamas se ejecutará")
elif True:
    print("Esto siempre se ejecuta (ELIF)")
else:
    print("Esto jamas se ejecutará")

print("------------\n")

# En una estructura condicional como la anterior SIEMPRE hay una unica sección de código
# que se ejecuta. Si una de las condiciones de la estrutura se cumple las demás ya no se evaluan.
# Ejemplo:
if True:
    print("Condicion (1)")
elif True:
    print("Condicion (2)")
elif True:
    print("Condicion (3)")
else:
    print("Condicion (4)")
    
print("------------\n")

if False:
    print("Condicion (1)")
elif True:
    print("Condicion (2)")
elif True:
    print("Condicion (3)")
else:
    print("Condicion (4)")

print("------------\n")

# Por ello los condicionales IF y ELIF solo son útiles cuando queremos evaluar una serie de
# condicciones que seon excluyentes entre si (si tenemos un escenario no tenemos el otro).

# En caso de querer evaluar siempre todas las condiciones usaremos IF (en combinación con ELSE).
if True:
    print("Condicion (1)")

if True:
    print("Condicion (2)")

if True:
    print("Condicion (3)")
else:
    print("Condicion (4)")

print("------------\n")

# Darse cuenta que al no poner ELIF ahora tenemos tres estruturas independientes en lugar de una
# única estrutura condicional más compleja.

# Finalmente las propias condiciones que se emplean en los IF pueden volverse más complejas
# mediante el uso de los operaodres and (&), or (|) y los paréntesis.
# Ejemplos:
condicion = 10 > 5 and False 
print(condicion)
print("------------\n")

condicion = 10 > 5 or False
print(condicion)
print("------------\n")

condicion = (5 < 1 and True) 
print(condicion)
print("------------\n")

condicion = (10 > 5 or False) or (5 < 1 and True) 
print(condicion)
print("------------\n")

# ------- BUCLES FOR -----------
# La sentencia FOR de Python itera sobre los ítems de cualquier secuencia (una lista o una cadena 
# de texto), en el orden que aparecen en la secuencia. Es por ello diferente a los bucles FOR de
# otros lenguajes como C. 

# Por ejemplo:
secuencia1 = "abcdefgh"
secuencia2 = [1,2,3,4,5]
secuencia3 = range(0,10)

for item in secuencia1:
    print(item)

print("------------\n")


for item in secuencia2:
    print(item)

print("------------\n")


for item in secuencia3:
    print(item)

print("------------\n")

# Más ejemplos de uso:
words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

print("------------\n")

# Los bucles for en Python permiten recorer secuencias compuestas de secuencias.
secuencia4 = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6],[7, 8, 9], [8, 9, 0]]

for i, j, k in secuencia4:
    print(i, j, k)

# Por supuesto los bucles se pueden anidar.
for i in range(0,10):
    for j in range(0, 10):
        print(i*j, end="\t")
    print()
    
print("------------\n")

# Si tenemos dos listas que queremos recorrer de manera simultanea
# lo más sencillo es usar la función zip que agrega ambos iterables
# y devuelve cuando se itera una tupla con los elementos agregados.
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

for tupla in zip(lista1, lista2):
    print(tupla)
    
print("------------\n")

# Como zip devuleve una tupla al iterar se puede directameneta asignar varios valores
# mientras iteramos el elemento.
for num, letra in zip(lista1, lista2):
    print(num, letra)
    
print("------------\n")

# A veces queremos iterar una secuencia (una lista, un dict, ...) y a la vez modificarlo.
# En algunos lenguajes esto no esta permitido y aunque lo este puede llevar a resultados
# inesperados como saltarnos elementos. Ejemplo:
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in lista1:
    print(num)
    del lista1[0]
print(lista1)
print("------------\n")

# Una estyrategia puede ser iterar sobre una copia:
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in lista1.copy():
    print(num)
    del lista1[0]
print(lista1)
print("------------\n")

# En ocasiones si lo que queremos es modificar valores puede ser más útil
# directamente crear una secuencia vacia y como ya hemos visto en otras ocasiones recorrerla.

# La función ENUMERATE. A veces iteramos una secuencia y necesitamos no solo el elemento de la
# secuncia si no su indice (su posición) en la propia secuencia. Para ello esta esta función.

# Sin enumerate:
lista2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

for n, letra in zip(range(len(lista2)), lista2):
    print(n, letra)
print("------------\n")

# Con enumerate
lista2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

for n, letra in enumerate(lista2):
    print(n, letra)
print("------------\n")

# Por último porque no usar range para crear directamenete una lista de numeros?
lista_rango = range(0, 10)

print(lista_rango)
print(type(lista_rango))
print("------------\n")

# El objeto retornado por range() se comporta de muchas maneras como si fuera una lista, 
# pero no lo es. Es un objeto que retorna los ítems sucesivos de la secuencia deseada cuando 
# iteras sobre él, pero realmente no construye la lista, ahorrando entonces espacio.
# Podemos hacer un cast de range a una lista.
lista_rango = list(range(0, 10))

print(lista_rango)
print(type(lista_rango))
print("------------\n")


# Decimos que tal objeto es iterable; esto es, que se puede usar en funciones y construcciones 
# que esperan algo de lo cual obtener ítems sucesivos hasta que se termine. Hemos visto que la declaración 
# for es una de esas construcciones, mientras que un ejemplo de función que toma un iterable es 
# la función sum().
lista_rango = list(range(0, 10))

print("Suma del rango:", sum(lista_rango))
print("------------\n")

# --------- BREAK, CONTINUE, y ELSE en bucles --------------
# Para dotar de mayor felxibilidad a los bucles existen algunas sentencias que nos permiten salir del 
# bucle (BREAK), continuar en la siguiente iteración (CONTINUE) y ELSE que permite ejecutar un último 
# trozo de código cuando acaba el bucle.

# Salir o romper el bucle
for n in range(1, 20):
    # Rompemos el bucle si encontramos un multiplo de 3
    if n % 3 == 0:
        break
    print(n)

print("------------\n")

# Continuar en la siguiente iteracción.
for n in range(1, 20):
    # Si no es multiplo de 3 continuamos en la siguiente vuelta
    if n % 3 != 0:
        continue
    print(n)

print("------------\n")

# A veces es interesante poder ejecutar una última linea de código. Por ejemplo este
# caso de cálculo de números primos. Fíjate bien: el else pertenece al ciclo for, no al if.)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

print("------------\n")

# Para entender mejor esto podemos verlo de la siguiente forma. Cuando se usa con un bucle, 
# la cláusula else tiene más en común con el else de una sentencia try que con el de un if. 
# En una sentencia try la cláusula else se ejecuta cuando no se genera ninguna excepción, 
# y el else de un bucle se ejecuta cuando no hay ningún break. 

# ------- La sentencia PASS ------
# La sentencia pass no hace nada. Se puede usar cuando una sentencia es requerida por la 
# sintaxis pero el programa no requiere ninguna acción. Esto puede ser útil para definir 
# estructuras o funciones a modo de plantilla antes de implementarlas. Ejemplos:

for n in range(10):
    pass

print("------------\n")

def plantilla_funcion(argumento1, argumento2):
    """Esto es una plantilla de función.

    Args:
        argumento1 (None): Este es el primer argumento.
        argumento2 (None): Este es el segundo argumento.
    """
    pass

print("------------\n")

# Se usa normalmente para crear clases en su mínima expresión.
class MiClaseVacia:
    pass

MiInstanciaVacia = MiClaseVacia()
print(MiInstanciaVacia)


for n in range(1, 20):
    for m in range(1, 20):
        print(m, end=" ")
        if m == n:
            break
    print()
        
        