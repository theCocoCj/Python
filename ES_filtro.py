#definire una lista di nomi di matematici
l = ["Gauss", "Cornway", "Eulero", "Hilbent"]
#definire una lista con i nomi che iniziano solamente con una h o g

l_GH = [nome for nome in l if nome[0] == "G" or nome[0] == "H"]
print(l_GH)