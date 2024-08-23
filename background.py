import pygame
from dasar import *

class BaseBg():
    def __init__(self):
        self.logo_surf = pygame.image.load('Assets/Bg/Icon.png')
        self.logo_rect = self.logo_surf.get_rect(center = (500, 150))

    def display_logo(self):
        screen.blit(self.logo_surf,self.logo_rect)

# untuk menampilkan tema 1
class Bg(BaseBg):
    def __init__(self, backgroundName: str):
        super().__init__()
        self.sky_surface = pygame.image.load(f'Assets/Bg/{backgroundName}.jpg').convert_alpha()
        self.sky_surface = pygame.transform.scale(self.sky_surface,(1000,600))
        self.sky_surface_blur = pygame.image.load(f'Assets/Bg/{backgroundName}_blur.jpg').convert_alpha()
        self.sky_surface_blur = pygame.transform.scale(self.sky_surface_blur,(1000,600))
        self.ground_surface = pygame.image.load('Assets/Bg/tanah.png').convert_alpha()
        self.ground_surface = pygame.transform.scale(self.ground_surface,(1000,100))
        self.ground_surface_blur = pygame.image.load('Assets/Bg/tanah_blur.png').convert_alpha()
        self.ground_surface_blur = pygame.transform.scale(self.ground_surface_blur,(1000,100))

    def display_bg(self):
        screen.blit(self.sky_surface, (0,0))
        screen.blit(self.ground_surface, (0,500))

    def display_bg_blur(self):
        screen.blit(self.sky_surface_blur, (0,0))
        screen.blit(self.ground_surface_blur, (0,500))
