#Credits Andrei Tulpan, Irina Nita, Sebastian Severin 2022

from gameObject import GameObject
from constants import *

class Ball(GameObject):
    def __init__(self, game, position, dimensions):
        velocity = [0, 0]
        velocity[0] = randint(-10, 10)
        if velocity[0] < 5:
            velocity[0] = random.choice([-10, 10])
        velocity[1] = 7
        super().__init__(game, position, velocity, dimensions)
        self.image = pygame.image.load(BALL_IMG)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def update(self):
        self.rect.x += int(self.velocity[0])
        self.rect.y += int(self.velocity[1])

        if self.rect.x < 0:
            self.velocity[0] *= -1
        if self.rect.x + self.dimensions[0] > WIDTH:
            self.velocity[0] *= -1

        if self.rect.y < 0:
            self.velocity[1] *= -1
        if self.rect.y - BALL_RADIUS > HEIGHT:
            self.reset()
            self.game.lives -= 1
        if self.velocity[0] >= 20:
            self.velocity[0] = 20
        if self.velocity[1] >= 20:
            self.velocity[1] = 20

    def reset(self):
        self.game.ball = Ball(self.game, [WIDTH // 2, HEIGHT // 2], [BALL_RADIUS, BALL_RADIUS])
        self.game.gameObjects.remove(self)
        self.game.gameObjects.add(self.game.ball)

    def onCollision(self, other):
        if (other.getType() == 'paddle'):            self.velocity[1] *= -1
        if (other.getType() == 'brick'):
            self.velocity[1] *= -1
            other.hits += 1
        pygame.time.wait(100)