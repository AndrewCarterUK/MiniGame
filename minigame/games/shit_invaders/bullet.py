from minigame.games.shit_invaders.global_constants import WIDTH, HEIGHT
from PIL import ImageDraw

BULLET_WIDTH = 1
BULLET_HEIGHT = 4


class Bullet:
    def __init__(self, source_x1, source_y1, source_x2, source_y2, direction):
        self.x1 = int((source_x1 + source_x2 + BULLET_WIDTH) / 2)
        self.x2 = self.x1 + BULLET_WIDTH - 1

        if direction == 'down':
            self.y1 = source_y2 + 1
            self.y2 = self.y1 + BULLET_HEIGHT - 1
        elif direction == 'up':
            self.y2 = source_y1 - 1
            self.y1 = self.y2 - BULLET_HEIGHT + 1

        self.direction = direction
        self.dead = False

    def update(self):
        if self.direction == 'up':
            self.y1 = self.y1 - 1
            self.y2 = self.y2 - 1
        elif self.direction == 'down':
            self.y1 = self.y1 + 1
            self.y2 = self.y2 + 1 

        if self.y1 < 0 or self.y1 >= HEIGHT or self.y2 < 0 or self.y2 >= HEIGHT:
            self.dead = True
        else:
            self.dead = False

    def kill(self):
        self.dead = True

    def is_dead(self):
        return self.dead

    def check_hit(self, x1, y1, x2, y2):
        if self.dead:
            return False

        if x1 <= self.x2 and x2 >= self.x1 and y1 <= self.y2 and y2 >= self.y1:
            return True
        else:
            return False

    def render(self, image):
        if not self.dead:
            draw = ImageDraw.Draw(image)
            draw.rectangle((self.x1, self.y1, self.x2, self.y2, ), fill='#ffffff')
            del draw
