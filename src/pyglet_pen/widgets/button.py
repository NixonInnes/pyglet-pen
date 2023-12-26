import pyglet
from typing import Optional

from pyglet_pen.ui_element import UIElement
from pyglet_pen.layouts import FloatingLayout
from pyglet_pen.renderables.shapes import Background, Rectangle
from pyglet_pen.renderables.text import Label


from .widget import WidgetAttribute


class ButtonWidget(UIElement, FloatingLayout):
    text = WidgetAttribute[str]("Button")
    batch = WidgetAttribute[Optional[pyglet.graphics.Batch]](None)
    group = WidgetAttribute[Optional[pyglet.graphics.Group]](None)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.vertical_fill = True
        self.horizontal_fill = True
        
        self.background = Rectangle(
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
            color=(100, 100, 100, 255),
            batch=self.batch,
            group=self.group,
        )
        print(self.background.initial)
        self.label = Label(
            text=self.text,
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height//2,
            batch=self.batch,
            group=self.group,
            align="center",
        )
        self.add(self.background)
        self.add(self.label)
    