import pygame
import time
import random
import math
import os

WIDTH = 720
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
clock = pygame.time.Clock()
color_black = (0, 0, 0)
directory = os.getcwd()

class target:
    def __init__(self, x, y, radius, val, distance, lock, mousedis):
        self.x = x
        self.y = y
        self.radius = radius
        self.val = val
        self.distance = distance
        self.lock = lock
        self.mousedis = mousedis

def start():
    font = pygame.font.Font("freesansbold.ttf", 30)
    while True:
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (155, 0, 0), [WIDTH // 2, HEIGHT // 2], 100)
        pygame.draw.circle(screen, (155, 155, 0), [WIDTH // 2, HEIGHT // 2], 100 - 100 // 3 * 1)
        pygame.draw.circle(screen, (0, 155, 0), [WIDTH // 2, HEIGHT // 2], 100 - 100 // 3 * 2)
        text = font.render("APASA CLICK CA SA INCEPI", False, (255, 255, 255))
        screen.blit(text,(WIDTH // 2 - 200, HEIGHT // 2))
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            return 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

def menu():
    FPS = 60
    x = WIDTH // 2 - 50
    y = HEIGHT // 2 + 75
    while True:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
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

def fin( a, score):
    screen.fill((0, 0, 0))
    font = pygame.font.Font("freesansbold.ttf", 40)
    text1 = font.render('Scor:' + str(score), False, (255, 255, 255))
    if a == 1:
        text2 = font.render("AI CASTIGAT", False, (255, 255, 255))
    if a == 0:
        text2 = font.render("AI PIERDUT", False, (255, 255, 255))
    screen.blit(text1, (WIDTH / 2 - 100, HEIGHT / 2))
    screen.blit(text2, (WIDTH / 2 - 150, HEIGHT / 2 - 40))
    pygame.display.update()
    time.sleep(2)

def draw(nr, tg, radius, max_radius, jum, text):
    pygame.draw.circle(screen, (255, 0, 0), [jum[0], jum[1]], max_radius)
    pygame.draw.circle(screen, (255, 255, 0), [jum[0], jum[1]], max_radius - max_radius // 3 * 1)
    pygame.draw.circle(screen, (0, 255, 0), [jum[0], jum[1]], max_radius - max_radius // 3 * 2)
    pygame.draw.circle(screen, (0, 0, 255), [WIDTH/2, HEIGHT/2], radius)
    for i in range(nr):
        if tg[i].val == 1:
            pygame.draw.circle(screen, (255, 255, 255), [tg[i].x, tg[i].y], tg[i].radius)
    screen.blit(text, (0, 0))

def main():
    click = False
    score = 0
    scorest = 1
    min_radius =9
    max_radius = 100
    radius = min_radius
    delay = 0.07
    nrin= 5
    nr = nrin
    tg = []
    tgradius = 35

    FPS = 60
    jum = [WIDTH / 2, HEIGHT / 2]
    apas = 0
    font = pygame.font.Font("freesansbold.ttf", 20)
    for i in range(nr):
        tg.append(target(0, 0, tgradius, 1, 0, 0, 0))
    while True:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        text = font.render("Scor:" + str(score), False, (255, 255, 255))
        screen.fill((color_black))

        for i in range(nr):
            if tg[i].lock == 0:
                while tg[i].distance < max_radius + tg[i].radius or tg[i].lock == 0:
                    tg[i].x = random.randint(0 + tgradius, WIDTH - tgradius)
                    tg[i].y = random.randint(0 + tgradius, HEIGHT - tgradius)
                    tg[i].distance = math.sqrt( ((tg[i].x-jum[0])**2)+((tg[i].y-jum[1])**2) )
                    tg[i].lock = 1
    
        draw(nr, tg, radius, max_radius, jum, text)


        if radius <= max_radius:
            radius += delay
        mouse_presses = pygame.mouse.get_pressed()
        for i in range(nr):
            tg[i].mousedis = math.sqrt( ((tg[i].x-mouse[0])**2)+((tg[i].y-mouse[1])**2) )
            if tg[i].mousedis < tg[i].radius:
                if mouse_presses[0] and click == False:
                    tg[i].lock = 0
                    radius -= 1.5
                    score += 1
                    scorest = 0
                    click = True

        for ev in pygame.event.get():
          
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONUP:
                click = False
       
        if score % 20 == 0 and score != 0 and scorest == 0:
                nr -= 1
                scorest = 1

        if nr == 0 :
            fin(1, score)
            return 1
        if radius >= max_radius:
            fin(0, score)
            return 1
        pygame.display.update()

if __name__ == "__main__":
    menu()
    while True:
        start()
        main()