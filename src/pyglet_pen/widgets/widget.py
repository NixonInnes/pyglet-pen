from pyglet_pen.component import ComponentAttribute
from pyglet_pen.utilities.types import T


class WidgetAttribute[T](ComponentAttribute[T]):
    __name_container__ = "__widget_attributes__"