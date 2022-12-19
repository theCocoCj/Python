"""
-->non esistono metodi pubblici e privati, tutto è pubblico
-->anche un metodo che non ha parametri deve avere self tra i parametri
"""

class IPadress():
    def __init__(self, ip_stringa):#ip_stringa ip scritto come su carta
        self.ip_notazione_dec = ip_stringa #il self corrisponde al this.ip_notazione_dec
        self.ip_notazione_bin = None
        self.ip_binario = None #IP senza punti

    #subnet mask data come /n
    def ipBroadcast(self,subnetMask="/24"):
        pass

    def dec2bin(self):
        lista_stringhe = self.ip_notazione_dec.split(".")
        lista_gruppi = self.tolist()
        s = ""
        s1 = ""
        for gruppo in lista_gruppi:
            temp = bin(gruppo)[2:] #da il valore in binario
            temp = "0"*(8-len(temp))+temp#aggiunge gli 0 mancanti
            s += temp + "."
            s1 += temp
        self.ip_notazione_bin = s[:-1]
        self.ip_binario = s1

    def bin2dec(self):
        lista_stringhe = self.ip_notazione_bin.split(".")
        print(lista_stringhe)
        lista_gruppi = self.tolist()
        str(lista_gruppi)
        print(lista_gruppi)
        s = ""

        for gruppo in lista_gruppi:
            s = lista_gruppi[gruppo] + "."
        print(s[:-1])


    def tolist(self):
        lista_stringhe = self.ip_notazione_dec.split(".")#si ottiene una lista di stringhe
        return [int(gruppo) for gruppo in lista_stringhe]

        
def main():
    indirizzoIP = IPadress("102.168.0.123") #istanza di una classe
    print(indirizzoIP.ip_notazione_dec)
    print(indirizzoIP.tolist())#stampa la lista di stringhe
    indirizzoIP.dec2bin()
    print(indirizzoIP.ip_notazione_bin)
    print(indirizzoIP.ip_binario)
    indirizzoIP.bin2dec()
    

if __name__ == "__main__":
    main()
