import pygame
from Player import Player
from Grid import Grid
from BoxMovable import BoxMovable
from BoxMovableOnline import BoxMovableOnline
from network import Network
import mainPage
import time

pygame.init()

width, height = 1060, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sokoban GAME / HEM-ES")

background1 = pygame.image.load("assets/level_music.png")

background_congrats = pygame.image.load("assets/congrats.png")

background_mute = pygame.image.load("assets/level_mute.png")

victory_image = pygame.image.load("assets/just_back.png") 

img =  pygame.image.load("assets/seed.png")

mute = False

class levels:

    def __init__(self, grid, player, movables):
        self.grid = grid
        self.player = player
        self.movables = movables

        self.box_in_place = False

        

        self.img =  pygame.image.load("assets/seed.png")

        self.win_sound = pygame.mixer.Sound("assets/flowerput.wav")
        self.sound_played = False

        self.main_music = pygame.mixer.Sound("assets/Village.ogg")

        self.restart_sound = pygame.mixer.Sound("assets/restart.wav")
        

        self.initial_player_state = (player.grid_x, player.grid_y)
        self.initial_movables_states = [(m.grid_x, m.grid_y) for m in movables]

    def reset_level(self):
        
        self.player.grid_x, self.player.grid_y = self.initial_player_state
        self.player.update_pixel_position()

        
        for movable, (grid_x, grid_y) in zip(self.movables, self.initial_movables_states):
            movable.grid_x, movable.grid_y = grid_x, grid_y
            movable.update_pixel_position()

        
        self.restart_sound.play().set_volume(0.8)
        
    
    def draw(self, win):

        win.blit(background1, (0, 0))
        self.grid.dessinerGrid(win)
        self.player.draw(win)
        for movable in self.movables:  
            movable.draw(win)

    def check_victory(self):
        pygame.mixer.init()

        for box in self.movables:
            if (box.grid_y, box.grid_x) not in self.grid.checkpoints:
                self.sound_played = False
                return False    
        return True
    
    def update_images(self):
        #checks if the box is in place
        if self.box_in_place == True:
            self.img = pygame.image.load("assets/flower.png")
            
        else:
            self.img =  pygame.image.load("assets/seed.png")
            #giving the img as conditions and according them to the movable in movables list
        for movable in self.movables:
            movable.img = self.img
            
        






##########################################################LEVEL 1############################################################################
checkpoints = [(3,2)]
nonPassable = []
grid = Grid(50, 10, 9, nonPassable, checkpoints)

WHITE = (255, 255, 255)
player = Player(2, 1, WHITE, grid, grid.GetGridWidth(), grid.GetGridHeight())

