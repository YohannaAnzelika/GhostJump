import pygame
from abc import ABC, abstractmethod

# Parrent class
class Player(pygame.sprite.Sprite, ABC):
    ground = 520

    def __init__(self):
        super().__init__()

        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('Assets/Suara/jump.mp3')
        self.sesajen_get = pygame.mixer.Sound('Assets/Suara/get_point.mp3')
        self.game_over_sound = pygame.mixer.Sound('Assets/Suara/game_over.mp3')
        self.is_jump_normal = True

    @abstractmethod
    def masking(self):
        pass
            
    def flipJump(self):
        self.is_jump_normal = not self.is_jump_normal

    def resetJump(self):
        self.is_jump_normal = True

    def jump(self):
        self.gravity = -24
        self.player_index = 0
        self.jump_sound.play()
        self.jump_sound.set_volume(0.15)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if self.rect.bottom >= Player.ground:
            if keys[pygame.K_UP] and self.is_jump_normal:
                self.jump()
            elif keys[pygame.K_DOWN] and not self.is_jump_normal:
                self.jump()
            

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= Player.ground:
            self.rect.bottom = Player.ground
    
    @abstractmethod
    def animation_state(self):
        pass

    def game_over_sound_play(self):
        self.game_over_sound.play()
        self.game_over_sound.set_volume(0.2)

    def get_sesajen_sound_play(self):
        self.sesajen_get.play()
        self.sesajen_get.set_volume(0.3)

    def update(self):
        self.masking()
        self.player_input()
        self.apply_gravity()
        self.animation_state()

# berfungsi unutk mengatur animasi player pada saat lompat atau berlari
class Hantu(Player):
    def __init__(self, filename: str):
        super().__init__()
        player_walk1 = pygame.image.load(f"Assets/Ghost/{filename}_1.png").convert_alpha()
        player_walk1 = pygame.transform.scale_by(player_walk1, 0.2)
        player_walk2 = pygame.image.load(f"Assets/Ghost/{filename}_2.png").convert_alpha()
        player_walk2 = pygame.transform.scale_by(player_walk2, 0.2)
        self.player_walk = [player_walk1,player_walk2]

        player_jump1 = pygame.image.load(f"Assets/Ghost/{filename}_2.png").convert_alpha()
        player_jump1 = pygame.transform.scale_by(player_jump1, 0.2)
        self.player_jump = [player_jump1]
        self.player_index = 0

        self.image = self.player_walk[self.player_index]        
        self.rect = self.image.get_rect(midbottom = (100, Player.ground))

    def masking(self):
        for masking1 in self.player_walk:
            pygame.mask.from_surface(masking1)
        for masking2 in self.player_jump:
            pygame.mask.from_surface(masking2)
        
    def animation_state(self):         
        if self.rect.bottom < Player.ground:
            # jump
            self.player_index += 1
            if self.player_index >= len(self.player_jump):
                self.player_index = 0
            self.image = self.player_jump[int(self.player_index)]
        else:
            # walk
            self.player_index += 0.15
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]