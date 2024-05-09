"""
A continuación vamos a realizar una serie de ejercicios de cara a repasar algunos de los fundamentos de Python. Repasaremos las partes más importantes y sobre las que más hemos hecho hincapié. En concreto:
    • Declaración de variables y tipos.
    • Estructuras de datos 1:
        ◦ Listas.
        ◦ Diccionarios.
    • Estructuras de datos 2:
        ◦ Como indexar una lista.
            ▪ Como modificar un elemento indexado
        ◦ Como añadir un elemento a la lista.
        ◦ Como acceder a un valor de un diccionario por clave.
            ▪ Como modificar un valor del diccionario
        ◦ Como añadir elementos al diccionario.
"""

# Declaración de variables. Siempre con un = y separando por espacios para mayor calidad.
a = 0 # int
b = "0" # str
c = True # Bolean

print(a, "-", b, "-", c)
print("------------\n")

# O vacias usando los tipos.
a = int() # int
b = str() # str
c = bool() # Bolean

print(a, "-", b, "-", c)
print("------------\n")


# Conversión de variables. Se emplean los tipos simplemente
a = 0 # int
b = str(a) # str

print(type(a))
print(type(b))
print("------------\n")


# Estructuras de datos 1: Listas.
lista = [] # lista vacia

print(type(lista))
print("------------\n")

lista = ["1", 1, 3, True] # las listas admiten elemntos de distintos tipos

print(lista)
print("------------\n")

# tambien podemos usar el tipo
lista = list() # lista vacia

print(type(lista))
print("------------\n")

# Estructuras de datos 1: diccionarios.
dict_ = {} # Diccionario vacio
print(type(dict_))
# Truco: cuando queremos usar una variable y es variable de Python,
# por ejemplo dict o len o list, podemos usarla poniendo siempre un _ detrás para diferenciarla

# Los diccionarios estan compuestos de pares de clave y valor (key and value).
dict_ = {"key": "value"}
print(dict_)
print("------------\n")

# Los diccionarios aceptan distintos tipos de variables para clave y valor (key and value)
dict_ = {1:0, "key": "value", "key": 1, "clave": "valor"}
print(dict_)
print("------------\n")

# Estructuras de datos 2: Como indexar una lista.
#   ▪ Como modificar un elemento indexado
#         ◦ Como añadir un elemento a la lista.

# Indexamos listas usando [] y un entero que es el valor del elemento
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista[0])
print("------------\n")

# Si nos pasamos de largo indexando da error:
# print(lista[100])

# También da error si la lista esta vacía
# lista = []
# print(lista[0])

# Podemos indexar más de un elemento así
print(lista[0:4])
print("------------\n")

# El último elemento siempre se puede obtener asi
print(lista[-1])
print("------------\n")

# Tambien podemos decirle que salte elementos o vaya hacía atrás
print(lista[0:6:2])
print("------------\n")

print(lista[4::-2])
print("------------\n")

# Podemos omitir el final si no ponemos nada
print(lista[4:])
print("------------\n")

# Por supuesto todas estas listas indexadas pueden ser asignadas a una variable
a = lista[4:]
print(a)
print("------------\n")

# Podemos modificar un elemento de la lista de la manera siguiente
lista[0] = 10000
print(lista)
print("------------\n")

# Modifica ahora un valor de a y comprueba la lista original para ver si ha cambiado
# Si no ha cambiado quiere decir que es una copia y no una referencia (como un enlace).
a = lista[4:]
print(a)
a[0] = "Modificado"
print(a)
print(lista)
print("------------\n")

# Finalmente las listas tienen dos métodos o funciones fundamentales:
# Longitud
print(len(lista))
print("------------\n")

# Añadir elemento (siempre al final)
lista.append("ultimo elemento")
print(lista)
print("------------\n")


# Estructuras de datos 2: Como acceder a un valor de un diccionario por clave.
#   ▪ Como modificar un valor del diccionario
#         ◦ Como añadir elementos al diccionario.

# Los diccionarios son estructuras más complejas pero tremendamente útiles
# Para recupperar un valor del diccionario siempre debemos proporcionar su clave

# Al igual que las listas se indexa con []. 
# Por eso es importante ser explicito en el nombre para que no dar lugar a errores.
dict_ = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}

# En principio solo podemos recuperar valores del diccionario de uno en uno.
print(dict_["key1"])
print("------------\n")

# Para modificar un valor de un diccionario simplemenete indexamos por clave
dict_["key1"] = "elemento modificado"
print(dict_)

# Para añadir elementos nuevos simplemente indexamos una clave que no exista y le damos un valor
dict_["key5"] = "elemento nuevo"
print(dict_)
print("------------\n")

dict_["key100"] = "elemento nuevisimo"
print(dict_)
print("------------\n")

# De manera mu similar a las listas podemos asignar este valor a una variable
a = dict_["key1"]
print(a)
print("------------\n")

# Vamos a cambiar el valor de a y ver como afecta al dict_
a = "esto es una prueba de concepto"
print(a)
print(dict_)
print("------------\n")

# Como se puede ver, al igual que en las listas la asignación a una variable procude una copia
 