movables = [ 
            BoxMovable(2, 2, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
 
        ]

level1 = levels(grid, player, movables)

def GetLvl1():
    showLevel(level1)


###############################################################################################################################################

##########################################################LEVEL 2##############################################################################

checkpoints = [(3, 2), (3, 3)]
nonPassable = []
grid = Grid(50, 10, 9, nonPassable, checkpoints)

WHITE = (255, 255, 255)
player = Player(1, 1, WHITE, grid, grid.GetGridWidth(), grid.GetGridHeight())

movables = [ 
            BoxMovable(2, 2, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(2, 3, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),    
        ]

level2 = levels(grid, player, movables)

def GetLvl2():
    showLevel(level2)

###############################################################################################################################################

##########################################################LEVEL 3##############################################################################

checkpoints = [(4, 2), (4, 3)]
nonPassable = []
grid = Grid(50, 10, 9, nonPassable, checkpoints)

WHITE = (255, 255, 255)
player = Player(1, 1, WHITE, grid, grid.GetGridWidth(), grid.GetGridHeight())

movables = [ 
            BoxMovable(2, 2, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(3, 3, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
             
        ]

level3 = levels(grid, player, movables)

def GetLvl3():
    showLevel(level3)


################################################################################################################################################ 
    
##########################################################LEVEL 4 ##############################################################################

checkpoints = [(5, 2), (6, 3), (7, 4)]
nonPassable = []
grid = Grid(50, 10, 9, nonPassable, checkpoints)

WHITE = (255, 255, 255)
player = Player(1, 1, WHITE, grid, grid.GetGridWidth(), grid.GetGridHeight())

movables = [ 
            BoxMovable(2, 2, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(3, 3, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(4, 4, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),  
        ]

level4 = levels(grid, player, movables)

def GetLvl4():
    showLevel(level4)


################################################################################################################################################ 
    
##########################################################LEVEL 5 ##############################################################################

checkpoints = [(3, 4), (4, 5)]
nonPassable = [(3, 3), (4, 3)]
grid = Grid(50, 10, 9, nonPassable, checkpoints)

WHITE = (255, 255, 255)
player = Player(1, 1, WHITE, grid, grid.GetGridWidth(), grid.GetGridHeight())

movables = [ 
            
            BoxMovable(3, 2, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(4, 2, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),  
        ]

level5 = levels(grid, player, movables)

def GetLvl5():
    showLevel(level5)


################################################################################################################################################
    
##########################################################LEVEL 6 ##############################################################################

checkpoints = [(6, 2), (7, 4), (8, 3)]
nonPassable = []
grid = Grid(50, 10, 9, nonPassable, checkpoints)

WHITE = (255, 255, 255)
player = Player(1, 1, WHITE, grid, grid.GetGridWidth(), grid.GetGridHeight())

movables = [ 
            BoxMovable(2, 2, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(3, 4, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(4, 3, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),  
        ]

level6 = levels(grid, player, movables)

def GetLvl6():
    showLevel(level6)


################################################################################################################################################

##########################################################LEVEL 7 ##############################################################################

checkpoints = [(6, 2), (7, 3), (8, 4), (9, 5)]
nonPassable = []
grid = Grid(50, 10, 9, nonPassable, checkpoints)

WHITE = (255, 255, 255)
player = Player(1, 1, WHITE, grid, grid.GetGridWidth(), grid.GetGridHeight())

movables = [ 
            BoxMovable(2, 2, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(3, 3, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(4, 4, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(5, 5, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),  
        ]

level7 = levels(grid, player, movables)

def GetLvl7():
    showLevel(level7)


################################################################################################################################################
    
##########################################################LEVEL 8 ##############################################################################

checkpoints = [(9, 2), (9, 3), (9, 4), (9, 5), (9, 6)]
nonPassable = [(4, 8), (5, 3), (5, 7), (6, 4), (6, 8), (7, 1), (7, 5), (8, 2), (8, 6)]
grid = Grid(50, 10, 9, nonPassable, checkpoints)

WHITE = (255, 255, 255)
player = Player(1, 1, WHITE, grid, grid.GetGridWidth(), grid.GetGridHeight())

movables = [ 
            BoxMovable(2, 2, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(3, 3, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(4, 4, img, grid, grid.GetGridWidth(), grid.GetGridHeight()), 
            BoxMovable(5, 5, img, grid, grid.GetGridWidth(), grid.GetGridHeight()), 
            BoxMovable(6, 6, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),  
        ]

level8 = levels(grid, player, movables)

def GetLvl8():
    showLevel(level8)


################################################################################################################################################
    
##########################################################LEVEL 9 ##############################################################################

checkpoints = [(8, 2), (8, 3), (8, 4), (8, 5), (8, 6)]
nonPassable = [(5, 4), (5, 6), (6, 1), (6, 3), (6, 5), (7, 2), (7, 4), (7, 6), (8, 1), (8, 7)]
grid = Grid(50, 10, 9, nonPassable, checkpoints)

WHITE = (255, 255, 255)
player = Player(1, 1, WHITE, grid, grid.GetGridWidth(), grid.GetGridHeight())

movables = [ 
            BoxMovable(2, 2, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(3, 3, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(4, 4, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),  
            BoxMovable(5, 3, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(6, 2, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
        ]

level9 = levels(grid, player, movables)

def GetLvl9():
    showLevel(level9)


################################################################################################################################################
    
##########################################################LEVEL 10 ##############################################################################

checkpoints = [(8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)]
nonPassable = [(6, 3), (6, 7), (7, 2), (7, 6), (8, 4), (8, 8)]
grid = Grid(50, 10, 9, nonPassable, checkpoints)

WHITE = (255, 255, 255)
player = Player(1, 1, WHITE, grid, grid.GetGridWidth(), grid.GetGridHeight())

movables = [ 
            BoxMovable(2, 2, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(2, 3, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(2, 4, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),  
            BoxMovable(3, 5, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(4, 6, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
            BoxMovable(5, 7, img, grid, grid.GetGridWidth(), grid.GetGridHeight()),
        ]

level10 = levels(grid, player, movables)

def GetLvl10():
    showLevel(level10)


################################################################################################################################################
    
############################################################ONLINE LVL##########################################################################

class onlinelvl:

    def __init__ (self):

        self.network = Network()

        self.checkpoints = [(1, 2), (1, 5)]

        self.nonPassable = [(0, 0), (0, 1), (0, 2), (2, 0), (2, 1), (2, 2)]

        self.grid = Grid(50, 10, 9, self.nonPassable, self.checkpoints)

        self.movables = [ 
            BoxMovableOnline(2, 1, (5, 200, 200), self.grid, self.grid.GetGridWidth(), self.grid.GetGridHeight()),
            BoxMovableOnline(3, 3, (5, 200, 200), self.grid, self.grid.GetGridWidth(), self.grid.GetGridHeight()),
        ]

        self.p1 = Player(5, 5, (0, 255, 255), self.grid, self.grid.GetGridWidth(), self.grid.GetGridHeight())  
        self.p2 = Player(5, 5, (0, 255, 255), self.grid, self.grid.GetGridWidth(), self.grid.GetGridHeight())

        #self.startPos = read_pos(self.network.getPos())

    @staticmethod
    def read_pos(pos_str):
        player_pos_str = pos_str.split("|")[0]
        x, y = player_pos_str.split(",")
        return int(x), int(y)
    
    @staticmethod
    def make_pos(tup):
        return str(tup[0]) + "," + str(tup[1])
    
    def redrawWindow(self, win, player, player2, movable):
        
        self.grid.dessinerGrid(win)  # Draw the grid
        player.draw(win)
        player2.draw(win)
        for m in movable:  
                m.draw(win)
        pygame.display.update()
    
    



def showOnline(level):
    run = True
    clock = pygame.time.Clock()
    #startPos = level.read_pos(level.network.getPos())
    move_made = False

    while run:
        win.blit(background1 ,(0,0))
        clock.tick(60)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN and not move_made:
                    if event.key == pygame.K_LEFT:
                        level.p1.movingArround(level.movables, -1, 0)
                        move_made = True
                    elif event.key == pygame.K_RIGHT:
                        level.p1.movingArround(level.movables, 1, 0)
                        move_made = True
                    elif event.key == pygame.K_UP:
                        level.p1.movingArround(level.movables, 0, -1)
                        move_made = True
                    elif event.key == pygame.K_DOWN:
                        level.p1.movingArround(level.movables, 0, 1)
                        move_made = True
                if event.type == pygame.KEYUP:
                    move_made = False

        p2Pos = level.read_pos(level.network.send(level.make_pos((level.p1.grid_x, level.p1.grid_y))))
        level.p2.grid_x = p2Pos[0]
        level.p2.grid_y = p2Pos[1]
        level.p2.update_pixel_position()

        level.redrawWindow(win, level.p1, level.p2, level.movables)


    pygame.quit()

levelOnline = onlinelvl()
def GetOnline():
    showOnline(levelOnline)
####################################################################################################################################






def showLevel(level):
    run = True
    clock = pygame.time.Clock()
    

    font = pygame.font.Font("assets/Anokha-Bold.ttf", 30)
    start_time = pygame.time.get_ticks()

    pygame.mixer.init()
    level.main_music.play(10 , 0 , 800).set_volume(0.5)

    def render_text(text, position):
            text_surface = font.render(text, True, (246, 221, 204))
            win.blit(text_surface, position)

    
    mute = False
    
    
    background = background1
    victory = False
    
    while run:
        win.blit(background ,(0,0))
        

        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60

        time_str = f"{minutes:02d}:{seconds:02d}"

        if not victory:
         
         render_text(time_str, (102, 190))
         render_text(str(level.player.player_movement_counter), (105 , 290))
         render_text(str(level.player.box_movement_counter), (107 , 412))

        level.grid.dessinerGrid(win)
        level.player.draw(win)
        for movable in level.movables:
            movable.draw(win)

        

        if level.check_victory():
         #give the box in place true to update the image according to the condition
         level.box_in_place = True
         level.update_images()
         victory = True

         if not level.sound_played:
            level.win_sound.play()
            level.sound_played = True
         background = background_congrats
         
         
         



        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    level.player.movingArround(level.movables, -1, 0)
                elif event.key == pygame.K_RIGHT:
                    level.player.movingArround(level.movables, 1, 0)
                elif event.key == pygame.K_UP:
                    level.player.movingArround(level.movables, 0, -1)
                elif event.key == pygame.K_DOWN:
                    level.player.movingArround(level.movables, 0, 1)
                elif event.key == pygame.K_r:
                    level.reset_level()


                if event.key == pygame.K_m:
                    mute = not mute
                    if mute:
                     
                     level.main_music.set_volume(0.0)
                     background = background_mute
                     
                    else:
                     
                     level.main_music.set_volume(0.5)
                     background = background1
                     win.blit(background , (0,0))


                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_h:
                   pygame.mixer.quit()
                   mainPage.main()
        
        
        
  
        pygame.display.update()
        clock.tick(60)

    pygame.quit()



if __name__ == "__main__":
    GetLvl1()
    GetLvl2()
    GetLvl3()
    GetLvl4()
    GetLvl5()
    GetLvl6()
    GetLvl7()
    GetLvl8()
    GetLvl9()
    GetLvl10()
    GetOnline()



