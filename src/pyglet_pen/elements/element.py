from typing import Any, Literal

from pyglet_pen.component import Component, ComponentProperty
from pyglet_pen import layout


class ElementProperty[T](ComponentProperty[T]):
    pass


class Element(Component):
    Proxy = None
    mouse_over_enabled = True

    callback_on_mouse_motion

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.proxy = None
        return instance

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.proxy = self.Proxy(*args, **kwargs)
        self.apply_proxy_property_subscriptions()
        
    def apply_proxy_property_subscriptions(self, properties=None):
        if properties is None:
            properties = self.property_names
        for property_name in properties:
            self.subscribe_to_property(
                property_name, 
                self.passthrough_subscription_factory(
                    self.proxy,
                    property_name
                )
            )

    def is_mouse_over(self, x, y):
        if not self.mouse_over_enabled:
            return False
        if self.width is None or self.height is None:
            return False
        try:
            return (x, y) in self.proxy.base
        except TypeError:
            return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_enter(self, x, y):
        pass

    def on_mouse_leave(self, x, y):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        pass




