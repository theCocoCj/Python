import queue
import pygame
import random
import time
import serial
import threading

#schermo
width = 500
height = 500

#righe e colonne
COLS = 25
ROWS = 20

#coda con i valori
q = queue.Queue()

class Read_Microbit(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._running = True
      
    def terminate(self):
        self._running = False
        
    def run(self):
        #serial config
        port = "COM10"
        s = serial.Serial(port)
        s.baudrate = 115200
        while self._running:
            data = s.readline().decode() 
            acc = [float(x) for x in data[1:-3].split(",")]
            q.put(acc)
            print(acc)
            time.sleep(0.01)
            
class cube():
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start #posizione di start
        self.dirnx = dirnx #direzione asse x
        self.dirny = dirny #direzione asse y
        self.color = color #colore cubo

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    #funzione per disegnare il cubo nella direzione specificata
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows #disegna n cubi in base alla grandezza della finestra
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        #se è il primo cubo
        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)
            
            
class snake():
    body = [] #lista dei cubi del serpente
    turns = {} #lista delle posizioni dei cubi del serpente

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        acc = q.get()
        #in base ai valori ottenuti dall'accelerometro
        if abs(acc[0]) > abs(acc[1]):
            if acc[0] > 0:
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] #punto in cui il serpente gira
            else:
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        else:
            if acc[1] > 0:
                    self.dirny = -1
                    self.dirnx = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            else:
                    self.dirny = 1
                    self.dirnx = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        q.task_done()

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
        #in base alla direzione del serpente aggiunge un cubo
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

#ridisegna la finestra 
def redrawWindow():
    global win
    win.fill((0, 0, 0))
    drawGrid(width, ROWS, win)
    s.draw(win)
    snack.draw(win)
    pygame.display.update()
    

#disegna griglia
def drawGrid(w, ROWS, surface):
    sizeBtwn = w // ROWS #in base alla larghezza della finestra e alle righe selezionate disegna la griglia

    x = 0
    y = 0
    for _ in range(ROWS):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

#disegna frutto
def randomSnack(ROWS, item):
    positions = item.body

    while True:
        x = random.randrange(1, ROWS - 1) #posizione x frutto
        y = random.randrange(1, ROWS - 1) #posizione y frutto
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0: #funzione che restituisce una booleana
            continue
        else:
            break

    return (x, y)

 
def main():
    
    pygame.init()
    global s, snack, win
    win = pygame.display.set_mode((width, height))
    s = snake((0, 250, 0), (10, 10)) #creazione del serpente
    s.addCube()
    snack = cube(randomSnack(ROWS, s), color=(250, 250, 0))
    clock = pygame.time.Clock()
    running = True           
    rm = Read_Microbit()
    rm.start()
    while running:
        pygame.time.delay(50)
        clock.tick(5)
        s.move()
        headPos = s.head.pos #posizione primo cubo del serpente
        if headPos[0] >= ROWS or headPos[0] < 0 or headPos[1] >= ROWS or headPos[1] < 0: #se la testa del serpente esce...
            print("Score:", len(s.body))
            x = random.randrange(1, ROWS - 1)
            y = random.randrange(1, ROWS - 1)
            s.reset((x, y))
            rm.join()
            del s


        #se la testa del serpente prende un frutto...
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(ROWS, s), color=(0, 255, 0))

        
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print("Score:", len(s.body))
                x = random.randrange(1, ROWS - 1)
                y = random.randrange(1, ROWS - 1)
                s.reset((x, y))
                rm.join()
                del s

        redrawWindow()

main()
    