lista = [110, 12, 3, 5, 8]

#modo preferito (pythonico)
for elemento in lista:
    print(elemento)

#mode C-Style
for i in range (0, len(lista)):
    print(lista[i], end="-")
    print("")


massimo = lista[0]
minimo = lista[0]

for elemento in lista[1:]:
    if elemento > massimo: 
        massimo = elemento
    else:
        pass
    if elemento < minimo:
         minimo = elemento

print(f"Il minimo è {minimo}")
print(f"Il massimo è {massimo}")