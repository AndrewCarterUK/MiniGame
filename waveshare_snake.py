from minigame.waveshare.button import Button
from minigame.waveshare.display import Display
from minigame.games.snake import Snake

WIDTH = 20
HEIGHT = 20
STEP_TIME = 0.5
BLOCK_SIZE = 32


def main():
    display = Display()
    l_button = Button(5)
    r_button = Button(26)
    u_button = Button(6)
    d_button = Button(19)

    snake = Snake(display, WIDTH, HEIGHT, l_button, r_button, u_button, d_button)
    snake.play()


if __name__ == '__main__':
    main()
