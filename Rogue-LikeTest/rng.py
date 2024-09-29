import random

def ran(initial, enem, WIDTH, HEIGHT):
    for i in range(initial[0].enemynr):
        if enem[i].status != 1 and enem[i].lock == 0:
            ran= random.randint(0, 3)
            if ran == 0 or ran == 1:
                enem[i].x=random.randint(0, WIDTH)
                if ran == 1:
                    enem[i].y= HEIGHT + initial[0].radius/2
                else:
                    enem[i].y=0 - initial[0].radius/2
            else:
                enem[i].y=random.randint(0, HEIGHT)
                if ran == 3:
                    enem[i].x= WIDTH + initial[0].radius/2
                else:
                    enem[i].x=0 - initial[0].radius/2
            enem[i].status = 1