import pygame
import time
import random

WIDTH = 700
HEIGHT = 700
patratm = 50

ceas = pygame.time.Clock()
timp = time.time()
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def menu():
    FPS = 60
    x = WIDTH // 2 - 50
    y = HEIGHT // 2 + 75
    while True:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        bg()
        pygame.draw.rect(screen,(255, 255, 0),[WIDTH / 2 - 250, 200 - 50, 50, 40])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            mouse_presses = pygame.mouse.get_pressed()
        if x <= mouse[0] <= x+140 and y <= mouse[1] <= y+40:
            font = pygame.font.Font("freesansbold.ttf", 100)
            text = font.render('Start', False, (255, 0, 0))
            screen.blit(text,(x - 60, y))
            if mouse_presses[0]:
                return 1
        if (x <= mouse[0] <= x+140 and y <= mouse[1] <= y+40) == False:
            font = pygame.font.Font("freesansbold.ttf", 50)
            text = font.render('Start', False, (255, 0, 0))
            screen.blit(text,(x, y))

        pygame.display.update()

def lost(pipew, hcrnt, pipenr, size, pipeh, lock, pipehead, pipebody, score):
    screen.fill((0, 0, 0))
    bg()
    pygame.draw.rect(screen,(255, 255, 0),[WIDTH / 2 - 250, hcrnt - 50, 50, 40])
    for i in range(pipenr):
        pipew[i] -= 2
    desenpipe(pipenr, size, pipew, pipeh, lock, pipehead, pipebody)
    font = pygame.font.Font("freesansbold.ttf", 40)
    text = font.render('Scor:' + str(score), False, (255, 255, 255))
    screen.blit(text,(WIDTH / 2 - 100, HEIGHT / 2))
    pygame.display.update()
    time.sleep(2)

def bg():
    pygame.draw.rect(screen, (0, 255, 0), [0, HEIGHT - HEIGHT / 8, WIDTH, HEIGHT / 8])
    pygame.draw.rect(screen, (100, 100, 255), [0, 0, WIDTH, HEIGHT - HEIGHT / 8])
    nori (50, 100)
    nori (328, 200)
    nori (160, 320)
    nori (520 , 130)
    nori (604, 310)

def nori(w, h):
    pygame.draw.circle(screen, (255, 255, 255), [w, h], 20)
    pygame.draw.circle(screen, (255, 255, 255), [w + 23, h + 15], 20)
    pygame.draw.circle(screen, (255, 255, 255), [w - 23, h + 15], 20)
    pygame.draw.circle(screen, (255, 255, 255), [w, h + 15], 20)


def pipe(size, w, h, pipehead, pipebody, nr):
    L = (WIDTH / 23) * size
    l = (HEIGHT / 50) * size
    h2 = h + 250
    u = L / 5
    dif = HEIGHT - h2 - l - (HEIGHT / 8)
    pipehead[2 * nr] = pygame.draw.rect(screen,(0, 215, 0), [w, h, L, l])
    pipebody[2 * nr] = pygame.draw.rect(screen,(0, 230, 0), [w + u, 0, L - 2 * u, h])
    pipehead[2 * nr + 1] = pygame.draw.rect(screen,(0, 215, 0), [w, h2, L, l])
    pipebody[2 * nr + 1] = pygame.draw.rect(screen,(0, 230, 0), [w + u, h2 + l, L - 2 * u, dif])

def desenpipe(pipenr, size, pipew, pipeh, lock, pipehead, pipebody):
    for i in range(pipenr):
        if pipew[i] + (WIDTH / 23) * size < 0 :
            lock[i] = 1
            pipew[i] = WIDTH
            pipeh[i] = random.randint(100, 300)
        if pipew[i - 1] < WIDTH - 300:
            lock[i] = 0
        if i == 0 and pipew[pipenr - 1] < WIDTH - 300:
            lock[i] = 0
        if lock[i] == 0:
            pipew[i] -= 2
        pipe(size, pipew[i], pipeh[i], pipehead, pipebody, i)


def main():
    score = 0
    viteza = 0
    vitezamaxima = 10
    hcrnt = HEIGHT / 2
    start = 0
    pipenr = 4
    pipew = []
    pipeh = []
    size = 3
    lock = []
    scor = 0
    pipehead = []
    pipebody = []
    font = pygame.font.Font("freesansbold.ttf", 20)


    for i in range(pipenr):
        pipew.append(WIDTH)
        pipeh.append(random.randint(100, 300))
        pipehead.append(0)
        pipehead.append(0)
        pipebody.append(0)
        pipebody.append(0)
        lock.append(1)

    while True:
        clock.tick(60)
        screen.fill((0, 0, 0))
        bg()
        block = pygame.draw.rect(screen,(255, 255, 0),[WIDTH / 2 - 250, hcrnt - 50, 50, 40])
        desenpipe(pipenr, size, pipew, pipeh, lock, pipehead, pipebody)
        if hcrnt < (HEIGHT / 8)*7 and start == 1 or viteza > 0:
            hcrnt -= viteza
            viteza -= 1
        if hcrnt > (HEIGHT /8)*7:
            hcrnt = (HEIGHT /8)*7

        for i in range(pipenr):
            if  pipew[i] > WIDTH / 2 - 250 and pipew[i] <= WIDTH / 2 - 250 + 2:
                score += 1
            if block.colliderect(pipehead[2 * i]):
                lost(pipew, hcrnt, pipenr, size, pipeh, lock, pipehead, pipebody, score)
                return 1
            if block.colliderect(pipehead[2 * i + 1]):
                lost(pipew, hcrnt, pipenr, size, pipeh, lock, pipehead, pipebody, score)
                return 1
            elif block.colliderect(pipebody[2 * i + 1]):
                lost(pipew, hcrnt, pipenr, size, pipeh, lock, pipehead, pipebody, score)
                return 1
            elif block.colliderect(pipebody[2 * i + 1]):
                lost(pipew, hcrnt, pipenr, size, pipeh, lock, pipehead, pipebody, score)
                return 1

        text = font.render(("Scor:" + str(score)), False, (255, 255, 255))
        screen.blit(text, (0, 0))  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                viteza = vitezamaxima
                if start == 0:
                    lock[0] = 0
                start = 1
      
        
        pygame.display.update()
    

if __name__ == '__main__':
    menu()
    while True:
        main()

