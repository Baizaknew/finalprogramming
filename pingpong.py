import pygame as pg
import random

pg.init()
pg.font.init()

TITLE = 'Game'
WIDTH = 800
HEIGHT = 480

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 15
PLATFORM_SPEED = 10

platform_rect = pg.rect.Rect(WIDTH/2 - PLATFORM_WIDTH/2,
                             HEIGHT - PLATFORM_HEIGHT*2,
                             PLATFORM_WIDTH,
                             PLATFORM_HEIGHT)

BALL_RADIUS = 15
BALL_SPEED = 10
ball_first_collide = False
ball_x_speed = 0
ball_y_speed = BALL_SPEED
ball_rect = pg.rect.Rect(WIDTH/2 - BALL_RADIUS,
                         HEIGHT/2 - BALL_RADIUS,
                         BALL_RADIUS * 2,
                         BALL_RADIUS * 2)

score = 0

ARIAL_FONT_PATH = pg.font.match_font('arial')
ARIAL_FONT_48 = pg.font.Font(ARIAL_FONT_PATH, 48)
ARIAL_FONT_36 = pg.font.Font(ARIAL_FONT_PATH, 36)

screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption(TITLE)

clock = pg.time.Clock()

game_over = False
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            continue
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                continue
            elif event.key == pg.K_r:
                game_over = False

                platform_rect.centerx = WIDTH / 2
                platform_rect.bottom = HEIGHT - PLATFORM_HEIGHT

                ball_rect.center = [WIDTH / 2, HEIGHT / 2]
                ball_x_speed = 0
                ball_y_speed = BALL_SPEED
                ball_first_collide = False

                score = 0

    screen.fill(BLACK)

    if not game_over:
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            platform_rect.x -= PLATFORM_SPEED
        elif keys[pg.K_d]:
            platform_rect.x += PLATFORM_SPEED

    if platform_rect.colliderect(ball_rect):
        if not ball_first_collide:
            if random.randint(0, 1) == 0:
                ball_x_speed = BALL_SPEED
            else:
                ball_x_speed = -BALL_SPEED

            ball_first_collide = True

        ball_y_speed = -BALL_SPEED

        score += 1

    pg.draw.rect(screen, WHITE, platform_rect)

    ball_rect.x += ball_x_speed
    ball_rect.y += ball_y_speed

    if ball_rect.bottom >= HEIGHT:
        game_over = True
        ball_y_speed = -BALL_SPEED
    elif ball_rect.top <= 0:
        ball_y_speed = BALL_SPEED
    elif ball_rect.left <= 0:
        ball_x_speed =  BALL_SPEED
    elif ball_rect.right >= WIDTH:
        ball_x_speed = -BALL_SPEED

    pg.draw.circle(screen, WHITE, ball_rect.center, BALL_RADIUS)

    score_surface = ARIAL_FONT_48.render(str(score), True, WHITE)
    if not game_over:
        screen.blit(score_surface, [WIDTH/2 - score_surface.get_width() / 2, 15])
    else:
        retry_surface = ARIAL_FONT_36.render('press R to restart', True, WHITE)
        screen.blit(score_surface, [WIDTH / 2 - score_surface.get_width() / 2, HEIGHT / 3])
        screen.blit(retry_surface, [WIDTH / 2 - retry_surface.get_width() / 2,
                                    HEIGHT / 3 + score_surface.get_height()])

    clock.tick(FPS)

    pg.display.flip()

pg.quit()
