lista= ["a", "b", "c", "d"]
lista1= [1, 2, 3, 4]

# for su lista1 c.style
print("CStyle")
for i in range(0, len(lista1)):
    print(lista1[i])

# for su lista1 python.style
print("PythonStyle")
for k in lista1:
    print(k)

# for su lista1 enumerate
print("enumerate")
for indice, elemento in enumerate(lista1): #cicla sia sull'indice che sull'elemento
    print(elemento)

# for su lista1, lista2 python.style (zip)
print("zip")
for k, v in zip(lista, lista1):
    print(k, v)

# for su lista1, lista2 c.style (range)
print("range")
for k in range(0, len(lista)):
    print(lista[k], lista1[k])

diz={"a":1, "b":2, "c":3, "d":4}

# for su diz usando items()
print("Diz con items")
for k, v in diz.items():
    print(k, v)

# for su diz senza items
print("Diz senza items")
for k in diz:
    print(k,diz[k])
