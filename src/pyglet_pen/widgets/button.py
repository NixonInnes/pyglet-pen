import pyglet
from typing import Callable, Optional

from pyglet_pen.interactable import Interactable
from pyglet_pen.layouts import FloatingLayout
from pyglet_pen.elements.shapes import Background, Rectangle
from pyglet_pen.elements.text import Label
from pyglet_pen.utilities.types import ColorType, AnchorType


from .widget import WidgetAttribute


class ButtonWidget(Interactable, FloatingLayout):
    label_text = WidgetAttribute[str]("Button")
    label_color = WidgetAttribute[ColorType]((255, 255, 255, 255))
    label_font_name = WidgetAttribute[str]("Arial")
    label_font_size = WidgetAttribute[int](12)

    background_color = WidgetAttribute[ColorType]((100, 100, 100, 255))
    
    batch = WidgetAttribute[Optional[pyglet.graphics.Batch]](None)
    button_group = WidgetAttribute[Optional[pyglet.graphics.Group]](None)
    label_group = WidgetAttribute[Optional[pyglet.graphics.Group]](None)
    
    on_click = WidgetAttribute[Optional[Callable]](None)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.vertical_alignment = "top"
        
        self.background = Rectangle(
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
            color=self.background_color,
            batch=self.batch,
            group=self.button_group,
        )
        if self.on_click is not None:
            self.background.on_mouse_press.subscribe(self.on_click)

        self.label = Label(
            text=self.label_text,
            font_name=self.label_font_name,
            font_size=self.label_font_size,
            x=self.x,
            y=self.y,
            anchor_y="center",
            color=self.label_color,
            width=self.width,
            height=self.height//2,
            batch=self.batch,
            group=self.label_group,
            align="center",
        )
        self.add(self.background)
        self.add(self.label)
        
        self.on_mouse_press.subscribe(self.background.on_mouse_press)

        self.subscribe_to_attribute("label_text", lambda value: setattr(self.label, "text", value))
        self.subscribe_to_attribute("label_color", lambda value: setattr(self.label, "color", value))
        self.subscribe_to_attribute("label_font_name", lambda value: setattr(self.label, "font_name", value))
        self.subscribe_to_attribute("label_font_size", lambda value: setattr(self.label, "font_size", value))

        self.subscribe_to_attribute("background_color", lambda value: setattr(self.background, "color", value))
    