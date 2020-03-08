from minigame.tk import MiniGameTk
from minigame.games.snake import Snake

WIDTH = 20
HEIGHT = 20
STEP_TIME = 0.5
BLOCK_SIZE = 32


def main():
    app = MiniGameTk()

    display = app.create_display(WIDTH * BLOCK_SIZE, HEIGHT * BLOCK_SIZE)
    l_button = app.create_button('Left')
    r_button = app.create_button('Right')
    u_button = app.create_button('Up')
    d_button = app.create_button('Down')
    sleep_fn = app.sleep

    snake = Snake(display, WIDTH, HEIGHT, STEP_TIME, l_button, r_button, u_button, d_button, sleep_fn)
    snake.play()


if __name__ == '__main__':
    main()
