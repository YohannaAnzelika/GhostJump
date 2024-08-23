from random import randint, random
import pygame

class Rintang(pygame.sprite.Sprite):
    ground = 410

    def __init__(self):
        super().__init__()
        imageName = "Onion.png" if randint(0, 1) else "batu.png"
        self.image = pygame.image.load(f"Assets/Rintangan/{imageName}").convert_alpha()
        self.image = pygame.transform.scale(self.image, (140,140) )
        self.rect = self.image.get_rect(topleft = (1100, Rintang.ground))
        pygame.mask.from_surface(self.image)

    def update(self):
        if self.rect.right <= 0:
            self.kill()
        self.rect.x -= 10 