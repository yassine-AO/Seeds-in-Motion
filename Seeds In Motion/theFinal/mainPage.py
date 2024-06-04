import pygame
from levels_grid import offline_game
from level_specs import GetOnline

pygame.init()


width, height = 1060, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Seeds in Motion / HEM ES")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

background = pygame.image.load("assets/menu_interface.png")

offlineButton = pygame.image.load("assets/one_player_button.png")
onlineButton = pygame.image.load("assets/two_player_button.png")

background_mute = pygame.image.load("assets/menu_mute.png")

offline_button = onlineButton.get_rect(center=(530 , 407))
online_button = onlineButton.get_rect(center=(530 , 490))



def main():
    
    pygame.mixer.init()
    main_music = pygame.mixer.Sound("assets/23_-_Road.ogg")
    main_music.play(10 , 0 , 800).set_volume(0.5)
    mute = False

    run = True
    win.blit(background , (0,0))
    while run:
        
        win.blit(offlineButton, offline_button)
        win.blit(onlineButton, online_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if offline_button.collidepoint(mouse_pos):
                    print("Ha7na dakhlin levelssss")
                    pygame.mixer.quit()
                    offline_game()

                elif online_button.collidepoint(mouse_pos):
                    print("Ha7na dakhlin l'Online awlidiii...")
                    GetOnline()
                    #run = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    mute = not mute
                    if mute:
                     # Mute the sound (set volume to 0.0)
                     main_music.set_volume(0.0)
                     win.blit(background_mute , (0,0))
                    else:
                     # Unmute the sound and set volume back to 0.5
                     main_music.set_volume(0.5)
                     win.blit(background , (0,0))
            
            pygame.display.update()

                
        pygame.display.update()

    pygame.quit()


