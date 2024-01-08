import pyglet
from typing import Optional

from pyglet_pen.utilities.types import ColorType, AnchorType

from .proxy import Proxy, ProxyAttribute


class LabelProxy(Proxy):
    BaseConstructor = pyglet.text.Label
    constructor_args = ["text", "font_name", "font_size", "bold", 
                        "italic", "stretch", "color", "x", "y", "anchor_x", 
                        "anchor_y", "width", "height", "rotation", "align", 
                        "multiline", "batch", "group"]
    color: ColorType = ProxyAttribute[ColorType]((255, 255, 255, 255))
    anchor_x = ProxyAttribute[AnchorType]("left")
    anchor_y = ProxyAttribute[AnchorType]("baseline")
    text = ProxyAttribute[str]("")
    align = ProxyAttribute[str]("left")
    font_name = ProxyAttribute[str]("Noto Sans")
    font_size = ProxyAttribute[int](12)
    bold = ProxyAttribute[bool](False)
    italic = ProxyAttribute[bool](False)
    stretch = ProxyAttribute[bool](False)
    color = ProxyAttribute[ColorType]((255, 255, 255, 255))
    rotation = ProxyAttribute[int](0)
    multiline = ProxyAttribute[bool](False)


class HTMLLabelProxy(Proxy):
    BaseConstructor = pyglet.text.HTMLLabel
    constructor_args = ["text", "location", "x", "y", "width", "height", "anchor_x", "anchor_y", "rotation", "multiline", "dpi", "batch", "group"]
    text = ProxyAttribute[str]("")
    location = ProxyAttribute[Optional[str]](None)
    anchor_x = ProxyAttribute[AnchorType]("left")
    anchor_y = ProxyAttribute[AnchorType]("baseline")
    rotation = ProxyAttribute[int](0)
    multiline = ProxyAttribute[bool](False)
    dpi = ProxyAttribute[Optional[int]](None)


class IncrementalTextLayoutProxy(Proxy):
    BaseConstructor = pyglet.text.layout.IncrementalTextLayout
    constructor_args = ["document", "width", "height", "multiline", "dpi", "batch", "group", "wrap_lines"]
    anchor_x = ProxyAttribute[AnchorType]("left")
    anchor_y = ProxyAttribute[AnchorType]("bottom")
    rotation = ProxyAttribute[int](0)
    multiline = ProxyAttribute[bool](False)
    dpi = ProxyAttribute[Optional[int]](None)
    wrap_lines = ProxyAttribute[bool](True)
    font_color = ProxyAttribute[ColorType]((255, 255, 255, 255))
    font_name = ProxyAttribute[str]("Noto Sans")
    font_size = ProxyAttribute[int](12)

    def pre_build(self):
        self.document = pyglet.text.document.UnformattedDocument("")
        self.document.set_style(0, -1, dict(color=self.font_color, font_name=self.font_name, font_size=self.font_size))

    def post_build(self):
        self.base.x = self.x
        self.base.y = self.y
        self.caret = pyglet.text.caret.Caret(self.base)

    @property
    def text(self):
        return self.document.text.strip()
    
    def clear(self):
        self.document.delete_text(0, len(self.document.text))
