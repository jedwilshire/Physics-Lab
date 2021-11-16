import pygame
# Screen Settings
WIDTH = 1000
HEIGHT = 800
TITLE = 'PHYSICS LAB'
FPS = 60

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
ORANGE = (255, 128, 0)

# Particle Settings
NUM_PARTICLES = 10
MIN_RADIUS = 20
MAX_RADIUS = 50
MIN_SPEED = 600
MAX_SPEED = 800

# Physics Settings
GRAVITY = 700
FRICTION = 0.2
ELASTICITY = 0.9
LEFT_WALL_NORMAL = pygame.math.Vector2(1, 0)
RIGHT_WALL_NORMAL = pygame.math.Vector2(-1, 0)
BOTTOM_WALL_NORMAL = pygame.math.Vector2(0, -1)
TOP_WALL_NORMAL = pygame.math.Vector2(0, 1)
EFFECTIVE_ZERO = 1.5

# Mouse Settings
LAUNCH_SCALAR = 2