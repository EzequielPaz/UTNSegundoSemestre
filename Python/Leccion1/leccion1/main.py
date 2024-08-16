nombres = ["Naty", "Osvaldo", "Lily", "Ariel"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])#podemos recorrer mediante el uso de negativos
print(nombres[0:2])
#Ir del inicio de la lista hasta el indice (sin incluir)
print(nombres[ :3])#Da por entendido el compilador que es del cero en adelante
print(nombres[1: ])
#Modificamos un valor dentro de la lista
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)
#Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

#Preguntamos cuantos elementos tiene una lista
print(len(nombres)) #Le pasamos como parametro la lista
#Agregamos un elemento a una lista
nombres.append("Marcelo")#al final de la lista
print(nombres)
#Insertamos un elemento en un indice especifico
nombres.insert(1,"Alberto")
print(nombres)
#Eliminamos un elemento
nombres.remove("Alberto")
print(nombres)
#Eliminar el ultimo elemento
nombres.pop()
print(nombres)
#Eliminar un indice especifico
del nombres[2]
print(nombres)
#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)
#Eliminar la lista
#del nombres

#Ejercicio1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
#Ejemplo de ejercucion: 0,3,6,9
print("Rango de 0 a 10 con numero divisibles por 3")
x = range(0,10,3)
for i in x:
    print(i)
#Ejercicio2: Crear un rango de numeros de 2 a 6 e impremelos
#Ejemplo de ejecucion: 2,3,4,5,6
print("Rango de 2 a 6")
y = range(2,7)
for i in y:
    print(i)
#Ejercicio3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
#Ejemplo de ejecucion: 3,5,7,9
print("Rango con valores de inicio=3, fin=10 y incremento=2")
z = range(3,10,2)
for i in z:
    print(i)

#Definimos una tupla
cocina = ("Cuchara", "Cuchillo", "Tenedor")
print(len(cocina))

#Acceder a un elemento, para esto utilizamos corchetos no parentesis
print(cocina[0])
#Mostrar de manera inversa
print(cocina[0:2])
#Acceder a un rango
print(cocina[0:2])

#Ejemplo
verduras = ("papa",)
#De lo contrario solo seria un tipo de str cadena

#Recorremos los elementos de una tupla
for cocinar in cocina: #Print esta usando \n pars saltos de lineas
    print(cocinar, end=" ") #Usamos end para eliminar los saltos de lineas

cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print("\n", cocina)

# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
#Crear una lista que solo incluya los numeros menores a 5
#e imprima por consola[1, 3, 2]

lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)