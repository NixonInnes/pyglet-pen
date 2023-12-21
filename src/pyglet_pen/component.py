from typing import Any, Optional
from collections import namedtuple

from pyglet_pen.utilities.subscribe_properties import SubscribableProperty, SubscribeProperties
from pyglet_pen.utilities.types import T


class ComponentProperty[T](SubscribableProperty[T]):
    pass


class Component(SubscribeProperties):
    x = ComponentProperty[int](0)
    y = ComponentProperty[int](0)
    width = ComponentProperty[Optional[int]](None)
    height = ComponentProperty[Optional[int]](None)
    visible = ComponentProperty[bool](True)

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        InitialValues = namedtuple("initial", kwargs.keys())
        instance.initial = InitialValues(**kwargs)
        return instance
    
    def __init__(self, *args, **kwargs):
        pass

    def passthrough_subscription_factory(self, target: Any, property_name: str):
        def callback(value):
            setattr(target, property_name, value)
        return callback
    
    