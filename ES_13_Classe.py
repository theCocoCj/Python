KGMAX = 100

#classe robot con attributi e metodi
class Robot():
    def __init__(self, nome, massa, tipo):#ip_stringa ip scritto come su carta
        self.nomeRob = nome #stringa
        self.massaRob = massa #float
        self.tipologiaRob = tipo #stringa

    def stampaNome(self):
        print(self.nomeRob)

    def isDangerous(self):
        if(self.massaRob >= KGMAX and self.tipologiaRob == "umanoide"):
            return True
        else:
            return False

    def stampaTipologia(self):
        if(self.isDangerous() == True):
            print(f"Il robot {self.nomeRob} è pericoloso")
        else:
            print(f"Il robot {self.nomeRob} non è pericoloso")
    
def main():
    newRobot = Robot("R2-D2", 89, "non umanoide")
    newRobot.stampaNome()
    newRobot.stampaTipologia()


if __name__ == "__main__":
    main()