
vocali = ["a", "e", "i", "o", "u"]
stringa = input("inserisci la tua stringa: ")

caratteri = [car for car in stringa]

#funzione che verifica se è una vocale
def isVocale(car):
    for i in vocali:
        if car == i:
            return False
    return True


newStr=[car for car in caratteri if isVocale(car)]
print(newStr)
