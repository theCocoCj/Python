def leggi_file(nome_file):
    file = open(nome_file, "r")  
    lista_righe = file.readlines()
    file.close()

    diz_matematici = {"id":[], "nomi":[]} 

    for riga in lista_righe[1:]: 
        riga_senza_a_capo = riga[:-1]
        lista_campi = riga_senza_a_capo.split(",")
        id = int(lista_campi[0])
        nome = lista_campi[1]
        diz_matematici["id"].append(id)
        diz_matematici["nomi"].append(nome[1:])

    return diz_matematici

def leggiFile2(nome_file):
    file = open(nome_file, "r")  
    lista_righe = file.readlines()
    file.close()
    
    diz_matematici = {"id":[], "nomi":[]}

    

print("stampa attraverso la funzione")
diz = leggi_file("./matematici.csv")
print(diz)
print("")

idRic = input("Inserisci l'id da ricercare: ")

for k,v in diz.items(): #k chiave v valore
    if(k == idRic):
        print(v)

        

print("")
print("stampa senza funzione")

def main():

    file = open("./matematici.csv", "r")    #./ rimane nella cartella corrente
    lista_righe = file.readlines()  #ritorna la lista cone le righe, linea per linea
    #print(lista_righe)  #stampa lista di stringhe
    file.close()

    diz_matematici = {"id":[], "nomi":[]} #id sono numeri, nomi sono str
    #print(diz_matematici)

    #for riga in lista_righe[1:]: #[1:] stampa tutto tranne la prima riga
    #print(riga[:-1]) #[:-1]stampa tutto tranne l'ultima riga che è uno spazio

    for riga in lista_righe[1:]: 
        riga_senza_a_capo = riga[:-1]
        lista_campi = riga_senza_a_capo.split(",")#chiamata per ogni riga
        #print(lista_campi)#stampa 3 liste composte da due liste
        #print(lista_campi[0])#stampa solo il numero
        id = int(lista_campi[0])
        nome = lista_campi[1]
        #print(id, nome)
        diz_matematici["id"].append(id)
        diz_matematici["nomi"].append(nome[1:])
        print(diz_matematici)
        print("")


if __name__ == "__main__":
    main()





