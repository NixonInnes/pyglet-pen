from typing import Any, Callable, Optional

from pyglet_pen.component import Component, ComponentAttribute
from pyglet_pen.proxies.proxy import ProxyAttribute


class ElementAttribute[T](ComponentAttribute[T]):
    __name_container__ = "__element_attributes__"

class ElementCallback[T](ComponentAttribute[T]):
    __name_container__ = "__element_callbacks__"

    @staticmethod
    def __do_nothing(*args, **kwargs):
        pass

    def __init__(self, callback: Optional[Callable] = None):
        if callback is None:
            callback = ElementCallback.__do_nothing
        self._default_callback = callback
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        callback = instance.__dict__.get(self, self._default_callback)
        return callback
    
    def __set__(self, instance, value):
        instance.__dict__[self] = value
    
    def __call__(self, instance, *args, **kwargs):
        callback = instance.__dict__.get(self, self._default_callback)
        return callback(instance, *args, **kwargs)


class Element:
    mouse_over_enabled = True

    callback_on_mouse_motion = ElementCallback()
    callback_on_mouse_enter = ElementCallback()
    callback_on_mouse_leave = ElementCallback()
    callback_on_mouse_press = ElementCallback()
    callback_on_mouse_release = ElementCallback()
    callback_on_mouse_scroll = ElementCallback()

    def is_mouse_over(self, x, y):
        if not self.mouse_over_enabled:
            return False
        if self.width is None or self.height is None:
            return False
        try:
            return (x, y) in self.base
        except TypeError:
            return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def on_mouse_motion(self, x, y, dx, dy):
        self.callback_on_mouse_motion(self)

    def on_mouse_enter(self, x, y):
        print("on_mouse_enter")
        self.callback_on_mouse_enter(self)

    def on_mouse_leave(self, x, y):
        self.callback_on_mouse_leave(self)

    def on_mouse_press(self, x, y, button, modifiers):
        self.callback_on_mouse_press(self)

    def on_mouse_release(self, x, y, button, modifiers):
        self.callback_on_mouse_release(self)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.callback_on_mouse_scroll(self)
