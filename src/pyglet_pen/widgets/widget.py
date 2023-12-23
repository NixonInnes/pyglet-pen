from typing import Literal

from pyglet_pen.component import Component, ComponentAttribute
from pyglet_pen import layout


class WidgetAttribute[T](ComponentAttribute[T]):
    __name_container__ = "__widget_attributes__"


class Widget(Component):
    Layout = None

    vertical_alignment = WidgetAttribute[Literal["top", "center", "bottom"]]("center")
    horizontal_alignment = WidgetAttribute[Literal["left", "center", "right"]]("center")
    vertical_fill = WidgetAttribute[bool](False)
    horizontal_fill = WidgetAttribute[bool](False)
    margin = WidgetAttribute[int](0)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.layout = self.Layout(
            **{
                k: v
                for k, v in kwargs.items()
                if k in self.Layout.__named_descriptors__
            }
        )


class FloatingWidget(Widget):
    Layout = layout.FloatingLayout


class GridWidget(Widget):
    Layout = layout.GridLayout

    n_rows = WidgetAttribute[int](1)
    n_cols = WidgetAttribute[int](1)


class StackWidget(Widget):
    Layout = layout.StackLayout
    
    stack_direction = WidgetAttribute[Literal["vertical", "horizontal"]]("vertical")
    padding = WidgetAttribute[int](0)