from minigame.games.shit_invaders.global_constants import WIDTH, HEIGHT
from minigame.games.shit_invaders.bullet import Bullet
from PIL import ImageDraw

CANNON_SIZE = 7

# Can only fire if this many time steps have passed since the last shot
CANNON_RATE_LIMIT = 8

class Cannon:
    def __init__(self, l_button, r_button, fire_button):
        self.l_button = l_button
        self.r_button = r_button

        fire_button.register_callback(self.fire)

    def begin(self):
        self.x1 = int((WIDTH - CANNON_SIZE) / 2)
        self.x2 = self.x1 + CANNON_SIZE - 1
        self.y2 = HEIGHT - 1
        self.y1 = self.y2 - CANNON_SIZE + 1

        self.fire = False
        self.dead = False

        self.steps_until_fire_available = 0

    def fire(self):
        self.fire = True

    def is_dead(self):
        return self.dead

    def test_bullet(self, bullet):
        if not self.dead:
            if bullet.check_hit(self.x1, self.y1, self.x2, self.y2):
                self.dead = True
                return True
    
        return False

    def update(self):
        if self.l_button.pressed():
            if self.x1 > 0:
                self.x1 = self.x1 - 1
                self.x2 = self.x2 - 1
        elif self.r_button.pressed():
            if self.x2 < WIDTH - 1:
                self.x1 = self.x1 + 1
                self.x2 = self.x2 + 1

        # If we are waiting to fire, decrease the countdown
        if self.steps_until_fire_available > 0:
            self.steps_until_fire_available = self.steps_until_fire_available - 1

        # No bullet fired
        if not self.fire:
            return None

        # Unable to fire, countdown not expired
        if self.steps_until_fire_available > 0:
            return None

        # Bullet fired, reset flag
        self.fire = False
        self.steps_until_fire_available = CANNON_RATE_LIMIT

        # Create and return bullet
        return Bullet(self.x1, self.y1, self.x2, self.y2, 'up')

    def render(self, image):
        draw = ImageDraw.Draw(image)
        draw.rectangle((self.x1, self.y1, self.x2, self.y2, ), fill='#00ff00')
        del draw
