import pygame
pygame.mixer.init()
walking_sound = pygame.mixer.Sound("assets/grass.mp3")



class Player:
    def __init__(self, grid_x, grid_y, color, grid, start_x, start_y):
        self.grid_x = grid_x  # Grid coordinate
        self.grid_y = grid_y  # Grid coordinate
        self.color = color
        self.grid = grid
        self.start_x = start_x  # Starting x-coordinate for the grid
        self.start_y = start_y  # Starting y-coordinate for the grid


        #init counter
        self.box_movement_counter = 0
        self.player_movement_counter = 0

        self.images = {
            'down': [pygame.transform.scale(pygame.image.load("assets/down/down1.png").convert_alpha(), (50, 50)),
                     pygame.transform.scale(pygame.image.load("assets/down/down2.png").convert_alpha(), (50, 50)),
                     pygame.transform.scale(pygame.image.load("assets/down/down3.png").convert_alpha(), (50, 50)),
                     ],
            'left': [pygame.transform.scale(pygame.image.load("assets/left/left1.png").convert_alpha(), (50, 50)),
                     pygame.transform.scale(pygame.image.load("assets/left/left2.png").convert_alpha(), (50, 50)),
                     pygame.transform.scale(pygame.image.load("assets/left/left3.png").convert_alpha(), (50, 50)),
                     ],
            'right':[pygame.transform.scale(pygame.image.load("assets/right/right1.png").convert_alpha(), (50, 50)),
                     pygame.transform.scale(pygame.image.load("assets/right/right2.png").convert_alpha(), (50, 50)),
                     pygame.transform.scale(pygame.image.load("assets/right/right3.png").convert_alpha(), (50, 50)),
                     ],
            'up':   [pygame.transform.scale(pygame.image.load("assets/up/up1.png").convert_alpha(), (50, 50)),
                     pygame.transform.scale(pygame.image.load("assets/up/up2.png").convert_alpha(), (50, 50)),
                     pygame.transform.scale(pygame.image.load("assets/up/up3.png").convert_alpha(), (50, 50)),
                     ],
        }

        self.current_direction = 'down'  # Default direction
        self.animation_index = 0  # Current image index in the animation



        self.update_pixel_position()

    def update_pixel_position(self):
        # Update pixel position based on grid coordinates and starting offsets
        self.x = self.start_x + self.grid_x * self.grid.cell_size
        self.y = self.start_y + self.grid_y * self.grid.cell_size

    def movingArround(self, movables, direction_x, direction_y):
        new_grid_x = self.grid_x + direction_x
        new_grid_y = self.grid_y + direction_y

        # First, check if the player's new position is valid
        if not (0 <= new_grid_x < self.grid.grid_width and 0 <= new_grid_y < self.grid.grid_height):
            return  # Player can't move out of bounds
        
        # Check if the new position is not blocked by an impassable cell
        if (new_grid_y, new_grid_x) in self.grid.impassable_cells:
            return  # Can't move into impassable cell
        ########################################################################################
        if direction_x or direction_y :
                walking_sound.play(0,0,0)
           

        if direction_x > 0:
            self.current_direction = 'right'
            self.player_movement_counter += 1
        elif direction_x < 0:
            self.current_direction = 'left'
            self.player_movement_counter += 1
        elif direction_y > 0:
            self.current_direction = 'down'
            self.player_movement_counter += 1
        elif direction_y < 0:
            self.current_direction = 'up'
            self.player_movement_counter += 1

        self.animation_index += 1
        if self.animation_index >= len(self.images[self.current_direction]):
            self.animation_index = 0  # Reset to loop the animation
########################################################################################
        # Check if the player is next to any box and try to move it
        box_to_move = None

        for box in movables:
            
            if (self.grid_x == box.grid_x and self.grid_y == box.grid_y - 1 and direction_y > 0) or \
               (self.grid_x == box.grid_x and self.grid_y == box.grid_y + 1 and direction_y < 0) or \
               (self.grid_y == box.grid_y and self.grid_x == box.grid_x - 1 and direction_x > 0) or \
               (self.grid_y == box.grid_y and self.grid_x == box.grid_x + 1 and direction_x < 0):
                # This box is adjacent to the player and in the direction of movement
                box_to_move = box
                break
        
        # If we found a box to move, try to move it
        if box_to_move:
            new_box_grid_x = box_to_move.grid_x + direction_x
            new_box_grid_y = box_to_move.grid_y + direction_y

            # Check if the new position of the box is valid and not blocked
            if not (0 <= new_box_grid_x < self.grid.grid_width and 0 <= new_box_grid_y < self.grid.grid_height):
                return  # Box can't move out of bounds
            
            if (new_box_grid_y, new_box_grid_x) in self.grid.impassable_cells:
                return  # Box can't move into an impassable cell

            for other_box in movables:
                if other_box != box_to_move and other_box.grid_x == new_box_grid_x and other_box.grid_y == new_box_grid_y:
                    return  # Can't move into a space occupied by another box

            # Move the box
            box_to_move.moveBox(new_box_grid_x, new_box_grid_y)
            self.box_movement_counter += 1
        
        # Move the player
        self.grid_x = new_grid_x
        self.grid_y = new_grid_y
        self.update_pixel_position()


    def draw(self, win):
       current_image = self.images[self.current_direction][self.animation_index]
       win.blit(current_image, (self.x, self.y))