import pygame



WHITE = (255, 255, 255)
limitCell_image_path = "assets/block_01.png"  
impassable_image = pygame.image.load(limitCell_image_path)
impassable_image = pygame.transform.scale(impassable_image, (50, 50))

normal_cell = "assets/ground_03.png"
normal_image = pygame.image.load(normal_cell)
normal_image = pygame.transform.scale(normal_image, (50, 50))

checkpoint_imagee = "assets/ground_06.png"
checkmark = pygame.image.load(checkpoint_imagee)
checkmark = pygame.transform.scale(checkmark, (50, 50))


class Grid:
    def __init__(self, cell_size, grid_width, grid_height, impassable_cells, checkpoints):
        self.cell_size = cell_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.impassable_cells = impassable_cells
        self.checkpoints = checkpoints

    def dessinerGrid(self, win):
        # Calculate the total grid size
        total_grid_width = self.grid_width * self.cell_size
        total_grid_height = self.grid_height * self.cell_size
        
        # Calculate starting positions to center the grid
        start_x = (win.get_width() - total_grid_width) // 2
        start_y = (win.get_height() - total_grid_height) // 2
        

        # Now draw the grid on top of the black background
        for row in range(self.grid_height): 
            for col in range(self.grid_width):
                cell_top_left = (start_x + col * self.cell_size, start_y + row * self.cell_size)
                if (row, col) in self.impassable_cells:
                    win.blit(impassable_image, cell_top_left)
                else:
                    win.blit(normal_image, cell_top_left)
                    
                if (row, col) in self.checkpoints:

                    win.blit(checkmark, cell_top_left)
                

    def GetGridWidth(self):
        totalWidth = self.grid_width * self.cell_size
        debX = (pygame.display.Info().current_w - totalWidth) // 2
        return debX
    
    def GetGridHeight(self):
        totalHeight = self.grid_height * self.cell_size
        debY = (pygame.display.Info().current_h - totalHeight) // 2
        return debY