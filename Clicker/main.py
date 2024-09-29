import pygame
import displ
import math
import click

WIDTH = 600
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

def main():
    FPS = 60
    ap = False
    score = [0]
    negru = (0, 0, 0)
    up = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    lock = [0, 0]
    nr = [1]
    while True:
        screen.fill(negru)
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        width= screen.get_width()
        height = screen.get_height()



        click.check(up, width, height, score, lock, mouse, nr)
        displ.patr(screen, width, height, score, nr, up)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            mouse_presses = pygame.mouse.get_pressed()
            dis = math.sqrt( ((width // 2 - mouse[0])**2)+((height // 2 - mouse[1])**2))
            if dis < width // 10 and mouse_presses[0] and ap == False:
                ap = True
            if not mouse_presses[0] and ap == True:
                score[0] += nr[0]
                ap = False

            

        pygame.display.update()

if __name__ == "__main__":
    main()