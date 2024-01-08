import pyglet
from typing import Optional

from pyglet_pen.proxies.proxy import Proxy, ProxyAttribute
from pyglet_pen.utilities.types import AnchorType, ColorType


class ShapeProxy(Proxy):
    color: ColorType = ProxyAttribute[ColorType]((255, 255, 255, 255))
    rotation = ProxyAttribute[int](0)
    anchor_x = ProxyAttribute[AnchorType](0)
    anchor_y = ProxyAttribute[AnchorType](0)
    opacity = ProxyAttribute[int](255)


class ArcProxy(ShapeProxy):
    BaseConstructor = pyglet.shapes.Arc
    constructor_args = ["x", "y", "radius", "angle", "start_angle", "closed", "color", "batch", "group"]
    base_property_subscriptions = False
    #radius = ProxyAttribute[float](10.0)
    angle = ProxyAttribute[float](6.283185307179586)
    start_angle = ProxyAttribute[float](0.0)
    closed = ProxyAttribute[bool](False)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.subscribe_to_attribute("x", self.x_mod)
        self.subscribe_to_attribute("y", self.y_mod)
        self.subscribe_to_attribute("width", self.width_mod)
        self.subscribe_to_attribute("height", self.height_mod)
        self.apply_base_attr_subscriptions(["visible", "color", "batch", "group"])

    def x_mod(self, value):
        self.base.x = self.x + self.width // 2
    
    def y_mod(self, value):
        self.base.y = self.y + self.height // 2
    
    def width_mod(self, value):
        self.base.radius = self.radius

    def height_mod(self, value):
        self.base.radius = self.radius

    @property
    def radius(self):
        return min(self.width, self.height) // 2

class CircleProxy(ShapeProxy):
    BaseConstructor = pyglet.shapes.Circle
    constructor_args = ["x", "y", "radius", "segments", "color", "batch", "group"]
    base_attr_subscriptions = False
    #radius = ProxyAttribute[float](10.0)
    segments = ProxyAttribute[Optional[int]](None)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.subscribe_to_attribute("x", self.x_mod)
        self.subscribe_to_attribute("y", self.y_mod)
        self.subscribe_to_attribute("width", self.width_mod)
        self.subscribe_to_attribute("height", self.height_mod)
        self.apply_base_attr_subscriptions(["visible", "color", "batch", "group"])

    def x_mod(self, value):
        self.base.x = self.x + self.width // 2

    def y_mod(self, value):
        self.base.y = self.y + self.height // 2

    def width_mod(self, value):
        self.base.radius = self.radius
    
    def height_mod(self, value):
        self.base.radius = self.radius

    @property
    def radius(self):
        return min(self.width, self.height) // 2



class EllipseProxy(ShapeProxy):
    BaseConstructor = pyglet.shapes.Ellipse
    constructor_args = ["x", "y", "a", "b", "segments", "color", "batch", "group"]
    base_attr_subscriptions = False
    # a = ProxyAttribute[float](10.0)
    # b = ProxyAttribute[float](10.0)
    segments = ProxyAttribute[Optional[int]](None)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.subscribe_to_attribute("x", self.x_mod)
        self.subscribe_to_attribute("y", self.y_mod)
        self.subscribe_to_attribute("width", self.width_mod)
        self.subscribe_to_attribute("height", self.height_mod)
        self.apply_base_attr_subscriptions(["visible", "color", "batch", "group"])

    def x_mod(self, value):
        self.base.x = self.x + self.width // 2

    def y_mod(self, value):
        self.base.y = self.y + self.height // 2

    def width_mod(self, value):
        self.base.b = self.width
    
    def height_mod(self, value):
        self.base.a = self.height
    
    @property
    def a(self):
        return self.width
    
    @property
    def b(self):
        return self.height


class SectorProxy(ShapeProxy):
    BaseConstructor = pyglet.shapes.Sector
    constructor_args = ["x", "y", "radius", "angle", "start_angle", "color", "batch", "group"]
    base_attr_subscriptions = False
    #radius = ProxyAttribute[float](10.0)
    angle = ProxyAttribute[float](6.283185307179586)
    start_angle = ProxyAttribute[float](0.0)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.subscribe_to_attribute("x", self.x_mod)
        self.subscribe_to_attribute("y", self.y_mod)
        self.subscribe_to_attribute("width", self.width_mod)
        self.subscribe_to_attribute("height", self.height_mod)
        self.apply_base_attr_subscriptions(["visible", "color", "batch", "group"])

    def x_mod(self, value):
        self.base.x = self.x + self.width // 2
    
    def y_mod(self, value):
        self.base.y = self.y + self.height // 2

    def width_mod(self, value):
        self.base.radius = self.radius

    def height_mod(self, value):
        self.base.radius = self.radius

    @property
    def radius(self):
        return min(self.width, self.height) // 2


class LineProxy(ShapeProxy):
    BaseConstructor = pyglet.shapes.Line
    constructor_args = ["x", "y", "width", "height", "thickness", "color", "batch", "group"]
    constructor_aliases = {"thickness": "width", "width": "x2", "height": "y2"}
    base_attr_subscriptions = False

    thickness = ProxyAttribute[int](1)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.subscribe_to_attribute("width", self.width_mod)
        self.subscribe_to_attribute("height", self.height_mod)
        self.apply_base_attr_subscriptions(["x", "y", "visible", "color", "batch", "group"])
    
    def width_mod(self, value):
        self.base.x2 = self.x + self.width
    
    def height_mod(self, value):
        self.base.y2 = self.y + self.height


class RectangleProxy(ShapeProxy):
    BaseConstructor = pyglet.shapes.Rectangle
    constructor_args = ["x", "y", "width", "height", "color", "batch", "group"]


class BoxProxy(ShapeProxy):
    BaseConstructor = pyglet.shapes.Box
    constructor_args = ["x", "y", "width", "height", "thickness", "color", "batch", "group"]
    thickness = ProxyAttribute[int](1)


class BorderedRectangleProxy(ShapeProxy):
    BaseConstructor = pyglet.shapes.BorderedRectangle
    constructor_args = ["x", "y", "width", "height", "border", "color", "border_color", "batch", "group"]
    border = ProxyAttribute[int](1)
    border_color: ColorType = ProxyAttribute[ColorType]((255, 255, 255, 255))


class TriangleProxy(ShapeProxy):
    BaseConstructor = pyglet.shapes.Triangle
    constructor_args = ["x", "y", "x2", "y2", "x3", "y3", "color", "batch", "group"]
    x2 = ProxyAttribute[int](0)
    y2 = ProxyAttribute[int](0)
    x3 = ProxyAttribute[int](0)
    y3 = ProxyAttribute[int](0)


class StarProxy(ShapeProxy):
    BaseConstructor = pyglet.shapes.Star
    constructor_args = ["x", "y", "outer_radius", "inner_radius", "num_spikes", "color", "batch", "group"]
    outer_radius = ProxyAttribute[float](10.0)
    inner_radius = ProxyAttribute[float](5.0)
    num_spikes = ProxyAttribute[int](5)



