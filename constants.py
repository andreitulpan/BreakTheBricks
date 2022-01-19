#Credits Andrei Tulpan, Irina Nita, Sebastian Severin 2022

# IMPORTS
import pygame, sys
from pygame.locals import *
import random
from random import randint

# CONSTANTS
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
LIGHT_BLUE = "#D6E5E3"

INITIAL_LIVES = 3
PAD_VELOCITY = 50

WIDTH = 1563
HEIGHT = 1042
BALL_RADIUS = 50
PAD_WIDTH = 250
PAD_HEIGHT = 25
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2
BRICK_WIDTH = 150
BRICK_HEIGHT = 50
HALF_BRICK_WIDTH = BRICK_WIDTH // 2
HALF_BRICK_HEIGHT = BRICK_HEIGHT // 2
BANNER_POS_X = (WIDTH - 900) // 2
BANNER_POS_Y = (HEIGHT - 500) // 2

FONT = "fonts/pixeled.ttf"
BACKGROUND_IMG = "images/background.png"
PADDLE_IMG = "images/paddle.png"
GAMEOVER_BANNER_IMG = "images/gameover_banner.png"
BALL_IMG = "images/ball.png"
BALL_PGP_IMG = "images/ball_pgp.png"
BALL_RR_IMG = "images/ball_rr.png"
BALL_LUMI_IMG = "images/ball_lumi.png"
COIN_IMG = "images/coin.png"
PGP_BANNER_IMG = "images/pgp_banner.png"
RR_BANNER_IMG = "images/rr_banner.png"
LUMI_BANNER_IMG = "images/lumi_banner.png"

BRICK1 = pygame.image.load("images/brick1.png")
BRICK2 = pygame.image.load("images/brick2.png")
BRICK3 = pygame.image.load("images/brick3.png")

GAME_NAME = "EL PULE NEGRO CEA MAI MARE DIN PARCARE"
GAMEOVER = ["MAI BAGA O FISA", "BRIBE ME", "WIN YOU SHALL NOT", "CE-I AIA COX?", "HAIDETI MAI, ZICETI", "A PIERDUT BARCA"]
EVENTS = ["Score", "Lives", "Bomb", "Damage", "Fatality"]
BONUSES = ["+1 Life", "+500 Points", "+1000 Points", "Viva Barcelona", "+750 Points", "+2 Lives"]
BONUS_MSG_PGP = ["Tiki taka Barcelona!", "Ai extrapolat bine!", "A iesit curba GAUSS!"]
BONUS_MSG_LUMI = ["Mai sunt 2 minute,", "   mai e timp sa", "spargi 2 randuri!"]
BONUS_MSG_RR = ["Am vorbit cu SRI-ul", "USO RULZ GHINDA FTW"]
BONUS_CHARACTER = ["PGP", "LUMI", "RR"]