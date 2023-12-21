from typing import Literal

from pyglet_pen.component import Component, ComponentProperty


class Layout(Component):
    vertical_alignment = ComponentProperty[Literal["top", "center", "bottom"]]("center")
    horizontal_alignment = ComponentProperty[Literal["left", "center", "right"]]("center")
    vertical_fill = ComponentProperty[bool](False)
    horizontal_fill = ComponentProperty[bool](False)
    margin = ComponentProperty[int](0)

    @property
    def n_items(self):
        raise NotImplementedError()
    
    def add(self, item):
        raise NotImplementedError()
    
    def update_content_geometry(self):
        raise NotImplementedError()