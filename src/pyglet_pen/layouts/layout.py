from typing import Literal
import pyglet

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
    allow_oversize = LayoutAttribute[bool](False)

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        # instance.subscribe_to_attribute("x", lambda _: instance.update_content_geometry())
        # instance.subscribe_to_attribute("y", lambda _: instance.update_content_geometry())
        # instance.subscribe_to_attribute("width", lambda _: instance.update_content_geometry())
        # instance.subscribe_to_attribute("height", lambda _: instance.update_content_geometry())
        # instance.subscribe_to_attribute("vertical_alignment", lambda _: instance.update_content_geometry())
        # instance.subscribe_to_attribute("horizontal_alignment", lambda _: instance.update_content_geometry())
        # instance.subscribe_to_attribute("vertical_fill", lambda _: instance.update_content_geometry())
        # instance.subscribe_to_attribute("horizontal_fill", lambda _: instance.update_content_geometry())
        # instance.subscribe_to_attribute("margin", lambda _: instance.update_content_geometry())
        # instance.subscribe_to_attribute("allow_oversize", lambda _: instance.update_content_geometry())
        return instance
    
    @property
    def contents(self):
        raise NotImplementedError()
    
    @property
    def n_items(self):
        return len(self.contents)
    
    @property
    def available_width(self):
        return self.width - (2 * self.margin)
    
    @property
    def available_height(self):
        return self.height - (2 * self.margin)
    
    def adjust_item_size(self, item):
        if self.horizontal_fill:
            item.width = self.available_width
        else:
            item.width = min(self.width, item.initial.width)
        
        if self.vertical_fill:
            item.height = self.available_height
        else:
            item.height = min(self.height, item.initial.height)
    
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
        instance._contents = []
        return instance
    
    @property
    def contents(self):
        return self._contents
    
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
        else:
            self.layout = self.Layout(
                x=self.x or 0, 
                y=self.y or 0, 
                width=self.width, 
                height=self.height
            )
        
    def add_content(self, item, *args, **kwargs):
        self.layout.add_content(item, *args, **kwargs)

    def update_content_geometry(self):
        self.layout.update_content_geometry()

    @property
    def widgets(self):
        return self.layout
    
    