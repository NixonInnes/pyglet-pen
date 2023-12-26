import pyglet

from pyglet_pen.utilities.types import ColorType

from .proxy import Proxy, ProxyAttribute


class LabelProxy(Proxy):
    BaseConstructor = pyglet.text.Label
    constructor_args = ["text", "font_name", "font_size", "bold", 
                        "italic", "stretch", "color", "x", "y", "width", 
                        "height", "rotation", "align", "multiline", "batch", 
                        "group"]
    color: ColorType = ProxyAttribute[ColorType]((255, 255, 255, 255))
    text = ProxyAttribute[str]("")
    align = ProxyAttribute[str]("left")
    font_name = ProxyAttribute[str]("Arial")
    font_size = ProxyAttribute[int](12)
    bold = ProxyAttribute[bool](False)
    italic = ProxyAttribute[bool](False)
    stretch = ProxyAttribute[bool](False)
    color = ProxyAttribute[ColorType]((255, 255, 255, 255))
    rotation = ProxyAttribute[int](0)
    multiline = ProxyAttribute[bool](False)
