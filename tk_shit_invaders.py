from minigame.tk import MiniGameTk
from minigame.games.shit_invaders import ShitInvaders

SCALE_FACTOR = 8
WIDTH = 128
HEIGHT = 128
STEP_TIME = 0.01


def main():
    app = MiniGameTk()

    display = app.create_display(WIDTH * SCALE_FACTOR, HEIGHT * SCALE_FACTOR)
    l_button = app.create_button('Left')
    r_button = app.create_button('Right')
    fire_button = app.create_button('Up')
    sleep_fn = app.sleep

    space_invaders = ShitInvaders(display, STEP_TIME, l_button, r_button, fire_button, sleep_fn)
    space_invaders.play()


if __name__ == '__main__':
    main()
