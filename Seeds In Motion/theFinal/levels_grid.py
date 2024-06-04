import pygame
import level_specs
import time

pygame.init()

width, height = 1060, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sokoban GAME / HEM-ES")

background = pygame.image.load("assets/just_back.png")
font = pygame.font.Font("assets/Anokha-Bold.ttf", 30)


level_button = pygame.image.load("assets/crate_11.png")

pygame.mixer.init()




button_width = level_button.get_width()
button_height = level_button.get_height()


margin_x = 100  
margin_y = 120  


total_grid_width = (button_width * 5) + (margin_x * 4)  
total_grid_height = (button_height * 2) + margin_y  


start_x = (width - total_grid_width) // 2
start_y = (height - total_grid_height) // 2


level_buttons_rects = [
    level_button.get_rect(topleft=(start_x + (button_width + margin_x) * i, start_y)) for i in range(5)
] + [
    level_button.get_rect(topleft=(start_x + (button_width + margin_x) * i, start_y + button_height + margin_y)) for i in range(5)
]


def render_text(text, position):
    text_surface = font.render(text, True, (246, 221, 204))
    win.blit(text_surface, position)



def offline_game():

    pygame.mixer.init()
    click_sound = pygame.mixer.Sound("assets/entring.wav")
    pygame.mixer.Sound("assets/11_-_Clearing_.ogg").play().set_volume(0.4)


    running = True
    clock = pygame.time.Clock()
    
   
    while running:
        win.blit(background , (0,0))  
        
        
        for i, button_rect in enumerate(level_buttons_rects):
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                win.blit(level_button, button_rect)
                render_text(str(i + 1), (button_rect.topleft[0] + 10, button_rect.topleft[1] - 10))

          
            else:
                win.blit(level_button, button_rect)
                render_text(str(i + 1), (button_rect.topleft[0] + 10, button_rect.topleft[1]  + 5 ))
                
                
               

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                
                for i, button_rect in enumerate(level_buttons_rects):
                    if button_rect.collidepoint(mouse_pos):

                        click_sound.play().set_volume(0.8)
                        pygame.time.delay(1200)
                        pygame.mixer.quit()
                    
                        if ( i+1 == 1):
                            level_specs.GetLvl1()

                        if ( i+1 == 2):
                            level_specs.GetLvl2()

                        if ( i+1 == 3):
                            level_specs.GetLvl3()
                        
                        if ( i+1 == 4):
                            level_specs.GetLvl4()

                        if ( i+1 == 5):
                            level_specs.GetLvl5()

                        if ( i+1 == 6):
                            level_specs.GetLvl6()

                        if ( i+1 == 7):
                            level_specs.GetLvl7()

                        if ( i+1 == 8):
                            level_specs.GetLvl8()

                        if ( i+1 == 9):
                            level_specs.GetLvl9()
                        
                        if ( i+1 == 10):
                            level_specs.GetLvl10()
        
                       
        clock.tick(60)  
        pygame.display.update()

    pygame.quit()