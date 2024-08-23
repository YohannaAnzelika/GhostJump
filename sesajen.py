import pygame
from dasar import *

# melakukan perhitungan sesajen yang didapat dan menampilkan sesajen saat game akan mulai
class Sesajen(pygame.sprite.Sprite):
    def __init__(self, sum, cn):
        super().__init__()

        self.__sesajen_display = pygame.image.load('Assets/sajen/Sesajen.png').convert_alpha()
        self.__sesajen_display = pygame.transform.scale(self.__sesajen_display,(60,60))

        self.__sesajen_index = 0
        self.__sesajen_list = [self.__sesajen_display]
        
        self.image = self.__sesajen_list[self.__sesajen_index]
        self.rect = self.image.get_rect(midbottom = (1100, 250))
        
        self.__sesajen_display_rect = self.image.get_rect(center = (450, 40))
        self.__total_sesajen = sum
        self.__sesajen = sajen.render(f"{cn}", False, ("#e6e7e7"))
        self.__sesajen_in_run = sajen.render(f"{sum}", False, ("#e6e7e7"))
        self.__sesajen_rect = self.__sesajen.get_rect(midtop = (520, 20))
        

    def mask(self):
        for i in self.__sesajen_list:
            pygame.mask.from_surface(i)

    def animation_state(self):
            self.__sesajen_index += 0.1
            if self.__sesajen_index >= len(self.__sesajen_list):
                self.__sesajen_index = 0
            self.image = self.__sesajen_list[int(self.__sesajen_index)]
    
    def display_sesajen(self):
        screen.blit(self.__sesajen_display, self.__sesajen_display_rect)
        screen.blit(self.__sesajen, self.__sesajen_rect)
    
    def display_sesajen_in_run(self):
        screen.blit(self.__sesajen_display, self.__sesajen_display_rect)
        screen.blit(self.__sesajen_in_run, self.__sesajen_rect)

    def destroy(self):
        if self.rect.x <= -80:
            self.kill()

    def sesajen_return(self, cn):
        return self.__total_sesajen + cn

    def update(self):
        self.mask()
        self.animation_state()
        self.rect.x -= 10 