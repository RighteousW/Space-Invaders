import constants as constant
import pygame

import sprite

# initialize pygame
pygame.init()

# creating screen
screen = pygame.display.set_mode((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))

# changing title and icon of game window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('png/sprites/spaceship.png')
background_image = pygame.image.load('png/background/outrun-neon-dark-background-purple-resized.png')
pygame.display.set_icon(icon)

# player attributes
player = sprite.Player()

# enemy attributes
enemy = sprite.Enemy('shuriken', 0, 0)

# enemies enemies
enemy_list = [enemy]

# control states
right = False
left = False
up = False
down = False


# player method to paint player at certain coordinates
def draw_player(x, y):
    screen.blit(player.player_img, (x, y))


def draw_enemy(enemies):
    for _ in enemies:
        screen.blit(pygame.image.load(_.enemy_img), (_.enemy_x, _.enemy_y))


def draw_background(x, y):
    screen.blit(background_image, (x, y))


def player_border_collision(player_sprite):
    if player_sprite.player_x < constant.SPRITE_MIN_X:
        player_sprite.player_x = 0

    if player_sprite.player_x > constant.SPRITE_MAX_X:
        player_sprite.player_x = constant.SPRITE_MAX_X

    if player_sprite.player_y < constant.SPRITE_MIN_Y:
        player_sprite.player_y = 0

    if player_sprite.player_y > constant.SPRITE_MAX_Y:
        player_sprite.player_y = constant.SPRITE_MAX_Y


def enemy_border_collision(enemy_sprite) -> bool:
    if enemy_sprite.enemy_x < constant.SPRITE_MIN_X:
        return True

    elif enemy_sprite.enemy_x > constant.SPRITE_MAX_X:
        return True

    else:
        return False


def update_enemies(enemies):
    for _ in enemies:
        if enemy_border_collision(_):
            _.direction *= -1

        _.enemy_y += constant.SPRITE_Y_MOVE_LENGTH_ENEMY


# Game loop
running = True
while running:
    # background color in RGB values
    screen.fill((0, 0, 0))

    # checking if exit button was pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check if keystroke pressed is ADWS (for left, right, up and down)
        if event.type == pygame.KEYDOWN:
            match event.key:
                # move player left
                case pygame.K_a:
                    player.player_x_change = -constant.SPRITE_X_MOVE_LENGTH_PLAYER
                    left = True
                # move player right
                case pygame.K_d:
                    player.player_x_change = constant.SPRITE_X_MOVE_LENGTH_PLAYER
                    right = True
                # move player up
                case pygame.K_w:
                    player.player_y_change = -constant.SPRITE_Y_MOVE_LENGTH_PLAYER
                    up = True
                # move player down
                case pygame.K_s:
                    player.player_y_change = constant.SPRITE_Y_MOVE_LENGTH_PLAYER
                    down = True

        # check if keystroke pressed is ADWS (for left, right, up and down)
        if event.type == pygame.KEYUP:
            match event.key:
                # set character x velocity to 0 when 'a' is released
                case pygame.K_a:
                    if not right:
                        player.player_x_change = 0
                    left = False
                # set character x velocity to 0 when 'd' is released
                case pygame.K_d:
                    if not left:
                        player.player_x_change = 0
                    right = False
                # set character y velocity to 0 when 'w' is released
                case pygame.K_w:
                    if not down:
                        player.player_y_change = 0
                    up = False
                # set character y velocity to 0 when 's' is released
                case pygame.K_s:
                    if not up:
                        player.player_y_change = 0
                    down = False

    # updating player's position
    player.player_x += player.player_x_change
    player.player_y += player.player_y_change

    # updating enemies position
    update_enemies(enemy_list)
    for villain in enemy_list:
        villain.enemy_x += constant.SPRITE_X_MOVE_LENGTH_ENEMY * villain.direction

    # check if player is colliding with border and not letting player pass through
    player_border_collision(player)

    # drawing background a sprites to game window
    draw_background(0, 0)
    draw_player(player.player_x, player.player_y)
    draw_enemy(enemy_list)
    # updating pygame for every loop iteration
    pygame.display.update()
