#Credits Andrei Tulpan, Irina Nita, Sebastian Severin 2022

from paddle import Paddle
from ball import Ball
from coin import Coin
from brick import Brick
from constants import *

class Game:

    def __init__(self):
        # PYGAME INIT
        pygame.init()
        pygame.display.set_caption(GAME_NAME)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.image.load(BACKGROUND_IMG)

        # SPAWN OBJECTS
        self.spawn_objects()

        # INIT GAME VARIABLES
        self.highscore = 0
        self.score = 0
        self.lives = INITIAL_LIVES
        self.show_bonus = False
        self.coin_is_spawned = False
        self.show_banner = False
        self.myfont_30 = pygame.font.Font(FONT, 30)
        self.myfont_60 = pygame.font.Font(FONT, 60)

        self.banner = pygame.image.load(GAMEOVER_BANNER_IMG)
        self.msg = random.choice(GAMEOVER)


    def spawn_objects(self):
        self.bricks = pygame.sprite.Group()
        self.gameObjects = pygame.sprite.Group()
        self.paddle = Paddle(self, [WIDTH / 2, HEIGHT / 2 + 460], [HALF_PAD_WIDTH, HALF_PAD_HEIGHT]) # ???
        self.ball = Ball(self, [WIDTH // 2, HEIGHT // 2 - 100], [BALL_RADIUS, BALL_RADIUS])

        self.spawn_bricks()

        self.gameObjects.add(self.paddle)
        self.gameObjects.add(self.ball)

    def spawn_bricks(self):
        for x in range(10):
            brick = Brick(self, [30 + (BRICK_WIDTH) * (x), BRICK_HEIGHT * 3], [HALF_BRICK_WIDTH, HALF_BRICK_HEIGHT], random.choice([0, 1, 2]))
            self.bricks.add(brick)
            self.gameObjects.add(brick)
            brick = Brick(self, [30 + (BRICK_WIDTH) * (x), BRICK_HEIGHT * 4], [HALF_BRICK_WIDTH, HALF_BRICK_HEIGHT], random.choice([0, 1, 2]))
            self.bricks.add(brick)
            self.gameObjects.add(brick)
            brick = Brick(self, [30 + (BRICK_WIDTH) * (x), BRICK_HEIGHT * 5], [HALF_BRICK_WIDTH, HALF_BRICK_HEIGHT], random.choice([0, 1, 2]))
            self.bricks.add(brick)
            self.gameObjects.add(brick)

    def spawn_coin(self, x, y):
        chance = random.choice([1, 2, 3, 4, 5])
        if chance == 3 and self.coin_is_spawned == False:
            self.coin = Coin(self, [x, y], [BALL_RADIUS, BALL_RADIUS])
            self.gameObjects.add(self.coin)
            self.coin_is_spawned = True

    def run(self):
        while(True):
            self.input()
            self.update()
            self.draw()
            if not self.lives:
                self.game_over()


    def collisionDetection(self):
        for target in self.gameObjects:
            if self.ball != target:
                if self.ball.collidesWith(target):
                    self.ball.onCollision(target)
        if self.coin_is_spawned == True and self.coin.collidesWith(self.paddle):
            self.coin.onCollision(self.paddle)

    def update(self):
        if not self.bricks and self.lives:
            self.respawn_bricks()
        self.gameObjects.update()
        self.collisionDetection()
        for gameObject in self.gameObjects:
            gameObject.update()

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.paddle.moveLeft()
        if keys[pygame.K_d]:
            self.paddle.moveRight()
        if keys[pygame.K_RETURN]:
            self.reset_game()

    def show_score(self):
        pygame.draw.line(self.window, LIGHT_BLUE, [0, HEIGHT - 30],[WIDTH, HEIGHT - 30], 1)
        self.score_label = self.myfont_30.render("Score: " + str(self.score), 1, LIGHT_BLUE)
        self.window.blit(self.score_label, (50,20))
        self.lives_label = self.myfont_30.render("Lives: " + str(self.lives), 1, LIGHT_BLUE)
        self.window.blit(self.lives_label, (WIDTH - 250, 20))

    def game_over(self):
        self.gameObjects.empty()
        self.bricks.empty()
        if (self.score > self.highscore):
            self.highscore = self.score
        self.score = 0
        self.show_banner = True

    def reset_game(self):
        if (self.lives == 0):
            self.lives = 3
            self.show_banner = False
            self.spawn_objects()
            self.msg = random.choice(GAMEOVER)

    def draw(self):
        self.window.blit(self.background, (0,0))
        self.gameObjects.draw(self.window)

        if (self.lives):
            self.show_score()
        else:
            self.highscore_label = self.myfont_60.render("HighScore: " + str(self.highscore), 1, LIGHT_BLUE)
            self.window.blit(self.highscore_label, (WIDTH - 1100, 20))
            self.continue_label = self.myfont_60.render("Press return to restart...", 1, LIGHT_BLUE)
            self.window.blit(self.continue_label, (130, 800))
            self.banner_label1 = self.myfont_30.render(self.msg, 1, LIGHT_BLUE)

        if (self.show_banner == True):
            self.window.blit(self.banner, (BANNER_POS_X, BANNER_POS_Y))
            self.window.blit(self.banner_label1, (660, 480))

        if (self.show_bonus == True):
            self.window.blit(self.b_banner, (BANNER_POS_X, BANNER_POS_Y))
            if self.bonus_msg == "LUMI":
                self.banner_b_label1 = self.myfont_30.render(BONUS_MSG_LUMI[0], 1, LIGHT_BLUE)
                self.banner_b_label2 = self.myfont_30.render(BONUS_MSG_LUMI[1], 1, LIGHT_BLUE)
                self.banner_b_label3 = self.myfont_30.render(BONUS_MSG_LUMI[2], 1, LIGHT_BLUE)
                self.window.blit(self.banner_b_label1, (660, 400))
                self.window.blit(self.banner_b_label2, (660, 470))
                self.window.blit(self.banner_b_label3, (660, 540))
            else:
                self.window.blit(self.banner_b_label, (650, 430))
                self.window.blit(self.banner_b_msg, (740, 500))

        pygame.display.update()
        pygame.time.Clock().tick(30)

    def respawn_bricks(self):
        pygame.time.wait(100)
        self.bonus_banner()
        self.draw()
        pygame.time.wait(5000)
        self.show_bonus = False
        self.spawn_bricks()

    def bonus_banner(self):
        self.show_bonus = True
        self.banner_type = random.choice(BONUS_CHARACTER)
        if self.banner_type == "PGP":
            self.b_banner = pygame.image.load(PGP_BANNER_IMG)
            self.bonus_msg = random.choice(BONUS_MSG_PGP)
            ball_image = pygame.image.load(BALL_PGP_IMG)
        if self.banner_type == "LUMI":
            self.b_banner = pygame.image.load(LUMI_BANNER_IMG)
            self.bonus_msg = "LUMI"
            ball_image = pygame.image.load(BALL_LUMI_IMG)
        if self.banner_type == "RR":
            self.b_banner = pygame.image.load(RR_BANNER_IMG)
            self.bonus_msg = random.choice(BONUS_MSG_RR)
            ball_image = pygame.image.load(BALL_RR_IMG)
        self.ball.image = ball_image
        self.banner_b_label = self.myfont_30.render(self.bonus_msg, 1, LIGHT_BLUE)
        self.give_bonus()

    def give_bonus(self):
        self.bonus = random.choice(BONUSES)
        if self.bonus == "+1 Life":
            self.lives += 1
        if self.bonus == "+2 Lives":
            self.lives += 2
        if self.bonus == "+500 Points":
            self.score += 500
        if self.bonus == "+750 Points":
            self.score += 750
        if self.bonus == "+1000 Points":
            self.score += 1000
        if self.bonus == "Viva Barcelona" and self.banner_type == "PGP":
            self.score += random.choice([5000, 7500, 6000, 6500, 7000, 20000])
            self.lives += 1
        elif self.bonus == "Viva Barcelona" and not self.banner_type == "PGP":
            self.bonus = "+1 Life"
            self.lives += 1
        self.banner_b_msg = self.myfont_30.render(self.bonus, 1, LIGHT_BLUE)
