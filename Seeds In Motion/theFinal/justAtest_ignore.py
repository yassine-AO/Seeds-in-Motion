import pygame
from Player import Player
from Grid import Grid
from BoxMovable import BoxMovable

pygame.init()

width, height = 1060, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sokoban GAME / HEM-ES")

background = pygame.image.load("C:/Users/Hamza/Desktop/32062.jpg")


nonPassable = [(0,0), (0,1), (0,2), (0,3), (0,5)]
grid = Grid(50, 12, 8, nonPassable)



################################################################
# Calculate the total grid size
#total_grid_width = grid.grid_width * grid.cell_size
#total_grid_height = grid.grid_height * grid.cell_size

# Calculate starting positions to center the grid
#start_x = (width - total_grid_width) // 2
#start_y = (height - total_grid_height) // 2
################################################################


WHITE = (255, 255, 255)
playerLvl1 = Player(1, 1, WHITE, grid, grid.GetGridWidth(), grid.GetGridHeight())

BLUE = (0, 0, 255) 
movable = BoxMovable(2, 2, BLUE, grid, grid.GetGridWidth(), grid.GetGridHeight())



def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        win.blit(background, (0, 0))

        
        grid.dessinerGrid(win)
        playerLvl1.draw(win)
        movable.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerLvl1.movingArround(movable, -1, 0)
                elif event.key == pygame.K_RIGHT:
                    playerLvl1.movingArround(movable, 1, 0)
                elif event.key == pygame.K_UP:
                    playerLvl1.movingArround(movable, 0, -1)
                elif event.key == pygame.K_DOWN:
                    playerLvl1.movingArround(movable, 0, 1)

        pygame.display.update()
        clock.tick(60)  

    pygame.quit()

main()