from operator import length_hint


nome = input(f"Inserisci un nome: ")
print(nome[0]+"*"*(len(nome)-1))