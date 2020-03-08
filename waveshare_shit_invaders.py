from minigame.waveshare.button import Button
from minigame.waveshare.display import Display
from minigame.games.shit_invaders import ShitInvaders

STEP_TIME = 0.01


def main():
    display = Display()
    l_button = Button(5)
    r_button = Button(26)
    fire_button = Button(6)

    space_invaders = ShitInvaders(display, STEP_TIME, l_button, r_button, fire_button)
    space_invaders.play()


if __name__ == '__main__':
    main()
