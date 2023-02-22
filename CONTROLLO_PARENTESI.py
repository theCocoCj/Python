
s="{[3+(a+b)]+8]"
pila=[]
diz = {"(":")", "[":"]", "{":"}" }
for i,carattere in enumerate(s):
    if(carattere=='{' or carattere=='['or carattere=='('):
        pila.append(carattere)
    if(carattere=='}' or carattere==']'or carattere==')'):
        parentesi = pila.pop()
        if diz[parentesi]!=carattere:
            print(f"errore sulla parentesi {carattere} {i+1}")






