import random

import constants as constant
import pygame


class Enemy:
    def __init__(self, image, x=random.randint(constant.SPRITE_MIN_X, constant.SPRITE_MAX_X), y=64):
        self.enemy_img = 'png/sprites/' + image + '.png'
        self.enemy_x = x
        self.enemy_y = y
        self.enemy_y_change = 0
        self.enemy_x_change = 0
        self.direction = 1  # direction on x-axis, 1 for right and -1 for left


class Player:
    def __init__(self):
        self.player_img = pygame.image.load('png/sprites/spaceship.png')
        self.player_x = constant.SPRITE_START_POSITION_X
        self.player_y = constant.SPRITE_START_POSITION_Y
        self.player_x_change = 0
        self.player_y_change = 0
