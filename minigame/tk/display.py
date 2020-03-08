import minigame
import tkinter as tk

from PIL import ImageTk


class Display(minigame.Display):
    def __init__(self, app, width, height):
        self.app = app
        self.width = width
        self.height = height

        self.canvas = tk.Canvas(app, width=width, height=height, bg='#ffffff')
        self.canvas.pack()

        self.canvas_image = None

    def get_resolution(self):
        return (self.width, self.height,)

    def update_screen_buffer(self, image):
        global tk_image
        tk_image = ImageTk.PhotoImage(image)

        if self.canvas_image == None:
            self.canvas_image = self.canvas.create_image((0, 0, ), anchor=tk.NW, image=tk_image)
        else:
            self.canvas.itemconfigure(self.canvas_image, image=tk_image)
