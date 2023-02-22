
def Leggi_file(nome_file):
    """La funzione legge i file"""

    file = open(nome_file, "r")

    lista_righe = file.readlines()
    
    l=list(range(len(lista_righe)))

    file.close()
    for k, riga in enumerate(lista_righe):
        #per stampare riga per riga senza andare a capo 2 volte
        if (k+1)!=len(lista_righe):
            riga_senza_linefeed = riga[:-1]
        else: riga_senza_linefeed = riga
        lista_campi = riga_senza_linefeed.split(",")
        l[k]=lista_campi

    return l

def MappaNumerata(l):
    l1=[]
    k=0
    for riga in l:
        l2=[]
        #print(riga)
        for cella in riga:
            if cella=='0':
                l2.append(k)
                k+=1
            else: l2.append(-1)
        l1.append(l2)
    return l1

def MatriceAdiacente(l1):
    matrice=[]
    for n, riga in enumerate(l1):
        for k, el in enumerate(riga):
            if el!=-1:
                l=[]
                #destra
                if k!=(len(riga)-1) and riga[k+1]!=-1:
                    l.append(riga[k+1])
                    #print(l)
                #sinistra 
                if k!=0 and riga[k-1]!=-1:
                    l.append(riga[k-1])
                #sopra 
                if n!=0 and l1[n-1][k]!=-1:
                    l.append(l1[n-1][k])
                #sotto
                if n!=(len(riga)-1) and l1[n+1][k]!=-1:
                    l.append(l1[n+1][k])
                matrice.append(l)
    return matrice

"""
def PrintMatriceAdiacente(mat):
    matAd=[]
    c=False
    for el1 in mat:
        l=[]
        for k in range(len(mat)):
            c=False
            for j in range(len(el1)):
                if k==el1[j]:
                    l.append(1)
                    c=True
            if c==False:
                l.append(0)
        matAd.append(l)
    #print(matAd)
    
    for k in matAd:
        print(k)
"""               

        
            
def main():
   l = Leggi_file("dati.csv")
   print("l")
   print(l) 
   l1= MappaNumerata(l)
   print("l1")
   print(l1)
   print("matrice di adiacenza:")
   mat = MatriceAdiacente(l1)
   print(mat)

if __name__ =="__main__":
    main()