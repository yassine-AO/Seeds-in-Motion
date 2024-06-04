import pygame


crate_image_path = "assets/seed.png"  
crate_image = pygame.image.load(crate_image_path)
crate_image = pygame.transform.scale(crate_image, (50, 50))


class BoxMovableOnline:
    def __init__(self, grid_x, grid_y, img, grid, start_x, start_y):
        self.grid_x = grid_x  # Grid coordinate
        self.grid_y = grid_y  # Grid coordinate
        self.img = img
        self.grid = grid
        self.start_x = start_x  # Starting x-coordinate for the grid
        self.start_y = start_y  # Starting y-coordinate for the grid
        
        self.update_pixel_position()

    def update_pixel_position(self):
        self.x = self.start_x + self.grid_x * self.grid.cell_size
        self.y = self.start_y + self.grid_y * self.grid.cell_size

    def moveBox(self, new_grid_x, new_grid_y):
        # Check grid boundaries before moving the box
        if 0 <= new_grid_x < self.grid.grid_width and 0 <= new_grid_y < self.grid.grid_height:
            self.grid_x = new_grid_x
            self.grid_y = new_grid_y
            self.update_pixel_position()

    def draw(self, win):
       
        #pygame.draw.rect(win, (255,255,255), (self.x, self.y, self.grid.cell_size, self.grid.cell_size))
        win.blit(crate_image, (self.x, self.y))
        
    