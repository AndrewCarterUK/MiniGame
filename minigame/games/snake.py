from time import sleep
from random import randrange
from PIL import Image


class Snake:
    def __init__(self, display, width, height, step_time, l_button, r_button, u_button, d_button, sleep_fn=sleep):
        self.display = display
        self.width = width
        self.height = height
        self.step_time = step_time
        self.sleep_fn = sleep_fn

        l_button.register_callback(self.left)
        r_button.register_callback(self.right)
        u_button.register_callback(self.up)
        d_button.register_callback(self.down)

    def left(self):
        if self.direction != 'right':
            self.direction = 'left'

    def right(self):
        if self.direction != 'left':
            self.direction = 'right'

    def up(self):
        if self.direction != 'down':
            self.direction = 'up'

    def down(self):
        if self.direction != 'up':
            self.direction = 'down'

    def play(self):
        self.grid = [[0 for x in range(self.width)] for y in range(self.height)]
        self.snake = [(0, 0,)]
        self.grid[0][0] = 1
        self.score = 0
        self.food_active = False
        self.direction = 'right'

        self.snake_head_x = 0
        self.snake_head_y = 0

        self.add_food()

        while True:
            try:
                if not self.step():
                    break
            finally:
                self.render()

            self.sleep_fn(self.step_time)

    def step(self):
        next_x = self.snake_head_x
        next_y = self.snake_head_y

        if self.direction == 'left':
            next_x = next_x - 1
        elif self.direction == 'right':
            next_x = next_x + 1
        elif self.direction == 'up':
            next_y = next_y - 1
        elif self.direction == 'down':
            next_y = next_y + 1

        # Boundary collision
        if next_x < 0 or next_x >= self.width or next_y < 0 or next_y >= self.height:
            return False

        # Self collision
        if self.grid[next_y][next_x] == 1:
            return False

        # Detect food eaten
        food_eaten = True if self.grid[next_y][next_x] == 2 else False

        if food_eaten:
            self.score = self.score + 1
            self.add_food()

        # Draw new head
        self.snake.append((next_x, next_y,))
        self.grid[next_y][next_x] = 1

        if not food_eaten:
            # Remove tail
            tail = self.snake.pop(0)
            self.grid[tail[1]][tail[0]] = 0

        # Update snake coordinates
        self.snake_head_x = next_x
        self.snake_head_y = next_y

        return True

    def add_food(self):
        while True:
            food_x = randrange(0, self.width)
            food_y = randrange(0, self.height)

            # Slot free
            if self.grid[food_y][food_x] == 0:
                self.grid[food_y][food_x] = 2
                return


    def render(self):
        # White background, black snake, red food
        pixel_map = [(255, 255, 255,), (0, 0, 0,), (255, 0, 0,)]

        buffer = []

        for y in range(self.height):
            buffer = buffer + list(map(lambda v: pixel_map[v], self.grid[y]))

        image = Image.new(mode='RGB', size=(self.width, self.height,))
        image.putdata(buffer)
        image = image.resize(self.display.get_resolution(), Image.NEAREST)

        self.display.update_screen_buffer(image)
