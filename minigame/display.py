import abc


class Display(abc.ABC):
    @abc.abstractmethod
    def get_resolution(self):
        pass

    @abc.abstractmethod
    def update_screen_buffer(self, image):
        pass
