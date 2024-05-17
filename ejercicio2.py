"""
1. Declara un diccionario vacío llamado diccionario.

2. Declara una variable llamada count e igualala a 0.

3. Crea un bucle for en un rango de 0 a 100 donde sea la variable n 
la que tome estos valores.

4. Dentro del bucle realiza las siguientes acciones:

    1. Declara una variable llamada key que debe tomar en cada iteración del bucle el 
    valor de tipo string: “key_n” (Es decir: “key_0”, “key_1”, “key_2”, …).

    2. Añade al diccionario en cada iteración del bucle el item: “key_n”: n 
    (Es decir: “key_0”: 0, “key_1”: 1, “key_2”: 2, …)

5. Una vez llenado el diccionario haz un print del valor asignado a “key_0” y a “key_99”.

6. Modifica el valor asignado a la clave “key_64” por 1000.

7. Haz un print del valor asignado a “key_64”.
"""
diccionario = dict()
count = 0

for n in range(0, 101):
    key = "key_" + n
    diccionario[key] = n

print(diccionario["key_0"])
print(diccionario["key_99"])

diccionario["key_64"] = 1000

print(diccionario["key_64"])

print(diccionario)
