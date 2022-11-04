def leggi_file():
    file = open("./matematici.csv", "r")  
    righe = file.readlines()
    file.close()

    diz = {"id":[], "nome":[]} 

    for riga in righe[1:]:
        campi_riga = riga[:-1].split(",")
        diz["id"].append(int(campi_riga[0]))
        diz["nome"].append(campi_riga[1][1:]) #toglie lo spazio prima della parola 
    return diz

def nomeId(id,diz):
    lista_id = diz["id"]
    lista_nomi = diz["nome"]
    for i, n in zip(lista_id, lista_nomi): # i è l'id , n è il nome
        if i == id:
            return n

def main():
    diz = leggi_file()
    id = 2
    nome = nomeId(id, diz)
    print(nome)

if __name__ == "__main__":
    main()