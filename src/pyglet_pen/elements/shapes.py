from pyglet_pen.interactable import Interactable
from pyglet_pen.proxies.shapes import RectangleProxy, BorderedRectangleProxy, BoxProxy


class BorderedRectangle(Interactable, BorderedRectangleProxy):
    pass

class Box(Interactable, BoxProxy):
    pass
class Rectangle(Interactable, RectangleProxy):
    pass


class Background(Interactable, RectangleProxy):
    mouse_over_enabled = False