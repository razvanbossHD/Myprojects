import pygame
import os

pygame.init()
screen_width = 700
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
FPS = 60
directory = os.getcwd()

class platform():
    def __init__(self, culoare, x, y, width, height):
        self.x = x
        self.y = y
        self.culoare = culoare
        self.width = width
        self.height = height

pos = screen_height // 8


def bg(pos, camera, plat):
    pygame.draw.rect(screen, (100, 100, 255), [0, 0, screen_width, screen_height - pos] )
    pygame.draw.rect(screen, (100, 255, 100), [0, pos * 7, screen_width, pos])
    pygame.draw.rect(screen, (0, 0, 0), [900 - camera, 300, 100, pos * 7 - 300])
    for i in range(len(plat)):
        pygame.draw.rect(screen, plat[i].culoare, [plat[i].x, plat[i].y, plat[i].width, plat[i].height])

def check(oppos, plat, aer, lapamant, camera, cam, sar2):
    if oppos[1] + 100 > pos * 7:
        oppos[1] = pos * 7 - 99
        lapamant[0] = True
        sar2[0] = 1
    elif oppos[0] + 42 > plat[0].x and oppos[0] < plat[0].x + plat[0].width and oppos[1] + 100 > plat[0].y and  oppos[1] + 100 < plat[0].y + 15 and aer < 0:
        oppos[1] = plat[0].y - 99
        lapamant[0] = True
        sar2[0] = 1
    elif oppos[0] + 42 > plat[1].x and oppos[0] < plat[1].x + plat[1].width and oppos[1] + 100 > plat[1].y and  oppos[1] + 100 < plat[1].y + 15 and aer < 0:
        oppos[1] = plat[1].y - 99
        lapamant[0] = True
        sar2[0] = 1
    elif oppos[0] + 42 > plat[2].x and oppos[0] < plat[2].x + plat[2].width and oppos[1] + 100 > plat[2].y and  oppos[1] + 100 < plat[2].y + 15 and aer < 0:
        oppos[1] = plat[2].y - 99
        lapamant[0] = True
        sar2[0] = 1
    elif oppos[0] + 42 > plat[3].x and oppos[0] < plat[3].x + plat[3].width and oppos[1] + 100 > plat[3].y and  oppos[1] + 100 < plat[3].y + 15 and aer < 0:
        oppos[1] = plat[3].y - 99
        lapamant[0] = True
        sar2[0] = 1
    elif oppos[0] + 42 > 910 - camera and oppos[0] < 1000 - camera and oppos[1] + 100 > 300 and aer < 0:
        oppos[1] = 299 - 100
        lapamant[0] = True
        sar2[0] = 1
    else:
        lapamant[0] = False
    if oppos[0] + 42 > 900 - camera and oppos[0] < 910 - camera and oppos[1] + 100 > 300:
        oppos[0] = 899 - camera - 40
        cam[0] = False

def main():
    op = pygame.image.load(directory+"\\caract2.png")
    op = pygame.transform.scale(op, (42, 100))
    grav = 0.5
    aer = 0
    saritura = 12
    lapamant = [False]
    cam = [True]
    sar2 = [0]

    camera = 0
    rec = [0 , 15]
    oppos = [pos * 2 + rec[0] + camera, pos * 5 + 35 + rec[1] + camera]
    dir = 1

    while True:
        plat = [platform((148, 111, 52), 400 - camera, 450, 100, 50), platform((148, 111, 52), 500 - camera, 320, 100, 50), platform((148, 111, 52), 300 - camera, 230, 100, 50),
        platform((148, 111, 52), 700 - camera, 450, 100, 50)]
        clock.tick(FPS)
        screen.fill((0, 0, 0))
        bg(pos, camera, plat)
        check(oppos, plat, aer, lapamant, camera, cam, sar2)
        #hitbox = pygame.draw.rect(screen, (255, 255, 255), [oppos[0] + 3, oppos[1], 39, 100])
        screen.blit(op, (oppos[0], oppos[1]))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT] and cam[0] == True:
            camera += 4
            if dir == 0:
                op = pygame.transform.flip(op, True, False)
                oppos[0] += 5
                dir = 1
        cam[0] = True
        if keys_pressed[pygame.K_LEFT]:
            camera -= 4
            if dir == 1:
                op = pygame.transform.flip(op, True, False)
                oppos[0] -= 5
                dir = 0
            
        if keys_pressed[pygame.K_SPACE] and lapamant[0] == False and aer < 6 and sar2[0] == 1:
            aer = saritura
            sar2[0] = 0
        if keys_pressed[pygame.K_SPACE] and lapamant[0] == True and sar2[0] == 1:
            aer = saritura
            lapamant[0] = False
        
        if lapamant[0] == False:
            if aer > -14:
                aer -= grav
            oppos[1] -= aer
        pygame.display.update()

if __name__ == '__main__':
    main()