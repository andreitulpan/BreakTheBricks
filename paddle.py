#Credits Andrei Tulpan, Irina Nita, Sebastian Severin 2022

from gameObject import GameObject
from constants import *

class Paddle(GameObject):
    def __init__(self, game, position, dimensions):
        super().__init__(game, position, [0, 0], dimensions)
        self.image = pygame.image.load(PADDLE_IMG)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def update(self):
        if self.rect.x > WIDTH - PAD_WIDTH:
            self.rect.x = WIDTH - PAD_WIDTH
        if self.rect.x < 0:
            self.rect.x = 0

    def moveLeft(self):
        self.rect.x -= 50

    def moveRight(self):
        self.rect.x += 50

    def getType(self):
        return "paddle"
