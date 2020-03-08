import minigame
import ST7735

WIDTH = 128
HEIGHT = 128


class Display(minigame.Display):
    def __init__(self):
        self.st7735 = ST7735.ST7735(
            port=0,
            cs=ST7735.BG_SPI_CS_FRONT,
            dc=9,
            backlight=19,
            rotation=90,
            spi_speed_hz=4000000
        )

        self.st7735.begin()

    def get_resolution(self):
        return (WIDTH, HEIGHT,)

    def update_screen_buffer(self, image):
        self.st7735.display(image)
