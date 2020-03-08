import minigame


class Button(minigame.Button):
    def __init__(self, app, keysym):
        self.callbacks = []

        app.bind('<KeyPress-{}>'.format(keysym), self.callback)
        app.bind('<KeyRelease-{}>'.format(keysym), self.callback)

        self.down = False

    def register_callback(self, callback):
        self.callbacks.append(callback)

    def callback(self, event):
        event_type = str(event.type)

        if not self.down and event_type == 'KeyPress':
            self.down = True

            for callback in self.callbacks:
                callback()
        elif event_type == 'KeyRelease':
            self.down = False

    def pressed(self):
        return self.down
