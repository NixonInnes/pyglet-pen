import pyglet
from typing import Optional

from pyglet_pen.component import Component, ComponentProperty
from pyglet_pen.utilities.types import T


class ProxyProperty[T](ComponentProperty[T]):
    __name_container__ = "__proxy_properties__"


class Proxy(Component):
    BaseConstructor = None
    constructor_args = []
    constructor_aliases = {}
    base_property_subscriptions = True

    batch = ProxyProperty[Optional[pyglet.graphics.Batch]](None)
    group = ProxyProperty[Optional[pyglet.graphics.Group]](None)

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.base = None
        return instance
    
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.pre_build()
        self.build()
        self.post_build()
        if self.base_property_subscriptions:
            self.apply_base_property_subscriptions()

    def pre_build(self):
        pass

    def post_build(self):
        pass

    def build(self):
        if self.BaseConstructor is None:
            raise NotImplementedError(f"{self.__class__.__name__}.BaseConstructor is not set")
        
        self.base = self.BaseConstructor(
            **{self.constructor_aliases.get(arg, arg): getattr(self, arg) 
               for arg in self.constructor_args}
        )

    def apply_base_property_subscriptions(self, properties=None):
        if properties is None:
            properties = self.property_names
        for property_name in properties:
            self.subscribe_to_property(
                property_name, 
                self.passthrough_subscription_factory(
                    self.base,
                    property_name
                )
            )