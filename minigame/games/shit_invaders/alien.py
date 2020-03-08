from minigame.games.shit_invaders.bullet import Bullet
from minigame.games.shit_invaders.global_constants import ALIEN_BLOCK_SIZE
from PIL import ImageDraw

ALIEN_SIZE = 4


class Alien:
    def __init__(self, x1, y1):
        self.x1 = x1 + int((ALIEN_BLOCK_SIZE - ALIEN_SIZE) / 2)
        self.y1 = y1 + int((ALIEN_BLOCK_SIZE - ALIEN_SIZE) / 2)
        self.x2 = self.x1 + ALIEN_SIZE
        self.y2 = self.y1 + ALIEN_SIZE
        self.dead = False

    def move(self, direction):
        if direction == 'left':
            self.x1 = self.x1 - 1
            self.x2 = self.x2 - 1
        elif direction == 'right':
            self.x1 = self.x1 + 1
            self.x2 = self.x2 + 1
        elif direction == 'down':
            self.y1 = self.y1 + 1
            self.y2 = self.y2 + 1

    def test_bullet(self, bullet):
        if not self.dead:
            if bullet.check_hit(self.x1, self.y1, self.x2, self.y2):
                self.dead = True
                return True
    
        return False

    def is_dead(self):
        return self.dead

    def launch_bullet(self):
        return Bullet(self.x1, self.y1, self.x2, self.y2, 'down')

    def render(self, image):
        if not self.dead:
            draw = ImageDraw.Draw(image)
            draw.rectangle((self.x1, self.y1, self.x2, self.y2, ), fill='#ff0000')
            del draw
