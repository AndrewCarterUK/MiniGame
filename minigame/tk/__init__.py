try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

from minigame.tk.button import Button
from minigame.tk.display import Display
from time import sleep


class MiniGameTk:
    def __init__(self):
        self.app = tk.Tk()

    def create_display(self, width, height):
        return Display(self.app, width, height)

    def create_button(self, event_code):
        return Button(self.app, event_code)

    def sleep(self, time):
        milliseconds = time * 1000
        i = 0

        while i < milliseconds:
            sleep(0.001)

            self.app.update_idletasks()
            self.app.update()

            i = i + 1
