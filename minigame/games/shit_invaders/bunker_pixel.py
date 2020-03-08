from PIL import ImageDraw


class BunkerPixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.dead = False

    def test_bullet(self, bullet):
        if not self.dead:
            if bullet.check_hit(self.x, self.y, self.x, self.y):
                self.dead = True
                return True
    
        return False

    def render(self, image):
        if not self.dead:
            draw = ImageDraw.Draw(image)
            draw.rectangle((self.x, self.y, self.x, self.y), fill='#00ff00')
            del draw
