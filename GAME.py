import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 600, 400
TILE_SIZE = 40


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


player_x, player_y = 1, 1


goal_x, goal_y = 8, 7

def draw_maze():
    """Draw the maze based on the layout."""
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if maze[row][col] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)

def draw_player(x, y):
    """Draw the player at the current position."""
    rect = pygame.Rect(x * TILE_SIZE + 10, y * TILE_SIZE + 10, TILE_SIZE - 20, TILE_SIZE - 20)
    pygame.draw.rect(screen, BLUE, rect)

def draw_goal(x, y):
    """Draw the goal position."""
    rect = pygame.Rect(x * TILE_SIZE + 10, y * TILE_SIZE + 10, TILE_SIZE - 20, TILE_SIZE - 20)
    pygame.draw.rect(screen, GREEN, rect)


clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and maze[player_y - 1][player_x] == 0:
        player_y -= 1
    if keys[pygame.K_DOWN] and maze[player_y + 1][player_x] == 0:
        player_y += 1
    if keys[pygame.K_LEFT] and maze[player_y][player_x - 1] == 0:
        player_x -= 1
    if keys[pygame.K_RIGHT] and maze[player_y][player_x + 1] == 0:
        player_x += 1

    
    if player_x == goal_x and player_y == goal_y:
        print("You Win!")
        pygame.quit()
        sys.exit()

    
    screen.fill(WHITE)
    draw_maze()
    draw_goal(goal_x, goal_y)
    draw_player(player_x, player_y)

    pygame.display.flip()
    clock.tick(10)
