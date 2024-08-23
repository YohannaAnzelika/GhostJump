    # UNTUK LOGIC PEMBUATAN SESAJEN PALSU ATAU ASLI DI LINE 168
    # UNTUK LOGIC LOMPAT NYA KEBALIK ATAU ENGGAK DI FILE GHOST LINE 21-40


# import modul
import pygame
import json
from sys import exit
from random import randint
from SesajenPalsu import SesajenPalsu
from rintangan import *
from ghost import *
from Skor import Skor
from dasar import *
from sesajen import *
from button import *
from background import *

filename = "data.json"

# method hantu bertabrakan dengan rintangan
def collision_sprite(a):
    # jika hantu bertabrakan akan dijalankan
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        player.sprite.game_over_sound_play() # play suara game_over_sound_play()
        obstacle_group.empty() # mengosongkan grup obstacle
        sesajen_group.empty()  #mengosongkan grup sesajen
        sesajen_palsu_group.empty()  #mengosongkan grup sesajen palsu
        bg_music.stop() # backsound akan dimatikan
        return False, 0
    elif a == 3 : 
        return False, a
    else :
        return True, a
    
# method player mengenai sesajen
def onSesajenCollide():
    if pygame.sprite.spritecollide(player.sprite, sesajen_group, True):
        player.sprite.get_sesajen_sound_play()
        return True
    else:
        return False
    
def onSesajenPalsuCollide():
    if pygame.sprite.spritecollide(player.sprite, sesajen_palsu_group, True):
        player.sprite.get_sesajen_sound_play()
        return True
    else:
        return False
    
# method unutk membaca data pada file json
def jsonread():
    with open(filename, "r") as f:
        temp = json.load(f)
        for data in temp:
            cn = data["Sesajen"] 
            sk = data["skor"]
            thm = data["thema"]
        return cn, sk, thm
    
# method untuk mengedit data file json
def jsonedit(cn, sk, thm):
    new_data = {}
    with open(filename, "r") as f:
        current_data = json.load(f)
        del current_data[0]
    with open(filename, "w") as f:
        json.dump(current_data, f, indent = 4)
    with open(filename, "r") as f:
        current_data = json.load(f)

    new_data["Sesajen"]  = cn
    new_data["skor"] = sk
    new_data["thema"] = thm
    current_data.append(new_data)

    with open(filename, "w") as f:
        json.dump(current_data, f, indent = 4)
    
    return cn, sk, thm


pygame.init()
pygame.display.set_caption("Ghost Jump")

cn, sk, thm = jsonread() # deklarasi variable cn, sk, thm = jsonread()
icon = pygame.image.load('Assets//Bg/Icon.png') 
bg_music = pygame.mixer.Sound("Assets/Suara/Backsound.mp3") # backsound
pygame.display.set_icon(icon) # mengatur icon
game_active = False
sesajen_count= 0
game_state = 1
cond_button = ""
bg_music.set_volume(0.1) # set voulume
clock = pygame.time.Clock()
skor_count = 0
thema = thm
cond = False

# deklarasi objek
bg1 = Bg('Background1')
bg2 = Bg('Background2')

button_play = Button_play()        
button_resume = Button_resume()
button_pause = Button_Pause()
button_home = Button_home()
button_theme_1 = Button_Theme(0, 150, 250)
button_theme_2 = Button_Theme(1, 650, 250)

obstacle_group = pygame.sprite.Group()
sesajen_group = pygame.sprite.Group()
sesajen_palsu_group = pygame.sprite.Group()


player = pygame.sprite.GroupSingle()
player_1 = player.add(Hantu("pocong"))


# deklarasi vaiable unutuk game over
game_over = font.render("Game Over", False, ("#a30202"))
game_over_rect = game_over.get_rect(center = (500, 150))
board_surf = pygame.image.load("Assets/Bg/Game_over.jpg")
board_surf = pygame.transform.scale(board_surf,(1000,600))
board_rect = board_surf.get_rect(center = (500, 300))

