import pygame
import pygame.freetype

# dasar dasar game
pygame.init()
width = 1000
height = 600
FPS = 60
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font('Assets/Font_type/Creepster-Regular.ttf',56)
sajen = pygame.font.Font('Assets/Font_type/Eater-Regular.ttf',32)

obstacle_timer = pygame.USEREVENT + 1
sesajen_timer = pygame.USEREVENT + 2

pygame.time.set_timer(obstacle_timer, 2000)
pygame.time.set_timer(sesajen_timer, 3000)
