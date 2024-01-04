
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
    __callback_containers__ = (
        ("mouse", "on_mouse_motion"),
        ("mouse", "on_mouse_enter"),
        ("mouse", "on_mouse_leave"),
        ("mouse", "on_mouse_press"),
        ("mouse", "on_mouse_release"),
        ("mouse", "on_mouse_scroll"),
        ("mouse", "on_mouse_drag"),
        ("text", "on_text"),
        ("text", "on_text_motion"),
        ("text", "on_text_motion_select"),
    )

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance._has_focus = False
        for callback_type, callback_container in cls.__callback_containers__:
            setattr(instance, callback_container, CallbackContainer())
        return instance
        
    def is_mouse_over(self, x, y):
        if not self.mouse_over_enabled:
            return False
        if self.width is None or self.height is None:
            return False
        try:
            return (x, y) in self.base
        except (AttributeError, TypeError):
            return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height
        
    def focus(self):
        self._has_focus = True
        self.on_focus()
    
    def unfocus(self):
        self._has_focus = False
        self.on_unfocus()

    def on_focus(self):
        pass

    def on_unfocus(self):
        pass

