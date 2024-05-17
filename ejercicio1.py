"""
1. Declara una lista vacía llamada lista.

2. Crea un bucle for en un rango de 0 a 100 donde sea la variable 
n la que tome estos valores.

3. Dentro del bucle emplea la función append para llenar esta lista 
con todos los valores que ha ido tomando la variable n.                                                                                                      

4. Haz un print del primer elemento de la lista.

5. Haz un print del ultimo elemento de la lista.

6. Haz un print de una porción de la lista del elemento 25 al 50. 
(Recuerda que las listas empiezan en 0 y no en 1).

7. Asigna a una variable llamada sublista los valores del print anterior.

8. Toma el primer elemento de esta sublista y cambia su valor por 1000.

9. Haz un print de lista.

10. Haz un print de sublista.

11. ¿Que a ocurrido con el primer elemento en ambos casos?
"""
lista = list()

for n in range(0, 100):
    lista.append(n)

print(lista[0])

print(lista[-1])

print(lista[25:51])

sublista = lista[25:51]

sublista[0] = 1000

print(lista)

print(sublista)


print("\n")
lista_2 = lista.copy()
print(lista_2)
lista_2[0] = 100000
print("\n")
print(lista)
