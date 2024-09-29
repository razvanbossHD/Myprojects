import pygame

pygame.init()

VERDE = (0, 255, 0)
GRI = (150, 150, 150)

def click(screen, width, height):
    pygame.draw.circle(screen, (255, 0, 0), [width// 2, height//2], width//10)

def scor(screen, width, height, score):
    font = pygame.font.Font("freesansbold.ttf", (width + height) //30)
    text = font.render(str(score[0]), False, (255, 255, 255))
    screen.blit(text,(0 + width // 70, 0 + height // 70))

def butoane(screen, width, height, up):
    w1 = width // 14
    w2 = width - width // 14 - (width + height)//9
    h = height // 8
    cellw = (width + height)//9
    cellh = (width + height) //32
    for i in range(7):
        if up[i] > 0:
            pygame.draw.rect( screen, VERDE, [w1, (i + 1) * h, cellw, cellh])
        else:
            pygame.draw.rect( screen, GRI, [w1, (i + 1) * h, cellw, cellh])
        if up[7 + i] > 0:
            pygame.draw.rect( screen, VERDE, [w2, (i + 1) * h, cellw, cellh])
        else:
            pygame.draw.rect( screen, GRI, [w2, (i + 1) * h, cellw, cellh])

def scris(screen, width, height, up):
    w1 = width // 14
    w2 = width - width // 14 - (width + height)//9
    h = height // 8
    cellw = (width + height)//9
    cellh = (width + height) //32
    font = pygame.font.Font("freesansbold.ttf", (width + height) //100)
    font1 = pygame.font.Font("freesansbold.ttf", (width + height) //100)
    for i in range(7):    
        text = font.render(str(up[i]), False, (255, 255, 255))
        screen.blit(text, (w1 + cellw - (width + height) //100 + 5, (i + 1) * h + cellh - (width + height) //100))
        text = font.render(str(up[7 + i]), False, (255, 255, 255))
        screen.blit(text, (w2 + cellw - (width + height) //100 + 5, (i + 1) * h + cellh - (width + height) //100))
        text1 = font1.render(str(10**(1 + i)), False, (255, 255, 255))
        screen.blit(text1,(w1 + cellw // 2 - 4 * i, (1 + i) * h + cellh // 2))
        text1 = font1.render(str(10**(8+i)), False, (255, 255, 255))
        screen.blit(text1,(w2 + cellw // 2 - 4 * (7 +i), (1 + i) * h + cellh // 2))

def patr(screen, width, height, score, nr, up):
    butoane(screen, width, height, up)
    click(screen, width, height)
    scor(screen, width, height, score)
    scris(screen, width, height, up)
