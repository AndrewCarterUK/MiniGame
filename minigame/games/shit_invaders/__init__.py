from time import sleep
from random import random
from PIL import Image
from minigame.games.shit_invaders.global_constants import WIDTH, HEIGHT
from minigame.games.shit_invaders.global_constants import ALIENS_PER_ROW, ALIEN_ROWS, ALIEN_FIRE_PROBABILITY, ALIEN_TIME, ALIEN_BLOCK_SIZE
from minigame.games.shit_invaders.global_constants import BUNKER_MAP, BUNKER_WIDTH, BUNKER_HEIGHT, NUMBER_OF_BUNKERS
from minigame.games.shit_invaders.alien import Alien
from minigame.games.shit_invaders.bullet import Bullet
from minigame.games.shit_invaders.bunker_pixel import BunkerPixel
from minigame.games.shit_invaders.cannon import Cannon


class ShitInvaders:
    def __init__(self, display, step_time, l_button, r_button, fire_button, sleep_fn=sleep):
        self.display = display
        self.step_time = step_time
        self.sleep_fn = sleep_fn

        # Create the cannon
        self.cannon = Cannon(l_button, r_button, fire_button)

    def play(self):
        # Initialise the cannon
        self.cannon.begin()

        # Start with no aliens, bullets or bunkers
        self.alien_rows = []
        self.bullets = []
        self.bunker_pixels = []

        # Add in all the aliens
        for j in range(ALIEN_ROWS):
            self.add_alien_row(j)

        # Move them right initially, startnig in the middle of the screen
        self.alien_offset = 0
        self.alien_direction = 'right'
        self.alien_move_limit = int((WIDTH - (ALIENS_PER_ROW * ALIEN_BLOCK_SIZE)) / 2)

        # Draw the bunkers
        for i in range(NUMBER_OF_BUNKERS):
            self.draw_bunker(i)

        # Start from 0
        self.t = 0

        while True:
            try:
                # The step() method returns True to keep playing, and False when the game is over
                if not self.step():
                    break
            finally:
                self.render()

            self.sleep_fn(self.step_time)

    def draw_bunker(self, i):
        bunker_x1_start = int((((WIDTH / NUMBER_OF_BUNKERS) - BUNKER_WIDTH) / 2) + (i * (WIDTH / NUMBER_OF_BUNKERS)))
        bunker_y1_start = HEIGHT - (5 * BUNKER_HEIGHT)

        for y_offset in range(len(BUNKER_MAP)):
            row = BUNKER_MAP[y_offset]

            for x_offset in range(len(row)):
                if row[x_offset]:
                    bunker_pixel = BunkerPixel(bunker_x1_start + x_offset, bunker_y1_start + y_offset)
                    self.bunker_pixels.append(bunker_pixel)

    def add_alien_row(self, j):
        alien_row = []

        alien_x1_start = int((WIDTH - (ALIENS_PER_ROW * ALIEN_BLOCK_SIZE)) / 2)
        alien_y1_start = 0

        for i in range(ALIENS_PER_ROW):
            alien_x1 = alien_x1_start + (i * ALIEN_BLOCK_SIZE)
            alien_y1 = alien_y1_start + (j * ALIEN_BLOCK_SIZE)

            alien = Alien(alien_x1, alien_y1)
            alien_row.append(alien)

        self.alien_rows.append(alien_row)

    def move_aliens(self):
        next_movement = None

        if self.alien_direction == 'left':
            if self.alien_offset < 0 - self.alien_move_limit:
                # If the aliens hit the left limit, move them down and change direction
                self.alien_direction = 'right'
                next_movement = 'down'
            else:
                self.alien_offset = self.alien_offset - 1
                next_movement = 'left'
        elif self.alien_direction == 'right':
            if self.alien_offset > self.alien_move_limit:
                # If the aliens hit the right limit, move them down and change direction
                self.alien_direction = 'left'
                next_movement = 'down'
            else:
                self.alien_offset = self.alien_offset + 1
                next_movement = 'right'

        for alien_row in self.alien_rows:
            for alien in alien_row:
                alien.move(next_movement)

    # Return an array containing all the aliens at the bottom of the screen (the ones eligible to fire)
    def get_bottom_aliens(self):
        bottom_aliens = [None for i in range(ALIENS_PER_ROW)]

        for alien_row in self.alien_rows:
            for i in range(ALIENS_PER_ROW):
                alien = alien_row[i]

                if not alien.is_dead():
                    bottom_aliens[i] = alien

        return list(filter(lambda a: a != None, bottom_aliens))

    def step(self):
        # Update the cannon
        new_bullet = self.cannon.update()

        if new_bullet != None:
            # If the cannon fired a bullet, add it to our list of bullets
            self.bullets.append(new_bullet)

        # Update all bullets
        for bullet in self.bullets:
            bullet.update()

            # Check to see if the bullet has hit a cannon
            if self.cannon.test_bullet(bullet):
                return False

            # Check to see if the buller has hit a bunker pixel
            for bunker_pixel in self.bunker_pixels:
                if bunker_pixel.test_bullet(bullet):
                    bullet.kill()

            # Check to see if the bullet has hit an alien
            for alien_row in self.alien_rows:
                for alien in alien_row:
                    if alien.test_bullet(bullet):
                        bullet.kill()

        # Remove any bullets that are out of bounds or have hit their target
        self.bullets = list(filter(lambda b: not b.is_dead(), self.bullets))

        # Aliens move slower, only move them every ALIEN_TIME steps
        if self.t % ALIEN_TIME == 0:
            # Move all the aliens
            self.move_aliens()

            # Make some of the bottom aliens launch bullets
            for alien in self.get_bottom_aliens():
                if random() < ALIEN_FIRE_PROBABILITY:
                    bullet = alien.launch_bullet()
                    self.bullets.append(bullet)

        # Update the time step
        self.t = self.t + 1

        return True

    def render(self):
        # Create a PIL image
        image = Image.new(mode='RGB', size=(WIDTH, HEIGHT,))

        # Draw the cannon
        self.cannon.render(image)

        # Draw the aliens
        for alien_row in self.alien_rows:
            for alien in alien_row:
                alien.render(image)

        # Draw the bullets
        for bullet in self.bullets:
            bullet.render(image)

        # Draw the bunker pixels:
        for bunker_pixel in self.bunker_pixels:
            bunker_pixel.render(image)

        # Scale to the display
        image = image.resize(self.display.get_resolution(), Image.NEAREST)

        # Update the display
        self.display.update_screen_buffer(image)
