from tkinter import font
import pygame

WIDTH = 700
HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font('freesansbold.ttf', 40)
score = 50
text = font.render('Hello, world', False, (255, 255, 255))

def main():
    while True:
        screen.fill((0, 0, 0))
        screen.blit(text, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

if __name__ == '__main__':
    main()