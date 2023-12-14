import pygame
import constants as constant

# initialize pygame
pygame.init()

# creating screen
screen = pygame.display.set_mode((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))

# changing title and icon of game window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('alien-spaceship.png.jpg')
pygame.display.set_icon(icon)

# player attributes
player_img = pygame.image.load('spaceship-player.png')
player_x = constant.PLAYER_START_POSITION_X
player_y = constant.PLAYER_START_POSITION_Y
player_x_change = 0
player_y_change = 0

# control states
right = False
left = False
up = False
down = False


# player method to paint player at certain coordinates
def player(x, y):
    screen.blit(player_img, (x, y))


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
                    if not right:
                        player_x_change = -constant.PLAYER_X_MOVE
                    left = True
                # move player right
                case pygame.K_d:
                    if not left:
                        player_x_change = constant.PLAYER_X_MOVE
                    right = True
                # move player up
                case pygame.K_w:
                    if not down:
                        player_y_change = -constant.PLAYER_Y_MOVE
                    up = True
                # move player down
                case pygame.K_s:
                    if not up:
                        player_y_change = constant.PLAYER_Y_MOVE
                    down = True

        # check if keystroke pressed is ADWS (for left, right, up and down)
        if event.type == pygame.KEYUP:
            match event.key:
                # set character x velocity to 0 when 'a' is released
                case pygame.K_a:
                    if not right:
                        player_x_change = 0
                    left = False
                # set character x velocity to 0 when 'd' is released
                case pygame.K_d:
                    if not left:
                        player_x_change = 0
                    right = False
                # set character y velocity to 0 when 'w' is released
                case pygame.K_w:
                    if not down:
                        player_y_change = 0
                    up = False
                # set character y velocity to 0 when 's' is released
                case pygame.K_s:
                    if not up:
                        player_y_change = 0
                    down = False

    # calling player method to paint the player on the screen
    player_x += player_x_change
    player_y += player_y_change
    player(player_x, player_y)

    # updating pygame for every loop iteration
    pygame.display.update()
