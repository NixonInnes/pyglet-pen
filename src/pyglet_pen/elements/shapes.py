from pyglet_pen.interactable import Interactable
from pyglet_pen.proxies.shapes import RectangleProxy



class Rectangle(Interactable, RectangleProxy):
    pass


class Background(Interactable, RectangleProxy):
    mouse_over_enabled = False