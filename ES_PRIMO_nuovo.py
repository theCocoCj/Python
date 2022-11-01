def isPrimo(x): #verifica che il numero sia primo 
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
        
    return True

list = []

n=100
list = [i for i in range(2,n) if isPrimo(i)] #aggiunge alla lista i numeri primi se la condizione if e' vera

print(list)