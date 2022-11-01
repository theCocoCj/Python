#tuple simili alle liste ma immutabili 
punto = (1.5, 3.6)
print(f"La cordinata x del punto è {punto[0]}")
triangolo = [(1.5, 3.6), (-1.0, 0.0), (5.1, 4.3)]
print(f"La coordinata y del secondo vertice è {triangolo[1][1]}")

#dizionari 

d={1:"Abello", 2:"Armando"} #composto da una chiave(numero) e da un valore(argomento, qualunque tipo)
d2={"Abello":[8, 9, 7, 10], "Armando":[10, 8, 9, 10]}
#esiste l'indicizzazione attraverso le chiavi
print(d[2])
print(d2["Abello"])#si stampa solo attraverso la chiave
