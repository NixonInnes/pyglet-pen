import pyglet
from typing import Optional

from pyglet_pen.component import Component, ComponentAttribute
from pyglet_pen.utilities.types import T


class ProxyAttribute[T](ComponentAttribute[T]):
    __name_container__ = "__proxy_attributes__"


class Proxy(Component):
    BaseConstructor = None
    constructor_args = []
    constructor_aliases = {}
    base_attr_subscriptions = True

    batch = ProxyAttribute[Optional[pyglet.graphics.Batch]](None)
    group = ProxyAttribute[Optional[pyglet.graphics.Group]](None)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base = None
        self.pre_build()
        self.build()
        self.post_build()
        if self.base_attr_subscriptions:
            self.apply_base_attr_subscriptions()

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

    def apply_base_attr_subscriptions(self, attr_names=None):
        if attr_names is None:
            attr_names = self.named_attributes
        for attr_name in attr_names:
            self.subscribe_to_attribute(
                attr_name, 
                self.passthrough_subscription_factory(
                    self.base,
                    attr_name
                )
            )