from typing import Literal

from pyglet_pen.component import Component, ComponentAttribute
from pyglet_pen.utilities.types import T

class LayoutAttribute[T](ComponentAttribute[T]):
    __name_container__ = "__layout_attributes__"

class Layout(Component):
    vertical_alignment = LayoutAttribute[Literal["top", "center", "bottom"]]("center")
    horizontal_alignment = LayoutAttribute[Literal["left", "center", "right"]]("center")
    vertical_fill = LayoutAttribute[bool](False)
    horizontal_fill = LayoutAttribute[bool](False)
    margin = LayoutAttribute[int](0)

    @property
    def n_items(self):
        raise NotImplementedError()
    
    def add(self, item):
        raise NotImplementedError()
    
    def update_content_geometry(self):
        raise NotImplementedError()