# Seeds in Motion✨🎮

Welcome to the "Seeds in Motion" project, a modern rendition of the classic Sokoban puzzle game, developed using Python and Pygame. This game blends traditional strategic gameplay with new interactive features, offering a seamless experience on Windows and Linux platforms. Players navigate through increasingly challenging levels, tracking their progress by time and moves, fostering continual improvement and competition.

## Game Overview⭐

"Seeds in Motion" is a puzzle game where the player moves boxes to designated spots on a grid. Our version includes a single-player mode with time and move tracking for competitive play.

### Features

- Intuitive and engaging user interface.
- Single-player mode.
- Increasing difficulty levels.
- Time and move tracking for competitive play.
- Robust and educational gameplay experience.

## UML and Class Diagram⭐

The UML and class diagrams illustrate the architecture of the game. The primary classes are `Player`, `Grid`, `BoxMovable`, and several levels.

### Class Descriptions

1. **Player**: Manages the player's position and movements.
2. **Grid**: Represents the game grid.
3. **BoxMovable**: Handles movable boxes within the game.

## Game Logic⭐

### Main Components

1. **MainPage**: The main menu of the game.
2. **LevelsGrid**: Manages the game levels.
3. **LevelsSpecs**: Contains the specifications for each level.
4. **Player**: Controls player actions and movements.
5. **BoxMovable**: Handles the movable boxes.
6. **Grid**: Draws and updates the game grid.

### Detailed Explanation

### MainPage

The `mainPage.py` initializes the game, sets up the display, and manages the main menu interface. It includes buttons for starting single-player games and handles user interactions to navigate through the game options.

```python
import pygame
from levels_grid import offline_game

pygame.init()

width, height = 1060, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Seeds in Motion / HEM ES")

# Load assets
background = pygame.image.load("assets/menu_interface.png")
offlineButton = pygame.image.load("assets/one_player_button.png")

offline_button = offlineButton.get_rect(center=(530, 407))

def main():
    pygame.mixer.init()
    main_music = pygame.mixer.Sound("assets/23_-_Road.ogg")
    main_music.play(-1).set_volume(0.5)
    run = True
    win.blit(background, (0, 0))
    while run:
        win.blit(offlineButton, offline_button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if offline_button.collidepoint(mouse_pos):
                    pygame.mixer.quit()
                    offline_game()

```

### LevelsGrid

The `levels_grid.py` manages the different levels in the game, including loading levels, resetting them, and checking for victory conditions.

```python
import pygame
from Player import Player
from Grid import Grid
from BoxMovable import BoxMovable

pygame.init()

width, height = 1060, 600
win = pygame.display.set_mode((width, height))
pygame.display.setCaption("Sokoban GAME / HEM-ES")

background1 = pygame.image.load("assets/level_music.png")
background_congrats = pygame.image.load("assets/congrats.png")
background_mute = pygame.image.load("assets/level_mute.png")
victory_image = pygame.image.load("assets/just_back.png")
img = pygame.image.load("assets/seed.png")

class Levels:
    def __init__(self, grid, player, movables):
        self.grid = grid
        self.player = player
        self.movables = movables
        self.box_in_place = False
        self.img = pygame.image.load("assets/seed.png")
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
            movable.grid_x, grid_y = grid_x, grid_y
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

```

## Instructions for Users⭐

1. **Installation**:
    - Ensure Python and Pygame are installed on your system.
    - Clone the repository from GitHub.
    - Navigate to the project directory.
2. **Running the Game**:
    - To start the game, run `mainPage.py`.
    - Choose the single-player mode.
3. **Controls**:
    - Use arrow keys to move the player.
    - Move boxes to designated spots to complete levels.
4. **Creating an Executable**:
    - Install PyInstaller using `pip install pyinstaller`.
    - Navigate to the project directory in the command prompt.
    - Run the following command to create an executable: `pyinstaller --onefile mainPage.py`.
    - The executable file will be created in the `dist` directory.

## Conclusion⭐

"Seeds in Motion" is a comprehensive project that not only revitalizes a classic game but also incorporates modern features. This project allowed us to delve deep into Python programming and game development with Pygame, resulting in a robust, enjoyable, and educational game.

We hope you enjoy playing "Seeds in Motion" as much as we enjoyed developing it. For any questions or contributions, please feel free to open an issue or submit a pull request on our GitHub repository. Thank you for your support and interest!
