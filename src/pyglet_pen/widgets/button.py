import pyglet
from typing import Callable, Optional

from pyglet_pen.layouts import FloatingLayout
from pyglet_pen.elements.shapes import BorderedRectangle
from pyglet_pen.elements.text import Label
from pyglet_pen.utilities.types import ColorType


from .widget import Widget, WidgetAttribute


class BaseButtonWidget(Widget):
    Layout = FloatingLayout
    
    label_text = WidgetAttribute[str]("Button")
    label_color = WidgetAttribute[ColorType]((255, 255, 255, 255))
    label_font_name = WidgetAttribute[str]("Noto Sans")
    label_font_size = WidgetAttribute[int](12)

    background_color = WidgetAttribute[ColorType]((100, 100, 100, 255))
    border_color = WidgetAttribute[ColorType]((25, 25, 25, 255))
    border_width = WidgetAttribute[int](3)
    
    batch = WidgetAttribute[Optional[pyglet.graphics.Batch]](None)
    button_group = WidgetAttribute[Optional[pyglet.graphics.Group]](pyglet.graphics.Group(2))
    label_group = WidgetAttribute[Optional[pyglet.graphics.Group]](pyglet.graphics.Group(3))
    
    on_click = WidgetAttribute[Optional[Callable]](None)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.background = self.build_background()
        self.subscribe_to_attribute("background_color", lambda value: setattr(self.background, "color", value))
        self.subscribe_to_attribute("border_color", lambda value: setattr(self.background, "border_color", value))
        self.subscribe_to_attribute("border_width", lambda value: setattr(self.background, "border", value))
        if self.on_click is not None:
            self.background.on_mouse_press.subscribe(self.on_click)
        
        self.label = self.build_label()
        self.subscribe_to_attribute("label_text", lambda value: setattr(self.label, "text", value))
        self.subscribe_to_attribute("label_color", lambda value: setattr(self.label, "color", value))
        self.subscribe_to_attribute("label_font_name", lambda value: setattr(self.label, "font_name", value))
        self.subscribe_to_attribute("label_font_size", lambda value: setattr(self.label, "font_size", value))
        
        self.add_content(self.background)
        self.add_content(self.label)

    def build_background(self):
        background = BorderedRectangle(
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
            color=self.background_color,
            border=self.border_width,
            border_color=self.border_color,
            batch=self.batch,
            group=self.button_group,
        )
        return background
    
    def build_label(self):
        label = Label(
            text=self.label_text,
            font_name=self.label_font_name,
            font_size=self.label_font_size,
            x=self.x,
            y=self.y,
            anchor_y="baseline",
            color=self.label_color,
            width=self.width,
            height=self.label_font_size*1.2,
            batch=self.batch,
            group=self.label_group,
            align="center",
        )
        return label

class ButtonWidget(BaseButtonWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self._current_background_color = self.background_color
        self.on_mouse_press.subscribe(self.press_animation)
        self.on_mouse_release.subscribe(self.release_animation)

    def press_animation(self, *args, **kwargs):
        self._current_background_color = self.background.color
        r, g, b, a = self.background.color
        self.background.color = (max(0, r-25), max(0, g-25), max(0, b-25), a)
    
    def release_animation(self, *args, **kwargs):
        self.background.color = self._current_background_color

class ToggleButtonWidget(ButtonWidget):
    state = WidgetAttribute[bool](False)
    on_toggle = WidgetAttribute[Optional[Callable]](None)

    label_text_true = WidgetAttribute[str]("On")
    label_text_false = WidgetAttribute[str]("Off")

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.subscribe_to_attribute("state", self.update_label)
        self.background.on_mouse_press.subscribe(self.toggle)

    def toggle(self, *args, **kwargs):
        self.state = not self.state
        if self.on_toggle is not None:
            self.on_toggle(self.state)
    
    def update_label(self, value: bool):
        if self.state:
            self.label.text = self.label_text_true
        else:
            self.label.text = self.label_text_false

