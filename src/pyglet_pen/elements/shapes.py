
from pyglet_pen.proxies.shapes import RectangleProxy

from .element import Element


class Rectangle(Element):
    Proxy = RectangleProxy


class Background(Element):
    Proxy = RectangleProxy
    mouse_over_enabled = False