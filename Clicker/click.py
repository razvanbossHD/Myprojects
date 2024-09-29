from this import s
import pygame



def check(up, width, height, score, lock, mouse, nr):
    w = width // 14
    h = height // 8
    buttw = (width + height)//9
    butth = (width + height) //32
    w1 = width - width // 14 - buttw
    mouse_presses = pygame.mouse.get_pressed()
    for i in range(7):
        if mouse_presses[0] and lock[1] == 0:
            if w <= mouse[0] <= w + buttw and (i + 1) * h <= mouse[1] <= (i + 1) * h + butth:
                if up[i] and score[0] >= 10**(i + 1):
                    up[i] -= 1
                    nr[0] = nr[0] + 10**(i)
                    score[0] -= 10**(i + 1)
                lock[1] = 1
            if w1 <= mouse[0] <= w1 + buttw and (i + 1) * h <= mouse[1] <= (i + 1) * h + butth:
                if up[7 + i] and score[0] >= 10**(i + 8):
                    up[7 + i] -= 1
                    nr[0] = nr[0] + 1 * 10**(7 + i)
                    score[0] -= 10**(i + 8)
                lock[1] = 1
        if not mouse_presses[0] and lock[1] == 1: 
            lock[1] = 0
        

