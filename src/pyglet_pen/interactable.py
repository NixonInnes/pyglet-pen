
class CallbackContainer:
    def __init__(self):
        self.callbacks = []
    
    def __call__(self, element, *args, **kwargs):
        for callback in self.callbacks:
            callback(element, *args, **kwargs)
        
    def subscribe(self, callback):
        self.callbacks.append(callback)


class Interactable:
    mouse_over_enabled = True

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.on_mouse_motion = CallbackContainer()
        instance.on_mouse_enter = CallbackContainer()
        instance.on_mouse_leave = CallbackContainer()
        instance.on_mouse_press = CallbackContainer()
        instance.on_mouse_release = CallbackContainer()
        instance.on_mouse_scroll = CallbackContainer()
        return instance

    def is_mouse_over(self, x, y):
        if not self.mouse_over_enabled:
            return False
        if self.width is None or self.height is None:
            return False
        try:
            return (x, y) in self.base
        except TypeError:
            return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

