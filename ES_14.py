class quadrato():
    def __init__(self, x, y, lato):
        self.x = x
        self.y = y
        self.lato = lato

    def perimetro(self):
        return (self.lato*4)

    def area(self):
        return (self.lato*self.lato)

    def isdentro(self, xp, yp):
        if(self.x < xp and self.x + self.lato >= xp and self.y <= yp and self.y+self.lato >= yp):
            print("interno")
        else:
            print("esterno")
        

def main():
    q = quadrato(11, 15, 5)
    print(q.area())
    print(q.perimetro())
    q.isdentro(20,30)

if __name__ == "__main__":
    main()

        
        
        