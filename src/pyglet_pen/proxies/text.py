import pyglet

from pyglet_pen.utilities.types import ColorType

from .proxy import Proxy, ProxyAttribute


class LabelProxy(Proxy):
    BaseConstructor = pyglet.text.Label
    constructor_args = ["x", "y", "text", "font_name", "font_size", "multiline", "color", "batch", "group"]
    color: ColorType = ProxyAttribute[ColorType]((255, 255, 255, 255))
    text = ProxyAttribute[str]("")
    font_name = ProxyAttribute[str]("Arial")
    font_size = ProxyAttribute[int](12)
    multiline = ProxyAttribute[bool](False)
