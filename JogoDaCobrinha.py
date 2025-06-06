import pygame
from pygame.locals import *
import random

WINDOW_SIZE = (600, 600)
PIXEL_SIZE = 10


def collision(pos1, pos2):
    return pos1 == pos2


def off_limits(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True


def random_on_grid():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake')

snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_surface.fill((255, 255, 255))
snake_direction = K_LEFT

apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
apple_surface.fill((255, 0, 0))
apple_pos = random_on_grid()

acabou = False
fonte = pygame.font.SysFont('arial', 25, True, True)
pontos = 0

def restart_game():
    global snake_pos, apple_pos, snake_direction, pontos
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    apple_pos = random_on_grid()
    acabou = False
    pontos = 0

def restart():
    global snake_pos, apple_pos, snake_direction, pontos, acabou
    apple_pos = random_on_grid()
    acabou = False
    pontos = 0

while True:
    pygame.time.Clock().tick(15)
    screen.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto_formado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    screen.blit(apple_surface, apple_pos)

    if collision(apple_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        apple_pos = random_on_grid()
        pontos += 1

    if pontos > 10:
        acabou = True
        fonte_fim = pygame.font.SysFont('arial', 30, False, True)
        mensagem_fim = 'Para reinicar se caso queira, tecle "R".'
        texto_formatado_fim = fonte_fim.render(mensagem_fim, True, (255, 255, 255))
        ret_texto = texto_formatado_fim.get_rect()
        
    while acabou:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    print('hihihi')
                    restart()

        ret_texto.center = (300, 300)
        screen.blit(texto_formatado_fim, ret_texto)
        pygame.display.update()
                        
    for pos in snake_pos:
        screen.blit(snake_surface, pos)

    for i in range(len(snake_pos) - 1, 0, -1):
        if collision(snake_pos[0], snake_pos[i]):
            restart_game()
            break
        snake_pos[i] = snake_pos[i - 1]

    if off_limits(snake_pos[0]):
        restart_game()

    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])
    screen.blit(texto_formado, (10, 5))

    pygame.display.update()
