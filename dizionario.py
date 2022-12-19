dizionario = {"w":"avanti", "a":"sinistra", "s":"indietro", "d":"destra", "i":"avanti", "j":"sinistra", "k":"indietro", "l":"destra"}

for chiave, valore in dizionario.items(): #stampa chiave e argomento del dizionario
    print(chiave, valore)

for chiave in dizionario: #stampa solo la chiave del dizionario
    print(chiave)

for chiave in dizionario: #stampa solo l'argomento del dizionario
    print(dizionario[chiave]) 

lista=[]   #serve per trovare le chiavi che hanno come argomento "avanti"
for chiave in dizionario:
    if dizionario[chiave] == "avanti":
        lista.append[chiave] #aggiunge alla lista la chiave che ha come argomento "avanti"
print(lista)

l = ["ciao", print,1,3.24]
print(l)

