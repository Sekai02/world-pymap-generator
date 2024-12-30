import pygame
import sys
import random
import os

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32  # Base tile size in pixels
MAP_WIDTH = 50
MAP_HEIGHT = 50
ZOOM_STEP = 0.1
MIN_ZOOM = 0.5
MAX_ZOOM = 2.0
FONT_SIZE = 18

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Main setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Map Generator and Explorer")

# Load tileset
TILESET_PATH = "res/tileset.png"
tileset_image = pygame.image.load(TILESET_PATH).convert_alpha()
tileset_cols = tileset_image.get_width() // TILE_SIZE
tileset_rows = tileset_image.get_height() // TILE_SIZE

def generate_random_map(width, height):
    """Generate a random map as a 2D list of tile indices."""
    return [[random.randint(0, tileset_cols * tileset_rows - 1) for _ in range(width)] for _ in range(height)]

def draw_map(screen, map_data, tileset, offset_x, offset_y, zoom):
    """Draw the map onto the screen."""
    tile_width = int(TILE_SIZE * zoom)
    tile_height = int(TILE_SIZE * zoom)
    tileset_cols = tileset.get_width() // TILE_SIZE

    for y, row in enumerate(map_data):
        for x, tile_index in enumerate(row):
            src_x = (tile_index % tileset_cols) * TILE_SIZE
            src_y = (tile_index // tileset_cols) * TILE_SIZE
            tile_rect = pygame.Rect(src_x, src_y, TILE_SIZE, TILE_SIZE)

            dest_x = int(x * tile_width - offset_x)
            dest_y = int(y * tile_height - offset_y)

            dest_rect = pygame.Rect(dest_x, dest_y, tile_width, tile_height)
            screen.blit(pygame.transform.scale(tileset.subsurface(tile_rect), (tile_width, tile_height)), dest_rect)

def draw_interface(screen, font, zoom, camera_x, camera_y):
    """Draw the user interface showing camera position and zoom level."""
    zoom_text = f"Zoom: {int(zoom * 100)}%"
    position_text = f"Camera: ({int(camera_x)}, {int(camera_y)})"

    zoom_surface = font.render(zoom_text, True, WHITE)
    position_surface = font.render(position_text, True, WHITE)

    screen.blit(zoom_surface, (10, 10))
    screen.blit(position_surface, (10, 40))

# Main setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Map Generator and Explorer")

font = pygame.font.Font(None, FONT_SIZE)
clock = pygame.time.Clock()

# Map and camera settings
map_data = generate_random_map(MAP_WIDTH, MAP_HEIGHT)
camera_x, camera_y = 0, 0
zoom = 1.0

# Main loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Camera movement
    if keys[pygame.K_LEFT]:
        camera_x -= 10 / zoom
    if keys[pygame.K_RIGHT]:
        camera_x += 10 / zoom
    if keys[pygame.K_UP]:
        camera_y -= 10 / zoom
    if keys[pygame.K_DOWN]:
        camera_y += 10 / zoom

    # Zoom controls
    if keys[pygame.K_MINUS]:
        zoom = max(MIN_ZOOM, zoom - ZOOM_STEP)
    if keys[pygame.K_PLUS] or keys[pygame.K_EQUALS]:
        zoom = min(MAX_ZOOM, zoom + ZOOM_STEP)

    # Draw the map and interface
    draw_map(screen, map_data, tileset_image, camera_x, camera_y, zoom)
    draw_interface(screen, font, zoom, camera_x, camera_y)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()