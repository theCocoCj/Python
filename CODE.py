import queue

coda = queue.Queue()#invocazione del costruttore
#enqueue viene chiamato -> put
#dequeue viene chiamato -> get

coda.put(3)
coda.put(5)
coda.put(19)
coda.put(23)

print(coda.get())
print(coda.get())
#la funzione list converte in lista
print(list(coda.queue)) #stampa tutta la coda
