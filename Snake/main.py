import pygame
import sys
import random
import time

screen  = pygame.display.set_mode((700, 700), pygame.RESIZABLE)
width= screen.get_width()
height= screen.get_height()
ssize = [21]
cellh = height // ssize[0]
cellw = width // ssize[0]
clock = pygame.time.Clock()
color_alb = (255, 255, 255)
color_negru = (0, 0, 0)
color_verde = (0, 255, 0)
color_cap = ( 0, 150, 0)
bg = color_negru

pygame.init()

font = pygame.font.Font("freesansbold.ttf", 30)

def desen(color_coada, color_head, color_food):
    pygame.draw.rect( screen, color_coada, [cellw * 8, cellh * 5, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 8, cellh * 4, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 8, cellh * 6, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 9, cellh * 4, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 10, cellh * 4, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 11, cellh * 4, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 12, cellh * 4, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 13, cellh * 4, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 13, cellh * 5, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 13, cellh * 6, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 13, cellh * 7, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 13, cellh * 8, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 13, cellh * 9, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 13, cellh * 10, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 12, cellh * 10, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 11, cellh * 10, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 10, cellh * 10, cellw, cellh])
    pygame.draw.rect( screen, color_coada, [cellw * 10, cellh * 9, cellw, cellh])
    pygame.draw.rect( screen, color_head, [cellw * 10, cellh * 8, cellw, cellh])
    pygame.draw.circle( screen, color_food, [cellw * 10 + cellw //2, cellh * 7+ cellh //2 ], cellw - cellw // 1.5)

def menu():
    FPS = 60
    x = width // 2 - 50
    y = height // 2 + 75
    while True:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        screen.fill(bg)

        desen(color_verde, color_cap, color_alb)

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


def lost(coadah, coadaw, color_coada, cellw, cellh, color_head, color_food, foodw, foodh, headw, headh, bg, score, width, height, x, y):
    screen.fill((bg))
    for k in range(len(coadah)):
        pygame.draw.rect( screen, color_coada, [cellw * coadaw[k], cellh * coadah[k], cellw, cellh])
    pygame.draw.circle( screen, color_food, [cellw * foodw[0] + cellw //2, cellh * foodh[0]+ cellh //2 ], cellw - cellw // 1.5)
    pygame.draw.rect( screen, color_head, [cellw * headw, cellh * headh, cellw, cellh])
    font = pygame.font.Font("freesansbold.ttf", height // 15)
    text = font.render('Scor:' + str(score), False, (255, 0, 0))
    screen.blit(text,(x, y))
    pygame.display.update()
    time.sleep(2)

def rng(rezerva, coadah, coadaw, headw, headh, rezerva2, foodw, foodh):
    while rezerva == 0:
        rezerva2 = 0
        foodw[0] =random.randint(0, ssize[0]-1)
        foodh[0] = random.randint(0, ssize[0]-1)
        for k in range(len(coadah)):
           if foodw[0] == coadaw[k] and foodh[0] == coadah[k] or foodw[0] == headw and foodh[0] == headh:
                rezerva2 = 1
        if rezerva2 == 0:
            rezerva = 1

def text(score, x, y):
    text = font.render('Scor:' + str(score), False, (255, 0, 0))
    screen.blit(text, (x, y))

def main():
    FPS = 60
    WIDTH = 700
    HEIGHT = 700
    score = 0
    screen.fill((0, 0, 0))

    radius = 50

        #game stats
    viteza = 40
    rezerva = 0
    rezerva2 = 0
    food = 0
    foodw =[random.randint(0, ssize[0]-1)]
    foodh = [random.randint(0, ssize[0]-1)]
    reset = 0

        #snake
    w = 0
    h = 0
    dir= 0
    ct = 0
    lock= 0
    coadaw = []
    coadah = []
    headw = ssize[0]//2
    headh = ssize[0]//2
    coadac = 0
        #celule
    while True:

        width= screen.get_width()
        height= screen.get_height()
        cellh = height // ssize[0]
        cellw = width // ssize[0]

        clock.tick(FPS)

            #refresh
        if ct == 1:
            screen.fill((0, 0, 0))

        #sarpele mananca
        if headw == foodw[0] and headh == foodh[0]:
            food = 1 
            score += 1
            reset = 1
            screen.fill((0, 0, 0))

        #se pune mancare intr-un punct random

        if food == 1 and reset == 1:
            rng(rezerva, coadah, coadaw, headw, headh, rezerva2, foodw, foodh)
            rezerva = 0
            rezerva2 = 0
            reset = 2
            #tot ce se deseneaza
        for k in range(len(coadah)):
            if ct == 1 and food == 0 or k != len(coadah)-1:
                pygame.draw.rect( screen, color_verde, [cellw * coadaw[k], cellh * coadah[k], cellw, cellh])
                if headw == coadaw[k] and headh == coadah[k] and k != 0:
                    lost(coadah, coadaw, color_verde, cellw, cellh, color_cap, color_alb, foodw, foodh, headw, headh, (0, 0, 0), score, width, height, (width // 2) - 50, (height // 2) - 20)
                    return 0
        if ct == 1:
            if  headh < ssize[0] - ssize[0] or headh > ssize[0] - 1 or headw < ssize[0] - ssize[0] or headw > ssize[0] - 1:
                lost(coadah, coadaw, color_verde, cellw, cellh, color_cap, color_alb, foodw, foodh, headw, headh, (0, 0, 0), score, width, height, (width / 2) - 50, (height / 2) - 20)
                return 1
            pygame.draw.circle( screen, color_alb, [cellw * foodw[0] + cellw //2, cellh * foodh[0]+ cellh //2 ], cellw - cellw // 1.5)
            pygame.draw.rect( screen, color_cap, [cellw * headw, cellh * headh, cellw, cellh])

        for event in pygame.event.get():

               #se iese afara
            if event.type == pygame.QUIT:
                pygame.quit()

                #schimba directia
            if event.type == pygame.KEYDOWN:
                if lock == 0:
                    if event.key == pygame.K_LEFT and dir!= 1  and dir!= -1:
                        dir = -1
                    elif event.key == pygame.K_UP and dir!= 2 and dir!= -2:
                        dir = -2
                    elif event.key == pygame.K_RIGHT and dir!= -1 and dir!= 1:
                        dir = 1
                    elif event.key == pygame.K_DOWN and dir!= -2 and dir!= 2:
                        dir = 2
                    #ct = 0
                    lock = 1

            #sarpele se mareste
        if score > 1 and food == 1 and reset == 2:
            coadac += 1
            coadah.append(len(coadah) - 1 )
            coadaw.append(len(coadaw) - 1 )
            reset = 0

        if score == 1 and coadac == 0:
            coadaw.append(headw)
            coadah.append(headh)
            coadac += 1

        if ct > FPS / 2 - viteza / 2:
            lock = 0

        if ct >= FPS - viteza:
            if score > 0:
                s = coadaw[0]
                h = coadah[0]
                coadah[0] = headh
                coadaw[0] = headw
                if len(coadah) > 1 and len(coadaw) > 1:
                    for i in range (len (coadah)):
                            if i != 0:
                                if i % 2 == 1:
                                    w = coadah[i] 
                                    coadah[i] = h
                                elif i % 2 == 0:
                                    h = coadah[i]
                                    coadah[i] = w
                    w = s
                    for i in range (len (coadaw)):
                            if i != 0:
                                if i % 2 == 1:
                                    h = coadaw[i] 
                                    coadaw[i] = w
                                elif i % 2 == 0:
                                    w = coadaw[i]
                                    coadaw[i] = h

            food = 0
            
                
                
            if dir == 1 or dir == -1:
                headw += dir
            elif dir == 2:
                headh += 1
            elif dir == -2:
                headh -= 1
            ct = 0
            

        ct += 1
        text(score, 0, 0)
        pygame.display.update()

if __name__ == '__main__':
    menu()
    ssize[0] = 13
    while True:
        main()