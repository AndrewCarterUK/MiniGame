import minigame
import RPi.GPIO as GPIO


class Button(minigame.Button):
    def __init__(self, bcm_pin):
        self.callbacks = []

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(bcm_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(bcm_pin, GPIO.RISING, callback=self.callback)

    def register_callback(self, callback):
        self.callbacks.append(callback)

    def callback(self, event):
        for callback in self.callbacks:
            callback()

    def pressed(self):
        return GPIO.input(bcm_pin)
