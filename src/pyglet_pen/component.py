import logging
from typing import Any, Optional
from collections import namedtuple

from pyglet_pen.utilities.attribute_subscriber import AttributeSubscriber, SubscriberContainer
from pyglet_pen.utilities.types import T


class ComponentAttribute[T](AttributeSubscriber[T]):
    __name_container__ = "__component_attributes__"


class Component(SubscriberContainer):
    x = ComponentAttribute[int](0)
    y = ComponentAttribute[int](0)
    width = ComponentAttribute[Optional[int]](None)
    height = ComponentAttribute[Optional[int]](None)
    visible = ComponentAttribute[bool](True)

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        InitialValues = namedtuple("initial", set(instance.named_attributes))
        instance.initial = InitialValues(**{attr: getattr(instance, attr) for attr in instance.named_attributes})
        return instance

    def passthrough_subscription_factory(self, target: Any, attr_name: str):
        def callback(value):
            setattr(target, attr_name, value)
        return callback
    
    