def leggi_file(nome_file):
    file = open(nome_file, "r")  
    lista_righe = file.readlines()
    file.close()

    diz_Alunni = {"data":[], "nome":[], "totale":[]} 

    for riga in lista_righe[1:]: 
        riga_senza_a_capo = riga[:-1]
        lista_campi = riga_senza_a_capo.split(";")
        data = lista_campi[0]
        nome = lista_campi[1]
        totale = int(lista_campi[2])

        diz_Alunni["data"].append(data)
        diz_Alunni["nome"].append(nome)
        diz_Alunni["totale"].append(totale)

    print(diz_Alunni)
    return diz_Alunni

diz = leggi_file("4AROB_GITA.csv")

def printIncassi(diz):

    

    return diz



printIncassi(diz)

#cercaNome(diz)

print(diz)