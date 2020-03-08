WIDTH = 128
HEIGHT = 128

# Must be more than ALIEN_SIZE, used to pad alien rows and columns
ALIEN_BLOCK_SIZE = 8

# Alien constants are global as their spacing is used to separate them
ALIENS_PER_ROW = int(WIDTH / ALIEN_BLOCK_SIZE) - 6
ALIEN_ROWS = int(HEIGHT / (2 * ALIEN_BLOCK_SIZE))

# How often to move the aliens
ALIEN_TIME = 4

# How likely an alien is to fire in a time step
ALIEN_FIRE_PROBABILITY = 0.005

# Bunker constants
NUMBER_OF_BUNKERS = 4

BUNKER_WIDTH = 8
BUNKER_HEIGHT = 8

BUNKER_MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
]