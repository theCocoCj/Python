numero = int(input("Inserisci un numero: "))
div = 1
conta = 0
for i in range (0, len(numero)):
    if(numero//div==0):
        div=div+1
        conta=conta+1

if(conta==1):
    print("Il numero è primo")
else:
    print("Il numero non è primo")


cont = 0
for i in range(2, int(numero**0.5)+1):
    y = numero % 1
    if y == 0:
        cont +=1
    if cont == 0:
        print("Il numero è primo")
    else:
        print("Il numero non è primo")

def isPrimo(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
        else:
            return True


        