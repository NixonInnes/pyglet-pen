from pyglet_pen.component import Component, ComponentAttribute
from pyglet_pen.interactable import Interactable
from pyglet_pen.layouts import LayoutMixin
from pyglet_pen.utilities.types import T


class WidgetAttribute[T](ComponentAttribute[T]):
    __name_container__ = "__widget_attributes__"

class Widget(Interactable, LayoutMixin, Component):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.subscribe_to_attribute("x", lambda value: setattr(instance.layout, "x", value))
        instance.subscribe_to_attribute("y", lambda value: setattr(instance.layout, "y", value))
        instance.subscribe_to_attribute("width", lambda value: setattr(instance.layout, "width", value))
        instance.subscribe_to_attribute("height", lambda value: setattr(instance.layout, "height", value))
        for callback_type, callback_container in cls.__callback_containers__:
            if callback_type == "mouse":
                getattr(instance, callback_container).subscribe(instance.mouse_callback_factory(callback_container))
            elif callback_type == "text":
                getattr(instance, callback_container).subscribe(instance.text_callback_factory(callback_container))
        return instance
    
    def mouse_callback_factory(self, callback_container):
        def callback(window, x, y, *args, **kwargs):
            for widget in self.widgets:
                if widget.is_mouse_over(x, y):
                    getattr(
                        widget, 
                        callback_container, 
                        lambda *_, **__: print(f"No container {callback_container}")
                    )(window, x, y, *args, **kwargs)
        return callback
    
    def text_callback_factory(self, callback_container):
        def callback(*args, **kwargs):
            for widget in self.widgets:
                if widget.has_focus:
                    getattr(
                        widget, 
                        callback_container, 
                        lambda *_, **__: print(f"No container {callback_container}")
                    )(*args, **kwargs)
        return callback
    