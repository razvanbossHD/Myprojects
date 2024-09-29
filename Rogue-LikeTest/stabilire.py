import pygame
import random
import rng

class car():
    def __init__(self, x, y, speed, status, radius, colour):
        self.x = x
        self.y = y
        self.speed = speed
        self.status = status
        self.radius = radius
        self.colour = colour
class enemy():
    def __init__(self, x, y, speed, status, colour, distance, lock):
        self.x = x
        self.y = y
        self.speed = speed
        self.status = status
        self.colour = colour
        self.distance = distance
        self.lock = lock

def start(initial, enem, WIDTH, HEIGHT):
    for i in range(initial[0].enemynr):
        enem.append(enemy(0, 500, 1.5, 0, (255, 0, 0), 500, 1))
    for i in range(initial[0].enemynr):
        rng.ran(initial, enem, WIDTH, HEIGHT)