while True:
    cn, sk, thm = jsonread() # deklarasi variable cn, sk, thm = jsonread()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Rintang())
            if event.type == sesajen_timer:
                # pembuatan sesajen asli atau palsu secara random menggunakan fungsi randint()
                # randint(0, 10) != 0 mengartikan kemungkinan sesajen palsu adalah 1 dari 10
                # dst...
                isPalsu = randint(0, 10) == 5
                if isPalsu:
                    sesajen_palsu_group.add(SesajenPalsu())
                else:
                    sesajen_group.add(Sesajen(sum, cn))

        elif game_active == False and game_state == 0: 
            button_home.button_display_game_over()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_home.rect_game_over.collidepoint(pygame.mouse.get_pos()):
                    game_active = False       
                    game_state = 1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if game_state == 0:
                    bg_music.play()
                game_state = 2
                skor_count = 0 
                sesajen_count = 0
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)






    # TAMPILAN HOME
    if game_active == False and game_state == 1:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_play.rect.collidepoint(pygame.mouse.get_pos()):
                    button_pressed = button_play.action()
                    bg_music.play()
                    game_state = 2
                    skor_count = 0
                    sesajen_count = 0
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)
            elif button_theme_1.rect.collidepoint(pygame.mouse.get_pos()):
                thema = 0
            elif button_theme_2.rect.collidepoint(pygame.mouse.get_pos()):
                thema = 1

        bg = bg1 if thema == 0 else bg2
        bg.display_bg_blur()

        bg.display_logo()
        
        Sesajen(sesajen_count, cn).display_sesajen()
        button_play.button_display()
        button_theme_1.button_display()
        button_theme_2.button_display()

        intro_message = font.render("Press Button to run", False, ("#f9981f"))
        intro_message_rect = intro_message.get_rect(center = (250, 150))


    if skor_count > 0 and skor_count <= 0.01:
        bg_music.play()

    # TAMPILAN GAME BERJALAN
    if game_active:
        
        (bg1 if thema == 0 else bg2).display_bg()

        score = Skor(int(skor_count))
        score.update()
        
        player.draw(screen)
        player.update()

        newSesajen = Sesajen(sesajen_count, cn).display_sesajen_in_run()
        
        sesajen_group.draw(screen)
        sesajen_group.update()

        sesajen_palsu_group.draw(screen)
        sesajen_palsu_group.update()
        
        obstacle_group.draw(screen)
        obstacle_group.update()

        # jika status 2 dan game_active True maka game dumulai        
        if game_active == True and game_state == 2:
            skor_count += 0.01

            button_pause.button_display()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_pause.rect.collidepoint(pygame.mouse.get_pos()):
                        cond = button_pause.action(True)
            
            if cond == True:
                game_state = 3

        # memanggil method collision_sprite() mengatur jika player bertabrakan dengan obstacle
        game_active, game_state = collision_sprite(game_state)
        
        if onSesajenCollide():
            sesajen_count += 1
            Sesajen(sesajen_count, cn)
        if onSesajenPalsuCollide():
            player.sprite.flipJump()
        

    # GAME OVER
    if  game_active == False and game_state == 0:
        player.sprite.resetJump()
        score_message = font.render(f"{'High Score' if skor_count > sk else 'Your'} Score {int(skor_count)}", False, pygame.Color("#a30202"))
        total_sesajen_message = font.render(f"Total Sesajen  {sesajen_count}", False, pygame.Color("#a30202"))

        score_message_rect = score_message.get_rect(center = (500, 250))
        total_sesajen_message_rect = score_message.get_rect(center = (500, 320))

        screen.blit(board_surf, board_rect)
        screen.blit(game_over, game_over_rect)

        screen.blit(score_message, score_message_rect)
        screen.blit(total_sesajen_message, total_sesajen_message_rect)

        intro_message = font.render("Press space to run", False, ("#a30202"))
        intro_message_rect = intro_message.get_rect(center = (500, 500))

        screen.blit(intro_message, intro_message_rect)
        kn = Sesajen(sesajen_count, cn).sesajen_return(cn)
        if sk < int(skor_count):
            jsonedit(kn, int(skor_count), thema)
        else:
            jsonedit(kn, sk, thema)
            
            

    # PAUSE
    if game_active == False and game_state == 3:
        button_pause.display_board()
        button_resume.button_display()
        button_home.button_display()
        bg_music.stop()

        # CONTINUE
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_resume.rect.collidepoint(pygame.mouse.get_pos()):
                cond = False
                skor_count = 0
                sesajen_count = 0
                game_active = True
                game_state = 2

        # HOME
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_home.rect.collidepoint(pygame.mouse.get_pos()):
                cond = False
                game_active = False            
                sesajen_count = 0
                skor_count = 0
                game_state = 1
                bg_music.stop()

    pygame.display.update()
    clock.tick(FPS)