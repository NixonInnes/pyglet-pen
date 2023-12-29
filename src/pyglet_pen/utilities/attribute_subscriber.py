from typing import Callable

from .named_attribute import NamedAttribute, NamedAttributeContainer
from .types import T


class AttributeSubscriber[T](NamedAttribute):
    def __init__(self, default: T):
        self._default = default
    
    def __get__(self, instance, owner) -> T:
        if instance is None:
            return self
        return instance.__dict__.get(self, self._default)
    
    def __set__(self, instance, value: T):
        instance.__dict__[self] = value
        #if hasattr(instance, "_subscriptions"):
        for callback in instance._subscriptions.get(self.name, []):
            callback(value)
    
    def __delete__(self, instance):
        del instance.__dict__[self]


class SubscriberContainer(NamedAttributeContainer):
    def __new_instance__(cls, instance):
        instance._subscriptions = {}
        return instance

    def subscribe_to_attribute(self, attr_name: str, callback: Callable[[T], None]) -> None:
        self._subscriptions.setdefault(attr_name, []).append(callback)
