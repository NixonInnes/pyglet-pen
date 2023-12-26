from pyglet_pen.ui_element import UIElement
from pyglet_pen.proxies.shapes import RectangleProxy



class Rectangle(UIElement, RectangleProxy):
    pass


class Background(UIElement, RectangleProxy):
    mouse_over_enabled = False