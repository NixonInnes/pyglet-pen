import pyglet

from pyglet_pen.utilities.types import ColorType

from .proxy import Proxy, ProxyProperty


class LabelProxy(Proxy):
    BaseConstructor = pyglet.text.Label
    constructor_args = ["x", "y", "text", "font_name", "font_size", "multiline", "color", "batch", "group"]
    color: ColorType = ProxyProperty[ColorType]((255, 255, 255, 255))
    text = ProxyProperty[str]("")
    font_name = ProxyProperty[str]("Arial")
    font_size = ProxyProperty[int](12)
    multiline = ProxyProperty[bool](False)
