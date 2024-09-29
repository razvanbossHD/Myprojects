import pygame
def dis(screen, charac, enem, initial, WIDTH, HEIGHT):
    screen.fill((0, 0, 0))
    width = screen.get_width()
    height = screen.get_height()

    pygame.draw.circle(screen, charac[0].colour, [charac[0].x, charac[0].y], charac[0].radius)

    for i in range(initial[0].enemynr):
        if enem[i].status == 1 and enem[i].lock ==0:
            pygame.draw.circle(screen, enem[i].colour, [enem[i].x, enem[i].y], initial[0].radius)

    font = pygame.font.Font("freesansbold.ttf", 40)
    text = font.render('Score:' + str(initial[0].score), False, (255, 255, 255))
    screen.blit(text, (0, 0))

    pygame.display.update()