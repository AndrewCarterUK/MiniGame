WIDTH = 128
HEIGHT = 128

# Must be more than ALIEN_SIZE, used to pad alien rows and columns
ALIEN_BLOCK_SIZE = 8

# Alien constants are global as their spacing is used to separate them
ALIENS_PER_ROW = int(WIDTH / ALIEN_BLOCK_SIZE) - 6
ALIEN_ROWS = int(HEIGHT / (2 * ALIEN_BLOCK_SIZE))

# How often to move the aliens intially, how much to step the alien time down with each shift
ALIEN_START_TIME = 4
ALIEN_TIME_STEP = 0.2
ALIEN_MINIMUM_TIME = 1

# How likely an alien is to fire in a time step
ALIEN_START_FIRE_PROBABILITY = 0.01
ALIEN_FIRE_PROBABILITY_STEP = 0.005
ALIEN_MAXIMUM_FIRE_PROBABILITY = 0.03

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