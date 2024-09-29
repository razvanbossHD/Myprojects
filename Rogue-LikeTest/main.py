import pygame
import stabilire
import afisare
import calcule
import rng

screen = pygame.display.set_mode((700, 700), pygame.RESIZABLE)
width = screen.get_width()
height = screen.get_height()
pygame.init()

clock = pygame.time.Clock()

class inst():
    def __init__(self, distmin, score, enemynr, enemymax, lock, gameover, radius, diff):
        self.distmin = distmin
        self.score = score
        self.enemynr = enemynr
        self.enemymax = enemymax
        self.lock = lock
        self.gameover = gameover
        self.radius = radius
        self.diff = diff
    
initial= [inst(100, 0, 10, 50, 0, 0, 25, 2.5)]    

class car():
    def __init__(self, x, y, speed, status, radius, colour):
        self.x = x
        self.y = y
        self.speed = speed
        self.status = status
        self.radius = radius
        self.colour = colour
    
charac=[car(700/2, 700/2, 1, 1, 30, (0, 255, 0))]

class enemy():
    def __init__(self, x, y, speed, status, colour, distance, lock):
        self.x = x
        self.y = y
        self.speed = speed
        self.status = status
        self.colour = colour
        self.distance = distance
        self.lock = lock

enem=[]

def main():
    FPS= 60
    nr= [0, 0, 0]
    width = screen.get_width()
    height = screen.get_height()
    stabilire.start(initial, enem, width, height)
    while True:
        width = screen.get_width()
        height = screen.get_height()

        calcule.calcule1(initial, charac, enem, width, height, nr)
        rng.ran(initial, enem, width, height)
        clock.tick(FPS)
        afisare.dis(screen, charac, enem, initial, width, height)

        if initial[0].gameover == 1:
            return 1

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                initial[0].lock = False

        nr[0] += 1
        if nr[0] >= 60:
            nr[1] += 1
            nr[0]= nr[0] % 60
        if nr[1] >= 60:
            nr[2] += 1
            nr[1]= nr[1] % 60

if __name__ == '__main__':
    for i in range(5):
        main()