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

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.subscribe_to_attribute("x", lambda _: instance.update_content_geometry())
        instance.subscribe_to_attribute("y", lambda _: instance.update_content_geometry())
        return instance

    @property
    def n_items(self):
        raise NotImplementedError()
    
    def add_content(self, item):
        raise NotImplementedError()
    
    def update_content_geometry(self):
        raise NotImplementedError()
    
    def __iter__(self):
        for item in self.contents:
            if isinstance(item, Layout):
                yield from item
            else:
                yield item

class DummyLayout(Layout):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.contents = []
        return instance
    
    @property
    def n_items(self):
        return len(self.contents)
    
    def add_content(self, item):
        self.contents.append(item)

    def update_content_geometry(self):
        pass


class LayoutMixin:
    Layout = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.Layout is None:
            self.layout = DummyLayout()
            print("Using dummy layout")
        else:
            self.layout = self.Layout(
                x=self.x or 0, 
                y=self.y or 0, 
                width=self.width, 
                height=self.height
            )
        

    def add_content(self, item, *args, **kwargs):
        self.layout.add_content(item, *args, **kwargs)

    @property
    def widgets(self):
        return self.layout
    
    