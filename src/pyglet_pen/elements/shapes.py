from pyglet_pen.proxies.shapes import RectangleProxy

from .element import Element


class Rectangle(Element, RectangleProxy):
    pass


class Background(Element, RectangleProxy):
    mouse_over_enabled = False