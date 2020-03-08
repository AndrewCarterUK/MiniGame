import abc

class Button(abc.ABC):
    @abc.abstractmethod
    def register_callback(self, callabck):
        pass

    @abc.abstractmethod
    def pressed(self):
        pass
