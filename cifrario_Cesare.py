dizionario = {'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'l','l':'m','m':'n','n':'o','o':'p','p':'q','q':'r',
'r':'s','s':'t','t':'u','u':'v','v':'z','z':'a'}
parola = input('Inserisci la parola: ')

NuovaStr=""

for i in parola:
    NuovaStr+=dizionario[i]
print(NuovaStr)

decodificatore={} #dizionario vuoto
for k, v in dizionario.items(): #ciclo for che lavora simultaneamente su piu' variabili
   #print(k,v) stampa tutto il dizionario con chiave e argomento 
 decodificatore[v]=k

NuovaStr2=""
for lettera in NuovaStr:
    NuovaStr2=NuovaStr2+decodificatore[lettera]
print(NuovaStr2)

