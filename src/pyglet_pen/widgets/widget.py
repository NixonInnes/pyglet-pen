from typing import Literal

from pyglet_pen.component import Component, ComponentProperty
from pyglet_pen import layout


class WidgetProperty[T](ComponentProperty[T]):
    pass


class Widget(Component):
    Layout = None

    vertical_alignment = WidgetProperty[Literal["top", "center", "bottom"]]("center")
    horizontal_alignment = WidgetProperty[Literal["left", "center", "right"]]("center")
    vertical_fill = WidgetProperty[bool](False)
    horizontal_fill = WidgetProperty[bool](False)
    margin = WidgetProperty[int](0)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.layout = self.Layout(*args, **kwargs)


class FloatingWidget(Widget):
    Layout = layout.FloatingLayout


class GridWidget(Widget):
    Layout = layout.GridLayout


class StackWidget(Widget):
    Layout = layout.StackLayout
    stack_direction = WidgetProperty[Literal["vertical", "horizontal"]]("vertical")
    padding = WidgetProperty[int](0)