#stampare tavola pitagorica e salvare i numeri su delle liste

def make_tabella_pitagorica():
    return[[numero * indice for numero in range(1, 11)] for indice in range(1, 11)]

def write_file(nomeFile, tabella_pitagorica):
    file = open(nomeFile, "w")
    for riga in tabella_pitagorica:
        file.write(f"{riga}\n")
    file.close()

def main():
    tabella_pitagorica = make_tabella_pitagorica()
    write_file("tavola.txt", tabella_pitagorica)
    
if __name__ == "__main__":
    main()