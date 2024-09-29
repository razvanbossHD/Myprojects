import pygame
import math

class enemy():
    def __init__(self, x, y, speed, status, colour, distance, lock):
        self.x = x
        self.y = y
        self.speed = speed
        self.status = status
        self.colour = colour
        self.distance = distance
        self.lock = lock

def charac_movement(charac):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_d]:
        charac[0].x+= 5
    if keys_pressed[pygame.K_a]:
        charac[0].x -= 5
    if keys_pressed[pygame.K_w]:
        charac[0].y -= 5
    if keys_pressed[pygame.K_s]:
        charac[0].y += 5

def enemy_movement(initial, charac, enem):
    initial[0].distmin = 50000
    for i in range(initial[0].enemynr):

        
        
        if enem[i].status == 1 and enem[i].lock == 0:
            disx= abs(charac[0].x-enem[i].x)
            disy= abs(charac[0].y-enem[i].y)
            disxy= math.sqrt(disx**2 + disy**2)
            if charac[0].x > enem[i].x + 3:
        
                if disx > disy and enem[i].x!=0 and enem[i].y!=0:
                    enem[i].x += round((2 * enem[i].speed) * (1 - (disy/disx)), 2)
                elif disx < disy and enem[i].x!=0 and enem[i].y!=0:
                    enem[i].x += round((2*enem[i].speed)*(disx/disy), 2)
                else:
                    enem[i].x+= enem[i].speed

            elif charac[0].x < enem[i].x - 3:
                
                if disx > disy and enem[i].x!=0 and enem[i].y!=0:
                    enem[i].x -= round((2*enem[i].speed)*(1 - (disy/disx)), 2)
                elif disx < disy and enem[i].x!=0 and enem[i].y!=0:
                    enem[i].x -= round((2*enem[i].speed)*(disx/disy), 2)
                else:
                    enem[i].x-= enem[i].speed

            if charac[0].y > enem[i].y + 3:
                
                if disx > disy and enem[i].x!=0 and enem[i].y!=0:
                    enem[i].y += round((2*enem[i].speed)*(disy/disx), 2)
                elif disx < disy and enem[i].x!=0 and enem[i].y!=0:
                    enem[i].y += round((2*enem[i].speed)*(1 - (disx/disy)), 2)
                else:
                    enem[i].y+= enem[i].speed

            elif charac[0].y < enem[i].y - 3:
                if disx > disy and enem[i].x!=0 and enem[i].y!=0:
                    enem[i].y -= round((2*enem[i].speed)*(disy/disx), 2)
                elif disx < disy and enem[i].x!=0 and enem[i].y!=0:
                    enem[i].y -= round((2*enem[i].speed)*(1 - (disx/disy)), 2)
                else:
                    enem[i].y-= enem[i].speed
        
            if initial[0].distmin > disxy:
                initial[0].distmin = disxy


def collision_ceck(initial, charac, enem):
    if initial[0].distmin < charac[0].radius + initial[0].radius:
        initial[0].gameover = 1

def respawn(initial, nr, enem):
    if initial[0].score >= 10*(initial[0].enemynr-9):
        initial[0].enemynr+= 1
        enem.append(enemy(0, 500, 1.5, 0, (255, 0, 0), 500, 1))
        print(len(enem))
        print(initial[0].enemynr)
    if (nr[0] + nr[1]*60)%(round(60/initial[0].diff)) == 0:
        i=0
        while(i < initial[0].enemynr):
            if enem[i].lock == 1:
                enem[i].lock = 0
                i= initial[0].enemynr
            i+= 1

def click_ceck(initial, enem):
    mouse = pygame.mouse.get_pos()
    mouse_presses = pygame.mouse.get_pressed()
    for i in range(initial[0].enemynr):
        dis = math.sqrt( ((enem[i].x-mouse[0])**2)+((enem[i].y-mouse[1])**2) )
        if dis < initial[0].radius + 5 and mouse_presses[0] and initial[0].lock == 0 and enem[i].status ==1:
            enem[i].status= 0
            initial[0].score+= 1
            enem[i].lock= 1
    if mouse_presses[0] and initial[0].lock == 0:
        initial[0].lock= 1



def calcule1(initial, charac, enem, WIDTH, HEIGHT, nr):
    charac_movement(charac)
    enemy_movement(initial, charac, enem)
    respawn(initial, nr, enem)
    collision_ceck(initial, charac, enem)
    click_ceck(initial, enem)
    
    
    

