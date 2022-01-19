#Credits Andrei Tulpan, Irina Nita, Sebastian Severin 2022

from gameObject import GameObject
from constants import *

class Coin(GameObject):
    def __init__(self, game, position, dimensions):
        velocity = [0, 0]
        velocity[1] = 10
        super().__init__(game, position, velocity, dimensions)
        self.image = pygame.image.load(COIN_IMG)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def update(self):
        self.rect.x += int(self.velocity[0])
        self.rect.y += int(self.velocity[1])

        if self.rect.y - BALL_RADIUS > HEIGHT:
            self.game.gameObjects.remove(self)
            self.game.coin_is_spawned = False

    def onCollision(self, other):
        event = random.choice(EVENTS)
        if event == "Score":
            self.game.score += random.choice([100,200,300])
        if event == "Lives":
            self.game.lives += random.choice([1, 2])
        if event == "Bomb":
            for brick in self.game.bricks:
                brick.hits = 3
        if event == "Damage":
            for brick in self.game.bricks:
                brick.hits = 2
        if event == "Fatality":
            self.game.lives = 1
            self.game.ball.velocity[0] *= 2
            self.game.ball.velocity[1] *= 2
        self.game.gameObjects.remove(self)
        self.game.coin_is_spawned = False